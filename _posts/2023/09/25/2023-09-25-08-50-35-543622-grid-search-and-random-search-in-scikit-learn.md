---
layout: post
title: "Grid search and random search in Scikit-learn"
description: " "
date: 2023-09-25
tags: [GridSearch, RandomSearch]
comments: true
share: true
---

Performing hyperparameter tuning is a crucial step in building machine learning models. It involves finding the best combination of hyperparameters that optimize the model's performance. Scikit-learn, a popular machine learning library, provides two powerful tools for hyperparameter tuning: **Grid Search** and **Random Search**.

## Grid Search

Grid Search is a technique that exhaustively searches through a predefined set of hyperparameters and evaluates them using cross-validation to find the best combination. It generates a grid of all possible hyperparameter values and evaluates each option.

To implement Grid Search in Scikit-learn, we can use the `GridSearchCV` class from the `model_selection` module. Let's assume we have a Support Vector Machine (SVM) model and we want to tune its `C` and `gamma` parameters. Here's an example on how to use Grid Search:

```python
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC

# Define the parameter grid
param_grid = {
    'C': [0.1, 1, 10],
    'gamma': [0.01, 0.1, 1]
}

# Create the SVM model
svm_model = SVC()

# Create the grid search object
grid_search = GridSearchCV(svm_model, param_grid, cv=5)

# Fit the grid search to the data
grid_search.fit(X_train, y_train)

# Get the best parameters
best_params = grid_search.best_params_
```

In the example above, `param_grid` defines the possible values for `C` and `gamma`. The `cv` parameter specifies the number of cross-validation folds. `X_train` and `y_train` are the training data and labels, respectively. After fitting the grid search object, we can retrieve the best parameters by accessing the `best_params_` attribute.

## Random Search

Random Search is an alternative approach to hyperparameter tuning that randomly samples from a predefined distribution of hyperparameters. Unlike Grid Search, it does not exhaustively search through all possible combinations.

To use Random Search in Scikit-learn, we can make use of the `RandomizedSearchCV` class from the `model_selection` module. The usage is similar to Grid Search, but instead of specifying a grid of hyperparameter values, we define a distribution for each hyperparameter. Here's an example:

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint

# Define the parameter distributions
param_dist = {
    'n_estimators': randint(100, 1000),
    'max_depth': randint(5, 50),
    'min_samples_split': randint(2, 20)
}

# Create the Random Forest model
rf_model = RandomForestClassifier()

# Create the random search object
random_search = RandomizedSearchCV(rf_model, param_dist, n_iter=10, cv=5)

# Fit the random search to the data
random_search.fit(X_train, y_train)

# Get the best parameters
best_params = random_search.best_params_
```

In the above example, `param_dist` defines the distribution for `n_estimators`, `max_depth`, and `min_samples_split`. The `n_iter` parameter determines the number of random samples to try. Again, after fitting the random search object, we can retrieve the best parameters using the `best_params_` attribute.

## Conclusion

Grid Search and Random Search are powerful techniques for hyperparameter tuning in Scikit-learn. While Grid Search exhaustively evaluates all possible combinations, Random Search explores random combinations. Depending on the dataset and hyperparameter space, one approach might be more efficient than the other. **#GridSearch #RandomSearch**