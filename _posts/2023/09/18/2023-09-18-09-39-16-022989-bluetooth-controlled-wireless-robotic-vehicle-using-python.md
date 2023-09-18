---
layout: post
title: "Bluetooth-controlled wireless robotic vehicle using Python"
description: " "
date: 2023-09-18
tags: [python, robotics)]
comments: true
share: true
---

In this blog post, I will explain how to create a **Bluetooth-controlled wireless robotic vehicle** using Python. This project will allow you to **control a robotic vehicle wirelessly** using a Bluetooth connection.

## Hardware Required
To create this project, you will need the following hardware components:
1. Raspberry Pi (or any other similar microcontroller)
2. Motor driver module
3. Bluetooth module
4. DC motors
5. Chassis for the robotic vehicle
6. Power supply

## Software Required
In terms of software, you will need:
1. Python programming language
2. Raspberry Pi OS (or any other operating system compatible with your microcontroller)
3. Bluetooth library (for example, the PyBluez library)

## Step 1: Setting up the Hardware
1. Assemble the chassis and mount the motors on it.
2. Connect the motor driver module to the Raspberry Pi according to the manufacturer's instructions.
3. Connect the Bluetooth module to the Raspberry Pi, ensuring that the correct pins are connected for communication.

## Step 2: Setting up the Software
1. Install Python if it is not already installed on your system.
2. Install the necessary Bluetooth library. For example, if you are using a Raspberry Pi, you can install the PyBluez library by running `pip install PyBluez` in the terminal.
3. Write a Python script that will handle the Bluetooth connection and control the motors.

## Step 3: Coding the Python Script
```python
import bluetooth
from gpiozero import Motor

# Define the MAC address of the Bluetooth module
bluetooth_address = 'XX:XX:XX:XX:XX:XX'

# Connect to the Bluetooth module
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((bluetooth_address, 1))

# Create motor objects
motor1 = Motor(forward=4, backward=14)
motor2 = Motor(forward=17, backward=18)

# Control the motors based on received commands
while True:
    data = sock.recv(1024)
    command = data.decode().strip()
    
    if command == 'forward':
        motor1.forward()
        motor2.forward()
        
    elif command == 'backward':
        motor1.backward()
        motor2.backward()
        
    elif command == 'turn_left':
        motor1.forward()
        motor2.backward()
        
    elif command == 'turn_right':
        motor1.backward()
        motor2.forward()
        
    elif command == 'stop':
        motor1.stop()
        motor2.stop()
        
    elif command == 'exit':
        break

# Close the Bluetooth connection
sock.close()
```

## Step 4: Testing the Robotic Vehicle
1. Make sure the Bluetooth module is paired with your device or smartphone.
2. Upload the Python script to your Raspberry Pi or microcontroller.
3. Run the script to start the Bluetooth connection and wait for commands.
4. Use a Bluetooth terminal app on your device or smartphone to send commands like `forward`, `backward`, `turn_left`, `turn_right`, `stop`, or `exit`.
5. Test the robotic vehicle to see if it responds correctly to the commands sent via Bluetooth.

## Conclusion (#python #robotics)
In this blog post, we have learned how to create a Bluetooth-controlled wireless robotic vehicle using Python. By following these steps, you can control a robotic vehicle wirelessly using a Bluetooth connection and a few hardware components. This project can be a great way to explore robotics and practice your Python skills!