
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score, mean_absolute_error as mae, mean_squared_error as mse


def r2_adjusted(x, y, y_pred, r2=None):
    """


    Parameters
    ----------
    x : DataFrame or Serie
        Estimators
    y : DataFrame or Serie
        Observed Target Variable.
    y_pred : DataFrame or Serie
        Predicted Target Variable.
    r2 : Float, optional
        R2 value previously calculated. The default is None.

    Returns
    -------
    r2_adj : Float
        Adjusted R2 value.

    """

    if r2 is None:

        r2 = r2_score(y, y_pred)

    r2_adj = 1 - (1 - r2) * (len(y) - 1) / (len(y) - x.shape[1] - 1)

    return r2_adj


def perf_regression(y_train, y_test, y_pred_train, y_pred_test, x_train, x_test):
    """


    Parameters
    ----------
    y_train : DataFrame or Series
        Observed Target Variable (train set).
    y_test : DataFrame or Series
        Observed Target Variable (test set).
    y_pred_train : DataFrame or Series
        Predicted Target Variable (train set).
    y_pred_test : DataFrame or Series
        Predicted Target Variable (test set).
    x_train : DataFrame or Series
        Estimators (train set).
    x_test : DataFrame or Series
        Estimators (test set).

    Returns
    -------
    performance : DataFrame
        Dataframe containing the performance metrics (MAE, MSE, RMSE, R2 and R2 adj).

    """

    performance = pd.DataFrame({'error_metric': ['mae', 'mse', 'rmse', 'r2', 'r2_adj'],
                                'train': [mae(y_train, y_pred_train),
                                          mse(y_train, y_pred_train),
                                          mse(y_train, y_pred_train, squared=False),
                                          r2_score(y_train, y_pred_train),
                                          r2_adjusted(x_train, y_train, y_pred_train)],
                                'test': [mae(y_test, y_pred_test),
                                         mse(y_test, y_pred_test),
                                         mse(y_test, y_pred_test, squared=False),
                                         r2_score(y_test, y_pred_test),
                                         r2_adjusted(x_test, y_test, y_pred_test)]})

    performance = performance.set_index("error_metric")

    return performance


def perf_classification(y_train, y_test, y_pred_train, y_pred_test, pos_label=1):
    """


    Parameters
    ----------
    y_train : DataFrame or Series
        Observed Target Variable (train set).
    y_test : DataFrame or Series
        Observed Target Variable (test set).
    y_pred_train : DataFrame or Series
        Predicted Target Variable (train set).
    y_pred_test : DataFrame or Series
        Predicted Target Variable (test set).
    pos_label: integer, optional
        Label of interest to calculate metrics (recall, precision)

    Returns
    -------
    performance : DataFrame
        Dataframe containing the performance metrics (accuracy, precision, recall).

    """

    performance = pd.DataFrame({'error_metric': ['accuracy', 'precision', 'recall'],
                                'train': [accuracy_score(y_train, y_pred_train),
                                          precision_score(y_train, y_pred_train, pos_label=pos_label),
                                          recall_score(y_train, y_pred_train, pos_label=pos_label)],
                                'test': [accuracy_score(y_test, y_pred_test),
                                         precision_score(y_test, y_pred_test, pos_label=pos_label),
                                         recall_score(y_test, y_pred_test, pos_label=pos_label)]})

    performance = performance.set_index("error_metric")

    return performance

