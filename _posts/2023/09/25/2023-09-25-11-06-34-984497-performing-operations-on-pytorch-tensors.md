---
layout: post
title: "Performing operations on PyTorch tensors"
description: " "
date: 2023-09-25
tags: [PyTorch, Tensors]
comments: true
share: true
---

## Creating Tensors

To get started, let's first create some tensors. We can create tensors in PyTorch using the `torch.tensor()` function.

```python
import torch

# Create a 1-dimensional tensor
tensor1d = torch.tensor([1, 2, 3, 4, 5])

# Create a 2-dimensional tensor
tensor2d = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Create a tensor with random values
random_tensor = torch.rand(3, 3)
```

## Basic Operations

### Addition

We can perform addition on tensors using the `torch.add()` function or the `+` operator.

```python
tensor_a = torch.tensor([1, 2, 3])
tensor_b = torch.tensor([4, 5, 6])

# Using the add() function
result = torch.add(tensor_a, tensor_b)  # [5, 7, 9]

# Using the + operator
result = tensor_a + tensor_b  # [5, 7, 9]
```

### Subtraction

Subtraction on tensors can be done using the `torch.subtract()` function or the `-` operator.

```python
tensor_a = torch.tensor([4, 5, 6])
tensor_b = torch.tensor([1, 2, 3])

# Using the subtract() function
result = torch.subtract(tensor_a, tensor_b)  # [3, 3, 3]

# Using the - operator
result = tensor_a - tensor_b  # [3, 3, 3]
```

### Multiplication

Multiplication can be performed on tensors using the `torch.mul()` function or the `*` operator.

```python
tensor_a = torch.tensor([2, 4, 6])
tensor_b = torch.tensor([2, 3, 4])

# Using the mul() function
result = torch.mul(tensor_a, tensor_b)  # [4, 12, 24]

# Using the * operator
result = tensor_a * tensor_b  # [4, 12, 24]
```

## Broadcasting

In cases where the sizes of the tensors being operated on are not equal, PyTorch performs broadcasting. This allows for element-wise operations on tensors of different shapes.

```python
tensor_a = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor_b = torch.tensor([1, 2, 3])

# Broadcasting tensor_b to the shape of tensor_a
result = tensor_a + tensor_b  # [[2, 4, 6], [5, 7, 9]]
```

## Conclusion

PyTorch provides a wide range of operations that can be performed on tensors, making it a powerful library for deep learning and numerical computations. In this blog post, we explored some basic operations such as addition, subtraction, and multiplication, as well as the concept of broadcasting. By mastering these operations, you'll be well on your way to leveraging the full potential of PyTorch for your machine learning projects.

## #PyTorch #Tensors