---
layout: post
title: "Hierarchical Clustering in Scikit-learn"
description: " "
date: 2023-09-25
tags: [machinelearning, datascience]
comments: true
share: true
---

In this blog post, I will introduce hierarchical clustering and demonstrate how to use it in Scikit-learn, a powerful machine learning library in Python.

## What is Hierarchical Clustering?

Hierarchical clustering builds a hierarchy of clusters by recursively dividing or merging them based on their proximity or similarity. The result is a tree-like structure called a dendrogram, which shows the relationships between the clusters.

There are two main types of hierarchical clustering: agglomerative and divisive. Agglomerative clustering starts with each data point as a separate cluster and gradually merges them together, while divisive clustering starts with all data points in a single cluster and recursively splits them.

## Using Hierarchical Clustering in Scikit-learn

Scikit-learn provides a convenient implementation of hierarchical clustering through its `AgglomerativeClustering` class. Let's see how we can use it to cluster a dataset.

First, we need to import the necessary modules:
```python
from sklearn.cluster import AgglomerativeClustering
import numpy as np
```

Next, we define our dataset. For the purpose of this example, let's generate a random dataset with 100 points:
```python
X = np.random.rand(100, 2)
```

Now, we can create an instance of `AgglomerativeClustering` and fit it to our dataset:
```python
clustering = AgglomerativeClustering(n_clusters=3)
clustering.fit(X)
```

The `n_clusters` parameter specifies the number of clusters we want to obtain. In this case, we are setting it to 3.

To get the predicted labels for each data point, we can call the `labels_` attribute of the clustering object:
```python
labels = clustering.labels_
```

Finally, we can visualize the clusters using a scatter plot. Here's an example using Matplotlib:
```python
import matplotlib.pyplot as plt

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.show()
```

This will display a scatter plot where each point is colored according to its assigned cluster label.

## Conclusion

Hierarchical clustering is a powerful technique for grouping similar data points together. In this blog post, we learned how to perform hierarchical clustering using the `AgglomerativeClustering` class in Scikit-learn. By following these steps, you can easily apply hierarchical clustering to your own datasets in Python.

#machinelearning #datascience