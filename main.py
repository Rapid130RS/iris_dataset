# Main Python Code
# This file inports the CSV file and 

import csv
import pandas as pd
data = pd.read_csv('https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv')
print (data)
