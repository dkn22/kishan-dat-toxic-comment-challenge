Toxic Comments Classification Challenge
=======================================

This repository documents [Kishan Manani](https://github.com/KishManani) and [Dat Nguyen](http://dkn22.github.io)'s submission to
the Toxic Comments Classification Challenge hosted on Kaggle. A variety
of methods and tools were explored, these included: Bi-directional LSTMs
with word embeddings using Keras, gradient boosted trees using LigthGBM
and XGBoost, Logistic Regression, and LASSO along with standard text
processing methods such as TF-IDF. We also used model stacking, also
known as blending or ensembling.

# Notebook kernels

Here are some of the modelling ideas we explored during the competition.

1. [Exploratory data analysis](https://github.com/dkn22/kishan-dat-toxic-comment-challenge/blob/master/notebooks/1.1-eda.ipynb)
2. [Baseline model](https://github.com/dkn22/kishan-dat-toxic-comment-challenge/blob/master/notebooks/2.1-baseline-model.ipynb) using logistic regression with TF-IDF features
    - [Multi-label feature selection using LASSO](https://github.com/dkn22/kishan-dat-toxic-comment-challenge/blob/master/notebooks/3.1.1-multilabel-feature-selection.ipynb)
3. Gradient boosting
    - [XGBoost on features selected from LASSO](https://github.com/dkn22/kishan-dat-toxic-comment-challenge/blob/master/notebooks/3.2-pipeline-xgb.ipynb)
    - The multi-label nature of the target is handled through classifier chaining (which allows the model to learn correlations between labels)
4. Bi-directional LSTMs with word embeddings
    - [Google News word embeddings](https://github.com/dkn22/kishan-dat-toxic-comment-challenge/blob/master/notebooks/4.1-bidirectional-LSTM-with-word2vec.ipynb) (pre-trained word2vec)
    - GloVe
    - This was individually the best model.
5. Model ensembling

