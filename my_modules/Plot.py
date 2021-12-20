import matplotlib as plt
import seaborn as sns
import numpy as np


def regression_plots(pred_data, set_name, fig_size=(15, 5)):

    y = pred_data["y"]
    y_pred = pred_data["y_pred"]

    fig, axs = plt.subplots(1, 3, figsize=fig_size)

    sns.regplot(x="y", y="y_pred", data=pred_data, scatter_kws={"color": "red"}, line_kws={"color": "black"},
                ax=axs[0])
    sns.histplot(y - y_pred, kde=True, ax=axs[1])
    axs[2].plot(y_pred, y - y_pred, "o")
    axs[2].plot(y_pred, np.zeros(len(y_pred)), linestyle='dashed')

    axs[0].set_title(f"y_{set}".capitalize() + " Set - Observed VS Predicted")
    axs[1].set_title(f"y_{set}".capitalize() + " Set - Histogram of the Residuals")
    axs[1].set_xlabel(f"y_{set}" + " - y_pred")
    axs[2].set_xlabel("Predicted")
    axs[2].set_ylabel("Residuals")
    axs[2].set_title("Residuals by Predicted")

