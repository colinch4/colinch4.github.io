---
layout: post
title: "Implementing a real-time notification system with websockets in Django"
description: " "
date: 2023-09-22
tags: [django, websockets]
comments: true
share: true
---

In today's fast-paced world, users expect real-time updates and notifications when using web applications. One way to achieve this is by implementing a real-time notification system using websockets in Django. In this blog post, we will explore how to accomplish this using Django channels, a third-party library that enables the use of websockets in Django.

### Step 1: Setup Django Channels

1. Install Django Channels by running the following command:

```python
pip install channels
```

2. Add `channels` to your `INSTALLED_APPS` in your Django project's `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'channels',
    ...
]
```

3. Configure the Django Channels ASGI application by creating a `routing.py` file in your Django project's root directory:

```python
from django.urls import re_path

websocket_urlpatterns = [
    re_path(r'ws/notifications/$', consumers.NotificationConsumer.as_asgi()),
]
```

### Step 2: Create a Notification Consumer

1. Create a `consumers.py` file in your Django app's directory and define a `NotificationConsumer` class:

```python
from channels.generic.websocket import AsyncWebsocketConsumer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        # Clean up any resources (if necessary) when the websocket connection is closed
        pass

    async def receive(self, text_data):
        # Handle received data from the websocket
        pass
```

### Step 3: Send and Receive Notifications

1. In your view or model, whenever a new notification is generated, send it to the connected clients:

```python
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def send_notification(notification):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("notifications", {"type": "notification.message", "message": notification})
```

2. Modify the `NotificationConsumer` to receive and handle the notifications:

```python
async def receive(self, text_data):
    # Handle received data from the websocket
    pass

async def notification_message(self, event):
    await self.send(text_data=event['message'])
```

### Step 4: Connect to Websocket

1. In your frontend, connect to the websocket using JavaScript:

```javascript
const socket = new WebSocket("ws://localhost:8000/ws/notifications/");

socket.onmessage = function (e) {
    // Handle received messages from the websocket
};

socket.onclose = function (e) {
    // Handle websocket connection closed
};

socket.onopen = function (e) {
    // Perform any necessary initialization on websocket connection
};

socket.onerror = function (e) {
    // Handle any websocket errors
};
```

With these steps, you have now successfully implemented a real-time notification system with websockets in Django. Users will receive instant updates and notifications, enhancing their overall experience on your web application.

#django #websockets