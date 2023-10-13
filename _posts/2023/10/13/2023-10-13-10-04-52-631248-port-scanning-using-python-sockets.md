---
layout: post
title: "Port scanning using Python sockets"
description: " "
date: 2023-10-13
tags: [portscanning]
comments: true
share: true
---

Port scanning is a fundamental technique used in the field of cybersecurity to identify open ports on a target system. It is employed to detect potential vulnerabilities or to determine which services are running on a particular machine. In this blog post, we will explore how to perform port scanning using Python sockets.

## What are sockets?

Sockets are the endpoints for sending and receiving data across a network. They provide a means of communication between two computers using IP addresses and port numbers. In the context of port scanning, we use sockets to establish a connection with different ports on a target system and analyze the response.

## Python socket module

Python provides a built-in `socket` module that allows us to create network sockets and interact with them. We can use this module to perform port scanning by attempting to establish a connection with different ports on a target system.

Here's a simple example of how to perform port scanning using Python sockets:

```python
import socket

target_host = "192.168.0.1"  # IP address of the target system

# Define a list of ports to scan
target_ports = [22, 80, 443, 8080]

def port_scan(target_host, target_port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout to avoid hanging on inactive ports
        sock.settimeout(2)

        # Attempt to establish a connection
        result = sock.connect_ex((target_host, target_port))

        if result == 0:
            print(f"Port {target_port} is open")
        else:
            print(f"Port {target_port} is closed")

        # Close the socket
        sock.close()

    except socket.error:
        print("Failed to create or connect the socket")

# Iterate over the list of ports and perform the port scan
for port in target_ports:
    port_scan(target_host, port)
```

In the above code, we define a `port_scan` function that takes a target host IP address and a port number as parameters. The function creates a socket object, sets a timeout value, and attempts to connect to the specified port on the target host. If the result of the connection attempt is 0, the port is considered open. Otherwise, it is considered closed. The function is then called in a loop to scan multiple ports.

It is important to note that port scanning can be subject to legal and ethical considerations. Always ensure that you have proper authorization and adhere to applicable laws and regulations before conducting such activities.

## Conclusion

Port scanning is a valuable technique for identifying open ports and potential vulnerabilities in a target system. With the help of Python sockets, we can easily implement port scanning functionality. Understanding how to perform port scanning using Python allows us to strengthen our cybersecurity practices and protect our systems from potential threats.

**#python #portscanning**