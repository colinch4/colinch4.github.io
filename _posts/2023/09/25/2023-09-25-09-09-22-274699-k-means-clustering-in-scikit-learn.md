---
layout: post
title: "K-Means Clustering in Scikit-learn"
description: " "
date: 2023-09-25
tags: [datascience, machinelearning]
comments: true
share: true
---

K-Means is a popular clustering algorithm used to partition data into groups or clusters based on their similarity. In this blog post, we will explore how to perform K-Means clustering using Scikit-learn, a popular machine learning library in Python.

## Installing Scikit-learn

Before we begin, make sure you have Scikit-learn installed on your machine. You can install it using pip:

```
pip install scikit-learn
```

## Importing the Required Libraries

To perform K-Means clustering, we need to import the necessary libraries. In addition to Scikit-learn, we will also use numpy and matplotlib for data manipulation and visualization, respectively. Here's how you can import them:

```python
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
```

## Loading the Data

Next, let's load the data that we want to cluster. For this example, let's say we have a dataset called `data` with two features, `X` and `Y`. To load the data into a numpy array, you can use the following code:

```python
data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
```

## Performing K-Means Clustering

Now that we have our data, we can perform K-Means clustering. To do this, we need to specify the number of clusters we want to obtain. Let's say we want to cluster our data into 2 groups.

```python
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
```

Once the clustering is complete, we can access the cluster labels for each data point using the `labels_` attribute:

```python
cluster_labels = kmeans.labels_
```

## Visualizing the Clusters

To visualize the clusters, we can plot the data points and color them based on their cluster label. Here's an example code snippet to create a scatter plot:

```python
plt.scatter(data[:, 0], data[:, 1], c=cluster_labels)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('K-Means Clustering')
plt.show()
```

## Conclusion

K-Means clustering is a powerful technique for grouping similar data points together. In this blog post, we learned how to perform K-Means clustering in Scikit-learn using Python. We covered the installation of Scikit-learn, importing necessary libraries, loading the data, performing the clustering, and visualizing the results.

Experiment with different datasets and parameters to gain a deeper understanding of K-Means clustering. Happy clustering!

#datascience #machinelearning