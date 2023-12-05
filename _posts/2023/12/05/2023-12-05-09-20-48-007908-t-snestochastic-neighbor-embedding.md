---
layout: post
title: "[python] t-SNE(Stochastic Neighbor Embedding)"
description: " "
date: 2023-12-05
tags: [python]
comments: true
share: true
---

t-SNE, which stands for Stochastic Neighbor Embedding, is a popular machine learning algorithm used for data visualization. It is commonly used to visualize high-dimensional data in a lower-dimensional space (typically 2D or 3D) while preserving the local structure of the data.

## How t-SNE works

The t-SNE algorithm works by creating a probability distribution over pairs of high-dimensional data points and a probability distribution over pairs of corresponding low-dimensional points. It then aims to minimize the divergence between these two distributions.

The steps involved in t-SNE are as follows:

1. Compute pairwise similarities: First, the algorithm calculates the similarity between each pair of data points in the high-dimensional space. This similarity is typically calculated using a Gaussian kernel function.

2. Construct conditional probabilities: The algorithm then constructs a probability distribution that represents the affinities between data points in the high-dimensional space. This is done by normalizing the pairwise similarities.

3. Construct joint probabilities: In this step, the algorithm constructs another probability distribution that represents the similarities between data points in the low-dimensional space. This is done using a Student's t-distribution with one degree of freedom.

4. Minimize the divergence: Finally, t-SNE minimizes the Kullback-Leibler divergence between the conditional and joint probability distributions. This is achieved by altering the positions of the low-dimensional points iteratively.

## Advantages of t-SNE

t-SNE offers several advantages over other dimensionality reduction techniques:

- Capture local structures: t-SNE can effectively capture the local structures in the data and preserve the clusters and neighborhoods of points.

- Non-linear relationships: Unlike linear techniques such as Principal Component Analysis (PCA), t-SNE can capture non-linear relationships and uncover more complex patterns in the data.

- Robustness to outliers: Compared to other techniques, t-SNE is more robust to the presence of outliers in the dataset.

## Usage in Python

To apply t-SNE in Python, you can use the `scikit-learn` library, which provides an implementation of t-SNE. Here's an example:

```python
from sklearn.manifold import TSNE

# Create a TSNE object with desired parameters
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200)

# Fit and transform the data to the lower-dimensional space
embedded_data = tsne.fit_transform(data)

# Plot the embedded data
plt.scatter(embedded_data[:, 0], embedded_data[:, 1])
plt.show()
```

In this example, `data` is the high-dimensional input data. The `n_components` parameter specifies the dimensionality of the embedded space (2D in this case). The `perplexity` parameter controls the balance between preserving local and global structures, while the `learning_rate` parameter determines the step size during optimization.

## Conclusion

t-SNE is a powerful algorithm for visualizing high-dimensional data in a lower-dimensional space. It can capture local structures, handle non-linear relationships, and is robust to outliers. By applying t-SNE, you can gain valuable insights into your data and uncover hidden patterns.

If you want to learn more about t-SNE, you can refer to the following references:

- [Original t-SNE paper](http://www.jmlr.org/papers/volume9/vandermaaten08a/vandermaaten08a.pdf)
- [scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html)

Happy exploring with t-SNE!