---
layout: post
title: "Decision boundaries in decision trees and random forests"
description: " "
date: 2023-10-25
tags: [references]
comments: true
share: true
---

Decision trees and random forests are widely used machine learning algorithms that are capable of both classification and regression tasks. One interesting aspect of these algorithms is how they create decision boundaries to separate different classes or make predictions on the input data.

## Decision Trees

Decision trees are hierarchical models that make sequential decisions at each node to partition the feature space. These decisions are based on certain features and thresholds, allowing the tree to split the data into smaller homogeneous subsets.

The decision boundaries in decision trees are axis-parallel, which means they are always aligned with the coordinate axes. Each split in the decision tree creates a vertical or horizontal boundary in the feature space, dividing it into distinct regions corresponding to different predictions or classes.

![Decision Tree](decision_tree.png)

In the image above, the decision tree partitions the feature space into regions labeled A, B, and C. Each region represents a different prediction or class label assigned by the decision tree. The decision boundaries are represented by the dashed lines.

## Random Forests

Random forests, on the other hand, are based on an ensemble of decision trees. Instead of relying on a single decision tree, random forests combine the predictions of multiple decision trees to make more accurate and robust predictions.

Each decision tree in a random forest is trained on a random subset of the training data and a random subset of the available features. This variation in training data and features contributes to the diversity of the trees in the forest.

The decision boundaries in random forests are more complex compared to individual decision trees. The ensemble of decision trees works together to create decision boundaries that are better at capturing the underlying patterns and relationships in the data. 

![Random Forest](random_forest.png)

In the image above, the random forest creates decision boundaries that are highly non-linear. It combines the decision boundaries of multiple decision trees to form a more complex decision boundary that can better separate different classes or predict regression values.

## Conclusion

Decision trees and random forests are powerful machine learning algorithms that create decision boundaries to classify or predict input data. Decision trees have axis-parallel decision boundaries, while random forests generate more complex decision boundaries by combining multiple decision trees.

Understanding the decision boundaries created by these algorithms can provide insights into how they make predictions and classify data. This knowledge can help in interpreting and debugging the models, as well as exploring their limitations and potential improvements.

#references
- Decision Trees - https://en.wikipedia.org/wiki/Decision_tree
- Random Forests - https://en.wikipedia.org/wiki/Random_forest