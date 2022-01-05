import pandas as pd
from sklearn.model_selection import cross_val_score
import my_modules.Performance as Perf
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def regression(x_train, y_train, x_test, y_test, model, verbose=True, plot=True, y_transformer=None):

    # Model Fit

    model.fit(x_train, y_train)

    # Predictions

    y_pred_train = model.predict(x_train)
    y_pred_test = model.predict(x_test)

    if y_transformer is not None:

            y_train = pd.DataFrame(y_transformer.inverse_transform(np.array(y).reshape(-1, 1)))[0]
            y_pred_train = pd.DataFrame(y_transformer.inverse_transform(y_pred.reshape(-1, 1)))[0]

    prediction_train = pd.DataFrame({"y": y_train, "y_pred": y_pred_train})


def classification(x_train, y_train, x_test, y_test, model, cv=10, pos_label=1, verbose=True, plot=True):

    # Model cross validation
    val_scores = cross_val_score(model, x_train, y_train, cv=cv)

    # Fit the model
    model.fit(x_train, y_train)

    # Predictions
    y_pred_train = model.predict(x_train)
    y_pred_test = model.predict(x_test)

    prediction_results = pd.DataFrame({"train": {"y": y_train, "y_pred": y_pred_train},
                                           "test": {"y": y_test, "y_pred": y_pred_test}})
        

    # Build the performance df
    performance_metrics = pd.DataFrame({"error_metric": [f'val_mean_score (k={cv})', f'val_std (k={cv})'],
                                        "train": [val_scores.mean(), val_scores.std()],
                                        "test": ["-", "-"]})
    performance_metrics = performance_metrics.set_index("error_metric")



    # Performance Evaluation

    error_metrics = Perf.perf_classification(y_train, y_test, y_pred_train, y_pred_test, pos_label=pos_label)
    performance_metrics = pd.concat([performance_metrics, error_metrics], axis=0)

    if verbose:

        print("-----------------")
        print(f'The model score using K-fold cross validation (k={cv}) is {round(val_scores.mean(), 3)} '
              f'with a standard deviation of {round(val_scores.std(), 3)}')
        print("-----------------")
        print("The performance metrics of the model")
        display(performance_metrics)
        print("-----------------")

    if plot:

        print("Confusion matrix for the train set")
        print("-----------------")

        ConfusionMatrixDisplay.from_predictions(y_train, y_pred_train)
        plt.show()

        print("Confusion matrix for the test set")
        print("-----------------")

        ConfusionMatrixDisplay.from_predictions(y_test, y_pred_test)
        plt.show()

    return {"model": model, "val_scores": val_scores, "prediction_results": prediction_results
            , "performance_metrics": performance_metrics}


def model_comparison(list_models, predict_function, model_index=None, **kwargs):

    arrays = [[], []]

    for i in range(len(list_models)):

        if model_index is not None:

            arrays[0] = arrays[0] + [model_index[i], model_index[i]]

        else:

            arrays[0] = arrays[0] + [str(list_models[i])[0:str(list_models[i]).index("(")],
                                     str(list_models[i])[0:str(list_models[i]).index("(")]]

        arrays[1] = arrays[1] + ["train", "test"]
        tuples = list(zip(*arrays))
        columns = pd.MultiIndex.from_tuples(tuples)

    for j in range(len(list_models)):

        if j == 0:

            metrics_df = predict_function(model=list_models[j], **kwargs)["performance_metrics"]

        else:
            to_be_concat = predict_function(model=list_models[j], **kwargs)
            metrics_df = pd.concat([metrics_df, to_be_concat["performance_metrics"]], axis=1)

    metrics_df.columns = columns

    return metrics_df

