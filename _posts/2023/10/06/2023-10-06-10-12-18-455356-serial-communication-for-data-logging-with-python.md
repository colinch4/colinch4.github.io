---
layout: post
title: "Serial communication for data logging with Python"
description: " "
date: 2023-10-06
tags: []
comments: true
share: true
---

Serial communication is a common method for connecting and exchanging data between devices. In this article, we will explore how to use Python for serial communication to log data from a device.

## Table of Contents
- [Introduction to Serial Communication](#introduction-to-serial-communication)
- [Setting up the Serial Connection](#setting-up-the-serial-connection)
- [Reading Data from the Serial Port](#reading-data-from-the-serial-port)
- [Writing Data to the Serial Port](#writing-data-to-the-serial-port)
- [Logging Data to a File](#logging-data-to-a-file)
- [Conclusion](#conclusion)

## Introduction to Serial Communication

Serial communication is a method of data transfer that sends data in a series, one bit at a time, over a single wire or line. It is widely used for connecting microcontrollers, sensors, and other devices to a computer.

To establish a serial communication between a computer and a device, we need to know the port name (such as COM1 or /dev/ttyUSB0), baud rate, data bits, parity, and stop bits. These parameters differ depending on the device and the connection settings.

## Setting up the Serial Connection

To begin, we need to import the `serial` module in Python by executing the following code:

```python
import serial
```

To establish a serial connection, we need to create an instance of the `Serial` class and provide the required parameters. For example, to connect to a device at 9600 baud rate, 8 data bits, no parity, and 1 stop bit, we can use the following code:

```python
port = '/dev/ttyUSB0'  # Replace with your port name
baud_rate = 9600
ser = serial.Serial(port, baud_rate, timeout=1)
```

Ensure that you provide the correct `port` name for your device, which can vary depending on the operating system you are using.

## Reading Data from the Serial Port

To read data from the serial port, we can use the `read()` or `readline()` methods of the `Serial` object. The `read()` method allows us to read a specific number of bytes, whereas the `readline()` method reads until a newline character is encountered.

Here's an example that reads a single line from the serial port and prints it:

```python
line = ser.readline()
print(line)
```

## Writing Data to the Serial Port

To send data to the device via the serial port, we can use the `write()` method of the `Serial` object. You can write a string or bytes to the port.

Here's an example that writes a string to the serial port:

```python
message = "Hello, device!"
ser.write(message.encode())
```

## Logging Data to a File

To log data from the serial port to a file, we can open a file in write mode and write the received data to the file.

Here's an example that logs data received from the serial port to a file:

```python
filename = "serial_log.txt"
with open(filename, 'w') as file:
    while True:
        line = ser.readline().decode().strip()
        file.write(line + '\n')
```

In this example, the received data is stripped of any leading or trailing spaces and written to the file. The process runs indefinitely until interrupted.

## Conclusion

Serial communication provides a reliable way to exchange data between devices. Python's `serial` module makes it easy to establish a serial connection, read and write data, and log it to a file. With this knowledge, you can now start logging data from your own devices using Python. Happy experimenting!

\#python \#serialcommunication