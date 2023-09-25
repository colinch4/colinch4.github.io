---
layout: post
title: "Principal Component Analysis (PCA) in Scikit-learn"
description: " "
date: 2023-09-25
tags: [MachineLearning, DataAnalysis]
comments: true
share: true
---

Principal Component Analysis (PCA) is a popular dimensionality reduction technique used in machine learning and data analysis. It aims to find a lower-dimensional representation of a high-dimensional dataset while preserving as much of the original information as possible. In this blog post, we will explore how to perform PCA using the Scikit-learn library in Python.

## Step 1: Importing the Required Libraries

The first step is to import the necessary libraries. We will be using numpy for numerical computations, pandas for data manipulation, and scikit-learn for PCA.

```python
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
```

## Step 2: Loading the Dataset

Next, we need to load the dataset that we want to apply PCA on. For this demonstration, let's consider a sample dataset called "iris" from the Scikit-learn library, which contains measurements of flower species.

```python
from sklearn.datasets import load_iris

data = load_iris()
X = data.data
y = data.target
```

## Step 3: Standardizing the Data

PCA is highly sensitive to the scale of the input data. Therefore, we need to standardize the data before applying PCA. We can use the `StandardScaler` class from Scikit-learn to achieve this.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

## Step 4: Applying PCA

Now, we can apply PCA to the standardized data. We specify the number of components we want to retain and fit the PCA model on our data.

```python
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
```

## Step 5: Explained Variance Ratio

The `explained_variance_ratio_` attribute of the PCA object tells us the amount of variance explained by each of the selected components. We can calculate the cumulative explained variance to get an idea of how much information is preserved by the selected components.

```python
explained_variance = pca.explained_variance_ratio_
cumulative_variance = np.cumsum(explained_variance)
```

## Step 6: Visualizing the Results

Finally, we can visualize the dataset in the reduced dimension space. Let's plot the data points using a scatterplot.

```python
import matplotlib.pyplot as plt

plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA Visualization')
plt.show()
```

By examining the scatterplot, we can gain insights into the relationships between different data points and potentially identify clusters or patterns.

## Conclusion

Principal Component Analysis (PCA) is a powerful technique for dimensionality reduction and data visualization. In this blog post, we learned how to perform PCA using the Scikit-learn library in Python. By following these steps, you can apply PCA to your own high-dimensional datasets and gain valuable insights from the reduced-dimensional representation.

#MachineLearning #DataAnalysis