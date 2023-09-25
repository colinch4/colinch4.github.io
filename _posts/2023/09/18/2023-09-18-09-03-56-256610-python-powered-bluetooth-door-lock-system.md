---
layout: post
title: "Python-powered Bluetooth door lock system"
description: " "
date: 2023-09-18
tags: [tech]
comments: true
share: true
---

In this blog post, we will explore how to create a Bluetooth door lock system using the power of Python. With this system, you will be able to control the access to your door using your smartphone or any other Bluetooth-enabled device.

## Requirements

To create this system, you will need the following:

- A Raspberry Pi or any other single-board computer capable of running Python.
- A Bluetooth module compatible with your board.
- A servo motor to act as the door lock mechanism.
- A power source for your board and the servo motor.
- A smartphone or any other Bluetooth-enabled device.

## Setting Up the Hardware

1. Connect the Bluetooth module to your board according to the manufacturer's instructions.
2. Connect the servo motor to the appropriate pins on your board.
3. Make sure the power source is connected to your board and the servo motor.

## Setting Up the Software

1. Install the necessary Python libraries for Bluetooth communication and servo motor control.
```python
pip install pybluez           # for Bluetooth communication
pip install RPi.GPIO          # for servo motor control
```
2. Write the Python code to handle the Bluetooth communication and servo motor control.
```python
import bluetooth
import RPi.GPIO as GPIO

# Bluetooth connection setup
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
port = 1
server_socket.bind(("", port))
server_socket.listen(1)

# Servo motor setup
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

def lock_door():
    pwm.ChangeDutyCycle(5)    # change the duty cycle to rotate the servo in lock position

def unlock_door():
    pwm.ChangeDutyCycle(10)   # change the duty cycle to rotate the servo in unlock position

while True:
    print("Waiting for a connection...")
    client_socket, address = server_socket.accept()
    print("Accepted connection from", address)

    data = client_socket.recv(1024).decode()
    print("Received:", data)

    if data == "unlock":
        unlock_door()
        response = "Door unlocked"
    elif data == "lock":
        lock_door()
        response = "Door locked"
    else:
        response = "Invalid command"

    client_socket.send(response.encode())
    client_socket.close()
```

## Connecting and Controlling the Door Lock

1. Run the Python code on your board.
```bash
python door_lock.py
```
2. Open the Bluetooth settings on your smartphone or other Bluetooth-enabled device.
3. Search for Bluetooth devices and find your board.
4. Pair your device with the board.
5. Use a Bluetooth terminal app or any other Bluetooth communication tool to send the commands "unlock" or "lock" to your board.

## Conclusion

Congratulations! You have successfully created a Bluetooth door lock system using Python. With this system, you can conveniently control the access to your door using your smartphone or any other Bluetooth-enabled device. Feel free to enhance the system by adding security features or integrating it with other smart home technologies.

#tech #Python #Bluetooth #DoorLock #HomeAutomation