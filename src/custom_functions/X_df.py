import pandas
from sklearn import linear_model
import numpy
from sklearn.model_selection import train_test_split
import matplotlib
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def X_inputDataFrame(df):
    df_columns=[]
    df_columns=df.columns.tolist()
    param_names = []
    X_param_values = []
  
    while True:
        try:
            param_number = input("How many X parameters do you want to predict for? ")
            param_number=int(param_number)
            break
        except ValueError:
            print("I'm not sure that's the kind of value I need. Best put in an integer,yeah? :D")
        except TypeError:
            print("Whatever that was it wasn't an integer, nor could I make it into one. Best put in an integer,yeah? :D")
    

    for i in range(param_number):
        
        while True:
            param_name = input(f"What is the name of parameter {i + 1}? ")
                
            if param_name in df_columns:
                param_names.append(param_name)
                break
            
            else:    
                print("I need a parameter exactly as it appears in the list. Let's try that again.")


    for i in range(param_number):
        print(f"We need a {df[param_names[i]].dtype}. Best not mess up!")
        inputs = input(f"Value for {param_names[i]}: ")
            
        X_param_values.append(inputs)

    input_df = pandas.DataFrame([X_param_values],  columns=param_names)

    return input_df
