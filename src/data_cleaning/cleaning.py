import pandas as pd


def standard_info(df):
    df.shape
    df.columns.tolist()
    df.duplicated().sum()
    df.isnull().sum()
    df.info()
    df.describe()


def standard_cleaning(df):

    df.fillna('N/A', inplace=True)
    df.drop_duplicates(inplace=True)
