# Exploring the Iris Dataset through Python
# Overview
This relates to the classic Iris dataset. My objective is to understand the Iris dataset, analysis and make some insights into the dataset.
## Objectives of this work
My objective is to demonstrate some of the capabilities of Python in gaining insights from a dataset to an audience who may be aware of statistical methods, but not of Python functionality. I will achieve this by examining the Iris dataset and extrapolating some findings.
## What is the Iris dataset?
![Iris](iris.jpg)

The subject matter of the Iris dataset is a family of 260–300 types of flowers. In 1936 RA Fisher published a 
[paper](https://onlinelibrary.wiley.com/doi/epdf/10.1111/j.1469-1809.1936.tb02137.x "Named link title") in the _Annals of Eugenics_. RA Fisher sought to differentiate between flowers based on their characteristics. In particular, he aimed to assess whether some types (genus) were misclassified. 
The data set contains 150 records of three different types (classes) of iris flowers with numeric values for petal length and width and sepal length and width.

## Why use the Iris Dataset?

The data set has been used to demonstrate how features of an Iris flower can identify the class of Iris. The values for length and width can be used to classify an Iris into one of three classes: _Iris setosa_, _Iris versicolor_, or _Iris virginica_. 
In the paper, a table of values is provided; as can be seen, a visual inspection of the data does not provide any valuable insights.
![iris_dataset](iris_data.png)

# Utilising Python to Interpret Data

## Specific Insights using Python Libraries

### Numpy

### Matplotlib Pyplot

[Matplotlib Pyplot](https://matplotlib.org/api/pyplot_api.html) is a library that allows for creation of a wide range of data visualisations. I was especially interested in creating a 3D plot of the Iris dataset. A [tutotrial](https://jakevdp.github.io/PythonDataScienceHandbook/04.12-three-dimensional-plotting.html) on the topic 


### SciKit Learn

[SciKit Learn](https://scikit-learn.org/stable/index.html) is a Python library that provides visualisation and predicitve analytics tools. I researched the abiulity to use SciKit to allow users check if a flower matches one of the classess of Iris. The [SciKit tutorial](https://scikit-learn.org/stable/tutorial/basic/tutorial.html) on this subject led my thinking. 
The [python script](https://github.com/Rapid130RS/iris_dataset/blob/master/scikit.py) allows the user to enter measurements for a flower. The predicitve analaytics functions assesses if the data matches one of the four classes of Iris recorded in the Iris dataset.
This excercise did not shed any more light on the nature of the dataset, but is a proof of concept for a furhter iteration that would parse user's inputs and conduct a more sophisticated form of predicitve analytics.



