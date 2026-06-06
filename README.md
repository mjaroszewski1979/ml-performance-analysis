![caption](https://github.com/mjaroszewski1979/ml-performance-analysis/blob/main/gatling_load_report.jpg)

# ML-Based Performance Test Analysis — Predicting System Behaviour From Gatling Test Data

## Overview

This repository contains a machine learning project focused on analyzing and predicting the behaviour of a system under performance load based on metrics extracted from Gatling test reports.

The project was created as an extension of a separate Gatling + Java performance testing initiative executed against a cloud-native microservice architecture running in GCP and Kubernetes.

Instead of treating performance test results as static reports, the goal of this project was to explore whether historical performance testing data could be transformed into a predictive QA/Performance Engineering layer capable of estimating system behaviour under different load conditions.

---

# Project Goals

The main objectives of this project were:

* extract structured data from unstructured Gatling console reports
* prepare datasets for ML experiments
* identify relationships between load conditions and test outcomes
* predict pass/fail scenarios based on selected performance metrics
* experiment with feature engineering techniques
* evaluate ML models for QA/performance analysis use cases

---

# Related Performance Testing Repository

This project is directly connected to a separate Gatling/Java performance testing repository:

[[LINK_TO_GATLING_REPOSITORY](https://github.com/mjaroszewski1979/gatling-load-tests/tree/main)]

The Gatling project was responsible for:

* generating performance test traffic
* simulating multiple load conditions
* producing reports used later as ML input data

---

# Problem Statement

Performance testing reports are usually treated as historical output generated after test execution.

In many cases:

* reports are reviewed manually
* issues are identified reactively
* valuable patterns remain hidden inside raw metrics

This project explores whether performance test data can be reused to build predictive models capable of estimating the probability of system instability or test failure under specific load conditions.

---

# Data Collection Challenges

One of the biggest challenges was the format of the available data.

Due to client-side environment restrictions:

* JSON export from Gatling reports was unavailable
* raw structured performance metrics could not be exported directly
* reports had to be collected manually from IntelliJ console output

As a result, the project required building a custom Python-based extraction and preprocessing pipeline capable of transforming unstructured text reports into ML-ready datasets.

---

# Data Extraction Pipeline

The project includes custom Python scripts responsible for:

* parsing Gatling console reports
* extracting selected metrics
* cleaning and transforming raw data
* preparing structured datasets for ML analysis

Example extracted metrics included:

* virtual users (VU)
* attachment size
* test duration
* response time indicators
* failed request percentage
* pass/fail outcome classification

---

# Feature Engineering

Several feature engineering techniques were applied in order to improve model performance and better represent system behaviour under load.

Examples include:

* interaction features
* logarithmic transformations
* derived load indicators
* virtual user segmentation (binning)

Example engineered features:

* `vu_x_attachment`
* `attachment_log`
* `load_factor`
* `vu_bin`

The goal was to capture non-linear relationships between traffic intensity and application stability.

---

# Machine Learning Approach

The project focused on binary classification:

* `0 = test passed`
* `1 = test failed`

Multiple approaches and experiments were tested iteratively before selecting the final model.

The final implementation uses:

* CatBoostClassifier

The decision was based on:

* prediction consistency
* confusion matrix evaluation
* classification performance during iterative experiments

---

# Dataset Split

The dataset was divided using train/test split:

```python id="msn1v5"
test_size = 0.25
random_state = 42
```

This allowed evaluation of model generalization and prediction quality on unseen data.

---

# Model Evaluation

Model quality was evaluated using:

* confusion matrix
* classification report
* ROC AUC score

Special attention was paid to minimizing incorrect pass/fail predictions and improving classification reliability for QA-oriented scenarios.

---

# Repository Structure

```text id="2ez2g9"
ml-performance-analysis/
│
├── notebooks/
│   └── performance_ml_analysis.ipynb
│
├── src/
│   ├── parser.py
│   ├── feature_engineering.py
│   ├── model.py
│   └── data_generator.py
│
├── data/
│   ├── README.md
│   └── .gitkeep
│
├── requirements.txt
└── README.md
```

---

# Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* CatBoost
* Jupyter Notebook
* Matplotlib

---

# Running the Project

## Install Dependencies

```bash id="m6k06s"
pip install -r requirements.txt
```

## Start Jupyter Notebook

```bash id="w40nn9"
jupyter notebook
```

---

# Data Privacy & Security

No production or sensitive client data is included in this repository.

Due to confidentiality constraints related to the original environment:

* raw Gatling reports are not publicly available
* no real production datasets are shared
* synthetic/anonymized datasets are used for demonstration purposes

The focus of this repository is the ML pipeline, feature engineering process and predictive analysis approach rather than exposing internal system data.

---

# Key Takeaways

This project was an opportunity to combine:

* QA engineering
* performance testing
* cloud-native architecture understanding
* data analysis
* machine learning experimentation

It also demonstrated how performance testing data can evolve from static reporting into a predictive analysis layer supporting:

* QA teams
* DevOps engineers
* developers
* project stakeholders

Potentially reducing manual analysis effort and improving understanding of system behaviour under load.

---

# Future Improvements

Potential future extensions include:

* automated CI/CD integration
* real-time anomaly detection
* performance trend forecasting
* Grafana/Prometheus integration
* AI-assisted quality gates
* automated performance risk scoring

---

# Disclaimer

This repository was created for educational, research and portfolio purposes only.

The project does not represent any internal client implementation and contains no confidential production information.

---

