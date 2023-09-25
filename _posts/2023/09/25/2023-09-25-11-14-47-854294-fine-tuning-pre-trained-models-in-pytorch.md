---
layout: post
title: "Fine-tuning pre-trained models in PyTorch"
description: " "
date: 2023-09-25
tags: [DeepLearning, PyTorch]
comments: true
share: true
---

With the advent of deep learning and the availability of pre-trained models, fine-tuning has become a common practice in the field of computer vision. Fine-tuning allows us to leverage the knowledge learned by pre-trained models on large datasets and adapt them to our specific task or dataset.

In this blog post, we will explore how to fine-tune pre-trained models using PyTorch, one of the most popular deep learning frameworks. We will cover the following steps:

1. **Loading Pre-Trained Models**: We will discuss how to load pre-trained models, such as VGG, ResNet, or MobileNet, using PyTorch's model zoo.

2. **Freezing the Model**: We will freeze the layers of the pre-trained model to prevent them from being updated during training. This ensures that we retain the knowledge learned by the pre-trained model.

3. **Replacing the Classifier**: We will replace the classifier head of the pre-trained model with a new one tailored to our specific task, such as image classification or object detection.

4. **Training the Model**: We will enable training of the fine-tuned model and update the parameters of the new classifier head while keeping the pre-trained weights fixed.

5. **Evaluating the Model**: Finally, we will evaluate the performance of the fine-tuned model on a validation set to assess its effectiveness.

## Loading Pre-Trained Models

PyTorch provides a model zoo that contains pre-trained models for various computer vision tasks. We can easily load a pre-trained model using a few lines of code:

```python
import torchvision.models as models

model = models.resnet50(pretrained=True)
```

Here, we load the ResNet-50 model with pre-trained weights. You can replace `resnet50` with other models like `vgg16`, `densenet121`, or `mobilenet_v2` depending on your requirements.

## Freezing the Model

To freeze the layers of the pre-trained model, we set `requires_grad` to `False` for all the parameters of the model:

```python
for param in model.parameters():
    param.requires_grad = False
```

By freezing the model, we ensure that the gradients are not computed for these layers during backpropagation, and their weights remain unchanged.

## Replacing the Classifier

To adapt the pre-trained model to our specific task, we need to replace the classifier head with a new one. The classifier head is responsible for making predictions based on the features extracted by the pre-trained layers.

```python
model.fc = nn.Linear(model.fc.in_features, num_classes)
```

Here, we replace the fully connected layer (`model.fc`) with a new linear layer that predicts the number of classes in our task. Replace `num_classes` with the appropriate number for your task.

## Training the Model

After replacing the classifier, we can train the model using our own dataset. We need to enable the gradients for the parameters of the new classifier head, while keeping the pre-trained layers frozen:

```python
optimizer = optim.SGD(model.fc.parameters(), lr=0.001, momentum=0.9)
```

Here, we only optimize the parameters of the new classifier head using stochastic gradient descent (SGD) optimizer. Adjust the learning rate and momentum based on your requirements.

## Evaluating the Model

Once the model is trained, we can evaluate its performance on a validation set. This helps us assess how well the fine-tuned model generalizes to unseen data:

```python
model.eval()

with torch.no_grad():
    for images, labels in validation_loader:
        outputs = model(images)
        # Perform evaluation metrics calculation
```

Here, we set the model to evaluation mode (`model.eval()`) and iterate over the validation dataset to obtain predictions. We then perform the necessary evaluation metrics calculations using the predicted outputs.

## Conclusion

Fine-tuning pre-trained models in PyTorch is a powerful technique to leverage the knowledge learned from large datasets. By following these steps, you can adapt pre-trained models to your specific task and achieve better results with less training data. Fine-tuning helps in overcoming the limitations of limited data availability and reduces the computational cost required for training deep learning models.

#DeepLearning #PyTorch