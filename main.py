# Seamus Keating April 2019
# The objective of this project is to demonstrate how python libraries can make datat easily understood
# I will inially use a scatter plot to understand the realtionships between the four attributes
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns                                                           # used to generate pairplots
import pandas as pd                                                             # pandas is being used to obtain the CSV file
import csv                                                                      # csv allows me to manipulate the csv file
url = 'https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv'
irisDf=pd.read_csv(url)                                                         
#print(irisDf)                                                                  # This print output is just so I can read and understand the array.
                                                                                # the dataframe output is useful in extracting row and columns
#print(irisDf.head(50))                                                         # This is for example the first 50 rows of data, which is all of one class of iris
#print(irisDf['species'])                                                       # This is a print out of the speiceis column
#print(irisDf.loc[0,'species'])                                                 # Print output a specific location

## Obtian average for the four attributes
meanSepalLength = (round(irisDf["sepal_length"].mean(), 2))
meanSepalWidth = (round(irisDf["sepal_width"].mean(), 2))
meanPetalLength = (round(irisDf["petal_length"].mean(), 2))
meanPetalWidth = (round(irisDf["petal_width"].mean(), 2))
print("The mean Sepal length is "+str(meanSepalLength)+".cm")
print("The mean Sepal width is "+str(meanSepalWidth)+".cm")
print("The mean Petal length is "+str(meanPetalLength)+".cm")
print("The mean Petal width is "+str(meanPetalWidth)+".cm")

# Fiilter the IrisDb ( I know that there are three classes of iris so will use iloc)
isSetosa = irisDf.iloc[0:50]
isVersicolor = irisDf.iloc[51:99]
isVirginica = irisDf.iloc[100:150]
#print (isSetosa)                                                               
#print (isVersicolor)
#print (isVirginica)

#Review the Setosa Data
meanSetosaSepalLength = (round(isSetosa["sepal_length"].mean(), 2))
meanSetosaSepalWidth = (round(isSetosa["sepal_width"].mean(), 2))
meanSetosaPetalLength = (round(isSetosa["petal_length"].mean(), 2))
meanSetosaPetalWidth = (round(isSetosa["petal_width"].mean(), 2))
print("The mean Setosa Sepal length is "+str(meanSetosaSepalLength)+".cm")
print("The mean Setosa Sepal width is "+str(meanSetosaSepalWidth)+".cm")
print("The mean Setosa Petal length is "+str(meanSetosaPetalLength)+".cm")
print("The mean Setosa Petal width is "+str(meanSetosaPetalWidth)+".cm")
# Format a Scatter Plot for the Setosa Sepal Size
plt.title("Relative Sepal Sizes for Setosa")
plt.xlabel("Length")
plt.ylabel("Width")
plt.grid(True)
plt.legend([], loc='upper left')
marker_size=50
# Pass in the data
xSetosaPetal=isSetosa.sepal_length
ySteosaSepal=isSetosa.sepal_width
plt.scatter(xSetosaPetal, ySteosaSepal, marker_size, c= 'm') #marker_size determines size of data point on chart, c is colour
plt.show()
# Format a Scatter Plot for the Setosa Petal Size
plt.title("Relative Petal Sizes for Setosa")
plt.xlabel("Length")
plt.ylabel("Width")
plt.grid(True)
plt.legend([], loc='upper left')
marker_size=50
# Pass in the data
xSetosaP=isSetosa.petal_length
ySetosaP=isSetosa.petal_width
plt.scatter(xSetosaP, ySetosaP, marker_size, c='b')
plt.show()


#Review the Versicolor Data
meanVersicolorSepalLength = (round(isVersicolor["sepal_length"].mean(), 2))
meanVersicolorSepalWidth = (round(isVersicolor["sepal_width"].mean(), 2))
meanVersicolorPetalLength = (round(isVersicolor["petal_length"].mean(), 2))
meanVersicolorPetalWidth = (round(isVersicolor["petal_width"].mean(), 2))
print("The mean Versicolor Sepal length is "+str(meanVersicolorSepalLength)+".cm")
print("The mean Versicolor Sepal width is "+str(meanVersicolorSepalWidth)+".cm")
print("The mean Versicolor Petal length is "+str(meanVersicolorPetalLength)+".cm")
print("The mean Versicolor Petal width is "+str(meanVersicolorPetalWidth)+".cm")
# Format a Scatter Plot for the Versicolor Sepal Size
plt.title("Relative Sepal Sizes for Versicolor")
plt.xlabel("Length")
plt.ylabel("Width")
plt.grid(True)
plt.legend([], loc='upper left')
marker_size=50
# Pass in the data
xVersicolorPetal=isVersicolor.sepal_length
yVersicolorSepal=isVersicolor.sepal_width
plt.scatter(xVersicolorPetal, yVersicolorSepal, marker_size, c= 'k') #marker_size determines size of data point on chart, c is colour ('b', 'g', 'r', 'c', 'm', 'y', 'k', 'w')
plt.show()
# Format a Scatter Plot for the Versicolor Petal Size
plt.title("Relative Petal Sizes for Versicolor")
plt.xlabel("Length")
plt.ylabel("Width")
plt.grid(True)
plt.legend([], loc='upper left')
marker_size=50
# Pass in the data
xVersicolorP=isVersicolor.petal_length
yVersicolorP=isVersicolor.petal_width
plt.scatter(xVersicolorP, yVersicolorP, marker_size, c='b')
plt.show()
#Review the Virginica Data
meanVirginicaSepalLength = (round(isVirginica["sepal_length"].mean(), 2))
meanVirginicaSepalWidth = (round(isVirginica["sepal_width"].mean(), 2))
meanVirginicaPetalLength = (round(isVirginica["petal_length"].mean(), 2))
meanVirginicaPetalWidth = (round(isVirginica["petal_width"].mean(), 2))
print("The mean Virginica Sepal length is "+str(meanVirginicaSepalLength)+".cm")
print("The mean Virginica Sepal width is "+str(meanVirginicaSepalWidth)+".cm")
print("The mean Virginica Petal length is "+str(meanVirginicaPetalLength)+".cm")
print("The mean Virginica Petal width is "+str(meanVirginicaPetalWidth)+".cm")
# Format a Scatter Plot for the Virginica Sepal Size
plt.title("Relative Sepal Sizes for Virginica")
plt.xlabel("Length")
plt.ylabel("Width")
plt.grid(True)
plt.legend([], loc='upper left')
marker_size=50
# Pass in the data
xVirginicaPetal=isVirginica.sepal_length
yVirginicaSepal=isVirginica.sepal_width
plt.scatter(xVirginicaPetal, yVirginicaSepal, marker_size, c= 'g') #marker_size determines size of data point on chart, c is colour
plt.show()
# Format a Scatter Plot for the Versicolor Petal Size
plt.title("Relative Petal Sizes for Virginica")
plt.xlabel("Length")
plt.ylabel("Width")
plt.grid(True)
plt.legend([], loc='upper left')
marker_size=50
# Pass in the data
xVirginicaP=isVirginica.petal_length
yVirginicaP=isVirginica.petal_width
plt.scatter(xVirginicaP, yVirginicaP, marker_size, c='y')
plt.show()
# Generate Pairplot
sns.set()
sns.pairplot(data=irisDf, kind="reg", hue="species")
