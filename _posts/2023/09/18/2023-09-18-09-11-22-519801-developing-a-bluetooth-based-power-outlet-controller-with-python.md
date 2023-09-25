---
layout: post
title: "Developing a Bluetooth-based power outlet controller with Python"
description: " "
date: 2023-09-18
tags: [techblog]
comments: true
share: true
---

With the increasing adoption of Internet of Things (IoT) devices, home automation is gaining popularity. One common use case is controlling power outlets wirelessly. In this blog post, we will explore how to develop a Bluetooth-based power outlet controller using Python.

## Hardware Requirements

To get started, we need the following hardware components:

- Raspberry Pi or any other single-board computer
- Bluetooth module (like HC-05 or HC-06)
- Relay module
- Power outlet

## Software Requirements

To develop the Bluetooth-based power outlet controller, we require the following software:

- Python
- PyBluez library for Bluetooth communication

## Step 1: Setting Up the Hardware

1. Connect the Bluetooth module to the Raspberry Pi's GPIO pins.
2. Connect the relay module to the power outlet.

## Step 2: Installing Dependencies

1. Install Python on your Raspberry Pi.
2. Install the PyBluez library by running the following command in the terminal:

   ```
   pip install pybluez
   ```

## Step 3: Writing the Python Code

Now, let's write the Python code to control the power outlet.

```python
import bluetooth
import time

# Replace MAC_ADDRESS with the MAC address of your Bluetooth module
mac_address = "MAC_ADDRESS"

def send_command(command):
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((mac_address, 1))
    sock.send(command)
    sock.close()

def turn_on_outlet():
    send_command("ON")

def turn_off_outlet():
    send_command("OFF")

# Test the power outlet controller
# Uncomment one of the following lines to turn the outlet on or off

# turn_on_outlet()
# turn_off_outlet()
```

Make sure to replace `MAC_ADDRESS` with the MAC address of your Bluetooth module. The `send_command()` function establishes a Bluetooth connection and sends commands to control the power outlet. The `turn_on_outlet()` and `turn_off_outlet()` functions demonstrate how to send specific commands.

## Step 4: Testing the Power Outlet Controller

To test the power outlet controller, uncomment either the `turn_on_outlet()` or `turn_off_outlet()` line in the code. Run the Python script on your Raspberry Pi, and you should see the power outlet turning on or off.

## Conclusion

In this blog post, we learned how to develop a Bluetooth-based power outlet controller using Python. By leveraging the PyBluez library, we were able to establish a Bluetooth connection and send commands to control the power outlet. This project opens up possibilities for home automation and remote control of power outlets. Happy coding!

#techblog #python #bluetooth #homeautomation #iot