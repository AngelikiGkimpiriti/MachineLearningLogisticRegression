import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, roc_auc_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

from custom_functions.assessmentBusiness import assessmentBusiness1
from custom_functions.StandardInfo import StandardInfo1
from custom_functions.datasheetBusiness import datasetBusiness1
from custom_functions.ROC_AUC import ROC_AUC1
import os

def main():
    
# Dataset Handling
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    path1 = os.path.join(data_dir, 'winequality-red.csv')
    path2 =  os.path.join(data_dir, 'winequality-white.csv')
    full_df = datasetBusiness1(path1, path2)

    # Rudimentary cleaning
    full_df = full_df.drop_duplicates()

    print()
    print()
    print("=================================Standard Dataset Info===============================")
    # Standard Info
    StandardInfo1(full_df)
    

    # X and y assignment
    X = full_df[['fixed acidity', 'density', 'residual sugar', 'alcohol', 'pH']]
    y = full_df['is_red']
    
    
    #Scaling
    scaler=StandardScaler()
    X=scaler.fit_transform(X)
    #X = pd.DataFrame(X, columns=X.columns, index=X.index)
    
    
    # Train and Test split
   
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    

    # Model fitting
    regr = linear_model.LogisticRegression()
    regr.fit(X_train, y_train)
    

    print("=================================Prediction======================================")
    # Predict
    
    result = regr.predict(X_test)
    print("Result:",result)

    print("================================Assessment will be on a pop-up=======================================")
    # Assessment
    assessmentBusiness1(y_test, result)
    
    y_prob = regr.predict_proba(X_test)[:, 1]
    
    ROC_AUC1(y_test, y_prob)
    
    #8.Make a prediction
    #user_input=[[]]
    #results=regr.predict(user_input)
    #print(results)
    
if __name__ == "__main__":
    main()
