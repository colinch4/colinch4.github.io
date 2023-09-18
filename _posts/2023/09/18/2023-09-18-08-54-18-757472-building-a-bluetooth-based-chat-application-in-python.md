---
layout: post
title: "Building a Bluetooth-based chat application in Python"
description: " "
date: 2023-09-18
tags: [python, bluetooth]
comments: true
share: true
---

In this blog post, we will build a chat application using Bluetooth technology and Python. Bluetooth provides a convenient way to connect and communicate between devices wirelessly. By leveraging the capabilities of Python and its Bluetooth library, we can create a simple chat application that allows for text-based communication between devices.

## Prerequisites

To get started with building our Bluetooth chat application, make sure you have the following prerequisites:

1. Python installed on your system.
2. Bluetooth module installed. You can install it using pip:

```python
pip install pybluez
```

## Setting up the Server

First, let's set up the server that will handle the incoming connections and messages. Create a new Python file called `server.py` and add the following code:

```python
import bluetooth

host = ""
port = 1  # Use any available port

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind((host, port))
server_socket.listen(1)

print("Waiting for a connection...")

client_socket, client_address = server_socket.accept()
print("Client connected:", client_address)
```

This code sets up a server socket using Bluetooth RFCOMM protocol and waits for a connection. Once a client connects, we print the client's address to confirm the connection.

## Setting up the Client

Next, let's set up the client that will connect to the server and handle the message exchange. Create a new Python file called `client.py` and add the following code:

```python
import bluetooth

server_address = "XX:XX:XX:XX:XX:XX"  # Replace with server's Bluetooth address
port = 1

client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
client_socket.connect((server_address, port))

print("Connected to server.")
```

Replace `XX:XX:XX:XX:XX:XX` with the actual Bluetooth address of the server device. This code establishes a connection with the server using the server's address and the same port as in the server setup.

## Sending and Receiving Messages

Now that we have the server and client set up, let's implement the code for sending and receiving messages. Add the following code to both `server.py` and `client.py` files:

```python
def send_message(socket, message):
    socket.send(message.encode())

def receive_message(socket):
    message = socket.recv(1024)
    return message.decode()

while True:
    # Server code
    message = receive_message(client_socket)
    print("Received message:", message)

    # Client code
    message = input("Enter a message: ")
    send_message(server_socket, message)
```

This code defines two functions, `send_message` and `receive_message`, for sending and receiving messages over the Bluetooth socket. 

In the main loop, the server waits for incoming messages and prints them. The client prompts the user to enter a message and sends it to the server.

## Running the Chat Application

To run the chat application, follow these steps:

1. Start the server by running `server.py` on the server device.
2. Obtain the Bluetooth address of the server device.
3. Update `client.py` with the server's Bluetooth address.
4. Run `client.py` on the client device.

Once the client is connected, messages can be exchanged between the server and client.

## Conclusion

In this blog post, we built a Bluetooth-based chat application using Python and the Bluetooth library. We set up a server to handle incoming connections and messages, and a client to connect to the server and send/receive messages. You can further enhance this application by adding features like encryption, authentication, or a graphical user interface.

#python #bluetooth #chatapplication