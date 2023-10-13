---
layout: post
title: "Chatbot using Python sockets"
description: " "
date: 2023-10-13
tags: []
comments: true
share: true
---

In this tutorial, we will learn how to create a simple chatbot using Python sockets. We will use the socket module to establish a connection between a server and a client. The server will listen for incoming connections from clients and respond to their requests.

## Table of Contents
- [Setting up the Server](#setting-up-the-server)
- [Setting up the Client](#setting-up-the-client)
- [Running the Chatbot](#running-the-chatbot)
- [Conclusion](#conclusion)

## Setting up the Server

First, let's set up the server-side code. Create a new Python file, for example, `server.py`, and add the following code:

```python
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = 'localhost'
port = 12345

# Bind the address to the socket
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(1)

# Accept a connection from a client
client_socket, client_address = server_socket.accept()

# Send a welcome message to the client
message = "Welcome to the chatbot!"
client_socket.send(message.encode())

# Close the connection
client_socket.close()
```

In this code, we first create a `socket` object and specify the host and port. Then, we bind the address to the socket and start listening for incoming connections. When a client connects, we accept the connection and send a welcome message to the client. Finally, we close the connection.

## Setting up the Client

Next, let's set up the client-side code. Create a new Python file, for example, `client.py`, and add the following code:

```python
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = 'localhost'
port = 12345

# Connect to the server
client_socket.connect((host, port))

# Receive the welcome message from the server
message = client_socket.recv(1024).decode()
print(message)

# Close the connection
client_socket.close()
```

In this code, we create a `socket` object on the client side and specify the host and port. Then, we connect to the server using the `connect()` method. After connecting, we receive the welcome message from the server and print it to the console. Finally, we close the connection.

## Running the Chatbot

To run the chatbot, open two terminal windows. In one window, run the server using the command `python server.py`. In the other window, run the client using the command `python client.py`. You should see the welcome message printed in the client window.

## Conclusion

In this tutorial, we learned how to create a simple chatbot using Python sockets. We set up a server and a client, established a connection between them, and exchanged messages. You can further enhance this chatbot by implementing message handling and response logic.