---
layout: post
title: "Network mapping with Python and sockets"
description: " "
date: 2023-10-13
tags: [network]
comments: true
share: true
---

In today's interconnected world, understanding and visualizing network infrastructure is crucial for both security and troubleshooting purposes. Python, with its powerful socket library, provides a great platform for performing network mapping. In this blog post, we will explore how to use Python and sockets to perform network mapping.

## Table of Contents
- [Introduction to Network Mapping](#introduction-to-network-mapping)
- [Getting Started](#getting-started)
- [Discovering Devices on the Network](#discovering-devices-on-the-network)
- [Scanning Ports](#scanning-ports)
- [Mapping the Network](#mapping-the-network)
- [Conclusion](#conclusion)

## Introduction to Network Mapping

Network mapping involves discovering and mapping the devices and their connections in a network. It helps in visualizing the network, identifying potential vulnerabilities, and ensuring secure communication.

## Getting Started

To get started, we need to install the Python programming language and the `socket` library. Python is commonly pre-installed on most operating systems, but if not, you can download and install it from the official website (https://www.python.org/).

The `socket` library, which provides low-level networking support, is a built-in library and does not require additional installation.

## Discovering Devices on the Network

To discover devices on the network, we can use the `socket` library to send an ICMP Echo Request (Ping) to each IP address in a given range. If the device responds, it is considered active.

Here is an example code snippet to discover active devices on the network:

```python
import socket

def discover_devices(ip_range):
    for i in range(1, 255):
        ip = ip_range + '.' + str(i)
        try:
            host_name = socket.gethostbyaddr(ip)[0]
            print(f"Device found: {ip} - {host_name}")
        except socket.herror:
            pass

ip_range = "192.168.1"
discover_devices(ip_range)
```

In the above code, we iterate through IP addresses by appending them to the given IP range and then try to get the host name using `socket.gethostbyaddr()`. If successful, we print the device IP and host name.

## Scanning Ports

Once we have the list of active devices on the network, we can further scan the open ports on each device. This can help identify services running on specific ports and perform security checks.

Here is an example code snippet to scan open ports on a device:

```python
import socket

def scan_ports(ip, ports):
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}")
        s.close()

ip = "192.168.1.1"
ports_to_scan = [80, 443, 22, 21]
scan_ports(ip, ports_to_scan)
```

In the above code, we iterate through the list of ports to scan and use the `socket` library to establish a TCP connection. If the connection succeeds, the port is considered open.

## Mapping the Network

By combining device discovery and port scanning, we can map the network by identifying devices and their open ports. We can store this information in a data structure like a dictionary or a graph to visualize the network topology.

Here is an example code snippet to map the network:

```python
import socket

def discover_devices(ip_range):
    devices = {}
    for i in range(1, 255):
        ip = ip_range + '.' + str(i)
        try:
            host_name = socket.gethostbyaddr(ip)[0]
            devices[ip] = {
                'host_name': host_name,
                'open_ports': []
            }
        except socket.herror:
            pass
    return devices

def scan_ports(device, ports):
    ip = device['ip']
    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            device['open_ports'].append(port)
        s.close()

ip_range = "192.168.1"
ports_to_scan = [80, 443, 22, 21]

devices = discover_devices(ip_range)
for ip, device in devices.items():
    scan_ports(device, ports_to_scan)

for ip, device in devices.items():
    print(f"Device: {device['ip']} - {device['host_name']}")
    if device['open_ports']:
        print("Open ports:")
        for port in device['open_ports']:
            print(f"- Port {port}")
    else:
        print("No open ports found.")
    print()
```

In the above code, we first discover the devices on the network using the `discover_devices()` function and store them in a dictionary with their IP addresses as keys. Then, we scan the open ports for each device using the `scan_ports()` function and store the open ports in the respective device's dictionary entry.

Finally, we iterate through the devices and print the device IP, host name, and open ports (if any).

## Conclusion

Network mapping is a powerful technique to visualize and understand the network infrastructure. Through Python and the `socket` library, we can discover devices on the network and scan their open ports. This helps identify potential vulnerabilities and ensure network security. With the mapped network information, we can take appropriate steps to secure the network and troubleshoot connectivity issues.

By leveraging Python's flexibility and the socket library, network mapping becomes an accessible task for any network administrator or security enthusiast. So, start exploring and mapping your network with Python and sockets!

\#python \#network-mapping