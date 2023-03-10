"""
Author: Rohan Singh
1/2/2023
This module contains source code for a Single Layer (n-to-m) Neural Network in Python
"""

#imports 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class SingleLayerNN:


     #The constructor for the Neural Network class
    def __init__(self, dataset, targets, n, m):
        self.trainset = dataset
        self.targetset = targets
        self.n = n
        self.m = m
        self.init_w = np.zeros([m,n+1])
        pass

    

    #This function will give you the output of the neural network given a weight vector
    def get_NN_Output(self, weights):

        #This vector will contain the output of the neural network
        output = []

        #Getting the output for all of the datapoints within the dataset
        for i in range (0,len(self.trainset),1):

            #This will be added for the bias-term
            a = np.array([1]) 
            a = np.concatenate((a,self.trainset[i]),axis=0)

            #Appending the output for the point (inner-product) into the output list
            output.append(np.matmul(weights,a))

        #Converting the output into a numpy array
        return np.array(output)


    #This function will find the total squared error for the Neural Network from a given set of weights 
    def get_TSE(self,weights):

        #Predicting thee output of the neural network for the given weights
        y = self.get_NN_Output(weights=weights)

        #This variable will store the total squared error for the given output
        tse = 0.0

        #Iterating through all of the data points
        for i in range(0,len(y),1):
            #Adding the squared differences
            tse += ((y[i] - self.targetset[i])**2)
        
        #Dividing the sum by 2
        tse /=2 

        sum = 0
        for i in range(0,len(tse),1):
            sum += tse[i]

        return sum

    #This function will calculate the summed gradient that will be used in the learning rule
    def get_summed_gradient(self,weights):
        
        #This list will hold the summed gradient for all of the 'n' parameters
        gradient = []

        #Getting the temporary predictions for the given set of weights
        y = self.get_NN_Output(weights=weights)

        bias_sum = 0
        #Iterating through all of the data/target points
        for j in range(0,len(self.trainset),1):
            #Finding the difference between the prediction and the target
            temp = y[j] - self.targetset[j]

            #Adding the difference to the bias sum
            bias_sum += temp

        gradient.append(bias_sum)

        #Iterating through all of the 'n' parameter dimensions
        for i in range(0,self.n,1):

            #Calculating the gradient sum for the parameter
            grad_sum = 0
            
            #Iterating through all of the data/target points
            for j in range(0,len(self.trainset),1):
                #Finding the difference between the prediction and the target
                temp = y[j] - self.targetset[j]

                #Multiplying the difference with the datapoint's i-th component
                temp *= self.trainset[j][i]

                grad_sum += temp

            #Appending the gradient sum for the i-th feature to the gradient vector
            grad_sum /= len(self.trainset)
            gradient.append(grad_sum)

        
        gradient = np.array(gradient)
        return np.transpose(gradient)

    #This function will be used to create a matrix of initial weights
    def initial_weights(self):
        
        #The list of rows represents the matrix
        rows = []
        for i in range(0,self.m,1):

            #This represents an individual row
            row = []
            for j in range(0,self.n+1,1):
                row.append(0.0)

            rows.append(row)

        return np.array(rows)

    #This will be used to train the Neural Network using gradient descent, using the input step-size and stopping point and a maximum iteration count
    def train(self, epsilon, maxerr, maxiter):
        
        #Setting the intial weights to 0 for all of the n-parameters (and the bias), this makes the initial matrix an MxN matrix
        w = self.initial_weights()

        #Iterating within the maximum iteration limit
        for i in range (0,maxiter,1):

            #Getting the predicted values given the current weights
            y = self.get_NN_Output(w)

            #Geting the total squared error for the temporary output
            tse = self.get_TSE(w)

            #Checking if the mean-squared error has minimized to the threshold
            mse = tse/(len(self.trainset))
            if(mse < maxerr):
                break

            #Getting the summed gradient
            summed_grad = self.get_summed_gradient(w)
            
            #Updating the weights for the next iteration
            summed_grad *= epsilon
            w -= summed_grad

        self.trained_weight = w
        #Returning the optimal weights 
        return w

    #This will be used as the predict function for the neural-network after the training on the test-set
    def predict(self, test_set):
        
        #This vector will contain the output of the neural network
        output = []

        #Getting the output for all of the datapoints within the test set
        for i in range (0,len(test_set),1):

            #This will be added for the bias-term
            a = np.array([1]) 
            a = np.concatenate((a,test_set[i]),axis=0)

            #Appending the output for the point (inner-product with the optimum weights) into the output list
            output.append(np.matmul(self.trained_weight,a))

        #Converting the output into a numpy array
        return np.array(output)


