---
layout: post
title: "Bluetooth serial communication with Arduino using Python"
description: " "
date: 2023-09-18
tags: [Arduino, Python]
comments: true
share: true
---

In this tutorial, we will learn how to establish **Bluetooth serial communication** between an Arduino board and a computer using the Python programming language. Bluetooth communication enables wireless data transfer and is commonly used in projects where a physical connection between the Arduino and computer is not ideal.

## Prerequisites

To follow along with this tutorial, you will need the following:

1. An **Arduino board** (such as Arduino UNO or Arduino Nano) with a Bluetooth module (such as HC-05 or HC-06) connected.
2. A **computer** with Python 3.x installed (can be obtained from the official Python website).

## Step 1: Pairing the Bluetooth Module

First, we need to pair the Bluetooth module with our computer:

1. Turn on the Bluetooth module.
2. On your computer, open the Bluetooth settings and make sure Bluetooth is enabled.
3. Click on the option to add a new device.
4. Select the Bluetooth module from the list of available devices and click on "Pair" or "Connect".

## Step 2: Installing Required Libraries

We will be using the **PySerial** library to establish serial communication with the Arduino. You can install the PySerial library by running the following command in your terminal:

```shell
pip install pyserial
```

## Step 3: Establishing Serial Connection

Now let's write a Python script to establish a serial connection with the Arduino and send/receive data.

```python
import serial

# Define the serial port and baud rate
port = '/dev/tty.XXX'  # Update with your serial port
baud_rate = 9600

# Create a serial object
serial_obj = serial.Serial(port, baud_rate)

# Wait for the Arduino board to initialize
serial_obj.timeout = 5

# Send data to Arduino
serial_obj.write(b'Hello from Python')

# Read data from Arduino
received_data = serial_obj.readline()
print("Received from Arduino:", received_data.decode())

# Close the serial connection
serial_obj.close()
```

Make sure to update the `port` variable with the correct serial port of your Bluetooth module.

## Step 4: Uploading Arduino Sketch

Upload the following Arduino sketch to your Arduino board:

```c
void setup() {
  Serial.begin(9600);  // Set the baud rate
}

void loop() {
  while (Serial.available()) {
    // Read serial data
    String data = Serial.readString();

    // Print received data
    Serial.println(data);

    // Send data back to the computer
    Serial.println("Hello from Arduino");
  }
}
```

## Conclusion

By following these steps, you should be able to establish Bluetooth serial communication between an Arduino board and a computer using Python. This can open up possibilities for various projects where wireless data transfer is required.

#Arduino #Python #Bluetooth #SerialCommunication