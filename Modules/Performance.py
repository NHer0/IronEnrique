
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay


def perf_classification(y_train, y_test, y_pred_train, y_pred_test, pos_label=1, plot=False):

    performance = pd.DataFrame({'Error_metric': ['Accuracy', 'Precision', 'Recall'],
                                    'Train': [accuracy_score(y_train, y_pred_train),
                                              precision_score(y_train, y_pred_train, pos_label=pos_label),
                                              recall_score(y_train, y_pred_train, pos_label=pos_label)],
                                    'Test': [accuracy_score(y_test, y_pred_test),
                                             precision_score(y_test, y_pred_test, pos_label=pos_label),
                                             recall_score(y_test, y_pred_test, pos_label=pos_label)]})
    performance = performance.set_index("Error_metric")

    cm_train = confusion_matrix(y_train, y_pred_train)
    cm_test = confusion_matrix(y_test, y_pred_test)

    if plot:

        print("Confusion matrix for the train set")
        print("-----------------")

        ConfusionMatrixDisplay.from_predictions(y_train, y_pred_train)
        plt.show()

        print("Confusion matrix for the test set")
        print("-----------------")

        ConfusionMatrixDisplay.from_predictions(y_test, y_pred_test)
        plt.show()

    return {"performance": performance, "train": {"cm": cm_train}, "test": {"cm": cm_test}}
