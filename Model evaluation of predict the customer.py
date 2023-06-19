"""Suppose you are working on a project to predict whether a customer will buy a product 
based on their demographic information. Here are the variables in the dataset:
• Age (numeric): The age of the customer.
• Income (numeric): The annual income of the customer, in thousands of dollars.
• Gender (binary): A binary variable representing the gender of the customer, either 
"male" or "female".
• Education level (categorical): A categorical variable representing the education 
level of the customer, either "high school", "college", or "graduate school".
• Bought product (binary): A binary variable representing whether or not the 
customer bought the product, either "yes" or "no".
Using this dataset, a build a binary classification model to predict whether a customer 
will buy the product based on their demographic information was built. The following is 
the confusion matrix for the model
Using this confusion matrix, you can calculate the following evaluation 
criteria:
• Accuracy
• Precision
• Recall
• F1 Score  """

# Confusion matrix values
true_positive = 20
false_positive = 10
false_negative = 30
true_negative = 30

# Calculate accuracy
accuracy = (true_positive + true_negative) / (true_positive + false_positive + false_negative + true_negative)

# Calculate precision
precision = true_positive / (true_positive + false_positive)

# Calculate recall
recall = true_positive / (true_positive + false_negative)

# Calculate F1 score
f1_score = 2 * ((precision * recall) / (precision + recall))

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1_score)


"""The accuracy of this model is 0.5, which mean this model 
correctly predicted 50% of the cases. The precision of this 
model is 0.66, which mean when the model predict that a customer 
would buy the product it was correct 66% of the time. The recall 
of this model is 0.4 which mean that it correctly identified 40% 
of the customers who bought the product. The F1 score of this model 
is 0.5 which is the harmonic mean of precision and recall. Finally
 this model may need some improvement as its evaluation metrics are
 not very high."""





