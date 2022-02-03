def load_data(file, source_type="csv"):
    """


    Parameters
    ----------
    file : str
        Name of the file containing the data.
    source_type : str, optional
        The file type."csv" or "excel" accepted. The default is "csv".

    Returns
    -------
    file1 : Dataframe
        A DataFrame containing the data.

    """

    path = "Data/" + file

    try:

        read_f = eval(f'pd.read_{source_type}')
        file1 = read_f(path)
        return file1

    except AttributeError:

        print("Sorry, your input source_type is not supported. Try 'csv' or 'excel'.")


def nan_counter(df):
    """


    Parameters
    ----------
    df : DataFrame
        The target DataFrame.

    Returns
    -------
    remaining_nan : Dictionary
        A dictionary with the following structure. Key is the df column, value
        is the number of null values in the corresponding column.

    """

    remaining_nan = {}

    for column in df.columns:
        remaining_nan[column] = df[column][df[column].isna() == True].size

    return remaining_nan