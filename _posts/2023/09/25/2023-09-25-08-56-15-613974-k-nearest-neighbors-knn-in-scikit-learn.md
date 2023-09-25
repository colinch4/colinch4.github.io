---
layout: post
title: "K-Nearest Neighbors (KNN) in Scikit-learn"
description: " "
date: 2023-09-25
tags: [DataScience, MachineLearning]
comments: true
share: true
---

K-Nearest Neighbors (KNN) is a popular machine learning algorithm used for classification and regression tasks. It is a non-parametric algorithm that makes predictions based on the similarity of new data points to its k nearest neighbors in the training set.

In this blog post, we will explore how to implement the KNN algorithm using the Scikit-learn library in Python.

## Installation

First, let's ensure that Scikit-learn is installed in your Python environment. You can install it using pip:

```
pip install scikit-learn
```

## Data Preparation

Before we dive into the implementation, let's prepare our data for the KNN algorithm. We need to split our dataset into a training set and a test set. The training set will be used to train the model, while the test set will be used to evaluate its performance.

Let's assume we have a dataset `X` containing the features and a corresponding target variable `y` representing the class labels. We can split the data into training and test sets using Scikit-learn's `train_test_split` function:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
```

## KNN Implementation

To implement the KNN algorithm, we will use the `KNeighborsClassifier` class from Scikit-learn. Here's how you can create and train a KNN model:

```python
from sklearn.neighbors import KNeighborsClassifier

k = 3  # number of neighbors to consider

knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
```

In the above example, we create a `KNeighborsClassifier` object with `n_neighbors` set to 3. This means that the algorithm will consider the 3 nearest neighbors when making predictions.

## Making Predictions

After training the model, we can use it to make predictions on new data points. In Scikit-learn, we can use the `predict` method of the trained KNN model:

```python
y_pred = knn.predict(X_test)
```

`y_pred` will contain the predicted class labels for the test set.

## Evaluating the Model

To evaluate the performance of our KNN model, we can use various evaluation metrics such as accuracy, precision, recall, and F1 score. For classification tasks, we can use Scikit-learn's `classification_report` function:

```python
from sklearn.metrics import classification_report

print(classification_report(y_test, y_pred))
```

This will print a detailed classification report showing the precision, recall, F1-score, and support for each class in the test set.

## Conclusion

In this blog post, we learned about K-Nearest Neighbors (KNN) algorithm and its implementation in Scikit-learn. We discussed how to prepare the data, train the model, make predictions, and evaluate its performance. KNN is a simple yet powerful algorithm that can be used for both classification and regression tasks.

#DataScience #MachineLearning