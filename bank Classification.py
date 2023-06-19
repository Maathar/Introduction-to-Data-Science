"""Suppose you are working for a bank that is considering whether 
to approve or reject loan applications from customers. """
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Create the dataset
data = {
    'Credit score': [650, 7120, 5500, 800, 680],
    'Income': [5000, 8000, 3000, 10000, 6000],
    'Loan amount': [10000, 15000, 5000, 20000, 12000],
    'Loan term': ['short-term', 'long-term', 'short-term', 'long-term', 'short-term'],
    'Employment status': ['employed', 'self-employed', 'unemployed', 'employed', 'employed'],
    'Previous delinquencies': ['no', 'yes', 'no', 'yes', 'no'],
    'Approved': ['yes', 'no', 'no', 'yes', 'yes']
}

df = pd.DataFrame(data)

# Convert categorical variables into numerical using one-hot encoding
df = pd.get_dummies(df, columns=['Loan term', 'Employment status', 'Previous delinquencies'])

# Split the dataset into features and target variable
X = df.drop('Approved', axis=1)
y = df['Approved']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# Create the decision tree classifier
clf = DecisionTreeClassifier()

# Train the classifier
clf.fit(X_train, y_train)

# Plot the decision tree
plt.figure(figsize=(10, 6))
plot_tree(clf, filled=True, rounded=True, feature_names=X.columns)
plt.show()

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)