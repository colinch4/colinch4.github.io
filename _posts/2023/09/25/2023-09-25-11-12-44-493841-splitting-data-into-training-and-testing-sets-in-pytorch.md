---
layout: post
title: "Splitting data into training and testing sets in PyTorch"
description: " "
date: 2023-09-25
tags: [machinelearning, datascience]
comments: true
share: true
---

When working with machine learning models, it is essential to evaluate their performance on unseen data. This is typically done by splitting the dataset into training and testing sets. In this blog post, we will discuss how to split data into training and testing sets using PyTorch.

## Why Splitting Data is Important

Splitting data into training and testing sets allows us to assess the performance of our model on unseen data. This helps us understand how well our model generalizes to new examples. If we evaluate our model on the same data it was trained on, we may end up with overly optimistic performance metrics, leading to poor real-world performance.

## The PyTorch `Dataset` and `DataLoader` Classes

In PyTorch, the `Dataset` class is used to represent a dataset, while the `DataLoader` class is used to load the data in batches during training or testing. Before splitting the data, we need to create an instance of the `Dataset` class.

```python
import torch
from torch.utils.data import Dataset, DataLoader

# Create a custom dataset class
class MyDataset(Dataset):
    def __init__(self, features, labels):
        self.features = features
        self.labels = labels
        
    def __len__(self):
        return len(self.features)
    
    def __getitem__(self, idx):
        feature = self.features[idx]
        label = self.labels[idx]
        return feature, label

# Instantiate the dataset
dataset = MyDataset(features, labels)
```

## Splitting the Data

Now that we have our dataset, we can split it into training and testing sets. PyTorch provides the `random_split` function in the `torch.utils.data` module to split a dataset randomly.

```python
from torch.utils.data import random_split

# Define the ratios for splitting the dataset
train_ratio = 0.8
test_ratio = 0.2

# Calculate the number of samples in each split
train_size = int(train_ratio * len(dataset))
test_size = len(dataset) - train_size

# Split the dataset
train_set, test_set = random_split(dataset, [train_size, test_size])
```

In the code above, we define the ratios for splitting the dataset into training and testing sets. We then calculate the number of samples in each split based on these ratios. Finally, we use the `random_split` function to split the dataset into the desired sizes.

## Creating Data Loaders

After splitting the data, we can create `DataLoader` instances for the training and testing sets. The `DataLoader` class provides convenient methods for iterating over the data in batches.

```python
batch_size = 64

# Create data loaders for training and testing sets
train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True)
test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=False)
```

In the code snippet above, we specify the batch size for loading the data. We also set the `shuffle` parameter to `True` for the training set to randomly shuffle the samples in each epoch. For the testing set, we do not shuffle the samples.

## Conclusion

Splitting data into training and testing sets is an essential step in machine learning model development. In this blog post, we learned how to split data using PyTorch's `random_split` function and create `DataLoader` instances for the training and testing sets. By separating our data into these sets, we can evaluate the performance of our models accurately. 

#machinelearning #datascience