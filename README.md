1. Project title
ML-based Performance Test Analysis for Predicting System Failures
2. Problem
performance tests generate large amount of data
traditional reports are reactive
goal: predictive layer for QA insights
3. Solution
parsing Gatling-like reports
feature engineering
ML model predicting KO risk
4. Architecture
Performance Logs → Parser → Feature Engineering → ML Model → Prediction
5. Tech stack
Python
CatBoost
Scikit-learn
Jupyter
6. Key insight


7. How to run
pip install -r requirements.txt
jupyter notebook
8. Important note about data privacy


No production or sensitive data is included in this repository.
All experiments are performed on synthetic or anonymized data due to confidentiality constraints.