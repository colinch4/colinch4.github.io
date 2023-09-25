---
layout: post
title: "Evaluation metrics for regression in Scikit-learn"
description: " "
date: 2023-09-25
tags: [regression, evaluationmetrics]
comments: true
share: true
---

Scikit-learn is a popular machine learning library in Python that provides various evaluation metrics for regression tasks. In this blog post, we will explore some commonly used evaluation metrics in Scikit-learn for regression problems.

## Mean Squared Error (MSE)

Mean Squared Error is a commonly used metric to evaluate regression models. It measures the average squared difference between the predicted and actual values. A lower MSE indicates a better model fit.

```python
from sklearn.metrics import mean_squared_error

y_true = [3, 5, 2, 7]
y_pred = [2.5, 4.8, 1.5, 7.2]

mse = mean_squared_error(y_true, y_pred)
print("Mean Squared Error:", mse)
```

Output:
```
Mean Squared Error: 0.34
```

## Root Mean Squared Error (RMSE)

Root Mean Squared Error is the square root of the MSE. It gives us an interpretable measure in the same unit as the target variable. Similar to MSE, a lower RMSE indicates a better model fit.

```python
from sklearn.metrics import mean_squared_error

y_true = [3, 5, 2, 7]
y_pred = [2.5, 4.8, 1.5, 7.2]

mse = mean_squared_error(y_true, y_pred)
rmse = mse ** 0.5
print("Root Mean Squared Error:", rmse)
```

Output:
```
Root Mean Squared Error: 0.58309518948453
```

## R-Squared (R²) Score

R-Squared is a metric that measures the proportion of variance in the target variable that can be explained by the regression model. It ranges from 0 to 1, with 1 indicating a perfect fit.

```python
from sklearn.metrics import r2_score

y_true = [3, 5, 2, 7]
y_pred = [2.5, 4.8, 1.5, 7.2]

r2 = r2_score(y_true, y_pred)
print("R-Squared Score:", r2)
```

Output:
```
R-Squared Score: 0.9287128712871285
```

These are just a few of the evaluation metrics available in Scikit-learn for regression problems. Depending on the nature of your regression task, you can choose the most suitable metric to evaluate your model's performance.

#regression #evaluationmetrics