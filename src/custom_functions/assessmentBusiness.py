import pandas
from sklearn import linear_model
import numpy
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score, confusion_matrix
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error,
    r2_score,
    explained_variance_score,
    max_error,
    median_absolute_error
)


def assessmentBusiness1(y_test, result):
    accuracy = accuracy_score(y_test, result)
    precision = precision_score(y_test, result)
    recall = recall_score(y_test, result)
    f1 = f1_score(y_test, result)
    conf_matrix = confusion_matrix(y_test, result)
    return accuracy, precision, recall, f1, conf_matrix


def regressionAssessment1(y_test, result):
   
    m_sq_err = mean_squared_error(y_test, result)
    m_abs_perc_err = mean_absolute_percentage_error(y_test, result)
    r2 = r2_score(y_test, result)
    exp_var_sc = explained_variance_score(y_test, result)
    max_err = max_error(y_test, result)
    return m_sq_err, m_abs_perc_err, r2, exp_var_sc, max_err
