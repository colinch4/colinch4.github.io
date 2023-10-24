---
layout: post
title: "Object detection for autonomous parking systems in Python"
description: " "
date: 2023-10-24
tags: [tech]
comments: true
share: true
---

With the rapid advancement of autonomous vehicles, one crucial component is the ability to detect and understand objects in its surroundings. Object detection plays a crucial role in enabling autonomous parking systems, allowing vehicles to identify and navigate around obstacles accurately.

In this blog post, we will explore how to implement object detection using Python, specifically using the popular computer vision library, OpenCV, along with a pre-trained deep learning model.

## Table of Contents
- [Introduction](#introduction)
- [Object Detection with OpenCV](#object-detection-with-opencv)
- [Installing Dependencies](#installing-dependencies)
- [Loading Pre-trained Models](#loading-pre-trained-models)
- [Detecting Objects in Images](#detecting-objects-in-images)
- [Detecting Objects in Real-time](#detecting-objects-in-real-time)
- [Conclusion](#conclusion)

## Introduction
Object detection is the process of locating and classifying objects within an image or a video feed. It involves detecting the presence and position of objects in an image and performing accurate classification simultaneously.

## Object Detection with OpenCV
OpenCV is a popular open-source computer vision and machine learning library. It provides a broad range of functionality, including image and video processing, object detection, and more.

### Installing Dependencies
To get started, you need to install the necessary dependencies. Run the following command to install required packages:
```python
pip install opencv-python
```

### Loading Pre-trained Models
Object detection often requires the use of pre-trained models. These models are already trained on large datasets and can recognize a wide variety of objects. One commonly used pre-trained model for object detection is the **YOLO (You Only Look Once)** model.

You can download the pre-trained YOLO weights from the official website or use a pre-trained model that is already available in OpenCV's `dnn` module.

```python
import cv2

net = cv2.dnn.readNetFromDarknet("yolov3.cfg", "yolov3.weights")
```

### Detecting Objects in Images
To detect objects in a given image, follow these steps:

1. Load the image using `cv2.imread()`.
2. Prepare the image for input to the neural network by converting it to a blob using `cv2.dnn.blobFromImage()`.
3. Set the blob as input to the neural network and perform forward propagation.
4. Retrieve the resulting bounding boxes and confidence scores.
5. Filter out any low-confidence detections.
6. Draw bounding boxes and class labels on the image using `cv2.rectangle()` and `cv2.putText()`.

Here's an example implementation:

```python
image = cv2.imread("parking_image.jpg")
blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)

net.setInput(blob)
output_layers = net.getUnconnectedOutLayersNames()
layer_outputs = net.forward(output_layers)

class_ids = []
confidences = []
boxes = []

for output in layer_outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = center_x - w // 2
            y = center_y - h // 2
            class_ids.append(class_id)
            confidences.append(float(confidence))
            boxes.append([x, y, w, h])

indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

for i in indices:
    i = i[0]
    box = boxes[i]
    x, y, w, h = box[0], box[1], box[2], box[3]
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    label = str(class_ids[i])
    cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow("Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### Detecting Objects in Real-time
To perform real-time object detection, we need to capture frames from a video source (e.g., a webcam) and apply the same object detection steps as above.

```python
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)

    net.setInput(blob)
    output_layers = net.getUnconnectedOutLayersNames()
    layer_outputs = net.forward(output_layers)

    # Perform object detection steps and draw bounding boxes on frame

    cv2.imshow("Real-time Object Detection", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## Conclusion
Object detection is a crucial component in developing autonomous parking systems. With the help of Python and OpenCV, we can implement object detection using pre-trained models, enabling vehicles to effectively identify objects in their surroundings.

By following the steps outlined in this blog post, you can begin building your own object detection system or integrate it into your autonomous parking project. Remember to experiment with different pre-trained models and fine-tune the system based on your specific requirements.

Keep exploring the exciting field of computer vision, and happy coding!

---

References:
- [OpenCV](https://opencv.org/)
- [YOLO (You Only Look Once)](https://pjreddie.com/darknet/yolo/) 

#tech #python