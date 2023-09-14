---
layout: post
title: "Transfer learning for image classification in PyTorch"
description: " "
date: 2023-09-14
tags: [DeepLearning]
comments: true
share: true
---

Image classification is a fundamental task in computer vision, and deep learning models have significantly improved its accuracy. However, training a deep learning model from scratch can be a time-consuming and resource-intensive process. Transfer learning offers a solution by leveraging pre-trained models that have been trained on large datasets.

In this blog post, we will explore how to perform transfer learning for image classification using PyTorch, one of the most popular deep learning frameworks. We will use a pre-trained model as a feature extractor and build a classifier on top of it.

## What is Transfer Learning?

Transfer learning is a technique in which a model trained on one task is re-purposed for another related task. The idea is that the pre-trained model has already learned meaningful features from a large dataset, which can be useful for other tasks as well. By utilizing transfer learning, we can benefit from both the pre-trained model's feature extraction capabilities and the reduced training time.

## Getting Started

Before diving into the implementation, make sure you have PyTorch installed on your machine. You can install it using pip:

```python
pip install torch
```

We will also need torchvision, which provides various datasets and pretrained models:

```python
pip install torchvision
```

## Loading and Preprocessing the Dataset

To demonstrate transfer learning, let's use the CIFAR-10 dataset, which consists of 60,000 32x32 color images in 10 classes. We can easily load the dataset using torchvision:

```python
from torchvision import datasets, transforms

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

train_dataset = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
test_dataset = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)
```

Here, we are applying two transformations: converting the images to tensors and normalizing the pixel values. Normalization helps in reducing the differences in scale and brings the pixel values to a common range.

## Loading a Pre-trained Model

PyTorch provides a wide range of pre-trained models, such as ResNet, VGG, and DenseNet. For this example, let's use the ResNet-18 model:

```python
import torchvision.models as models

model = models.resnet18(pretrained=True)
```

By setting `pretrained=True`, we load the pre-trained weights of the model. It is worth mentioning that these pre-trained models are trained on the ImageNet dataset, which consists of millions of images from 1000 classes.

## Customizing the Classifier

The pre-trained ResNet model has a classifier at the end that is designed for the ImageNet dataset. Since our task is to classify CIFAR-10 images, we need to replace the classifier with a new one that suits our needs.

```python
import torch.nn as nn

num_features = model.fc.in_features
model.fc = nn.Linear(num_features, 10)
```

Here, we replace the last fully-connected layer (`model.fc`) with a new linear layer that outputs 10 classes. `num_features` is the number of input features to the last fully-connected layer, which we obtain using `model.fc.in_features`.

## Training the Model

Finally, we need to train the model on our dataset. We can use standard training techniques such as mini-batch gradient descent and backpropagation.

```python
import torch.optim as optim

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
criterion = nn.CrossEntropyLoss()

def train(model, train_loader, optimizer, criterion, device):
    model.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, target)
        loss.backward()
        optimizer.step()

def test(model, test_loader, criterion, device):
    model.eval()
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            data, target = data.to(device), target.to(device)
            
            output = model(data)
            test_loss += criterion(output, target).item()
            pred = output.argmax(dim=1, keepdim=True)
            correct += pred.eq(target.view_as(pred)).sum().item()
    
    test_loss /= len(test_loader.dataset)
    accuracy = 100.0 * correct / len(test_loader.dataset)
    
    print(f"Test loss: {test_loss:.4f}, Accuracy: {accuracy:.2f}%")

# Train the model
train(model, train_loader, optimizer, criterion, device)

# Evaluate the model
test(model, test_loader, criterion, device)
```

Note that in the code above, we are using the GPU to accelerate the training process if it is available (`torch.cuda.is_available()`). We also define the optimizer (Stochastic Gradient Descent) and the loss function (CrossEntropyLoss).

## Conclusion

Transfer learning is a powerful technique that allows us to leverage pre-trained models for image classification tasks. In this blog post, we have learned how to perform transfer learning for image classification using PyTorch. We loaded and preprocessed the dataset, loaded a pre-trained ResNet model, customized the classifier, and finally trained and evaluated the model.

By utilizing transfer learning, we can achieve better accuracy with less training time and computational resources. It is a valuable tool in the deep learning toolkit and can be applied to various real-world image classification problems.

#AI #DeepLearning