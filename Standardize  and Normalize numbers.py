"""Create a list of 10 random integers between 1 and 100. 
- Standardize the numbers 
- Normalize the numbers"""

import numpy as np

# Generate a list of 10 random integers between 1 and 100
random_integers = np.random.randint(1, 100, 10)

# Calculate the mean and standard deviation of the random integers 
m=np.mean(random_integers)
std_dev = np.std(random_integers)

# Standardize the random integers 
standardized_values = (random_integers - m) / std_dev

#Normalize the standardized values 
normalized_values = (standardized_values - np.min(standardized_values)) / (np.max(standardized_values) - np.min(standardized_values))
print("standardized_values",standardized_values)

print("normalized_values",normalized_values )

"""This code generates a list of 10 random integers between 1 
and 100 using NumPy's randint() function. It then calculates 
the mean and standard deviation of the random integers using 
NumPy's mean() and std() functions.The code then standardizes
 the random integers by subtracting the mean from each integer
 and dividing by the standard deviation. This creates a new list 
 of standardized values that have a mean of 0 and a standard 
 deviation of 1. The code normalizes the standardized values by
 subtracting the minimum value from each value and dividing by 
 the range of the values. This creates a new list of normalized
 values that have a range of 0 to 1.The output shows the list 
 of standardized values and the list of normalized values. 
 The standardized values have a mean of 0 and a standard 
 deviation of 1, while the normalized values have a range 
 of 0 to 1.  This code is useful because it can help to 
 and normalize data. Standardizing and normalizing data can
 be useful for comparing data that is measured in different
 units or has different scales. By standardizing and normalizing
 data, it becomes easier to compare and analyze the data."""
