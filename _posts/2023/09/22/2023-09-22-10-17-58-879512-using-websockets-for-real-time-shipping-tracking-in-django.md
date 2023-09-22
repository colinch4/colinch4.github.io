---
layout: post
title: "Using websockets for real-time shipping tracking in Django"
description: " "
date: 2023-09-22
tags: [websockets, django]
comments: true
share: true
---

Tracking shipping packages in real-time is essential for many businesses, especially those in the e-commerce industry. Django, a popular web development framework, provides a powerful solution for building real-time applications using **Websockets**.

In this tutorial, we will explore how to implement real-time shipping tracking in Django using Websockets and the **Channels** library.

## Prerequisites
Before starting, ensure you have the following installed:
- Python and Django
- Channels library (`pip install channels`)

## Setting up Django Channels
1. Create a new Django project:
```
$ django-admin startproject shipping_tracker
```
2. Create a new Django app:
```
$ cd shipping_tracker
$ python manage.py startapp tracking
```
3. Install Django Channels:
```
$ pip install channels
```
4. Add Channels to your Django project's settings:
```python
# settings.py

INSTALLED_APPS = [
    ...
    'channels',
    ...
]

ASGI_APPLICATION = 'shipping_tracker.routing.application'
```
5. Create a new file named `routing.py` in your Django project directory:
```python
# routing.py

from channels.routing import ProtocolTypeRouter

application = ProtocolTypeRouter({
    # (http->django views is added by default)
})
```
6. Update your Django project's `urls.py` file to include Channels' WebSocket routing:
```python
# urls.py

from django.urls import path
from tracking import consumers

websocket_urlpatterns = [
    path('ws/tracking/', consumers.TrackingConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(websocket_urlpatterns)
    ),
})
```

## Creating the Consumer
Consumers handle real-time messages received over Websockets. In our case, we need a consumer that receives shipping tracking updates from the server and relays them to the connected clients.

1. Create a new file named `consumers.py` in your `tracking` app directory:
```python
# consumers.py

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

class TrackingConsumer(WebsocketConsumer):
    def connect(self):
        # Connect to the websocket
        self.room_name = 'shipping_updates'
        self.room_group_name = 'shipping_updates_group'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Disconnect from the websocket
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        # Receive message from the websocket
        text_data_json = json.loads(text_data)
        tracking_id = text_data_json['tracking_id']

        # Simulate fetching tracking updates from database
        tracking_updates = [
            'Package is being processed',
            'Package has left the warehouse',
            'Package is out for delivery',
            'Package has been delivered',
        ]

        # Send tracking updates to connected clients
        for update in tracking_updates:
            self.send(text_data=json.dumps({
                'tracking_update': update
            }))
```

## Displaying Real-Time Tracking Updates
Finally, we need to display the real-time tracking updates on the client-side.

1. Create a new HTML file named `tracking.html` in your Django app's templates directory:
```html
<!-- tracking.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Shipping Tracking</title>
</head>
<body>
    <h1>Shipping Tracking</h1>
    <ul id="tracking-updates"></ul>

    <script>
        var wsProtocol = window.location.protocol === "https:" ? "wss:" : "ws:";
        var wsPath = wsProtocol + "//" + window.location.host + "/ws/tracking/";
        var socket = new WebSocket(wsPath);

        socket.onmessage = function(e) {
            var update = JSON.parse(e.data);
            var trackingUpdate = document.createElement('li');
            trackingUpdate.innerHTML = update.tracking_update;
            document.getElementById("tracking-updates").appendChild(trackingUpdate);
        };
    </script>
</body>
</html>
```

2. Create a Django view to render the `tracking.html` template:
```python
# views.py

from django.shortcuts import render

def track_package(request):
    return render(request, 'tracking.html')
```

3. Make sure you add the appropriate URL configuration in your Django app's `urls.py`:
```python
# urls.py

from django.urls import path
from tracking import views

urlpatterns = [
    path('tracking/', views.track_package, name='tracking'),
]
```

## Conclusion
By using Django Channels and Websockets, we have created a real-time shipping tracking system. The `TrackingConsumer` handles receiving and sending updates to the connected clients, while the JavaScript code in the `tracking.html` template displays the updates in real-time.

Using this setup, you can easily integrate real-time shipping tracking into your Django application and provide your users with an enhanced shipping experience.

#websockets #django