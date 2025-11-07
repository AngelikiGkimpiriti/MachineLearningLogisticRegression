import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

def scale_dataset(X_numerical):
    scaler=StandardScaler()
    scaled_dataset_cols=scaler_fit.fit_transform(X_numerical)
    return scaled_dataset_cols

def scale(X_numerical):
    
    combined = pd.concat([X, prediction_X]) 

    scaler = StandardScaler()
    scaled_combined = scaler.fit_transform(combined)

    scaled_X = pd.DataFrame(scaled_combined[:len(X),:], columns=X.columns, index=X.index)
    scaled_prediction_X = pd.DataFrame(scaled_combined[len(
        X):, :], columns=prediction_X.columns, index=prediction_X.index)

    return scaled_X, scaled_prediction_X
