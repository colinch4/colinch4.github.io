---
layout: post
title: "Bluetooth-controlled robotic arm using Python"
description: " "
date: 2023-09-18
tags: [python, robotics]
comments: true
share: true
---

In this tutorial, we will learn how to build a robotic arm that can be controlled wirelessly using Bluetooth and Python. With the combination of hardware and programming, we can create a simple yet impressive project that can be a great way to understand the concepts of robotics and wireless communication.

## Hardware Components

To build this project, we will need the following:

1. Robotic arm kit
2. Arduino Uno or any compatible microcontroller
3. Bluetooth module (HC-05 or HC-06)
4. Wires and jumper cables
5. Power supply

## Hardware Setup

1. Assemble the robotic arm kit according to the provided instructions.
2. Connect the servo motors of the robotic arm to the Arduino Uno. Make sure to connect the signal wires of the servos to the PWM capable pins of the microcontroller.
3. Connect the Bluetooth module to the Arduino Uno. The RX pin of the Bluetooth module should be connected to the TX pin of the Arduino, and the TX pin should be connected to the RX pin of the Arduino.
4. Connect the power supply to the Arduino and the servo motors.

## Software Setup

1. Install the required libraries for Bluetooth communication in Python:

```python
pip install pyserial
```

2. Write the Python code to control the robotic arm. Here's an example of how the code should be structured:

```python
import time
import serial

# establish a serial connection with the Bluetooth module
bluetooth = serial.Serial('/dev/rfcomm0', baudrate=9600)

def move_servo(servo_id, angle):
    # code to move the servo motor based on the provided angle
    pass

while True:
    # receive commands from the Bluetooth module
    command = bluetooth.readline().decode().strip()

    # split the command into servo ID and desired angle
    servo_id, angle = command.split(',')

    # move the corresponding servo motor
    move_servo(int(servo_id), int(angle))

    # wait for a short duration
    time.sleep(0.1)
```

## Control the Robotic Arm

1. Upload the Arduino sketch to the microcontroller. The sketch should include code to receive commands from the Python program and control the servo motors accordingly.
2. Run the Python program and establish a Bluetooth connection with the robotic arm. Make sure the Bluetooth module is paired with your computer or mobile device.
3. Send commands to the robotic arm using the format `SERVO_ID,ANGLE`. For example, to move servo 1 to angle 90 degrees, send `1,90` through the Bluetooth connection.

## Conclusion

By combining Python programming and Bluetooth communication, we have successfully built a robotic arm that can be controlled wirelessly. This project serves as a great starting point for diving deeper into the field of robotics and exploring more complex applications of Bluetooth technology.

#python #robotics