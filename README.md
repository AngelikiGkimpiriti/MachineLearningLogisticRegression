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

## Setup
1. Clone this repo
2. Run `pip install -r requirements.txt`
3. Execute 'python simple_students.py' from inside the src directory.

## How to run
1.Modify the parameters given in line 39 of the knn.py file in the src folder according to which you want to make the classification. The parameters provided must be one of the features of the dataset, specifically in their encoded form.
Then give your selected set of values in line 55 .

2.For testing:
 -Activate the virtual environment
 -From the root folder of the project run 'python -m unittest tests.test_file' in the command line