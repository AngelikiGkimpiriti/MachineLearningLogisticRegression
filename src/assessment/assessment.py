from sklearn.metrics import precision_score, accuracy_score, recall_score, f1_score, confusion_matrix
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt


def standard_metrics(predicted_y, true_y):
    precision = precision_score(true_y, predicted_y)
    accuracy = accuracy_score(true_y, predicted_y)
    recall = recall_score(true_y, predicted_y)
    f1 = f1_score(true_y, predicted_y)
    conf_matrix = confusion_matrix(true_y, predicted_y)


def ROC_and_AUC(true_y, predicted_probs):
    fpr, tpr, thresholds = roc_curve(true_y, predicted_probs)
    auc_score = roc_auc_score(true_y, predicted_probs)
    plt.figure()
    plt.plot(fpr, tpr)
    plt.plot([0, 1], [0, 1])
    plt.grid(True)
    plt.show()
