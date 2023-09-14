---
layout: post
title: "Image classification with PyTorch"
description: " "
date: 2023-09-14
tags: [pytorch, imageclassification]
comments: true
share: true
---

Image classification is a fundamental task in computer vision, where the goal is to categorize an image into predefined classes or categories. PyTorch, a popular deep learning framework, provides powerful tools and libraries to build and train image classification models efficiently. In this blog post, we will explore how to create an image classifier using PyTorch.

## 1. Getting Started

First, we need to set up our development environment. Make sure you have Python installed on your machine. Next, install PyTorch by running the following command:

```bash
pip install torch torchvision
```

This will install the necessary packages for image classification with PyTorch.

## 2. Dataset Preparation

To train an image classifier, we need a labeled dataset of images. There are many publicly available datasets for image classification, such as CIFAR-10, ImageNet, or MNIST. For the purpose of this blog post, let's use the CIFAR-10 dataset, which consists of 60,000 32x32 color images in 10 classes.

You can download the CIFAR-10 dataset using the torchvision package:

```python
import torchvision.datasets as datasets

# Download CIFAR-10 dataset
train_dataset = datasets.CIFAR10(root='./data', train=True, download=True)
test_dataset = datasets.CIFAR10(root='./data', train=False, download=True)
```

## 3. Model Architecture

Next, we need to define our image classification model. PyTorch allows us to create custom models by subclassing the `torch.nn.Module` class. Let's create a simple convolutional neural network (CNN) model for image classification:

```python
import torch.nn as nn

class MyClassifier(nn.Module):
    def __init__(self, num_classes):
        super(MyClassifier, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=1, padding=1)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        self.fc = nn.Linear(8*8*32, num_classes)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        x = self.conv2(x)
        x = self.relu2(x)
        x = self.pool2(x)
        # Flatten the feature maps
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x
```

## 4. Training the Model

Now let's train our image classifier using the CIFAR-10 dataset. We will use the cross-entropy loss function and the stochastic gradient descent (SGD) optimizer:

```python
import torch.optim as optim

# Create an instance of our image classifier
model = MyClassifier(num_classes=10)

# Define loss function and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# Training loop
for epoch in range(10):
    running_loss = 0.0
    for images, labels in train_dataset:
        # Zero the gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)

        # Backward pass and optimization
        loss.backward()
        optimizer.step()

        # Track the loss
        running_loss += loss.item()
    print(f"Epoch {epoch+1} loss: {running_loss/len(train_dataset)}")
```

## 5. Evaluating the Model

Once the model is trained, we can evaluate its performance on the test dataset:

```python
correct = 0
total = 0

# Disable gradient computation
with torch.no_grad():
    for images, labels in test_dataset:
        # Predict the class labels
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

# Calculate the accuracy
accuracy = correct / total
print(f"Accuracy: {accuracy}")
```

## Conclusion

In this blog post, we learned how to perform image classification with PyTorch. We covered the steps from dataset preparation to model training and evaluation. PyTorch provides a flexible and efficient framework for building image classifiers, making it ideal for a wide range of computer vision tasks. So go ahead, start exploring and building your own image classification models using PyTorch!

#pytorch #imageclassification