---
layout: post
title: "File sharing using Python sockets"
description: " "
date: 2023-10-13
tags: [sockets]
comments: true
share: true
---

In many applications, the ability to share files between different devices is essential. One popular method of accomplishing this is by using sockets in Python. Sockets allow for network communication between devices, enabling the transfer of data, including files.

In this article, we will explore how to implement file sharing using Python sockets. We will create a simple client-server model where the client sends a file to the server, and the server receives and saves the file.

## Getting Started

Before we begin, make sure you have Python installed on your system. You will also need the `socket` module, which is part of the Python standard library.

## Creating the Server

Let's start by creating the server-side code that will receive the file. Open a new Python file and add the following code:

```python
import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is ready to receive files...')

while True:
    # Wait for a connection
    connection, client_address = server_socket.accept()
    
    try:
        # Receive the file name
        file_name = connection.recv(1024).decode('utf-8')
        
        # Create a new file to save the received data
        with open(file_name, 'wb') as file:
            # Receive and write the file data in chunks
            while True:
                data = connection.recv(1024)
                if not data:
                    break
                file.write(data)
                
        print(f'File "{file_name}" received and saved successfully.')
        
    finally:
        # Close the connection
        connection.close()
```

In this code, we first create a TCP/IP socket using the `socket.socket()` function. Then, we bind the socket to an address and port using the `bind()` method. Next, we set the socket to listen for incoming connections with the `listen()` method.

Inside the infinite loop, we wait for a connection using the `accept()` method. Once a connection is established, we receive the file name from the client and create a new file to save the received data. We then receive the file data in chunks and write them to the file.

Finally, we close the connection. Run this code to start the server.

## Creating the Client

Next, we need to create the code for the client. Open another Python file and add the following code:

```python
import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server address and port
server_address = ('localhost', 8000)
client_socket.connect(server_address)

file_path = '<path-to-file>'
file_name = '<file-name>'

try:
    # Send the file name to the server
    client_socket.send(file_name.encode('utf-8'))
    
    # Open the file and send its contents in chunks
    with open(file_path, 'rb') as file:
        for data in iter(lambda: file.read(1024), b''):
            client_socket.send(data)
    
    print('File sent successfully.')
    
finally:
    # Close the connection
    client_socket.close()
```

In this code, we create a TCP/IP socket for the client and connect it to the server address and port using the `connect()` method.

We then specify the file path and name of the file we want to send. The client sends the file name to the server using the `send()` method.

After that, we open the file and send its contents in chunks using a loop. The `iter()` function is used to read the file data in chunks of 1024 bytes until the end of the file is reached. Each chunk is sent to the server using the `send()` method.

Finally, we print a success message and close the connection. Update the `file_path` and `file_name` variables with the appropriate values and run this code to send the file to the server.

## Conclusion

In this article, we explored how to implement file sharing using Python sockets. We created a simple client-server model where the client sends a file to the server. By understanding the concepts behind sockets in Python, you can create more complex file sharing systems and network applications.

Feel free to modify and enhance the code according to your specific requirements. Happy file sharing!

\#python #sockets