"""Suppose you are working on a project to predict a person's 
shoe size based on their 
height in centimeters. Here are the variables in the dataset:
• Height (numeric): The height of the person in centimeters.
• Shoe size (numeric): The shoe size of the person.
Using this dataset, you could build a regression model to 
predict a person's shoe size based on their height. You could 
use techniques such as linear regression, polynomial 
regression, or regression trees to build the model.
 build a regression model that predicts a person's 
shoe size based on their height. The model would take in
 a person's height as input and 
output a predicted shoe size """

import numpy as np
from sklearn.linear_model import LinearRegression

# Define the data
heights = np.array([[140], [150], [160], [170], [180]])
shoe_sizes = np.array([7, 8, 9, 10, 11])

# Create a linear regression model
model = LinearRegression()

# Train the model on the data
model.fit(heights, shoe_sizes)

# Ask the user to enter their height
user_height = float(input("Enter your height in cm: "))

# Predict the user's shoe size based on their height
new_height = [[user_height]]
predicted_shoe_size = model.predict(new_height)

# Print the predicted shoe size
print("Your predicted shoe size is:", predicted_shoe_size)


"""This is a simple linear regression model that predicts 
a person's shoe size based on their height. The model is 
trained on a dataset that contains the height and corresponding
 shoe size values of several people. The model uses the linear 
 regression algorithm to find the best-fit line that describes 
 the relationship between the height and the shoe size. Once the
 model is trained, it can be used to predict the shoe size of a 
 person based on their height. The model takes the person's height 
 as input and outputs the predicted shoe size. The accuracy of the
 model depends on the quality of the training data and the 
 assumptions made about the relationship between height and shoe size.
 If the relationship is not linear or there are other factors that 
 affect shoe size, the model may not be accurate. This model is  
 simple and effective for predicting shoe size based on height, 
 but it has limitations and may not be accurate for all individuals."""







