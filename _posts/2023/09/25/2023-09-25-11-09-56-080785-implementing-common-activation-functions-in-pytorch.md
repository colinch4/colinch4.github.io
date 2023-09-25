---
layout: post
title: "Implementing common activation functions in PyTorch"
description: " "
date: 2023-09-25
tags: [pytorch, deeplearning]
comments: true
share: true
---

Activation functions are an essential component in neural networks as they introduce non-linearity, allowing the network to learn complex patterns and relationships in data. PyTorch, a popular deep learning library, provides various built-in activation functions that can be easily integrated into your neural network models. In this blog post, we will explore how to implement some of the common activation functions in PyTorch.

## 1. ReLU (Rectified Linear Unit)

ReLU is one of the most widely used activation functions in deep learning due to its simplicity and effectiveness. It sets all negative values in the input tensor to 0, while leaving positive values unchanged.

```python
import torch
import torch.nn as nn

# Implementing ReLU activation function
relu = nn.ReLU()
```

## 2. Sigmoid

The sigmoid function maps any input value to a range between 0 and 1. It is commonly used in binary classification tasks as it can represent the probability of a sample belonging to a certain class.

```python
import torch
import torch.nn as nn

# Implementing Sigmoid activation function
sigmoid = nn.Sigmoid()
```

## 3. Tanh (Hyperbolic Tangent)

Tanh is another activation function that squashes the input tensor to a range between -1 and 1. It is often used in recurrent neural networks (RNNs) due to its ability to handle gradient explosion/vanishing problems.

```python
import torch
import torch.nn as nn

# Implementing Tanh activation function
tanh = nn.Tanh()
```

## 4. Softmax

Softmax is a popular activation function for multi-class classification tasks. It normalizes the input tensor into a probability distribution, where the sum of all output values is equal to 1.

```python
import torch
import torch.nn as nn

# Implementing Softmax activation function
softmax = nn.Softmax(dim=1)
```

These are just a few examples of common activation functions you can implement in PyTorch. However, PyTorch offers many other activation functions such as LeakyReLU, ELU, and more. Experimenting with different activation functions can help improve the performance of your neural network models depending on the nature of your specific task or data.

#pytorch #deeplearning