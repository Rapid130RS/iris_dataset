#!/usr/bin/env python  
#this is to demonstrate the use of Scikit learn in analysing a data set and creating a proof of concept for basic predicitive analytics
#see <https://scikit-learn.org/stable/tutorial/basic/tutorial.html>

import numpy as np
import sklearn                                                                  #import scikit learn
import pandas as pd                                                             # allows input/output of a CSV file and processing
#iris = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv') 
                                                                                # I imported the data set from a URL due to the IDE that I use, but the data also comes with scikit.
from sklearn.datasets import load_iris                                          # Sklearn has the Iris dataset preloaded. Equally, I could use the dataset that I imported to this repo.
iris = load_iris()
# print (iris)                                                                  # print output to see how the data is imported. I commented this out as I only wanted to read the data and the structure of the array.
n_samples, n_features = iris.data.shape                                         # the data the s_samples and n_features refer to the two dimensional array. Numpy recognises the columns and rows in the array as features and samples respectively. 
                                                                                # the iris data attribute is a numpy array
numberOfSamples = str(n_samples)
numberOfFeatures = str(n_features)
firstRecord = str(iris.data[0])                                                 # iris.data; data is an attribute already defined in the dataset
nameOfClasses = str(iris.target_names[0])                                       # in the scikit iris dataset, target names is assigned in the array.
print ("Overview of the dataset:\n")
print ("The number of samples studied is: "+ numberOfSamples)                   # there are 150 samples
print ("The number of features (Petal and Sepel) is: "+ numberOfFeatures)       # there are 4 columns
print ("The data for the first record is :"+ firstRecord)                       # this is the first sample in the dataset, the sepal length is 5.1cm, width 3.5cm, Petal length is 1.4cm and width 0.2cm
print ("The first record refers to Sepal length as "+str(iris.data[0,0])+".cm, Seple width is "+str(iris.data[0,1])+".cm, Petal length is "+str(iris.data[0,2])+".cm and Petal width is "+str(iris.data[0,3])+ ".cm ")
print ("The three classes of flowers are :"+ str(iris.target_names[0])+", "+str(iris.target_names[1])+" and "+str(iris.target_names[2])+".\n")
                                                                                # this outputs the values in the array.
                                                                                # Having had a brief look at the date set, I want to look at what SchKit can do in predictive analysis
X, y = iris.data, iris.target                                                   # I define two variables. X is in caps as the data var is two dimensional, while y is lower case as is one dimensional
from sklearn.svm import LinearSVC                                               # import linear support vector classification machine- a machine learning class that is used to conduct machine learning
clf = LinearSVC(C=150,max_iter=1000000)                                          # create the classifier (clf) and assign the value c=150, which is the total number of samples. The max number of iterations is quite high.
clf = clf.fit(X,y)                                                              # this is the fit function, which is an initial step in creating an machine learning environment. A convergence warning may appear here, depending on the version of python. It can be ignored.
#print ("The process of training the model revises the array: "+ str(clf.coef_))# I left these two lines as I twill want to print the output of the fit function in the future
#print (clf.intercept_) 
                                                                                # Having defined the model, it can be used to predict values
newSepelLength=float(input("Enter the length of the Sepel: "))                  # Next few lines are to gather user input - converting the string to float.
newSepelWidth=float(input("Enter the width of the Sepel: "))
newPetelLength=float(input("Enter the length of the Petel: "))
newPetelWidth=float(input("Enter the width of the Petel: "))
newMeasurement=np.array([newSepelLength, newSepelWidth, newPetelLength, newPetelWidth])
                                                                                # this is an array of user input
arrayForTest=newMeasurement.reshape(-1,4)                                       # I needed to resize the array as I kept getting errors; a 2 dem array was expected.
print ("You entered: "+str(arrayForTest))
clf.predict(arrayForTest)
#print (clf.predict(arrayForTest))                                              # the output of the predict function is a figure, indicating the class of Iris
print("The genus (class) of Iris you have is identifed as "+str(iris.target_names[clf.predict(arrayForTest)])+".")
                                                                                # this outputs the class of flower, there is not any exception catching feature as this is a proof of concept

