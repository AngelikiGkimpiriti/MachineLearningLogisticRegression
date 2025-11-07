import pandas
import numpy
from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score, confusion_matrix


def StandardInfo1(full_df):

    print("Shape:", full_df.shape)
    print("Columns:", full_df.columns.tolist())
    print("Number of duplicates:", full_df.duplicated().sum())
    print("Number of nulls:", full_df.isnull().sum())
    print("Info:", full_df.info())
    print(full_df.describe())
