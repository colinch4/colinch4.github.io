---
layout: post
title: "Bluetooth-enabled home security camera system using Python"
description: " "
date: 2023-09-18
tags: [Python, Bluetooth]
comments: true
share: true
---

With advancements in technology, it is now easier than ever to build a home security system using off-the-shelf components and the power of Python. In this blog post, we will explore how to create a Bluetooth-enabled home security camera system using Python and a few additional hardware components.

## Hardware Components Required
To build this system, you will need the following hardware components:
- Raspberry Pi 3 (or higher) with Bluetooth capability
- USB webcam or Raspberry Pi camera module
- Bluetooth-enabled motion sensor

## Setting Up the Raspberry Pi
Before we begin coding, let's first set up our Raspberry Pi. Follow these steps to get started:
1. Install the latest version of the Raspberry Pi operating system (Raspbian) on your Raspberry Pi.
2. Connect the USB webcam or Raspberry Pi camera module to the Raspberry Pi.
3. Enable the Bluetooth module on your Raspberry Pi using the inbuilt configuration options.

## Installing Required Python Libraries
To make our Python code work, we need to install a few libraries. Open up the terminal on your Raspberry Pi and run the following commands:
```python
pip install opencv-python   # For accessing and manipulating camera stream
pip install pybluez   # For working with Bluetooth connectivity
```

Once the installation is complete, we can proceed with writing the Python code.

## Python Code for Bluetooth-Enabled Home Security Camera System
Below is a sample code that captures video using the webcam and sends a notification to your smartphone when motion is detected:
```python
import cv2
import bluetooth

# Set up Bluetooth connection
target_address = 'XX:XX:XX:XX:XX:XX'    # Replace with your smartphone's Bluetooth MAC address
port = 1

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((target_address, port))

# Set up camera
video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    # Perform motion detection logic here
    # ...

    if motion_detected:
        sock.send("Motion Detected!")

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
sock.close()
```

Don't forget to assign the MAC address of your smartphone to the `target_address` variable in the code.

## Conclusion
In this blog post, we have learned how to build a Bluetooth-enabled home security camera system using Python. By harnessing the power of Python and Raspberry Pi, we can create an affordable and customizable solution to monitor our home. Feel free to expand upon this project by adding more features like image recognition or integrating with cloud storage.

#Python #Bluetooth #HomeSecurity #DIY