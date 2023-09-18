---
layout: post
title: "Bluetooth-based home automation using Python and Arduino"
description: " "
date: 2023-09-18
tags: [include, techblog]
comments: true
share: true
---

In this blog post, we will explore how to create a Bluetooth-based home automation system using Python and Arduino. Home automation refers to the control and automation of various household devices and appliances. Bluetooth technology allows us to wirelessly connect and control these devices.

## Requirements

To build this project, you will need the following components:

- Arduino board (such as Arduino Uno)
- Bluetooth module (such as HC-05 or HC-06)
- Relay module
- Jumper wires
- LED lights or any other devices you want to control

## Wiring

1. Connect the Bluetooth module's TX pin to the Arduino's RX pin and the RX pin to the Arduino's TX pin.
2. Connect the Bluetooth module's VCC pin to the Arduino's 5V pin and GND pin to the Arduino's GND pin.
3. Connect the relay module to the Arduino as per the specified pin configuration.
4. Connect the devices (such as LED lights) you want to control to the relay module.

## Setting up Python

1. Install the PySerial library by running the following command in your terminal:

```
pip install pyserial
```

2. Import the PySerial library in your Python script using the following line of code:

```python
import serial
```

## Arduino Code

Upload the following code to your Arduino board:

```cpp
#include <SoftwareSerial.h>

SoftwareSerial bluetoothSerial(10, 11);

void setup() {
  pinMode(7, OUTPUT);
  bluetoothSerial.begin(9600);
}

void loop() {
  if (bluetoothSerial.available()) {
    char command = bluetoothSerial.read();
    
    if (command == '1') {
      digitalWrite(7, HIGH);
    } else if (command == '0') {
      digitalWrite(7, LOW);
    }
  }
}
```

This code initializes a SoftwareSerial object for Bluetooth communication. Inside the `loop()` function, the code listens for incoming commands from the Bluetooth module. If the received command is '1', it turns ON the connected devices, and if the command is '0', it turns them OFF.

## Python Code

```python
import serial

# Define the Bluetooth serial port
bluetooth_port = "/dev/rfcomm0"

try:
    # Initialize the Bluetooth serial connection
    bluetooth = serial.Serial(bluetooth_port, baudrate=9600)
    print("Bluetooth connection established.")

    while True:
        command = input("Enter command (1 to turn ON, 0 to turn OFF): ")

        if command == '1' or command == '0':
            # Send the command to the Arduino board
            bluetooth.write(command.encode())
        else:
            print("Invalid command. Please enter either '1' or '0'.")

except serial.SerialException:
    print("Bluetooth connection failed. Make sure the port is correct.")
```

This Python code establishes a connection to the Bluetooth module using the specified port. It then prompts the user to enter a command (either '1' to turn ON or '0' to turn OFF the devices). The command is sent to the Arduino board via Bluetooth.

## Conclusion

Congratulations! You have successfully created a Bluetooth-based home automation system using Python and Arduino. You can now control your devices wirelessly by sending commands from your Python program to the Arduino board. Explore further by adding more devices and functionalities to enhance your home automation setup.

#techblog #homeautomation