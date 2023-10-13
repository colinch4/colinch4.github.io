---
layout: post
title: "Sending files over socket using Python"
description: " "
date: 2023-10-13
tags: []
comments: true
share: true
---

In many applications, it is necessary to transfer files over a network connection. One way to achieve this is by using sockets in Python. Sockets provide a way for two or more computers to communicate with each other.

In this blog post, we will learn how to send files using sockets in Python. We will create a client-server architecture where the client sends a file to the server.

## Table of Contents
- [Setting up the Server](#setting-up-the-server)
- [Establishing a Connection](#establishing-a-connection)
- [Receiving the File](#receiving-the-file)
- [Setting up the Client](#setting-up-the-client)
- [Sending the File](#sending-the-file)

## Setting up the Server
To set up the server, we first need to import the necessary modules and create a socket object. We will use the `socket` module for this purpose.

```python
import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Next, we will specify the IP address and port on which the server will listen for incoming connections.

```python
# Set the IP address and port
server_ip = '127.0.0.1'
server_port = 12345

# Bind the socket to the IP address and port
server_socket.bind((server_ip, server_port))
```

## Establishing a Connection
After setting up the server, we need to put it in the listening mode to establish a connection with the client.

```python
# Put the server in the listening mode
server_socket.listen(1)

# Accept the client connection
client_socket, address = server_socket.accept()
```

## Receiving the File
Once the connection is established, the server can receive the file sent by the client.

```python
# Specify the buffer size
buffer_size = 4096

# Open a file in write mode to save the received file
with open('received_file.txt', 'wb') as file:
    while True:
        # Receive data from the client
        data = client_socket.recv(buffer_size)
        if not data:
            break
        # Write the received data to the file
        file.write(data)
```

## Setting up the Client
To set up the client, we need to create a socket object similar to the server.

```python
import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Next, we will specify the IP address and port of the server to which we want to connect.

```python
# Set the IP address and port of the server
server_ip = '127.0.0.1'
server_port = 12345

# Connect to the server
client_socket.connect((server_ip, server_port))
```

## Sending the File
Once the client is connected to the server, we can send the file from the client to the server.

```python
# Specify the file to be sent
file_name = 'file_to_send.txt'

# Open the file in read mode
with open(file_name, 'rb') as file:
    # Read the contents of the file
    data = file.read()
    # Send the file data to the server
    client_socket.sendall(data)
```

That's it! Now you know how to send files over a socket using Python. This method can be useful for various applications, such as transferring files between computers or sharing files over a network.

Make sure to handle any errors that may occur during the file transfer process and handle file permissions appropriately.

Happy coding!

---

References:
- [Python Socket Programming](https://docs.python.org/3/library/socket.html)