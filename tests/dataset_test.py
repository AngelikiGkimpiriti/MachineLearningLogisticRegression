import unittest
import numpy as np
from src.custom_functions.datasheetBusiness import LoadDataset
import pandas as pd

#1.Dataset is not empty
#2.There are no NaN or infiinite values
#3.Features and Labels are the same shape
#4.Sufficient variety in values
#5.Classes are the  datatype they re supposed to be

class DatasetTestsStudents(unittest.TestCase):
    def setUp(self):
        path = r"C:\Users\cuppa\OneDrive\Υπολογιστής\projects\machine_learning\VALID_logistic_regression\data\student-mat.csv"
        self.data_arr = LoadDataset(path)
        self.X=self.data_arr[["age"]]
        self.y=self.data_arr[["failures"]]
        print(self.data_arr.columns)
    
    def test_EmptyDatasetNot(self):
        self.assertGreater(self.X.shape[0], 0)
        self.assertGreater(self.y.shape[0], 0)
        
    def test_InfinitesNot(self):
        self.assertTrue(np.isfinite(self.X).all().all())
        self.assertTrue(np.isfinite(self.y).all().all())
    
    def test_Nan_in_cols_not(self):
        self.assertFalse(pd.isnull(self.X).any().any())
        self.assertFalse(pd.isnull(self.y).any().any())
        
    def test_XandYSame(self):
        self.assertEqual(self.X.shape[0], self.y.shape[0])
        
    def test_morethan1(self):
     self.assertTrue(set(self.X["age"]).issubset(range(30)))
     
    def test_RightDataTypesandValues(self):
        self.assertEqual(self.data_arr["age"].dtype, np.int64)
        self.assertEqual(self.data_arr['failures'].dtype,bool)
        self.assertEqual(self.data_arr['freetime'].dtype,int64)
        self.assertEqual(self.data_arr['traveltime'].dtype,int64)
        self.assertEqual(self.data_arr['guardian_other'].dtype,bool)
        self.assertEqual(self.data_arr['famsup_no'].dtype,bool)
        self.assertEqual(self.data_arr['famsize_GT3'].dtype,bool)
        self.assertEqual(self.data_arr['romantic_no'].dtype,bool)

if __name__ == "__main__":
    unittest.main()