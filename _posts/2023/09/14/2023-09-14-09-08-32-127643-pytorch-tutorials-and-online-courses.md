---
layout: post
title: "PyTorch tutorials and online courses"
description: " "
date: 2023-09-14
tags: [Python, DeepLearning, PyTorch]
comments: true
share: true
---

If you're interested in learning about deep learning and prefer working with Python, PyTorch is a popular choice. Developed by Facebook's AI Research lab, PyTorch is an open-source machine learning library that provides a Pythonic interface for creating and training neural networks.

In this tutorial, we'll introduce you to PyTorch and guide you through the process of building a simple deep learning model. No prior knowledge of PyTorch is required, making it suitable for beginners.

## Installation and Setup

Before we begin, let's set up the PyTorch environment. You can install PyTorch using pip or conda, depending on your preference and operating system. Visit the PyTorch website [(www.pytorch.org)](www.pytorch.org) for detailed installation instructions.

Once you have PyTorch installed, you're ready to start coding!

## Building a Neural Network

Let's start by understanding the basics of PyTorch and building a simple neural network model. We'll use the MNIST dataset, which consists of handwritten digits, to train our model to classify digits.

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Define the neural network architecture
class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 64)
        self.relu1 = nn.ReLU()
        self.fc2 = nn.Linear(64, 10)
        
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu1(x)
        x = self.fc2(x)
        return x

# Create an instance of the neural network
model = Net()

# Define the loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
```

## Training the Model

Now that we have our model architecture defined and the necessary components in place, let's move on to training the model using the MNIST dataset.

```python
# Training loop
for epoch in range(10):
    running_loss = 0.0
    for i, data in enumerate(train_loader):
        inputs, labels = data
        
        optimizer.zero_grad()
        
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        
    print(f"Epoch {epoch+1} - Loss: {running_loss/len(train_loader)}")
```

## Evaluating the Model

After training the model, it's essential to evaluate its performance on unseen test data. Let's test our model using the MNIST test dataset.

```python
correct = 0
total = 0

with torch.no_grad():
    for data in test_loader:
        inputs, labels = data
        outputs = model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()
        
print(f"Accuracy on test data: {(correct/total)*100}%")
```

## Conclusion and Further Exploration

In this tutorial, we introduced you to PyTorch and guided you through the process of building a simple neural network model using the MNIST dataset. You have learned how to define the architecture, train the model, and evaluate its performance.

PyTorch offers extensive documentation and a vibrant community, making it easy to explore further with online tutorials and courses. If you're eager to go deeper into PyTorch and explore advanced topics like convolutional neural networks and transfer learning, consider enrolling in online courses offered by platforms like Coursera, Udemy, or edX.

#Python #DeepLearning #PyTorch