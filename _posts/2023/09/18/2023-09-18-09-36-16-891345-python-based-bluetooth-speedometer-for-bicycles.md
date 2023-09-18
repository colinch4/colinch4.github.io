---
layout: post
title: "Python-based Bluetooth speedometer for bicycles"
description: " "
date: 2023-09-18
tags: [python, BluetoothSpeedometer]
comments: true
share: true
---

![Bluetooth Speedometer](speedometer.jpg)

Are you a passionate cyclist who wants to track their speed and distance while enjoying the ride? Look no further! In this blog post, we will guide you through building a Python-based Bluetooth speedometer for your bicycle. So, let's get started!

## Why Build a Bluetooth Speedometer?

A Bluetooth speedometer provides real-time data on your bicycle's speed and distance traveled. It allows you to monitor your performance, set fitness goals, and track your progress over time. By building your own speedometer, you can customize it to meet your specific needs and preferences.

## Ingredients for Building the Speedometer

To build our Bluetooth speedometer, you will need the following components:

1. Raspberry Pi or any other microcontroller
2. Bluetooth module or USB Bluetooth dongle
3. Reed switch and neodymium magnet
4. Breadboard and jumper wires
5. Python programming environment

## Hardware Setup

1. Connect the Bluetooth module to the Raspberry Pi or microcontroller according to their respective pin configurations.
2. Attach the reed switch to the bicycle's fork, positioning it close to the wheel's spoke.
3. Securely mount the neodymium magnet to one of the wheel's spokes.
4. Connect the reed switch to the microcontroller using a breadboard and jumper wires.

## Software Implementation

### Step 1: Install Required Libraries

We need to install the required Python libraries for Bluetooth communication. Open your terminal and run the following command:
```python
pip install pybluez
```

### Step 2: Coding the Speedometer

Next, let's write the Python code for our Bluetooth speedometer. Create a new Python file, and let's get started with the necessary imports:
```python
import bluetooth
import RPi.GPIO as GPIO
import time
```

### Step 3: Initializing Bluetooth

```python
# Bluetooth UUID for serial communication
uuid = "00001101-0000-1000-8000-00805F9B34FB"

# Search for nearby Bluetooth devices
nearby_devices = bluetooth.discover_devices()

# Connect to the desired device
for device in nearby_devices:
    if device == 'Your Speedometer Device':  # Replace with your device name
        speedometer_address = device
        break

# Establish Bluetooth connection
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((speedometer_address, 1))
```

### Step 4: Reading Speed and Distance

```python
# Pin used by the reed switch
reed_switch_pin = 26

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(reed_switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Variables for speed and distance calculation
wheel_circumference = 2.14  # Modify according to your bicycle's wheel size

def calculate_speed(time_interval):
    # Speed calculation logic based on wheel circumference and time interval
    speed = (wheel_circumference / time_interval) * 3.6  # Convert m/s to km/h
    return speed

def calculate_distance(speed):
    # Distance calculation logic based on speed and time interval
    distance = speed * time_interval
    return distance

# Continuous loop for reading speed and distance
while True:
    # Check the state of the reed switch
    if GPIO.input(reed_switch_pin) == GPIO.LOW:
        start_time = time.time()

        # Wait until the reed switch state changes
        while GPIO.input(reed_switch_pin) == GPIO.LOW:
            pass

        end_time = time.time()
        time_interval = end_time - start_time

        # Calculate speed and distance
        speed = calculate_speed(time_interval)
        distance += calculate_distance(speed)

        # Send speed and distance to the connected device
        sock.send(str(speed) + ',' + str(distance))
```

### Step 5: Cleanup and Disconnect

```python
# Cleanup GPIO and close Bluetooth socket
GPIO.cleanup()
sock.close()
```

## Conclusion

Congratulations! You have successfully built a Python-based Bluetooth speedometer for your bicycle. Now, you can track your speed and distance while cycling and analyze your performance. Feel free to customize the code and add additional features to enhance your cycling experience. Happy coding and safe cycling!

#python #BluetoothSpeedometer