import pandas
import numpy


def datasetBusiness1(path1, path2):

    red_data_arr = pandas.read_csv(path1, sep=';')

    white_data_arr = pandas.read_csv(path2, sep=';')

    red_data_arr["is_red"] = 1
    white_data_arr["is_red"] = 0
    full_df = pandas.concat([red_data_arr, white_data_arr], ignore_index=True)
    return full_df

def LoadDataset(path):
    
    full_df=pandas.read_csv(path,sep=';')
    full_df=pandas.get_dummies(full_df)
    return full_df
    
