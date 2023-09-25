---
layout: post
title: "Python script to send and receive data over Bluetooth"
description: " "
date: 2023-09-18
tags: [Bluetooth]
comments: true
share: true
---

Bluetooth is a wireless communication technology used for short-range data transfer between devices. In this blog post, we will explore how to use Python to send and receive data over Bluetooth using the `pybluez` library.

## Prerequisites
1. Python installed on your system.
2. `pybluez` library installed. You can install it using `pip`:

```python
pip install pybluez
```

## Sender Code
To send data over Bluetooth, we need a device acting as a sender. Below is an example of a Python script that sends data to a Bluetooth device:

```python
import bluetooth

def send_data(device_address, data):
    try:
        # Creating a Bluetooth socket
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        # Connecting to the device
        socket.connect((device_address, 1))

        # Sending data
        socket.send(data)
        print("Data sent successfully")

        # Closing the socket
        socket.close()
        
    except Exception as e:
        print("Error occurred while sending data:", str(e))
        
# Usage
device_address = "00:11:22:33:44:55"  # Replace with actual device address
data = "Hello, Bluetooth!"  # Replace with your data

send_data(device_address, data)
```

In the above code, we create a Bluetooth socket and connect to the Bluetooth device with the specified device address. Then we send the data to the device and close the socket.

## Receiver Code
To receive data over Bluetooth, we need a device acting as a receiver. Below is an example of a Python script that receives data from a Bluetooth device:

```python
import bluetooth

def receive_data():
    try:
        # Creating a Bluetooth socket
        server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

        # Binding the socket to any available port
        server_socket.bind(("", bluetooth.PORT_ANY))

        # Listening for incoming connections
        server_socket.listen(1)

        # Accepting a connection
        client_socket, client_address = server_socket.accept()
        print("Connected to:", client_address)

        # Receiving data
        data = client_socket.recv(1024)
        print("Received Data:", data)

        # Closing the sockets
        client_socket.close()
        server_socket.close()

    except Exception as e:
        print("Error occurred while receiving data:", str(e))
        
# Usage
receive_data()
```

In the receiver code, we create a Bluetooth socket and bind it to any available port. We then listen for incoming connections and accept a connection from a client device. Once connected, we receive data from the client and print it.

## Conclusion
In this blog post, we have learned how to use Python to send and receive data over Bluetooth. By using the `pybluez` library, you can easily implement Bluetooth communication in your Python applications.

#Bluetooth #Python