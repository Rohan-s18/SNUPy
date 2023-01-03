"""
Author: Rohan Singh
1/2/2023
This Python Module contains source code to return the Iris Dataset in different formats like:
    - Pandas DataFrames
    - List
    - Numpy Array
"""

#Imports
import pandas as pd
import numpy as np

#Function to get the iris dataset as a pandas dataframe
def get_iris_pd():
    return pd.read_csv("src/Datasets/irisdata.csv")


#Function to get the iris dataset as a list
def get_iris_list():

    #Creating a dataset row
    dataset = []

    #Getting the dataframe
    df = get_iris_pd()

    #Getting numpy array columns from the dataframe
    pet_len = df["petal_length"].to_numpy()
    pet_wid = df["petal_width"].to_numpy()
    sep_len = df["sepal_length"].to_numpy()
    sep_wid = df["sepal_width"].to_numpy()

    for i in range(0,len(pet_len),1):

        #For a row of datapoints
        data_row = []
        data_row.append(pet_len[i])
        data_row.append(pet_wid[i])
        data_row.append(sep_len[i])
        data_row.append(sep_wid[i])

        #Adding the row to the dataset
        dataset.append(data_row)


    return dataset


#Function to get the iris dataset as a numpy ndarray
def get_iris_ndarray():
    return  np.array(get_iris_list())




