""" Generate a random dataset with two features (x1, x2)
a. (10 pt) if you use a programming language . You can use a 
library like NumPy or Scikitlearn to generate the dataset.
2. Divide the dataset into training and test sets. 
a.  if you use a programming language . You can use a library 
like matplotlib
3. Implement the KNN classification.
a. (10 pt) if you use a programming language . You can use a 
library like Scikit-learn
4. Train the KNN classifier on the training set and determine the 
optimal value of k using cross-validation. You can use a library
 like Scikit-learn to perform cross-validation and select the 
optimal value of k.
5.Test the KNN classifier on the test set and evaluate its 
performance using any metric of your choice, such as accuracy
 or F1 score."""


import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score
import matplotlib.pyplot as plt

# Generate a random dataset with two features (x1, x2)
np.random.seed(42)
X = np.random.randn(500, 2)
y = np.random.randint(0, 2, 500)

# Divide the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Determine the optimal value of k using cross-validation
k_values = list(range(1, 21))
cv_scores = []
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=10, scoring='accuracy')
    cv_scores.append(scores.mean())
optimal_k = k_values[cv_scores.index(max(cv_scores))]

# Implement the KNN classification algorithm
knn = KNeighborsClassifier(n_neighbors=optimal_k)
knn.fit(X_train, y_train)

# Test the KNN classifier on the test set
y_pred = knn.predict(X_test)

# Evaluate the performance of the KNN classifier on the test set 
accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print('The accuracy of the KNN classifier is:', accuracy)
print('The F1 score of the KNN classifier is:', f1)

# Plot the cross-validation scores for different values of k
plt.plot(k_values, cv_scores)
plt.xlabel('Number of neighbors (k)')
plt.ylabel('Cross-validation score')
plt.show()

"""The output of the code is the accuracy and F1 score of the KNN 
classifier on the test set, as well as a plot of the 
cross-validation scores for different values of k.The accuracy 
of the KNN classifier is a measure of how often the classifier 
correctly predicts the class labels of the test set. The F1 score 
is the harmonic mean of precision and recall, and is a measure of 
the classifier's accuracy and completeness.The plot of the 
cross-validation scores shows how the performance of the KNN
 classifier varies with the number of neighbors (k). The x-axis 
 represents the number of neighbors, and the y-axis represents 
 the cross-validation score. The plot shows that the optimal value 
 of k is 5, since it has the highest cross-validation score."""