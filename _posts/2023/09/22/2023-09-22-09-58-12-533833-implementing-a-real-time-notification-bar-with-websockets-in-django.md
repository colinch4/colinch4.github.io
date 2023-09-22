---
layout: post
title: "Implementing a real-time notification bar with websockets in Django"
description: " "
date: 2023-09-22
tags: [websockets, django]
comments: true
share: true
---

In this blog post, we will explore how to implement a real-time notification bar using WebSockets in a Django web application. WebSockets allow us to establish a persistent connection between the client and the server, enabling real-time communication.

## Why WebSockets?

Traditional request-response communication between the client and server can be inefficient for real-time updates, as it involves multiple requests from the client. With WebSockets, we can establish a long-lived connection that enables bi-directional communication. This makes it ideal for implementing features like real-time notifications.

## Setting up Django Channels

[Django Channels](https://channels.readthedocs.io/) is a powerful Django extension that enables WebSockets and other asynchronous functionality. To get started, we need to install it:

```shell
pip install channels
```

After installing channels, we need to add it to our Django project's settings:

```python
INSTALLED_APPS = [
    # ...
    'channels',
]

ASGI_APPLICATION = 'my-project.routing.application'
```
Don't forget to add the routing module: `my-project.routing.application` at the `ASGI_APPLICATION` setting.

## Creating a WebSocket consumer

To handle incoming WebSockets connections and communicate with clients, we need to create a consumer. Consumers are similar to Django views, but for WebSockets.

Create a new file called `consumers.py` in your app directory and define a WebSocket consumer:

```python
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Perform any necessary setup here, such as subscribing to a channel or initializing variables

    async def disconnect(self, close_code):
        # Cleanup logic, if any, goes here
        pass

    async def receive(self, text_data):
        # Handle incoming WebSocket messages
        pass
```

Within the consumer, we can define the logic for handling various WebSocket events such as `connect`, `disconnect`, and `receive`.

## Routing WebSockets to consumers

To route incoming WebSocket connections to the appropriate consumer, we need to define a routing configuration.

Create a new file called `routing.py` in your project root directory and define the routing configuration:

```python
from django.urls import re_path
from myapp.consumers import NotificationConsumer

websocket_urlpatterns = [
    re_path(r'ws/notifications/$', NotificationConsumer.as_asgi()),
]
```

This configuration will route any incoming WebSocket connection to the `NotificationConsumer`.

## Enabling channels in the Django project

To enable channels in our Django project, we need to configure the ASGI application.

Create a file called `asgi.py` in your project root directory and define the ASGI application:

```python
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from myproject.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(websocket_urlpatterns),
})
```

This configuration tells Django to use the URLRouter for WebSocket connections.

## Using the real-time notification bar in Django views

To display real-time notifications, we need to integrate the notification bar into our Django views.

First, include the JavaScript file that handles the WebSocket connection in your template:

```html
{% load static %}
<script src="{% static 'js/notification.js' %}"></script>
```

Create and include the `notification.js` file:

```javascript
const webSocket = new WebSocket('ws://' + window.location.host + '/ws/notifications/');

webSocket.onmessage = function (event) {
    const notification = JSON.parse(event.data);
    // Handle the received notification here
};
```

This code establishes a WebSocket connection with the server and listens for incoming messages. When a notification is received, it can be processed and displayed in the notification bar.

Finally, modify your Django views to send notifications to connected clients whenever necessary:

```python
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_notification(user):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'notifications',
        {
            'type': 'send_notification',
            'message': 'New notification for user: ' + user.username,
        }
    )
```

This code sends a notification to all connected clients through the WebSocket channel group named 'notifications'. The `send_notification` function can be called from any Django view whenever a new notification is generated.

# Conclusion

Implementing a real-time notification bar with WebSockets in Django allows for efficient and instant updates without the need for constant client requests. By using Django Channels, we can easily handle WebSocket connections and send real-time notifications to connected clients. This enhances the user experience and makes our Django application more interactive.

#websockets #django