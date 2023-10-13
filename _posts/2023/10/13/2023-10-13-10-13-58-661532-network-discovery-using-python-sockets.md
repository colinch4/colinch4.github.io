---
layout: post
title: "Network discovery using Python sockets"
description: " "
date: 2023-10-13
tags: [networking]
comments: true
share: true
---

In this blog post, we will explore how to perform network discovery using Python sockets. Network discovery is the process of finding devices, services, and resources on a network. Python provides a built-in module called `socket` that allows us to connect and interact with network sockets.

## Table of Contents
- [Introduction](#introduction)
- [Scanning for active hosts](#scanning-for-active-hosts)
- [Scanning open ports](#scanning-open-ports)
- [Conclusion](#conclusion)

## Introduction

Python's `socket` module provides a low-level interface for network communication. By utilizing this module, we can send network requests and receive responses from other devices on the network. This allows us to discover active hosts and open ports.

## Scanning for active hosts

To perform network discovery targeted at finding active hosts, we can send an ICMP echo request (ping) to each IP address in a given range. If an active host is present, we will receive an ICMP echo reply.

```python
import subprocess

def ping(ip):
    try:
        output = subprocess.check_output(['ping', '-c', '1', ip])
        return True
    except subprocess.CalledProcessError:
        return False

def scan_hosts(ip_range):
    for i in range(1, 255):  # assuming IP range is x.x.x.1-254
        ip = ip_range + '.' + str(i)
        if ping(ip):
            print(f"Host {ip} is active")
```

In the above example, we use the `ping` function to send an ICMP echo request to each IP address in the given range. If the host responds with an ICMP echo reply, it is considered active.

## Scanning open ports

To discover open ports on a specific host, we can use Python sockets to connect to the target IP address and try connecting to different ports. If a connection is successful, the port is considered open.

```python
import socket

def scan_ports(ip):
    target_ports = [80, 443, 22, 3389]  # example ports to scan

    for port in target_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}")
        sock.close()
```

The `scan_ports` function iterates over a list of target ports and attempts to connect to each port using the `socket` module. If the connection is successful (indicated by `result == 0`), the port is considered open.

## Conclusion

Python's `socket` module provides a powerful interface for network communication. By leveraging this module, we can perform network discovery by scanning for active hosts and open ports. This capability can be useful for various purposes, including network administration and security auditing.

By using the code examples provided, you can start exploring network discovery in Python and build upon them to develop more advanced network scanning tools.

Feel free to experiment with the code and adapt it to suit your specific network discovery needs!

\#python #networking