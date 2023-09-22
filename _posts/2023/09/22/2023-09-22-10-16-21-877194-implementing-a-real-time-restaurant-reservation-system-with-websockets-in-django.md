---
layout: post
title: "Implementing a real-time restaurant reservation system with websockets in Django"
description: " "
date: 2023-09-22
tags: [django, realtime]
comments: true
share: true
---

In this blog post, we will explore how to create a real-time restaurant reservation system using websockets in Django. This system will allow users to make reservations and receive instant updates when a reservation is made or cancelled.

## Why Websockets?

Traditional HTTP requests are request-response based, meaning the client makes a request to the server and waits for a response. This can lead to delays in receiving updates in real-time. Websockets, on the other hand, enable bidirectional communication between the client and the server, allowing for instant updates without the need for continuous polling.

## Setting up Django Channels

[Django Channels](https://channels.readthedocs.io/) is a powerful Django extension that allows for the handling of websockets and other asynchronous protocols. To get started, we need to install Django Channels using the following command:

\`\`\`bash
pip install channels
\`\`\`

Once installed, add Channels to your Django project by including it in the `INSTALLED_APPS` section of your project's `settings.py` file:

\`\`\`python
INSTALLED_APPS = [
    ...
    'channels',
    ...
]
\`\`\`

Next, we need to configure the routing for our websocket connections. Create a new file called `routing.py` in your application directory and add the following code:

\`\`\`python
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            ...
        )
    ),
})
\`\`\`

Make sure to replace `...` with the appropriate routing configuration for your application. We will come back to this later.

In the `settings.py` file, add the following configurations for Channels:

\`\`\`python
ASGI_APPLICATION = 'myproject.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
\`\`\`

The `ASGI_APPLICATION` should point to the `routing.py` file we created earlier.

## Creating the Reservation Model and Views

Before we dive into the websocket implementation, let's set up our reservation model and views. Create a new model called `Reservation` in your application's `models.py` file:

\`\`\`python
from django.db import models

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    guests = models.PositiveIntegerField()
    # Add any other necessary fields

    def __str__(self):
        return f'{self.user.username} - {self.datetime}'
\`\`\`

Next, create a view for making reservations and retrieving existing reservations. Add the following code to your application's `views.py` file:

\`\`\`python
from django.shortcuts import render
from .models import Reservation

def make_reservation(request):
    # Handle reservation form submission

def get_reservations(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservation_list.html', {'reservations': reservations})
\`\`\`

## Updating Reservations in Real-Time with Websockets

Now that we have our model and views set up, let's implement the real-time updates for new reservations using websockets.

First, define a consumer class in your application's `consumers.py` file:

\`\`\`python
from channels.generic.websocket import AsyncWebsocketConsumer

class ReservationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Perform any initial setup for the websocket connection

    async def receive(self, text_data):
        # Handle received data from the websocket connection

    async def disconnect(self, close_code):
        # Cleanup when the websocket connection is closed
\`\`\`

The `connect` method is used to perform any initial setup for the websocket connection, such as authenticating the user. The `receive` method handles incoming data from the websocket connection, such as new reservation notifications.

Next, update the routing configuration in your `routing.py` file to map the websocket path to the `ReservationConsumer`:

\`\`\`python
from django.urls import re_path
from .consumers import ReservationConsumer

websocket_urlpatterns = [
    re_path(r'ws/reservations/$', ReservationConsumer.as_asgi()),
]
\`\`\`

This configuration maps the URL pattern `/ws/reservations/` to the `ReservationConsumer.as_asgi()` method.

Lastly, update your reservation views to notify the connected clients when a new reservation is made:

\`\`\`python
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def make_reservation(request):
    # Handle reservation form submission

    # Notify connected clients
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'reservation_updates',
        {
            'type': 'reservation_notification',
            'message': 'New reservation made',
        }
    )
\`\`\`

In this example, we use the `channel_layer` to send a group notification to all connected clients. The group name `reservation_updates` can be customized to fit your needs.

## Conclusion

By implementing websockets using Django Channels, we've created a real-time restaurant reservation system that allows for instant updates. Clients connected to the websocket can receive notifications when new reservations are made or cancelled. This setup provides a seamless and efficient way to handle reservations in real-time.

#django #realtime