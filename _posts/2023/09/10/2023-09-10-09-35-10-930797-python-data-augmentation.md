---
layout: post
title: "[Python] Data augmentation"
description: " "
date: 2023-09-10
tags: [basic]
comments: true
share: true
---

Data augmentation is a technique used to artificially increase the size of a dataset by creating new training examples through various transformations of the existing data. It is commonly used in machine learning and computer vision tasks to improve model performance and prevent overfitting.

In this blog post, we will explore different data augmentation techniques in Python and demonstrate how they can be implemented using the popular `imgaug` library.

## Install `imgaug`

To get started, we need to install the `imgaug` library. Run the following command in your terminal:

```python
pip install imgaug
```

## Import Required Libraries

```python
import imgaug.augmenters as iaa
import numpy as np
import cv2
```

## Load and Display Image

Before applying data augmentation, let's first load and display an image that we will use as an example:

```python
image = cv2.imread('image.jpg')
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Data Augmentation Techniques

### 1. Rotation

Rotation randomly rotates the image within a specified range. Here's an example of how to apply rotation augmentation using `imgaug`:

```python
augmentation = iaa.Affine(rotate=(-45, 45))
image_augmented = augmentation.augment_image(image)

cv2.imshow('Augmented Image - Rotation', image_augmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 2. Horizontal Flip

Horizontal flip randomly flips the image horizontally. Here's how to apply horizontal flip augmentation using `imgaug`:

```python
augmentation = iaa.Fliplr(0.5)
image_augmented = augmentation.augment_image(image)

cv2.imshow('Augmented Image - Horizontal Flip', image_augmented)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Conclusion

Data augmentation is a powerful technique that can help improve the performance and generalization ability of machine learning models. In this blog post, we explored two commonly used data augmentation techniques, rotation and horizontal flip, using the `imgaug` library in Python.

Using `imgaug`, you can further customize and combine various augmentations to create a diverse and larger training dataset, leading to more robust and accurate models.

Remember to experiment with different augmentation techniques and adjust their parameters based on your specific dataset and problem. Happy augmenting!

**NOTE:** Remember to always respect the licenses and copyrights of the images you use for data augmentation purposes.