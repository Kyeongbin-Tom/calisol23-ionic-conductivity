# 🔋 CALiSol‑23: Ionic Conductivity Prediction

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains a machine learning project for predicting and analyzing the ionic conductivity of lithium-based electrolytes using the **CALiSol‑23 dataset**.  
The project includes feature importance analysis, model comparison (Random Forest, SVR, XGBoost), and a recommendation system for optimal electrolyte compositions.

---

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
Random Forest Regressor

Support Vector Regression (SVR)

XGBoost Regressor

Each model was trained on:

✅ Full Feature Set

✅ Top-5 Selected Features (from SHAP + Correlation)

## 📊 Model Performance Comparison

Model	R²	MSE	MAE
RandomForest (Full)	0.938418	1.09331	0.427362
RandomForest (Selected)	0.808744	3.39548	0.764524
SVR (Full)	0.962272	0.669801	0.428768
SVR (Selected)	0.786117	3.79718	0.793537
XGBoost (Full)	0.951320	0.86424	0.507642
XGBoost (Selected)	0.826873	3.07362	0.755049

## 📦 Installation

git clone https://github.com/Kyeongbin-Tom/calisol23-ionic-conductivity.git
cd calisol23-ionic-conductivity
pip install -r requirements.txt

## 🏃‍♂️ How to Run

python src/calisol23_modeling.py
