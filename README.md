## Project title
ML-based Performance Test Analysis for Predicting System Failures
## Problem
performance tests generate large amount of data
traditional reports are reactive
goal: predictive layer for QA insights
## Solution
parsing Gatling-like reports
feature engineering
ML model predicting KO risk
## Architecture
Performance Logs → Parser → Feature Engineering → ML Model → Prediction
## Tech stack
Python
CatBoost
Scikit-learn
Jupyter
## Key insight

## How to run
pip install -r requirements.txt
jupyter notebook
## Important note about data privacy

No production or sensitive data is included in this repository.
All experiments are performed on synthetic or anonymized data due to confidentiality constraints.
