---
layout: post
title: "DNS lookup using Python sockets"
description: " "
date: 2023-10-13
tags: []
comments: true
share: true
---

In this blog post, we will explore how to perform DNS lookup using Python sockets. DNS (Domain Name System) is responsible for resolving domain names to IP addresses. With the help of sockets, we can create a DNS client that sends a DNS request to a server and receives the corresponding IP address.

## Understanding DNS Lookup

Before we dive into the code, let's understand the basic steps involved in DNS lookup:

1. The client sends a DNS query to the DNS server, specifying the domain name it wants to resolve.

2. The DNS server checks its cache for the IP address corresponding to the domain name. If it has the information, it sends the response back to the client.

3. If the DNS server doesn't have the information in its cache, it forwards the request to other DNS servers until it finds the IP address or reaches the authoritative DNS server responsible for the domain.

4. The authoritative DNS server replies with the IP address, and the response is sent back to the client.

## Implementation with Python Sockets

Let's write a Python script to perform DNS lookup using sockets:

```python
import socket

def dns_lookup(domain):
    dns_server = '8.8.8.8'  # DNS server IP address (Google Public DNS)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(3)  # Set timeout to 3 seconds

    dns_query = bytearray()
    dns_query.append(0x00)  # Transaction ID
    dns_query.append(0x01)  # Standard query
    dns_query.append(0x01)  # Number of questions
    dns_query.append(0x00)  # Number of answers
    dns_query.append(0x00)  # Number of authority records
    dns_query.append(0x00)  # Number of additional records

    # Split the domain name into labels
    labels = domain.split('.')
    for label in labels:
        dns_query.append(len(label))  # Length of the label
        dns_query.extend(label.encode())  # Label encoded to bytes

    dns_query.append(0x00)  # End of domain name

    dns_query.append(0x00)  # Type (A record)
    dns_query.append(0x01)

    dns_query.append(0x00)  # Class (IN)
    dns_query.append(0x01)

    client_socket.sendto(dns_query, (dns_server, 53))  # Send the DNS query

    response, _ = client_socket.recvfrom(4096)  # Receive the response
    client_socket.close()  # Close the socket

    ip_address = socket.inet_ntoa(response[-4:])  # Extract the IP address from the response
    print("IP Address:", ip_address)

# Usage example
dns_lookup("example.com")
```

In the above code snippet, we first create a socket using `socket.socket()` with the `AF_INET` address family and `SOCK_DGRAM` socket type. We set a timeout of 3 seconds using `settimeout()` to avoid waiting indefinitely for a response.

We then construct the DNS query packet using a `bytearray()` and append the required fields as per the DNS protocol. We split the domain name into labels and encode them. Finally, we send the DNS query using `sendto()` to the DNS server.

Once we receive the response using `recvfrom()`, we extract the IP address from the response and print it.

## Conclusion

In this blog post, we have seen how to perform DNS lookup using Python sockets. The `socket` module provides a simple and powerful way to interact with DNS servers. You can customize the script to handle different types of DNS queries or parse additional information from the DNS response.

Feel free to explore further and enhance the script based on your requirements. Happy coding!

References:
- [Python socket module documentation](https://docs.python.org/3/library/socket.html)
- [DNS protocol specification](https://www.ietf.org/rfc/rfc1035.txt)

#dns #python