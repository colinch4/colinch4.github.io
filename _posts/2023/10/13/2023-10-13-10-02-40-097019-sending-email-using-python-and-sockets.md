---
layout: post
title: "Sending email using Python and sockets"
description: " "
date: 2023-10-13
tags: []
comments: true
share: true
---

Sending emails programmatically is a common task in many applications. In this tutorial, we will explore how to send an email using Python and sockets, without relying on external libraries.

## Table of Contents
- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setting Up](#setting-up)
- [Establishing a TCP Connection](#establishing-a-tcp-connection)
- [Preparing the Email](#preparing-the-email)
- [Sending the Email](#sending-the-email)
- [Conclusion](#conclusion)

## Introduction
Python provides the `smtplib` library to send emails, but for the purpose of learning, we will use the lower-level `socket` module to understand the underlying protocol. This will give us more control and a better understanding of how emails are sent over the network.

## Prerequisites
To follow this tutorial, you will need:
- Basic knowledge of Python
- A computer with Python installed

## Setting Up
Before we start, let's import the `socket` module:

```python
import socket
```

## Establishing a TCP Connection
To send an email, we need to establish a TCP connection to an SMTP (Simple Mail Transfer Protocol) server. SMTP servers handle outgoing mail and are responsible for relaying emails to their destinations.

```python
# Define the target SMTP server and its port
server = "smtp.example.com"
port = 25

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((server, port))

# Receive the server's response
response = sock.recv(1024).decode()
print(response)
```

## Preparing the Email
Next, we need to prepare the email to be sent. We will create a string that conforms to the SMTP protocol's email format.

```python
# Email details
sender = "sender@example.com"
recipient = "recipient@example.com"
subject = "Hello from Python"
message = "This is the body of the email."

# Format the email
email = f"From: {sender}\r\nTo: {recipient}\r\nSubject: {subject}\r\n\r\n{message}"
```

## Sending the Email
Now that we have established the connection and formatted the email, we can send it to the SMTP server.

```python
# Send the email
sock.sendall(email.encode())

# Receive the server's response
response = sock.recv(1024).decode()
print(response)

# Close the connection
sock.close()
```

## Conclusion
In this tutorial, we learned how to send an email using Python and sockets. We established a TCP connection to an SMTP server, formatted the email following the SMTP protocol, and sent it over the network.

By understanding the underlying mechanisms, we gained a deeper understanding of how emails are sent programmatically.