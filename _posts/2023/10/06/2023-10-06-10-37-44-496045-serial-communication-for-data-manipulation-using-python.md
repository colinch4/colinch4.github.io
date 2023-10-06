---
layout: post
title: "Serial communication for data manipulation using Python"
description: " "
date: 2023-10-06
tags: []
comments: true
share: true
---

Serial communication is a common method used to exchange data between a computer and peripheral devices like microcontrollers, sensors, and other hardware components. In this article, we will explore how to perform serial communication using Python, a popular programming language for data manipulation and automation.

## Table of Contents
1. [Introduction to Serial Communication](#introduction-to-serial-communication)
2. [Python Libraries for Serial Communication](#python-libraries-for-serial-communication)
3. [Setting up Serial Communication](#setting-up-serial-communication)
4. [Reading Data from Serial Port](#reading-data-from-serial-port)
5. [Writing Data to Serial Port](#writing-data-to-serial-port)
6. [Serial Communication Examples](#serial-communication-examples)
7. [Conclusion](#conclusion)

## Introduction to Serial Communication

Serial communication is a synchronous or asynchronous mode of transmitting data in a stream of bits. It involves a transmitter that sends data and a receiver that receives the data. The communication is performed using a serial port, which is a hardware interface that allows data transfer using a specific protocol.

## Python Libraries for Serial Communication

Python provides several libraries for serial communication. The most commonly used libraries are:

1. **PySerial**: PySerial is a cross-platform library that provides a simple interface for serial communication in Python. It supports both reading from and writing to the serial port.

2. **serial**: Serial is another library for serial communication in Python. It is built on top of PySerial and provides additional features like advanced port configuration and control.

In this article, we will mainly focus on using the PySerial library for serial communication.

## Setting up Serial Communication

To begin with, we need to install the PySerial library using the following command:

`pip install pyserial`

Once the installation is complete, we can import the library in our Python script using the `import` statement:

```python
import serial
```

Next, we need to establish a connection with the serial port. We can create a serial object by specifying the port name, baud rate, parity, etc. For example, to connect to a port named "COM1" with a baud rate of 9600, we can use the following code:

```python
ser = serial.Serial('COM1', 9600)
```

## Reading Data from Serial Port

To read data from the serial port, we can use the `read()` or `readline()` methods provided by the PySerial library. The `read()` method reads a specified number of bytes from the port, while the `readline()` method reads until a newline character is encountered.

Here's an example that reads a line of data from the serial port:

```python
data = ser.readline()
```

## Writing Data to Serial Port

To write data to the serial port, we can use the `write()` method provided by the PySerial library. The `write()` method accepts a string of data as input and sends it to the serial port.

Here's an example that writes data to the serial port:

```python
ser.write("Hello, Arduino!".encode())
```

## Serial Communication Examples

Let's take a look at a couple of examples to showcase the use of serial communication in Python:

### Example 1: Reading Sensor Data

In this example, we can read data from a sensor connected to the serial port and perform some data manipulation:

```python
data = ser.readline().decode().strip()
sensor_value = int(data)
processed_value = sensor_value * 2
```

### Example 2: Controlling Hardware

In this example, we can send commands to control a hardware device connected to the serial port:

```python
command = "LED_ON"
ser.write(command.encode())
```

## Conclusion

Serial communication is a powerful tool for interacting with hardware devices using Python. The PySerial library provides an easy-to-use interface for establishing serial connections, reading data, and writing data. By understanding the fundamentals of serial communication, you can leverage it to manipulate data and control various hardware components in your projects.