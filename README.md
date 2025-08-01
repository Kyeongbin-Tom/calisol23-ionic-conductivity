# 🔋 CALiSol‑23: Ionic Conductivity Prediction  
> *Machine learning-based prediction of lithium-ion electrolyte conductivity using the CALiSol‑23 dataset.*

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## 🔍 Overview
This project explores how machine learning can predict the ionic conductivity of lithium-ion electrolytes based on experimental composition data.
We utilize the **CALiSol‑23 dataset** and apply multiple regression models with SHAP analysis interpretation and optimal composition recommendation.

## 🎯 Objective
As a first-year chemical engineering student, I aimed to explore how machine learning can be applied to real experimental data.  
This project helped me understand the relationship between composition and conductivity, while gaining hands-on experience in end-to-end modeling.

## 📁 Project Structure

```bash
calisol23-ionic-conductivity/
├── data/
│   └── calisol23.xlsx
├── images/
│   ├── correlation_top20.png
│   ├── shap_rf_summary.png
│   ├── shap_xgb_summary.png
│   ├── parity_plot_all_models.png
│   ├── top10_recommendation.png
│   └── top10_recommendation.summary.png
├── results/
│   └── model_performance.csv
├── src/
│   └── calisol23_modeling.py
├── requirements.txt
└── README.md
```

## 📊 Dataset Information
This project uses the CALiSol‑23 dataset, which contains experimental ionic conductivity data for various lithium salt and solvent combinations.

| Item        | Detail                                                                                     |
|-------------|---------------------------------------------------------------------------------------------|
| **Name**    | CALiSol‑23                                                                                  |
| **Citation**| Mortensen et al., *Scientific Data* (2024)                                                  |
| **DOI**     | [10.1038/s41597-024-03575-8](https://doi.org/10.1038/s41597-024-03575-8)                    |
| **Source**  | [Scientific Data (Nature)](https://doi.org/10.1038/s41597-024-03575-8)                                    |
| **License** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)                                   |

This dataset is freely available for redistribution and modification, provided that appropriate credit is given.

## ⚙️ Models Used
- Random Forest Regressor
- Support Vector Regression (SVR)
- XGBoost Regressor

 Each model was trained on:

✅ Full Feature Set

✅ Top-5 Selected Features (from SHAP + Correlation)

## 📈 Correlation Analysis

![Correlation](images/correlation_top20.png)
This chart displays the top features most strongly correlated with log(k), aiding in feature selection and model interpretation.

## 🔬 Feature Importance (SHAP Analysis)

### 🔬 SHAP Summary — Random Forest
![SHAP RF](images/shap_rf_summary.png)

### 🔬 SHAP Summary — XGBoost
![SHAP XGB](images/shap_xgb_summary.png)

#### 🔍 What It Shows
Feature impact on conductivity prediction — helps interpret black-box models.

## 📊 Model Performance

### 📈 Model Comparison

| Model                   |   R²     |   MSE    |   MAE    |
|-------------------------|----------|----------|----------|
| RandomForest (Full)     | 0.938     | 1.093     | 0.427     |
| RandomForest (Selected) | 0.809     | 3.395     | 0.765     |
| SVR (Full)              | 0.962     | 0.670     | 0.429     |
| SVR (Selected)          | 0.786     | 3.797     | 0.794     |
| XGBoost (Full)          | 0.951     | 0.864     | 0.508     |
| XGBoost (Selected)      | 0.827     | 3.074     | 0.755     |

📁 See full table: [results/model_performance.csv](./results/model_performance.csv)

📈 Parity Plot (All Models)

![Parity Plot](images/parity_plot_all_models.png)

This scatter plot visualizes the agreement between actual and predicted values for each model.
XGBoost and SVR perform particularly well with low scatter.


## 🧪 Recommendation System

The top 10% of conductivity samples were analyzed to extract the most frequent composition patterns and optimal conditions.

### 🧪 Top Solvent Fractions in High-Conductivity Samples

![Top Solvents](images/top10_recommendation.png)
This bar chart shows the average solvent fractions among the top 10% highest conductivity samples.  
**PC**, **EC**, and **DME** were most frequently used in high-performance compositions.

### 📋 Recommended Electrolyte Summary

![Recommendation Summary](images/top10_recommendation.summary.png)
This summary box presents the optimal electrolyte condition based on the top-performing 10% samples:

- **Salt**: LiPF₆  
- **Solvent Ratio Type**: w  
- **Average Temperature**: 323.4 °C  
- **Average Concentration**: 0.95 mol/L

These conditions reflect the most commonly observed trends in high-performance samples.  
Notably, LiPF₆ salt and PC-rich solvents yielded consistently higher conductivity.

## 📦 Installation

Clone the repository and install required dependencies:

```bash
git clone https://github.com/Kyeongbin-Tom/calisol23-ionic-conductivity.git
cd calisol23-ionic-conductivity
pip install -r requirements.txt
```

## 🏃‍♂️ How to Run

```bash
python src/calisol23_modeling.py

This script will:
  - Preprocess the CALiSol‑23 dataset
  - Train SVR, Random Forest, and XGBoost models
  - Generate SHAP plots and performance comparison
  - Recommend top electrolyte compositions based on top 10% conductivity samples
```

## ✨ Future Improvements

  - Hyperparameter tuning (GridSearchCV, Optuna)
  - More advanced models (CatBoost, LightGBM)
  - SHAP dependence plots for continuous variables
  - External validation with other electrolyte datasets

## 📜 License
This project is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0).
