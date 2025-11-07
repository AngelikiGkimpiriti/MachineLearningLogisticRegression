<<<<<<< HEAD
## Overview
This project focuses on the use of multiple regression in conjunction with data provided by the dataset
to make predictions on selected qualities based on specific values of described traits of student cases.
It also completely handles the process of loading and cleaning data, as well as training, encoding, and assessment.

Key Features

Modular design using custom_functions for:

Dataset handling

Encoding categorical data

Scaling numerical data

Use of Multiple Regression model to make predictions

Train/test split and performance evaluation

## Assesment 
=======
## Wine Classification with Logistic Regression

This project uses Logistic Regression to classify wines as red or white based on their chemical properties.
It demonstrates key concepts in data preprocessing, model training, evaluation, and visualization using the Wine Quality Dataset.
The goal of this project is to build a simple but effective binary classifier that distinguishes between red and white wines.
The dataset includes several features describing the physicochemical characteristics of wine samples (e.g., acidity, sugar, pH, alcohol).


The project involves:

Loading and preparing the dataset using Pandas

Scaling data using StandardScaler

Splitting the data into training and testing sets

Training a Logistic Regression model

Evaluating performance using common classification metrics

Visualizing results such as the ROC curve and confusion matrix

## Dataset

Wine Quality Dataset from the UCI Machine Learning Repository:
https://archive.ics.uci.edu/dataset/186/wine+quality
>>>>>>> 064c025777bf53615021cd2354f6363c8d78b7fb

## Setup
1. Clone this repo
2. Run `pip install -r requirements.txt`
<<<<<<< HEAD
3. Execute 'python simple_students.py' from inside the src directory.

## How to run
1.Modify the parameters given in line 39 of the knn.py file in the src folder according to which you want to make the classification. The parameters provided must be one of the features of the dataset, specifically in their encoded form.
Then give your selected set of values in line 55 .

2.For testing:
 -Activate the virtual environment
 -From the root folder of the project run 'python -m unittest tests.test_file' in the command line
=======
3. Execute 'python wine.py' from inside the src directory.

## How to run
1.Modify the parameters given in line 31 of the knn.py file in the src folder according to which you want to make the classification.The parameters provided must be features of the dataset.


2.For testing:
 -Activate the virtual environment
 -From the root folder of the project run 'python -m unittest tests.test_file' in the command line

3.To make your own predictions based on user input, look to lines 64-67 to give your values. The code is currently commented out.
>>>>>>> 064c025777bf53615021cd2354f6363c8d78b7fb
"# MachIneLearningMultipleRegression" 
