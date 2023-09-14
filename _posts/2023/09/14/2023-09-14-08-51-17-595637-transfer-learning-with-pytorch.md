---
layout: post
title: "Transfer learning with PyTorch"
description: " "
date: 2023-09-14
tags: [deeplearning, pytorch]
comments: true
share: true
---

Transfer learning is a technique in deep learning where a pre-trained model, trained on a large dataset, is used as a starting point for training a new model on a different but related dataset. This approach can save significant time and computational resources, especially when working with limited data.

In this post, we will explore how to perform transfer learning using PyTorch, a popular deep learning framework. We will cover the following steps:

1. Load and preprocess the pre-trained model.
2. Customize the model for the new task.
3. Train the model on the new dataset.
4. Evaluate the performance of the transferred model.

## Loading and Preprocessing the Pre-trained Model

PyTorch provides various pre-trained models, such as ResNet, VGG, and Inception, which have been trained on large-scale image classification tasks. To use a pre-trained model, we first need to load it and replace the last fully connected layer with a new one that matches the number of classes in our new dataset.

```python
import torch
from torchvision import models

# Load the pre-trained ResNet model
model = models.resnet18(pretrained=True)

# Freeze all the layers except the last one
for param in model.parameters():
    param.requires_grad = False

# Replace the last fully connected layer with a new one
num_classes = 10  # replace with the number of classes in your dataset
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
```

## Customizing the Model for the New Task

Once we have loaded the pre-trained model and replaced the last fully connected layer, we can customize the model further by modifying the remaining layers according to our specific task. For example, we can fine-tune the model by unfreezing some of the layers and allowing them to be trained on the new dataset.

```python
# Unfreeze the last few layers for fine-tuning
unfreeze_layers = 5  # replace with the number of layers to unfreeze
for param in model.layer[-unfreeze_layers:].parameters():
    param.requires_grad = True
```

## Training the Model on the New Dataset

After customizing the model, we can start training it on the new dataset. We will need to define a loss function and an optimizer, and then iterate over the training dataset for multiple epochs.

```python
loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

for epoch in range(num_epochs):
    for images, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(images)
        loss = loss_fn(outputs, labels)
        loss.backward()
        optimizer.step()
```

## Evaluating the Performance of the Transferred Model

Finally, we can evaluate the performance of the transferred model on the test dataset. We can calculate metrics such as accuracy, precision, and recall to assess the model's performance.

```python
correct = 0
total = 0

with torch.no_grad():
    for images, labels in test_loader:
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

accuracy = correct / total
print("Accuracy: {:.2f}%".format(accuracy * 100))
```

In conclusion, transfer learning is a powerful technique that allows us to leverage pre-trained models and adapt them to new tasks with minimal effort. By following the steps outlined in this post, you can easily implement transfer learning using PyTorch and achieve impressive results on your own datasets. #deeplearning #pytorch