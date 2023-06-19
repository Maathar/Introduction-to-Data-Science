"""Create a list of 1000 random integers between 1 and 100000,
 then calculate the Z-Score to check for the outliers. 
 Consider values Z-Score > 2 as outliers"""
import random
import numpy as np

# Generate 1000 random integers between 1 and 100000
data = [random.randint(1, 100000) for i in range(1000)]

# Calculate the mean and standard deviation of the data
mean = np.mean(data)
std_dev = np.std(data)

# Calculate the Z-Score for each value in the data
z_scores = [(x - mean) / std_dev for x in data]

# Identify the outliers with Z-Score > 2
outliers = [data[i] for i in range(len(data)) if z_scores[i] > 2]

print("Outliers:", outliers)

"""The output of this code will be a list of any outliers found in
 the data.The Z-Score is a useful statistical measure to check 
 for outliers in a dataset. In this case, the code generates 1000 
 random integers between 1 and 100000 and calculates the Z-Score 
 for each value. Any values with a Z-Score greater than 2 are 
 considered outliers. The Z-Score indicates how many standard 
 deviations a value is away from the mean. A Z-Score greater than
 2 means that the value is more than 2 standard deviations away 
 from the mean, which is a relatively rare occurrence. Therefore,
 values with a Z-Score greater than 2 are considered outliers.
 The code identifies any outliers found in the data and prints
 them out. This can be useful for further data analysis and can 
 help to identify any anomalies in the data. There are no outliers
 in this code. """

