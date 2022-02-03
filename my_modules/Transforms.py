
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (StandardScaler, MinMaxScaler)
from sklearn.preprocessing import OrdinalEncoder


def my_transformations(x, y, test_size=0.2, numerical=True, scaler="standard",
                       categorical=True, ordinal_dict=None, nominal_list=[]):
    """


    Parameters
    ----------
    x : DataFrame or Series
        Estimators
    y : DataFrame or Series
        Target Variable
    test_size : float, optional
        Size in fraction (0-1) of the test set. The default is 0.2.
    numerical : Boolean, optional
        Numerical Flag, True if the output DataFrame should contain numerical variables.
        The default is True.
    scaler : String, optional
        The type of numerical scaling method to be used. Values accepted are
        "standard" and "minmax". The default is "standard".
    categorical : Boolean, optional
        Categorical Flag, True if the output DataFrame should contain categorical variables.
        The default is True.
    ordinal_dict : Dictionary, optional
        Dictionary containing the rules for the ordinal encoding. The default is None.
    nominal_list : List, optional
        List containing the columns that require one-hot encoding . The default is [].

    Returns
    -------
    dict
        A dictionary containing two records, "train" and "test".
        These two are lists containing the transformed train and test set:
            - Scaled Numerical columns
            - Ordinal Encoded columns
            - One-Hot Encoded columns
            - Target Variable

    """

    # Train/Test Split

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=0)

    x_train = x_train.reset_index(drop=True)
    x_test = x_test.reset_index(drop=True)

    y_train = y_train.reset_index(drop=True)
    y_test = y_test.reset_index(drop=True)

    # Numerical variables - assign and scale them

    if numerical:

        x_train_num = x_train._get_numeric_data()
        x_test_num = x_test._get_numeric_data()

        if scaler is not None:

            if scaler == "minmax":

                scaler = MinMaxScaler()

            elif scaler == "standard":

                scaler = StandardScaler()

            else:

                print("The input scaling method is not supported. Please use 'standard' or 'minmax'.")
                return

            scaler.fit(x_train_num)
            output_train_num = pd.DataFrame(scaler.transform(x_train_num), columns=x_train_num.columns)
            output_test_num = pd.DataFrame(scaler.transform(x_test_num), columns=x_test_num.columns)

        else:

            output_train_num = x_train_num
            output_test_num = x_test_num
    else:

        output_train_num = "None"
        output_test_num = "None"

    # Categorical variables - assign and encode them

    if categorical:

        x_train_cat = x_train.select_dtypes(["category", "object"])
        x_test_cat = x_test.select_dtypes(["category", "object"])

        # Encoding - Ordinals

        if ordinal_dict is not None:

            x_train_cat_ord = x_train_cat[list(ordinal_dict.keys())]
            x_test_cat_ord = x_test_cat[list(ordinal_dict.keys())]

            categories = [t[1] for t in list(ordinal_dict.items())]

            ordinal_encoder = OrdinalEncoder(categories=categories)
            x_train_cat[x_train_cat_ord.columns] = pd.DataFrame(ordinal_encoder.fit_transform(x_train_cat_ord)
                                                                , columns=x_train_cat_ord.columns)
            output_train_cat_ord = x_train_cat.drop(nominal_list, axis=1)
            x_test_cat[x_test_cat_ord.columns] = pd.DataFrame(ordinal_encoder.fit_transform(x_test_cat_ord)
                                                              , columns=x_test_cat_ord.columns)
            output_test_cat_ord = x_test_cat.drop(nominal_list, axis=1)

        else:

            output_train_cat_ord = x_train_cat
            output_test_cat_ord = x_test_cat

        # Encoding - Nominals

        if len(nominal_list) != 0:

            output_train_cat_nom = pd.get_dummies(x_train_cat.loc[:, nominal_list], drop_first=True)
            output_test_cat_nom = pd.get_dummies(x_test_cat.loc[:, nominal_list], drop_first=True)

        else:

            output_train_cat_nom = "None"
            output_test_cat_nom = "None"

    else:

        output_train_cat_ord = "None"
        output_train_cat_nom = "None"
        output_test_cat_ord = "None"
        output_test_cat_nom = "None"

    return {"train": [output_train_num, output_train_cat_ord, output_train_cat_nom, y_train],
            "test": [output_test_num, output_test_cat_ord, output_test_cat_nom, y_test]}


def var_normalization(df):
    """


    Parameters
    ----------
    df : DataFrame or Series
        Target Dataframe to be nomalized.

    Returns
    -------
    transformer : Sklearn Transformet Object
        Box-Cox Transformer Object.
    power_norm : DataFrame or Series
        Target DataFrame or Series Normalized using a box-cox transformation.

    """

    transformer = PowerTransformer(method="box-cox").fit(df.to_numpy().reshape(-1, 1))
    power_norm = transformer.transform(df.to_numpy().reshape(-1, 1))
    power_norm = pd.DataFrame(power_norm)[0]

    return transformer, power_norm

