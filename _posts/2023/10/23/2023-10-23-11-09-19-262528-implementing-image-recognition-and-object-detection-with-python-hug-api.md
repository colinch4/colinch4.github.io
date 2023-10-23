---
layout: post
title: "Implementing image recognition and object detection with Python Hug API"
description: " "
date: 2023-10-23
tags: []
comments: true
share: true
---

In this blog post, we will explore how to implement image recognition and object detection using the Python Hug API. Image recognition and object detection are widely used in various applications such as self-driving cars, surveillance systems, and augmented reality.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Image Recognition](#image-recognition)
- [Object Detection](#object-detection)
- [Conclusion](#conclusion)

## Introduction
Python Hug is a powerful API framework that allows us to easily create and deploy APIs with minimal code. It provides a simple and intuitive way to build RESTful APIs, making it a perfect choice for implementing image recognition and object detection APIs.

## Getting Started
To get started, let's first install Python Hug by running the following command:
```shell
pip install hug
```

Once installed, we can create a new Python file, `app.py`, and import the necessary modules:

```python
import hug
from PIL import Image
import numpy as np
import tensorflow as tf
```

We will be using the `PIL` library to handle image processing and the `tensorflow` library for performing image recognition and object detection.

## Image Recognition
To implement image recognition, we need to first load a pre-trained deep learning model. For this example, we will be using the popular InceptionV3 model. We can load the model using the following code:

```python
model = tf.keras.applications.InceptionV3(weights='imagenet')
```

Next, we define the API endpoint for image recognition using the Hug decorator:

```python
@hug.post('/recognize')
def recognize_image(image: hug.types.File) -> str:
    img = Image.open(image)
    img = img.resize((299, 299))
    img_arr = np.expand_dims(np.array(img), axis=0)
    img_arr_processed = tf.keras.applications.inception_v3.preprocess_input(img_arr)
    predictions = model.predict(img_arr_processed)
    decoded_predictions = tf.keras.applications.inception_v3.decode_predictions(predictions, top=3)[0]
    result = ', '.join(f'{label}: {round(float(score) * 100, 2)}%' for (_, label, score) in decoded_predictions)
    return result
```

This API endpoint expects an image file as input and returns the top 3 predicted labels with their respective confidence scores.

## Object Detection
For implementing object detection, we can use the SSD Mobilenet model, which is a fast and accurate model for real-time object detection. We load the model using the following code:

```python
model = tf.saved_model.load('ssd_mobilenet_v2_coco_2018_03_29/saved_model')
```

Next, we define the API endpoint for object detection:

```python
@hug.post('/detect')
def detect_objects(image: hug.types.File) -> dict:
    img = Image.open(image)
    img = img.convert('RGB')
    img_arr = np.array(img)
    input_tensor = tf.convert_to_tensor(img_arr)
    input_tensor = input_tensor[tf.newaxis, ...]
    detections = model(input_tensor)
    num_detections = int(detections.pop('num_detections'))
    detections = {key: value[0, :num_detections].numpy() for key, value in detections.items()}
    detections['num_detections'] = num_detections
    return detections
```

This API endpoint expects an image file as input and returns a dictionary containing information about the detected objects, such as the bounding box coordinates, class labels, and confidence scores.

## Conclusion
In this blog post, we learned how to implement image recognition and object detection using the Python Hug API. We explored loading pre-trained models, processing images, and exposing the functionality through API endpoints. Python Hug makes it easy to build powerful APIs with minimal effort, making it a great choice for implementing image recognition and object detection services.

# References
- [Python Hug Documentation](https://www.hug.rest/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
- [PIL Documentation](https://pillow.readthedocs.io/)