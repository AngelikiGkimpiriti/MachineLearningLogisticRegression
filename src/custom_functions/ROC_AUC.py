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

def ROC_AUC1(y_test,y_prob):
    fpr,tpr,thresholds=roc_curve(y_test,y_prob)
    roc_auc_score(y_test,y_prob)

    plt.figure()    
    plt.plot(fpr,tpr)
    plt.plot([0,1],[0,1])
    plt.show()