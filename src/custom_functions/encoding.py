import pandas


def enc(dataset_df):

    encoded_df = pandas.get_dummies(dataset_df)
    bool_cols = encoded_df.select_dtypes(include=bool).columns
    encoded_df[bool_cols] = encoded_df[bool_cols].astype(int)
   

    return encoded_df
