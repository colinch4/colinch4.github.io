---
layout: post
title: "Different ways to create PyTorch tensors"
description: " "
date: 2023-09-25
tags: [PyTorch, Tensors]
comments: true
share: true
---

PyTorch is a popular open-source machine learning framework that provides a powerful library for creating and manipulating tensors. Tensors are multi-dimensional arrays used for storing and manipulating numerical data efficiently. In this blog post, we will explore different ways to create PyTorch tensors.

## Method 1: Using the `torch.Tensor()` constructor

The `torch.Tensor()` constructor is the most basic method for creating tensors in PyTorch. You can create an uninitialized tensor of a specific size by passing the desired dimensions as arguments. Here's an example:

```python
import torch

# Create a tensor of size (3, 2)
tensor1 = torch.Tensor(3, 2)
print(tensor1)
```

Output:
```
tensor([[0.0000e+00, 0.0000e+00],
        [1.2612e-44, 0.0000e+00],
        [1.2612e-44, 1.2612e-44]])
```

## Method 2: Using `torch.zeros()` or `torch.ones()`

`torch.zeros()` and `torch.ones()` are convenient functions for creating tensors filled with zeros or ones, respectively. You can pass the desired size of the tensor as arguments. Here's an example:

```python
import torch

# Create a tensor of size (2, 3) filled with zeros
tensor2 = torch.zeros(2, 3)
print(tensor2)
```

Output:
```
tensor([[0., 0., 0.],
        [0., 0., 0.]])
```

```python
import torch

# Create a tensor of size (2, 3) filled with ones
tensor3 = torch.ones(2, 3)
print(tensor3)
```

Output:
```
tensor([[1., 1., 1.],
        [1., 1., 1.]])
```

## Method 3: Using `torch.arange()`

`torch.arange()` function creates a tensor containing values from a given range. You can specify the start, end, and step size of the range. Here's an example:

```python
import torch

# Create a tensor with values from 0 to 9
tensor4 = torch.arange(10)
print(tensor4)
```

Output:
```
tensor([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

## Method 4: Using `torch.linspace()` or `torch.logspace()`

`torch.linspace()` and `torch.logspace()` functions create tensors with values linearly or logarithmically spaced between two points. You can specify the start, end, and the number of steps between the points. Here's an example:

```python
import torch

# Create a tensor with 5 linearly spaced values between 0 and 1
tensor5 = torch.linspace(0, 1, 5)
print(tensor5)
```

Output:
```
tensor([0.0000e+00, 2.5000e-01, 5.0000e-01, 7.5000e-01, 1.0000e+00])
```

```python
import torch

# Create a tensor with 4 logarithmically spaced values between 1e-2 and 1e2
tensor6 = torch.logspace(start=-2, end=2, steps=4)
print(tensor6)
```

Output:
```
tensor([1.0000e-02, 1.0000e+00, 1.0000e+02, 1.0000e+04])
```

These are just a few methods for creating tensors in PyTorch. There are many more functions and techniques available depending on your specific needs. Experiment with these methods and explore the PyTorch documentation for more information. #PyTorch #Tensors