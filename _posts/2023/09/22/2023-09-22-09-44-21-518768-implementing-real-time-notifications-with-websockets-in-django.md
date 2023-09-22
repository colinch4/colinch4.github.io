---
layout: post
title: "Implementing real-time notifications with websockets in Django"
description: " "
date: 2023-09-22
tags: [django, websockets]
comments: true
share: true
---

In today's fast-paced digital world, real-time notifications have become an essential feature in web applications. WebSockets provide a powerful mechanism for achieving real-time communication between a server and a client. In this blog post, we will explore how to implement real-time notifications using WebSockets in Django.

## Prerequisites

Before we begin, make sure you have the following prerequisites:

- Basic knowledge of Django framework
- Familiarity with JavaScript and HTML
- Django project setup with a database

## What are WebSockets?

WebSockets is a protocol that enables full-duplex communication between a client and a server over a single TCP connection. Unlike traditional HTTP requests, where the server can only respond to a client's request, WebSockets allow for bidirectional communication, enabling real-time updates from the server to the client.

## Setting up Django Channels

[Django Channels](https://channels.readthedocs.io/en/stable/) is a third-party Django library that provides support for handling WebSockets and other asynchronous protocols. 
Here's how you can set up Django Channels in your Django project:

1. Install Django Channels:

   ```bash
   pip install channels
   ```

2. Add Channels to your Django project's settings:

   ```python
   INSTALLED_APPS = [
       # Other apps
       'channels',
   ]
   ```

3. Define the routing configuration for Channels:

   Create a `routing.py` file in your Django project directory and define your routing configuration. For example:

   ```python
   from django.urls import path

   from .consumers import NotificationConsumer

   websocket_urlpatterns = [
       path('ws/notifications/', NotificationConsumer.as_asgi()),
   ]
   ```

4. Define and create a consumer:

   Create a `consumers.py` file in your Django app directory and define your consumer. A consumer handles the WebSockets connections and receives/sends messages to the clients. For example:

   ```python
   from channels.generic.websocket import AsyncWebsocketConsumer

   class NotificationConsumer(AsyncWebsocketConsumer):
       async def connect(self):
           await self.accept()
           # Perform any initial setup or authorization checks here

       async def disconnect(self, close_code):
           # Cleanup logic, if required
           pass

       async def receive(self, text_data):
           # Process incoming messages from the client
           pass

       async def send_notification(self, event):
           # Send notifications to the client
           pass
   ```

5. Include the routing configuration in your Django project's `asgi.py`:

   ```python
   from django.urls import re_path
   from channels.routing import ProtocolTypeRouter, URLRouter
   from channels.auth import AuthMiddlewareStack

   from myproject.routing import websocket_urlpatterns

   application = ProtocolTypeRouter({
       'http': get_asgi_application(),
       'websocket': AuthMiddlewareStack(
           URLRouter(
               websocket_urlpatterns
           )
       ),
   })
   ```

## Broadcasting Notifications

To broadcast notifications to connected clients, you can make use of the `send_notification` method in the `NotificationConsumer` we defined earlier. 

Here's an example of how you can send a notification to all connected clients:

```python
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()

async def send_notification(message):
    await channel_layer.group_send('notifications', {
        'type': 'send_notification',
        'message': message
    })
```

In the above code, we use `channel_layer.group_send` to broadcast the `message` to all clients that have joined the `notifications` group. The `send_notification` method in the `NotificationConsumer` receives this message and can then send it to the appropriate client.

## Handling Notifications on the Client Side

On the client side, you can use JavaScript frameworks like [Socket.IO](https://socket.io/) or the WebSocket API to handle the real-time notifications received from the server.

Here's an example of how you can handle notifications using JavaScript with the WebSocket API:

```javascript
const socket = new WebSocket('ws://localhost:8000/ws/notifications/');

socket.onmessage = function(event) {
    const message = JSON.parse(event.data);
    // Handle the received notification message here
};

socket.onclose = function(event) {
    // Socket connection closed
};

socket.onerror = function(event) {
    // Socket connection error
};
```

In the above code, we create a WebSocket connection to the `ws://localhost:8000/ws/notifications/` URL, which matches the URL pattern defined in the Django routing configuration. We then handle the received notifications in the `onmessage` event handler.

## Conclusion

Implementing real-time notifications with WebSockets in Django can greatly enhance the user experience of your web application. By leveraging Django Channels, you can easily handle WebSocket connections and broadcast real-time notifications to connected clients. With this knowledge, you can extend the functionality of your Django applications and provide your users with real-time updates.

#django #websockets