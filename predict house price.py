"""Suppose you are working on a project to predict the price of a house
 based on its size in square feet. Here are the variables in 
 the dataset:
• Size (numeric): The size of the house in square feet.
• Price (numeric): The price of the house in dollars.
 shows a regression model prediction for the price of a house 
based on its size. 
Calculate the mean squared error (MSE) of the model
•  Calculate the accuracy and error rate of the model (assuming 10% 
acceptable error margin). That means, if the predicted price is 
within 10% of the actual price, it is considered a correct prediction.""""

import numpy as np

# Define the dataset
size = np.array([1000, 1500, 2000, 2500, 3000])
actual_price = np.array([14500, 26500, 33000, 44500, 60000])
predicted_price = np.array([15000, 25000, 35000, 45000, 55000])

# Calculate the mean squared error
mse = np.mean((actual_price - predicted_price) ** 2)
print("Mean squared error (MSE) =", mse)

# Calculate the accuracy and error rate
acceptable_error_margin = 0.1
error = np.abs(actual_price - predicted_price) / actual_price
accuracy = np.mean(error <= acceptable_error_margin)
error_rate = 1 - accuracy
print("Accuracy =", accuracy)
print("Error rate =", error_rate)


