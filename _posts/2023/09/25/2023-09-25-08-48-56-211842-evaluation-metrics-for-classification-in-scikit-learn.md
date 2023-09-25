---
layout: post
title: "Evaluation metrics for classification in Scikit-learn"
description: " "
date: 2023-09-25
tags: [scikit, classification]
comments: true
share: true
---

When working on a classification problem in machine learning, it's important to evaluate the performance of your model using appropriate evaluation metrics. Scikit-learn, a popular machine learning library in Python, provides a range of evaluation metrics to assess the accuracy, precision, recall, and F1-score of your classification models.

Here, we'll discuss some commonly used evaluation metrics in Scikit-learn for classification tasks.

### 1. Accuracy

Accuracy is one of the simplest and most commonly used metrics to evaluate a classification model. It measures the overall correctness of the model's predictions. The accuracy score is calculated as the ratio of the correctly predicted samples to the total number of samples:

```python
from sklearn.metrics import accuracy_score

y_true = [0, 1, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1]

accuracy = accuracy_score(y_true, y_pred)
print(f"Accuracy: {accuracy}")
```

Output: Accuracy: 0.8

### 2. Precision, Recall, and F1-Score

In addition to accuracy, precision, recall, and F1-score are widely used evaluation metrics to measure the performance of classification models, especially in cases where the data is imbalanced.

- Precision: It quantifies the ability of the model to correctly identify the positive samples among the ones it predicts as positive.

- Recall: It measures the ability of the model to find all the positive samples.

- F1-score: It is the harmonic mean of precision and recall. F1-score provides a balanced measure that considers both precision and recall.

```python
from sklearn.metrics import precision_score, recall_score, f1_score

y_true = [0, 1, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1]

precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1-Score: {f1}")
```

Output:
Precision: 1.0
Recall: 0.6666666666666666
F1-Score: 0.8

These are just a few examples of evaluation metrics in Scikit-learn. Depending on the nature of your classification problem, you may also consider other metrics such as AUC-ROC, log loss, or confusion matrix.

Remember to choose the most appropriate evaluation metrics based on your specific problem and requirements to ensure accurate model assessment.

## #scikit-learn #classification-metrics