---
layout: post
title: "Entropy in decision trees"
description: " "
date: 2023-10-25
tags: [References]
comments: true
share: true
---

Decision Trees are powerful machine learning algorithms used for classification and regression tasks. They work by recursively partitioning the feature space based on a series of decision rules. One important aspect of decision trees is the concept of entropy, which plays a key role in determining the best split at each node of the tree.

## What is Entropy?

Entropy is a measure of impurity or randomness in a dataset. In the context of decision trees, it quantifies the uncertainty of the target variable given the values of the input features. The goal of a decision tree is to minimize entropy, which corresponds to maximizing the information gain at each split.

## Calculating Entropy

To calculate entropy, we use the formula:

```
Entropy = - Σ (P_i * log2(P_i))
```

where P_i is the proportion of the samples that belong to class i in a particular node.

## Information Gain

Information gain is the reduction in entropy achieved by splitting the dataset based on a particular feature. It helps us determine the most informative feature to use for splitting. The information gain is calculated using the formula:

```
Information Gain = Entropy(parent_node) - Σ [(Proportion_of_samples_in_child_node) * Entropy(child_node)]
```

## Example

Let's illustrate the calculation of entropy with a simple example. Suppose we have a dataset with binary classification, where 70% of the samples belong to class A and 30% belong to class B. The entropy of the parent node can be calculated as:

```
Entropy(parent) = -(0.7 * log2(0.7)) - (0.3 * log2(0.3)) ≈ 0.881 
```

Now, let's say we split the dataset based on feature X, where 80% of the samples have X = 0 and 20% have X = 1. For the child node with X = 0, we have 60% of class A and 40% of class B. For the child node with X = 1, we have 100% of class A and 0% of class B. The entropy of the child nodes can be calculated as:

```
Entropy(child_X=0) = -(0.6 * log2(0.6)) - (0.4 * log2(0.4)) ≈ 0.971
Entropy(child_X=1) = 0 (since all samples belong to the same class)
```

Finally, we calculate the information gain:

```
Information Gain = Entropy(parent) - ((0.8 * Entropy(child_X=0)) + (0.2 * Entropy(child_X=1)))
                = 0.881 - ((0.8 * 0.971) + (0.2 * 0))
                ≈ 0.19 
```

In this example, the information gain for splitting based on feature X is approximately 0.19.

## Conclusion

Entropy is a fundamental concept in decision trees that quantifies the impurity of a dataset. By using entropy and information gain, decision trees are able to make informed decisions when creating splits in the tree. Understanding the role of entropy can help you better utilize decision trees in your machine learning projects.

#References:

1. Decision Trees - Concepts, Methods, and Applications by Jiye Liang and Rongxin Xu
2. "Decision Trees" by Trevor Hastie, Robert Tibshirani, and Jerome Friedman