def standard_headings(df):
    """


    Parameters
    ----------
    df : DataFrame
        The DataFrame which headings will be standardized.

    Returns
    -------
    df : DataFrame
        A DataFrame with standardized headings, i.e. lower case and " " replaced by "_".

    """

    heading = df.columns
    df.columns = [clabel.lower().replace(" ", "_") for clabel in heading]

    return df


def obj_to_cat(df, columns_list):
    """


    Parameters
    ----------
    df : DataFrame
        Target DataFrame
    columns_list : List
        List of columns to be casted into category type.

    Returns
    -------
    df : DataFrame
        The target DataFrame with the specific columns converted to category type.

    """

    for column in columns_list:
        df[column] = df[column].astype("category")

    return df