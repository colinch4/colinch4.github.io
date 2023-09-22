---
layout: post
title: "Implementing a real-time flight tracker with websockets in Django"
description: " "
date: 2023-09-22
tags: [django, websockets]
comments: true
share: true
---

In this tutorial, we will explore how to build a real-time flight tracker using Websockets in Django. Websockets allow for bidirectional communication between the client and the server, enabling real-time updates without the need for continuous HTTP requests.

## Prerequisites

Before getting started, ensure that you have the following:

- Django installed on your local machine
- Basic knowledge of Django and Python
- Basic understanding of Websockets and their usage

## Setting Up the Django Project

First, let's create a new Django project by running the following command:

```
django-admin startproject flight_tracker
```

Once the project is created, navigate into the project's directory:

```
cd flight_tracker
```

Next, create a new Django app called `tracker`:

```
python manage.py startapp tracker
```

Include the `tracker` app in the project's `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'tracker',
    ...
]
```

## Installing Required Packages

To implement Websockets in Django, we need to install the `Channels` package. Open a terminal, navigate to the project directory, and run the following command:

```
pip install channels
```

## Creating WebSocket Consumer

In Django Channels, a websocket consumer handles the websocket connections and events. Create a new file called `consumers.py` inside the `tracker` app directory.

```python
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class FlightTrackerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = 'flight_room_%s' % self.room_id

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive websocket data
    async def receive(self, text_data):
        data = json.loads(text_data)
        # Process data and update flight details
        ...

        # Send updated data to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'flight_update',
                'data': updated_data
            }
        )

    # Receive updated flight data
    async def flight_update(self, event):
        data = event['data']

        # Send data to websocket
        await self.send(text_data=json.dumps({
            'data': data
        }))
```

## Routing Websocket Connections

To route our websocket connections to the consumer, we need to create a `routing.py` file in the project's directory.

```python
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/tracker/(?P<room_id>\w+)/$', consumers.FlightTrackerConsumer.as_asgi()),
]
```

## Updating Project's Routing Configuration

Lastly, we need to update the project's routing configuration to include the websocket routing. Modify the `urls.py` file in the project's directory:

```python
from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    ...
    re_path('tracker/', include('tracker.urls')),
    re_path('ws/', include('tracker.routing.websocket_urlpatterns')),
    ...
]
```

## Testing the Flight Tracker

To test the flight tracker, start the Django development server:

```
python manage.py runserver
```

Open your web browser and navigate to `http://localhost:8000/tracker/`. You should see a page where you can enter the `room_id`. Open another browser window or tab, enter the same `room_id`, and click the "Connect" button.

You can now send flight data in real-time from one browser window to another. The flight data will be updated instantly for all connected users.

## Conclusion

Congratulations! You have successfully implemented a real-time flight tracker using websockets in Django. By utilizing Django Channels, you can enhance the interactivity and real-time updates of your Django applications. Enjoy exploring this powerful technology and have fun building innovative projects!

#django #websockets