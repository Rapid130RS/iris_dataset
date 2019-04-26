# Main Python Code
# This file inports the CSV file and 
import csv
import pandas as pd # allows input/output of a CSV file and processing
import numpy as np # allows for linear algebra
import matplotlib.pyplot as plt #allows for visualisation
data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
print (data)
