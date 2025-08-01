# 🔋 CALiSol‑23: Ionic Conductivity Prediction

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

## 🔍 Overview
This project explores how machine learning can predict the ionic conductivity of lithium-ion electrolytes based on experimental composition data.
We utilize the **CALiSol‑23 dataset** and apply multiple regression models with SHAP analysis interpretation and optimal composition recommendation.

## 🎯 Objective
As a first-year chemical engineering student, my goal was to combine machine learning and experimentation to predict and optimize the results. 
I focused on figuring out how composition and temperature affect ionic conductivity, and how to recommend better electrolyte formulations.

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

📊 Dataset Information
This project uses the CALiSol‑23 dataset, which contains experimental ionic conductivity data for various lithium salt and solvent combinations.

  - 📚 Citation:
Niels Asger Mortensen et al., "CALiSol‑23: Experimental electrolyte conductivity data for various Li‑salts and solvent combinations", Scientific Data (2024)
DOI: 10.1038/s41597-024-03575-8

  - 📁 Dataset Repository: DTU Data Portal

  - 📄 License: Creative Commons Attribution 4.0 International (CC BY 4.0)

This dataset is freely available for redistribution and modification, provided that appropriate credit is given.

  - 📜 This project is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0).
See the LICENSE file for details.

## ⚙️ Models Used
- Random Forest Regressor
- Support Vector Regression (SVR)
- XGBoost Regressor

 Each model was trained on:

✅ Full Feature Set

✅ Top-5 Selected Features (from SHAP + Correlation)

## 📈 Correlation Analysis

This chart shows the top features most correlated with log(k), helping guide feature selection and model interpretation.

## 🔬 Feature Importance (SHAP Analysis)
SHAP Summary (Random Forest)

SHAP Summary (XGBoost)


## 📊 Model Performance Comparison

Model	R²	MSE	MAE
RandomForest (Full)	0.938418	1.09331	0.427362
RandomForest (Selected)	0.808744	3.39548	0.764524
SVR (Full)	0.962272	0.669801	0.428768
SVR (Selected)	0.786117	3.79718	0.793537
XGBoost (Full)	0.951320	0.86424	0.507642
XGBoost (Selected)	0.826873	3.07362	0.755049


📈 Parity Plot (All Models)

This chart compares actual vs predicted ionic conductivity across all models.
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

## 📦 Installation

git clone https://github.com/Kyeongbin-Tom/calisol23-ionic-conductivity.git
cd calisol23-ionic-conductivity
pip install -r requirements.txt

## 🏃‍♂️ How to Run

python src/calisol23_modeling.py

## ✨ Future Improvements

  - Hyperparameter tuning (GridSearchCV, Optuna)
  - More advanced models (CatBoost, LightGBM)
  - SHAP dependence plots for continuous variables
  - External validation with other electrolyte datasets

## 📜 License
This project is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0).
