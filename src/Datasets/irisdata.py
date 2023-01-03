"""
Author: Rohan Singh
1/2/2023
This Python Module contains source code to return the Iris Dataset in different formats like:
    - Pandas DataFrames
    - Numpy Arrays
    - Lists
"""

#Imports
import pandas as pd
import numpy as np

def get_iris_pd():
    return pd.read_csv("src/Datasets/irisdata.csv")





#Main method
def main():

    print(get_iris_pd())

if __name__ == "__main__":
    main()
