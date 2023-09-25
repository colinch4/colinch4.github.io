---
layout: post
title: "Hyperparameter tuning with Scikit-learn"
description: " "
date: 2023-09-25
tags: [hyperparameter, tuning]
comments: true
share: true
---

Scikit-learn is a popular machine learning library in Python that provides a wide range of tools for building and training various machine learning models. When working with machine learning algorithms, it is important to tune hyperparameters to find the best combination that maximizes model performance.

In this blog post, we will explore the concept of hyperparameter tuning and demonstrate how to use Scikit-learn for this purpose.

## What are hyperparameters?

Hyperparameters are the settings of a machine learning algorithm that are set before the learning process begins. These parameters are not learned from the data, but rather chosen by the data scientist or machine learning engineer.

Examples of hyperparameters include learning rate, number of hidden units in a neural network, regularization penalty, and kernel type in support vector machines.

Hyperparameter tuning involves adjusting these settings to find the optimal configuration that results in the best performance of the machine learning model.

## Grid Search Cross-Validation

One approach to hyperparameter tuning is using grid search cross-validation. Grid search involves defining a grid of parameter values to search over. The algorithm then evaluates each combination of parameter values using cross-validation and returns the best performing combination.

Scikit-learn provides a convenient `GridSearchCV` class that automates the process of grid search cross-validation. Let's see an example:

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10],
    'min_samples_split': [2, 5, 10]
}

model = RandomForestClassifier()

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print("Best cross-validation score:", grid_search.best_score_)
```

In this example, we are using a `RandomForestClassifier` model and searching over a grid of different values for the `n_estimators`, `max_depth`, and `min_samples_split` hyperparameters. The `GridSearchCV` class automatically performs the grid search cross-validation with 5-fold cross-validation.

After fitting the grid search object to our training data, we can access the best parameters and best cross-validation score.

## Randomized Search Cross-Validation

Grid search can be computationally expensive when dealing with a large number of hyperparameters or large search spaces. Another approach to hyperparameter tuning is using randomized search cross-validation.

Randomized search involves specifying a distribution or set of possible values for each hyperparameter. The algorithm then samples a fixed number of parameter settings from the distribution and evaluates them using cross-validation. This approach is particularly useful when you have limited computational resources.

Scikit-learn provides a `RandomizedSearchCV` class that can be used for performing randomized search cross-validation. Here's an example:

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVC
from scipy.stats import uniform

param_dist = {
    'C': uniform(loc=0, scale=10),
    'gamma': ['scale', 'auto'],
    'kernel': ['linear', 'poly', 'rbf']
}

model = SVC()

random_search = RandomizedSearchCV(estimator=model, param_distributions=param_dist, n_iter=10, cv=5, scoring='accuracy')
random_search.fit(X_train, y_train)

print("Best parameters:", random_search.best_params_)
print("Best cross-validation score:", random_search.best_score_)
```

In this example, we are using a `SVC` model and defining a distribution or set of possible values for the `C`, `gamma`, and `kernel` hyperparameters. The `RandomizedSearchCV` class randomly samples 10 parameter settings from the distribution and evaluates them using 5-fold cross-validation.

After fitting the randomized search object to our training data, we can access the best parameters and best cross-validation score.

## Conclusion

Hyperparameter tuning is an essential part of building machine learning models. Scikit-learn provides powerful tools like `GridSearchCV` and `RandomizedSearchCV` to automate the process of finding the best hyperparameter configuration.

By experimenting with different hyperparameter settings, you can significantly improve the performance of your machine learning models.

#hyperparameter #tuning