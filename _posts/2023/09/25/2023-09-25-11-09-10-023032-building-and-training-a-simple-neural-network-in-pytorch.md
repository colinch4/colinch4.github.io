---
layout: post
title: "Building and training a simple neural network in PyTorch"
description: " "
date: 2023-09-25
tags: [PyTorch]
comments: true
share: true
---

Neural networks have become a popular tool for solving complex problems in various fields. With the availability of libraries like PyTorch, building and training neural networks has become easier and more efficient. In this tutorial, we will walk through the process of building and training a simple neural network using PyTorch.

## Installation
Before we begin, make sure you have PyTorch installed on your machine. You can install it using pip:

```shell
pip install torch
```

## Importing Required Libraries
First, let's import the required libraries for building and training our neural network:

```python
import torch
import torch.nn as nn
import torch.optim as optim
```

## Defining the Neural Network Architecture
Next, we need to define the architecture of our neural network. For this example, we will create a simple feedforward neural network with two hidden layers:

```python
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.fc1 = nn.Linear(784, 128)
        self.fc2 = nn.Linear(128, 64)
        self.fc3 = nn.Linear(64, 10)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x
```

In the `__init__` method, we define the layers of our neural network using `nn.Linear`. The `forward` method specifies the forward pass of the neural network, i.e., how the input flows through the layers.

## Loading and Preparing Data
To train our neural network, we need a dataset. For this tutorial, we will use the popular MNIST dataset, which contains images of handwritten digits. We can load the dataset using `torchvision`:

```python
import torchvision
import torchvision.transforms as transforms

transform = transforms.Compose([
    transforms.ToTensor(), # Converts PIL image or numpy array to Tensor
    transforms.Normalize((0.5,), (0.5,)) # Normalize the image data
])

trainset = torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

testset = torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
testloader = torch.utils.data.DataLoader(testset, batch_size=64, shuffle=False)
```

Here, we define data transformations using `transforms.Compose` and apply them to our training and testing datasets. We also define data loaders to load the datasets in batches for efficient training.

## Training the Neural Network
Now that our data is loaded and preprocessed, we can move on to training our neural network:

```python
net = NeuralNetwork()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

for epoch in range(10):
    running_loss = 0.0
    for i, data in enumerate(trainloader, 0):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = net(inputs.view(-1, 784))
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        
        running_loss += loss.item()
        if i % 200 == 199:
            print(f"[Epoch {epoch+1}, Batch {i+1}] Loss: {running_loss / 200:.3f}")
            running_loss = 0.0
```

In the code above, we define the neural network, loss function (`nn.CrossEntropyLoss`), and optimizer (`optim.SGD`). We then iterate over the training data in batches, calculate the loss, perform backpropagation, and update the network parameters using the optimizer.

## Evaluating the Neural Network
After training the neural network, we can evaluate its performance on the test dataset:

```python
correct = 0
total = 0

with torch.no_grad():
    for data in testloader:
        inputs, labels = data
        outputs = net(inputs.view(-1, 784))
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = correct / total
print(f"Test Accuracy: {accuracy*100:.2f}%")
```

Here, we iterate over the test dataset, make predictions using the trained network, and calculate the accuracy by comparing the predictions with the ground truth labels.

## Conclusion
In this tutorial, we learned how to build and train a simple neural network using PyTorch. We covered the steps of defining the network architecture, loading and preparing the data, training the network, and evaluating its performance. With PyTorch's simplicity and flexibility, you can easily experiment and build more complex neural networks for various applications.

#AI #PyTorch