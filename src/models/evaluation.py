import numpy as np
from sklearn.metrics import roc_auc_score

TARGETS = ['toxic', 'severe_toxic', 'obscene', 'threat', 'insult', 'identity_hate']


def multi_roc_auc(y_true, y_score, verbose=False):
    ''' Compute roc auc for each target and then average them
    y_true - dataframe of true targets
    y_score - dataframe of predicted target
    '''
    roc_scores = dict()
    for target in TARGETS:
        roc_score = roc_auc_score(y_true=y_true[target], y_score=y_score[target])
        roc_scores[target] = roc_score

    mean_roc_score = np.mean(list(roc_scores.values()))

    if verbose:
        print('Mean ROC AUC overall all targets: {}'.format(mean_roc_score))

    return mean_roc_score, roc_scores

