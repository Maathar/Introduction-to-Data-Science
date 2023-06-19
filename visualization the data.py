"""Create a list of 100 random pair of integers (x,y) between
 1 and 100. Draw visualization of the data using different 
 Draw scatter plot of the numbers using Python"""

import random
import matplotlib.pyplot as plt

# Create an empty list to store the (x,y) pairs
data = []

# Generate 100 random pairs of integers between 1 and 100
for i in range(100):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    data.append((x, y))

# Create two lists to store the x-coordinates and y-coordinates separately
x_coords = [x[0] for x in data]
y_coords = [x[1] for x in data]

# Create a scatter plot of the data using matplotlib
plt.scatter(x_coords, y_coords)

# Add a title and axis labels to the plot
plt.title("Random Scatter Plot")
plt.xlabel("X Values")
plt.ylabel("Y Values")

# Display the plot
plt.show()

"""This code generates 100 random pairs of integers between 
1 and 100 using Python's random module. It stores these pairs
 as (x,y) tuples in a list called data. The code then creates
 two lists to store the x-coordinates and y-coordinates separately.
 It does this by iterating over the (x,y) tuples in the data list
 and appending the x-coordinate to the x_coords list and the
 y-coordinate to the y_coords list. The code then creates a scatter
 plot of the data using matplotlib's scatter() function. 
 This function takes the x-coordinates and y-coordinates as
 arguments and creates a scatter plot of the data. Since the data 
 is randomly generated, there are no specific patterns or trends 
 in the data. However, there seem to be a few clusters of points 
 in the scatter plot. There are no significant outliers.There 
 doesn't seem to be any strong correlation between the x and y
 variables. The scatter plot shows that the data points are 
 randomly distributed and there is no clear linear or non-linear 
 relationship between the variables."""
