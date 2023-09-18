---
layout: post
title: "Python-based Bluetooth clock project"
description: " "
date: 2023-09-18
tags: [bluetooth, python]
comments: true
share: true
---

In this blog post, we will explore how to build a Bluetooth-enabled clock using Python. This project will allow you to display the time on a digital screen, retrieve it from a Bluetooth-enabled device, and synchronize it wirelessly. Let's get started!

## Requirements

To complete this project, you will need the following:

1. Raspberry Pi or any other development board with Bluetooth capabilities
2. A Bluetooth-enabled device, such as a smartphone or tablet
3. A digital screen or display module
4. Python development environment

## Step 1: Setting Up the Hardware 

First, connect the digital screen module to your development board. Make sure it is properly connected and powered on. If required, install any drivers or libraries needed to interact with the screen.

## Step 2: Pairing the Bluetooth Devices

Using the Bluetooth settings on your development board, pair it with your Bluetooth-enabled device. Ensure that both devices are discoverable and can connect to each other.

## Step 3: Installing Required Libraries

To interact with Bluetooth on the Raspberry Pi, we need to install the required Python libraries. Open a terminal and run the following command:

    ```python
    pip install pybluez
    ```

## Step 4: Writing the Python Code

Create a new Python script and import the necessary modules and libraries:

```python
import bluetooth
from time import sleep

# Define the Bluetooth service UUID
uuid = "00001101-0000-1000-8000-00805F9B34FB"

# Create a server socket
server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_sock.bind(("", bluetooth.PORT_ANY))
server_sock.listen(1)

# Wait for a client connection
print("Waiting for Bluetooth connection...")
client_sock, address = server_sock.accept()

print("Accepted connection from", address)

# Continuously receive and display the time from the client
while True:
    try:
        # Receive data from the client
        time_data = client_sock.recv(1024)
        print("Received time:", time_data)

        # Display the time on the screen
        display_time(time_data)
    except bluetooth.btcommon.BluetoothError:
        # Client disconnected, wait for a new connection
        client_sock.close()
        print("Waiting for Bluetooth connection...")
        client_sock, address = server_sock.accept()

# Disconnect from the client
client_sock.close()
server_sock.close()
```

## Step 5: Displaying the Time

Implement the `display_time()` function to update the screen with the received time data. This implementation depends on the specific screen you are using. Consult the documentation or examples provided by the screen manufacturer for displaying text or graphics.

## Step 6: Running the Code

Save the Python script and run it on your development board. Ensure that the Bluetooth connection is active on both devices. You should see the time data being received and displayed on the screen.

## Conclusion

In this project, we have learned how to build a Bluetooth clock using Python. By establishing a Bluetooth connection between a development board and a Bluetooth-enabled device, we were able to synchronize the time wirelessly. This project can be extended to add more features like alarms, timer functionalities, or even integrating with other IoT devices. Have fun exploring further possibilities!

#bluetooth #python #iot