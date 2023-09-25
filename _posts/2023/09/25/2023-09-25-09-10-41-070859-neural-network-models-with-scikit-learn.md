---
layout: post
title: "Neural Network models with Scikit-learn"
description: " "
date: 2023-09-25
tags: [ScikitLearn]
comments: true
share: true
---

Neural networks have gained massive popularity in the field of machine learning due to their ability to tackle complex tasks effectively. Scikit-learn, a renowned Python library, provides a convenient and user-friendly interface to build neural network models. In this blog post, we will explore how to use Scikit-learn to build neural network models for various tasks, such as classification and regression.

## Installation and Setup

Before we dive into building neural network models, let's make sure we have Scikit-learn installed. You can install Scikit-learn using pip by running the following command:

```
pip install scikit-learn
```

Once Scikit-learn is successfully installed, we can import it into our Python program using the following code:

```python
import sklearn
```

## Classification with Neural Networks

Let's start by building a neural network model for classification. We will use the famous Iris dataset for this task. First, we need to import the necessary modules and load the dataset:

```python
from sklearn.datasets import load_iris
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

Next, we can create an instance of the MLPClassifier class, which is the neural network model in Scikit-learn:

```python
# Create an instance of MLPClassifier
model = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42)
```

In the above code, we define a neural network model with two hidden layers, each containing 100 and 50 neurons, respectively. We also set the maximum number of iterations to 1000 and the random state to 42 for reproducibility.

We can now fit the model to our training data and make predictions on the test data:

```python
# Fit the model to the training data
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)
```

Finally, we can evaluate the performance of our model by comparing the predictions with the actual labels:

```python
from sklearn.metrics import accuracy_score

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, predictions)
print("Accuracy: {:.2f}".format(accuracy))
```
#ML #ScikitLearn