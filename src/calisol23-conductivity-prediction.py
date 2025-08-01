# calisol23_modeling.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from xgboost import XGBRegressor
import shap
import warnings
warnings.filterwarnings("ignore")

# =====================
# 📥 1. Load and preprocess data
# =====================

# Load dataset
df = pd.read_excel(r"C:\Users\USER\Desktop\Python\data\calisol23.xlsx")

# Drop unnecessary columns
df.drop(columns=["Unnamed: 0", "doi", "c units"], inplace=True, errors="ignore")

# Drop rows with missing target
df.dropna(subset=["k"], inplace=True)

# Log-transform the target
df["log_k"] = np.log1p(df["k"])

# One-hot encode categorical features
cat_cols = df.select_dtypes(include='object').columns.tolist()
print("🧪 Categorical columns:", cat_cols)
df = pd.get_dummies(df, columns=cat_cols)

# =====================
# 📊 2. Correlation analysis
# =====================

# Pearson correlation with log(k)
corr_matrix = df.corr(numeric_only=True)
corr_series = corr_matrix["log_k"].drop("log_k").sort_values(ascending=False)

# Display top correlations
print("\n📊 Top 20 features correlated with log(k):")
for f, val in corr_series.head(20).items():
    print(f"{f:<30} : {val:.4f}")

# Bar plot of top correlations
plt.figure(figsize=(10, 8))
corr_series.head(20).plot(kind='barh', color='skyblue')
plt.gca().invert_yaxis()
plt.title("Top Features Correlated with log(k)")
plt.xlabel("Correlation Coefficient")
plt.grid(True)
plt.tight_layout()
plt.show()

# =====================
# 🎯 3. Train/test split
# =====================

X = df.drop(columns=["k", "log_k"])
y = df["log_k"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
y_true = np.expm1(y_test)

# =====================
# 🌲 4. Train Random Forest (All features)
# =====================

rf = RandomForestRegressor()
rf.fit(X_train, y_train)
y_pred_rf = np.expm1(rf.predict(X_test))
print("✅ [RandomForest] MSE:", mean_squared_error(y_true, y_pred_rf))

# =====================
# ⚙️ 5. Train SVR (All features)
# =====================

svr_model = make_pipeline(StandardScaler(), SVR(kernel='rbf', C=10, epsilon=0.1))
svr_model.fit(X_train, y_train)
y_pred_svr = np.expm1(svr_model.predict(X_test))
print("⚙️ [SVR] MSE:", mean_squared_error(y_true, y_pred_svr))

# =====================
# 🔬 6. SHAP analysis for Random Forest
# =====================

explainer_rf = shap.TreeExplainer(rf)
shap_values_rf = explainer_rf.shap_values(X_test)

# SHAP summary plots
shap.summary_plot(shap_values_rf, X_test, plot_type="bar")
shap.summary_plot(shap_values_rf, X_test)

# Extract top 5 features from SHAP
shap_df_rf = pd.DataFrame(shap_values_rf, columns=X_test.columns)
top5_shap = shap_df_rf.abs().mean().sort_values(ascending=False).head(5).index.tolist()
print("🌟 Top 5 SHAP features (RandomForest):", top5_shap)

# =====================
# 🔍 6-bis. SHAP analysis for XGBoost (Full features)
# =====================

xgb_full = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
xgb_full.fit(X_train, y_train)

explainer_xgb = shap.TreeExplainer(xgb_full)
shap_values_xgb = explainer_xgb.shap_values(X_test)

# SHAP summary plots
shap.summary_plot(shap_values_xgb, X_test, plot_type="bar")
shap.summary_plot(shap_values_xgb, X_test)

# Extract top 5 SHAP features from XGBoost
shap_df_xgb = pd.DataFrame(shap_values_xgb, columns=X_test.columns)
top5_xgb = shap_df_xgb.abs().mean().sort_values(ascending=False).head(5).index.tolist()
print("🌟 Top 5 SHAP features (XGBoost):", top5_xgb)

# =====================
# ✂️ 7. Feature selection from SHAP + correlation
# =====================

top5_corr = corr_series.head(5).index.tolist()
selected_features = list(set(top5_shap + top5_corr))
selected_features = [f for f in selected_features if f in X.columns]

print("🎯 Selected features for retraining:", selected_features)

X_train_sel = X_train[selected_features]
X_test_sel = X_test[selected_features]

# =====================
# 📊 8. Evaluation function
# =====================

def evaluate_model(name, model, X_tr, X_te):
    model.fit(X_tr, y_train)
    y_pred_log = model.predict(X_te)
    y_pred = np.expm1(y_pred_log)
    return {
        "Model": name,
        "R2": r2_score(y_true, y_pred),
        "MSE": mean_squared_error(y_true, y_pred),
        "MAE": mean_absolute_error(y_true, y_pred)
    }

# =====================
# 🚀 9. Train and evaluate all models
# =====================

results = []

results.append(evaluate_model("RandomForest (Full)", RandomForestRegressor(), X_train, X_test))
results.append(evaluate_model("RandomForest (Selected)", RandomForestRegressor(), X_train_sel, X_test_sel))

svr_pipe = make_pipeline(StandardScaler(), SVR(kernel='rbf', C=10, epsilon=0.1))
results.append(evaluate_model("SVR (Full)", svr_pipe, X_train, X_test))
results.append(evaluate_model("SVR (Selected)", svr_pipe, X_train_sel, X_test_sel))

xgb_sel = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
results.append(evaluate_model("XGBoost (Full)", xgb_full, X_train, X_test))
results.append(evaluate_model("XGBoost (Selected)", xgb_sel, X_train_sel, X_test_sel))

# =====================
# 📝 10. Display comparison table
# =====================

df_results = pd.DataFrame(results)
print("\n📋 Model Performance Comparison:\n")
try:
    print(df_results.to_markdown(index=False))  # requires 'tabulate'
except:
    print(df_results)

# =====================
# 📈 11. Parity plot for all models
# =====================

# Predict again for plotting
rf_pred = np.expm1(rf.predict(X_test))
svr_pred = np.expm1(svr_model.predict(X_test))
xgb_pred = np.expm1(xgb_full.predict(X_test))

plt.figure(figsize=(8, 6))
plt.scatter(y_true, rf_pred, label="Random Forest", alpha=0.6)
plt.scatter(y_true, svr_pred, label="SVR", alpha=0.6)
plt.scatter(y_true, xgb_pred, label="XGBoost", alpha=0.6)
plt.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], 'k--', label="Ideal")
plt.xlabel("Actual k")
plt.ylabel("Predicted k")
plt.title("📈 Predicted vs Actual (All Models)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# =====================
# 🧪 12. Recommend optimal compositions (Top 10% by conductivity)
# =====================

# Get top 10% of true conductivity
threshold = df["k"].quantile(0.90)
top_df = df[df["k"] >= threshold]
print(f"\n🔎 Top 10% cutoff for k: {threshold:.4f}")
print(f"📈 Top 10% samples count: {len(top_df)} / {len(df)}")

# Extract original categorical columns before one-hot
original_df = pd.read_excel(r"C:\Users\USER\Desktop\Python\data\calisol23.xlsx")
original_df = original_df.loc[top_df.index]  # same top 10% index

# Display mode (most common value) for salt / solvent ratio / c / T ranges
print("\n🎯 Recommended Electrolyte Conditions (from Top 10%):")
recommend = {}

for col in ['salt', 'solvent ratio type']:
    mode_val = original_df[col].mode()[0]
    recommend[col] = mode_val
    print(f" - {col}: {mode_val}")

# Also print mean of concentration and temperature
recommend["T"] = round(original_df["T"].mean(), 1)
recommend["c"] = round(original_df["c"].mean(), 2)
print(f" - T (mean): {recommend['T']} °C")
print(f" - c (mean): {recommend['c']} mol/L")

# Optional: display most common solvents used
solvent_cols = ['EC', 'DMC', 'EMC', 'PC', 'DEC', 'EA', 'DME', '2-Glyme', 'AN', 'THF']
if all(col in top_df.columns for col in solvent_cols):
    solvent_avg = top_df[solvent_cols].mean().sort_values(ascending=False)
    print("\n🧪 Average solvent fractions in top samples:")
    print(solvent_avg.head(5))

# =====================
# 📊 13. Visualize recommended electrolyte composition
# =====================

# 1️⃣ Bar plot: Solvent composition (Top 5 only)
plt.figure(figsize=(8, 5))
solvent_avg.head(5).plot(kind='bar', color='mediumseagreen')
plt.title("Top 5 Solvent Fractions in Top 10% Conductivity Samples")
plt.ylabel("Average Fraction")
plt.xlabel("Solvent")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2️⃣ Annotated box: Recommended conditions summary
plt.figure(figsize=(6, 4))
textstr = "\n".join([
    "📌 **Recommended Conditions**",
    f"• Salt: {recommend['salt']}",
    f"• Solvent Ratio Type: {recommend['solvent ratio type']}",
    f"• T (avg): {recommend['T']} °C",
    f"• c (avg): {recommend['c']} mol/L"
])
plt.axis("off")
plt.gca().text(0.05, 0.8, textstr, fontsize=12, verticalalignment='top', bbox=dict(boxstyle="round", facecolor="whitesmoke", edgecolor="gray"))
plt.title("Recommended Electrolyte Summary", pad=20)
plt.tight_layout()
plt.show()