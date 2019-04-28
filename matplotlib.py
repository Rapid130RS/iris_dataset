# Seamus Keating April 2019


import numpy as np
import matplotlib.pyplot as pl
import numpy as np
import urllib


url = 'https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv'
data = urllib.request.urlopen(url).read().decode()
print (data)
# Plot
#pl.scatter(data)


# Config the graph
#plt.title('Plotting Graph for functions f(x), f(x^2) and f(2^x)')
#plt.xlabel('X - Axis')
#plt.ylabel('Y - Axis')

# turnon grid lines visibility
#plt.grid(True)

# setup plot legends for each line and their locations for display
#plt.legend(['y1 = x', 'y2 = x^2', 'y3 = 2^x'], loc='upper left')

# plot the y1, y2 and y3 functions on the graph
#plt.show()
