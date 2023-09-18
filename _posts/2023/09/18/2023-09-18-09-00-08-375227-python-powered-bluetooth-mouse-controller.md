---
layout: post
title: "Python-powered Bluetooth mouse controller"
description: " "
date: 2023-09-18
tags: [Bluetooth, Python]
comments: true
share: true
---

In today's tech-savvy world, wireless devices have become increasingly popular. Bluetooth technology has paved the way for the development of wireless peripherals like keyboards and mice. In this blog post, we will explore how to build a Python-powered Bluetooth mouse controller using the PyBluez library.

## Prerequisites

Before diving into the implementation, make sure you have the following prerequisites:

- Python 3.x installed on your machine
- PyBluez library installed (`pip install pybluez`)
- A Bluetooth-enabled mouse

## Step 1: Discover the Mouse

The first step is to discover the Bluetooth mouse and obtain its address. We can use the `discover_devices()` function from the PyBluez library to scan for nearby Bluetooth devices. Let's write a Python code snippet to achieve this:

```python
import bluetooth

def discover_mouse():
    nearby_devices = bluetooth.discover_devices()
    for device in nearby_devices:
        if "Mouse" in bluetooth.lookup_name(device):
            return device

mouse_address = discover_mouse()
print(f"Mouse discovered: {mouse_address}")
```

## Step 2: Connect to the Mouse

Now that we have the mouse address, we can connect to it using the `BluetoothSocket` class from the PyBluez library. We will establish a socket connection to the mouse for further communication.

```python
import bluetooth

def connect_to_mouse(address):
    socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    socket.connect((address, 1))
    return socket

mouse_socket = connect_to_mouse(mouse_address)
print("Connected to the mouse.")
```

## Step 3: Control the Mouse

The final step is to implement the logic to control the mouse. We can utilize the `mousemove` function from the `pynput` library which provides cross-platform support for controlling input devices.

```python
from pynput.mouse import Controller

mouse_controller = Controller()

def move_mouse(dx, dy):
    x, y = mouse_controller.position
    mouse_controller.move(x + dx, y + dy)
    
move_mouse(10, 5)  # Move the mouse 10 pixels to the right and 5 pixels downward
```

## Conclusion

In this blog post, we have learned how to build a Python-powered Bluetooth mouse controller. By leveraging the PyBluez library for Bluetooth communication and the pynput library for mouse control, we can create a simple but effective solution to interact with a Bluetooth-enabled mouse wirelessly.

Give it a try and enjoy the freedom of controlling your mouse without being bound by cables!

#Bluetooth #Python