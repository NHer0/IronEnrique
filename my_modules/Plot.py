import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np


def my_correlation_heatmap(df, figsize = (16,16)):
    """
    A function to plot a correlation heatmap from a DataFrame.

    Parameters
    ----------
    df : DataFrame
        The target DataFrame
    figsize : Tuple, optional
        Tuple seting the figure size. The default is (16,16).

    Returns
    -------
    None.

    """

    # correlation matrix

    correlation_matrix = df.corr()

    # create figure and axes
    fig, ax = plt.subplots(figsize = figsize)

    # set title
    ax.set_title('Correlation Heatmap', fontweight='bold')


    sns.heatmap(correlation_matrix,  # the data for the heatmap
                annot=True,  # show the actual values of correlation
                cmap='seismic',  # provide the 'seismic' colormap
                center=0,  # specify the value at which to center the colormap
                )


def regression_plots(pred_data, set_id, fig_size=(15, 5)):
    """


    Parameters
    ----------
    pred_data : Dictionary
        Contains the observed and the predicted target variable.
    set_id : String
        "train" or "test".
    fig_size : Tuple, optional
        Figure size. The default is (15, 5).

    Returns
    -------
    None.

    """

    y = pred_data["y"]
    y_pred = pred_data["y_pred"]

    fig, axs = plt.subplots(1, 3, figsize=fig_size)

    sns.regplot(x="y", y="y_pred", data=pred_data, scatter_kws={"color": "red"}, line_kws={"color": "black"}, ax=axs[0])
    sns.histplot(y - y_pred, kde=True, ax=axs[1])
    axs[2].plot(y_pred, y - y_pred, "o")
    axs[2].plot(y_pred, np.zeros(len(y_pred)), linestyle='dashed')

    axs[0].set_title(f"{set_id}".capitalize() + " Set - Observed VS Predicted")
    axs[1].set_title(f"{set_id}".capitalize() + " Set - Histogram of the Residuals")
    axs[2].set_title("Residuals by Predicted")

    axs[1].set_xlabel(f"y_{set_id}" + " - y_pred")
    axs[2].set_xlabel("Predicted")
    axs[2].set_ylabel("Residuals")


