---
layout: post
title: "Using websockets for real-time temperature monitoring in Django"
description: " "
date: 2023-09-22
tags: [Websockets, RealTimeMonitoring]
comments: true
share: true
---

In today's tech-driven world, real-time monitoring is becoming increasingly important. Being able to receive and display live data updates is crucial for many applications. With Django, a powerful Python web framework, we can easily achieve real-time functionality using websockets.

## What are Websockets? ##
Websockets provide a two-way, persistent connection between a client and a server. This allows for real-time communication, making it perfect for applications such as chat systems, real-time collaboration, and, in this case, temperature monitoring.

## Setting up Django Channels ##
Django Channels is a great extension for Django that enables the use of websockets. Let's start by setting up Django Channels in our Django project.

1. Install Django Channels by running the following command:
```bash
pip install channels
```

2. Add 'channels' to the `INSTALLED_APPS` list in your project's `settings.py` file.

3. We need to configure the ASGI application. Create a new file called `asgi.py` in your project's root directory and add the following code:

```python
import os
import django
from channels.routing import get_default_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
django.setup()
application = get_default_application()
```

4. Finally, update your project's `urls.py` file to include the necessary routing configuration. Add the following code:

```python
from django.urls import path
from your_app.consumers import TemperatureConsumer

websocket_urlpatterns = [
    path('ws/temperature/', TemperatureConsumer.as_asgi()),
    # Add other websocket routes if needed
]
```

## Implementing the Temperature Consumer ##
Now that we have set up Django Channels, let's implement a consumer that will handle incoming websocket connections and send real-time temperature updates to connected clients.

1. Create a new file called `consumers.py` in your app's directory and add the following code:

```python
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TemperatureConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'temperature_room'
        self.room_group_name = 'temperature_group'

        # Join the room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Handle incoming messages (if any)
        pass

    async def temperature_update(self, event):
        # Send temperature updates to connected clients
        temperature = event['temperature']
        await self.send(text_data=json.dumps({
            'temperature': temperature
        }))
```

2. In your Django app, whenever there is a temperature update, you can send it to the connected clients by using the following code:

```python
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

async def send_temperature_update(temperature):
    await channel_layer.group_send(
        'temperature_group',
        {
            'type': 'temperature_update',
            'temperature': temperature
        }
    )
```

## Connecting to the Websocket from the Frontend ##
To display the real-time temperature updates, you will need to establish a connection from the frontend using JavaScript. Here's an example of how you can do it using the `WebSocket` API:

```javascript
const websocket = new WebSocket('ws://localhost:8000/ws/temperature/');

websocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const temperature = data.temperature;
    // Update UI with the received temperature
}

websocket.onclose = function(e) {
    // Handle disconnection
}
```

Make sure to update `ws://localhost:8000/ws/temperature/` with the correct URL of your Django development server.

## Conclusion ##
By leveraging websockets and Django Channels, we can easily implement real-time temperature monitoring in Django applications. The ability to receive and display live updates can enhance the user experience and provide valuable insights. It's a powerful feature that can be extended to various other real-time use cases as well.

#Websockets #RealTimeMonitoring