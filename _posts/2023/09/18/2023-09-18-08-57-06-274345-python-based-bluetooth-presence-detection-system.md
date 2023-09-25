---
layout: post
title: "Python-based Bluetooth presence detection system"
description: " "
date: 2023-09-18
tags: [Bluetooth]
comments: true
share: true
---

In today's blog post, we will explore how to create a Bluetooth presence detection system using Python. This system will allow you to track the presence of Bluetooth devices within a certain range, making it useful for various applications such as tracking attendance or monitoring equipment.

## Prerequisites
To follow along with this tutorial, you will need:

- A computer with **Python** installed (version 3.5 or above).
- A **Bluetooth adapter** on your computer (most laptops have built-in Bluetooth).
- The **PyBluez** library installed. You can install it using the following command:

```python
pip install pybluez
```

## Setting up the System
1. Import the required libraries:

```python
import bluetooth
import time
```

2. Define a function to detect nearby Bluetooth devices:

```python
def detect_devices():
    devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

    if len(devices) > 0:
        for addr, name in devices:
            print("Found device:", name, "with MAC address:", addr)
    else:
        print("No devices found.")

while True:
    detect_devices()
    time.sleep(10)
```

In the code above, we use the `discover_devices` function from the `bluetooth` library to scan for nearby devices. The `duration` parameter specifies the duration of the scan (in seconds). You can adjust this value based on your requirements.

We then loop over the detected devices and print their names and MAC addresses. Finally, we use the `time.sleep` function to set a delay between scans (in seconds). Feel free to modify this delay to suit your needs.

## Running the System
To run the Bluetooth presence detection system, simply execute the Python script. You will start seeing the detected devices in the console output. Make sure that your Bluetooth adapter is turned on and within range of the devices you want to detect.

## Conclusion
In this blog post, we have learned how to create a Bluetooth presence detection system using Python. This system can be useful for various applications where tracking the presence of Bluetooth devices is required. Feel free to customize and expand on this system to suit your specific needs.

#Bluetooth #Python #PresenceDetection #PyBluez