
import pandas
from sklearn import linear_model
import numpy
from sklearn.model_selection import train_test_split
import matplotlib
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

from custom_functions.assessmentBusiness import regressionAssessment1
from custom_functions.StandardInfo import StandardInfo1
from custom_functions.datasheetBusiness import datasetBusiness1, LoadDataset
from custom_functions.X_df import X_inputDataFrame
from custom_functions.encoding import enc
from custom_functions.scaling import scale
import os

def main():

    #1. == == == == == == == == == == Loading Dataset == == == == == == == == == == == == == ==
    data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
    path = os.path.join(data_dir, 'student-mat.csv')
    data_arr = LoadDataset(path)

    # Printing Info
    print()
    print()
    print("=================================Standard Dataset Info===============================")
    # StandardInfo1(data_arr)
    print("Here are all the columns:")
    print(data_arr.columns.tolist())


    # 2.Encoding categorical data
    data_arr = enc(data_arr)

    #3. Capturing X and y
    X=data_arr[["age"]]
    y=data_arr[["absences"]]

    #4. Train_and_Test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1) 


    #5. Fitting
    regr = linear_model.LinearRegression()
    regr.fit(X_train, y_train)


    #6. == == == == == == == == == == == == == == == == == = Prediction == == == == == == == == == == == == == ==

    print("=================================Prediction===============================")

    # Predict
    input_df=[[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[15],[18],[11],[12],[19],[13],[11],[12],[19],[13],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[15],[18],[11],[12],[19],[13],[11],[12],[19],[13]]
    result=regr.predict(input_df)
    print("Result:",result)



    #7.Rgression Assesment 
    print("================================Assessment=======================================")
    mean_sq_err,m_abs_perc_err, r2, exp_var_sc , max_err=regressionAssessment1(y_test, result)
    print("Mean Square Error:",mean_sq_err)
    print("Mean Abstract Percentage error:",m_abs_perc_err)
    print("R2:", r2)
    print("Exponential Variance score:",exp_var_sc)
    print("Max error:",max_err)


if __name__ == "__main__":
    main()