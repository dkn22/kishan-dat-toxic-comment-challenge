Toxic Comments Classification Challenge
=======================================

This repository documents Kishan Manani and Dat Nguyen's submission to
the Toxic Comments Classification Challenge hosted on Kaggle. A variety
of methods and tools were explored, these included: Bi-directional LSTMs
with word embeddings using Keras, gradient boosted trees using LigthGBM
and XGBoost, Logistic Regression, and LASSO along with standard text
processing methods such as TF-IDF. We also used model stacking, also
known as blending or ensembling.

# Notebooks
1. Exploratory data analysis
2. Baseline model using logistic regression
3. Gradient boosting
4. Bi-directional LSTMs with word embeddings
5. Model ensembling



Project Organization
--------------------

    ├── README.md          <- The top-level README for developers using this project
    │
    ├── data               <- The original data dump from Kaggle
    │
    ├── embeddings         <- The word embeddings .txt files
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         and a short `-` delimited description, e.g. 1.0-exploratory-data-analysis`.
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

