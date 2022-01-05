
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error as mae, mean_squared_error as mse


def r2_adjusted(x, y, y_pred, r2=None):

    if r2 is not None:

        r2 = r2_score(y, y_pred)

    else:

        r2_adj = 1 - (1 - r2) * (len(y) - 1) / (len(y) - x.shape[1] - 1)

    return R2_adj

def perf_regression(y_train, y_test, y_pred_train, y_pred_test, x_train, x_test, plot=False):

    performance = pd.DataFrame({'error_metric': ['mae', 'mse', 'rmse', 'r2', 'r2_adj'],
                                'train': [mae(y_train, y_pred_train),
                                          mse(y_train, y_pred_train),
                                          mse(y_train, y_pred_train, squared=False),
                                          r2_score(y_train, y_pred_train),
                                          r2_adjusted(x_train, y_train, y_pred_train)],
                                'test':  [mae(y_test, y_pred_test),
                                          mse(y_test, y_pred_test),
                                          mse(y_test, y_pred_test, squared=False),
                                          r2_score(y_test, y_pred_test),
                                          r2_adjusted(x_test, y_test, y_pred_test)]})
    performance = performance.set_index("error_metric")


def perf_classification(y_train, y_test, y_pred_train, y_pred_test, pos_label=1, plot=False):

    performance = pd.DataFrame({'error_metric': ['accuracy', 'precision', 'recall'],
                                'train': [accuracy_score(y_train, y_pred_train),
                                          precision_score(y_train, y_pred_train, pos_label=pos_label),
                                          recall_score(y_train, y_pred_train, pos_label=pos_label)],
                                'test':  [accuracy_score(y_test, y_pred_test),
                                          precision_score(y_test, y_pred_test, pos_label=pos_label),
                                          recall_score(y_test, y_pred_test, pos_label=pos_label)]})

    performance = performance.set_index("error_metric")

    return performance

