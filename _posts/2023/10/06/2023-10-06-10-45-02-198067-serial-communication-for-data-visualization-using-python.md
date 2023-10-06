---
layout: post
title: "Serial communication for data visualization using Python"
description: " "
date: 2023-10-06
tags: []
comments: true
share: true
---

In many applications, data is often collected from sensors or other external devices through a serial communication interface. Python provides a powerful library called `pySerial` that allows us to establish connections with these devices and read the incoming data. In this blog post, we will explore how to use `pySerial` library to visualize the data received through a serial port in real-time.

## Table of Contents
- [Introduction](#introduction)
- [Setting up the serial connection](#setting-up-the-serial-connection)
- [Reading and visualizing the data](#reading-and-visualizing-the-data)
- [Conclusion](#conclusion)

## Introduction

Serial communication is a common method to transfer data between electronic devices. It uses a predefined protocol to send and receive data bit by bit through a dedicated connection called a serial port. Python, being a versatile programming language, provides various libraries to interact with these serial ports.

## Setting up the serial connection

To get started, we need to install the `pySerial` library. You can install it using pip:

```bash
pip install pyserial
```

Next, we need to import the `serial` module in our Python script:

```python
import serial
```

To establish a connection with the serial port, we need to create an instance of the `Serial` class and specify the port and baud rate:

```python
ser = serial.Serial('COM1', 9600)  # Replace 'COM1' with the appropriate serial port and 9600 with your desired baud rate
```

Make sure to replace `'COM1'` with the correct serial port name, such as `'/dev/ttyUSB0'` on Linux or `'COM3'` on Windows.

## Reading and visualizing the data

Once the serial connection is established, we can start reading the incoming data. We can use the `readline()` method to read a line of data and decode it using the appropriate encoding:

```python
while True:
    data = ser.readline().decode('utf-8')
    print(data)
```

Here, we are continuously reading the data and printing it to the console. However, to visualize the data in real-time, we can utilize libraries like `Matplotlib` or `PyQtGraph`. Let's use `Matplotlib` for this example:

```python
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis for plotting
fig, ax = plt.subplots()

# Create empty lists to store the x and y values
x_vals = []
y_vals = []

# Create a function to update the plot
def update_plot(data):
    # Split the incoming data into x and y values
    x, y = data.split(',')

    # Append the values to the lists
    x_vals.append(float(x))
    y_vals.append(float(y))

    # Clear the axis and plot the updated data
    ax.clear()
    ax.plot(x_vals, y_vals)

# Create an animation using the update_plot function
ani = animation.FuncAnimation(fig, update_plot, frames=data_generator, interval=100)

# Display the plot
plt.show()
```

In this code snippet, we create a figure and axis object using `Matplotlib`, and then define a function `update_plot()` to update the plot with the incoming data. We split the incoming data into x and y values, append them to the respective lists, and plot them on the axis. Finally, we create an animation using `FuncAnimation()` and display the plot.

## Conclusion

Serial communication is a powerful tool for collecting data from external devices. By using the `pySerial` library in Python, we can establish a connection with a serial port and read the incoming data. We can further enhance the visualization of this data in real-time using libraries like `Matplotlib`. This opens up opportunities to monitor and analyze data from various sensors or devices seamlessly in Python.

#python #data #visualization