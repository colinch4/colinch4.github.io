---
layout: post
title: "Implementing a real-time collaborative document editor with websockets in Django"
description: " "
date: 2023-09-22
tags: [Django, WebSocket]
comments: true
share: true
---

In this tutorial, we will explore how to build a real-time collaborative document editor using websockets in Django. This will allow multiple users to simultaneously edit a document and see the changes in real-time, similar to Google Docs.

## Prerequisites
Before we begin, make sure you have the following:
- Basic knowledge of **Python** and **Django**
- Understanding of websockets and some knowledge of **JavaScript**

## Setting up the Project
1. Start by creating a new Django project using the following command:

```
django-admin startproject document_editor
```

2. Create a new Django app within the project:

```
cd document_editor
python manage.py startapp editor
```

3. Install the required dependencies:

```
pip install channels channels_redis
```

4. Add the following configurations to your project's `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'channels',
    'editor',
    ...
]

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [("localhost", 6379)],
        },
    },
}
```

## Implementing Websockets with Django Channels
1. Create a new file called `consumers.py` within the `editor` app:

```python
from channels.generic.websocket import AsyncWebsocketConsumer

class EditorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'editor_%s' % self.room_name

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        # Process received data and broadcast the changes to other users
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'editor_update',
                'data': text_data
            }
        )

    async def editor_update(self, event):
        text_data = event['data']

        # Send the updated data to the connected users
        await self.send(text_data)
```

2. Update your project's `routing.py` file to include the following code:

```python
from django.urls import re_path

from .consumers import EditorConsumer

websocket_urlpatterns = [
    re_path(r'ws/editor/(?P<room_name>\w+)/$', EditorConsumer.as_asgi()),
]
```

## Creating the Document Editor Templates
1. Create a new file called `document.html` within the `templates` directory:

```html
{% raw %}
{% extends 'base.html' %}

{% block content %}
    <div id="editor"></div>

    <script>
        const socket = new WebSocket('ws://' + window.location.host + '/ws/editor/{{ room_name }}/');
        
        socket.onopen = () => {
            console.log('Connection established.');
        };
        
        socket.onmessage = (event) => {
            // Update the document's content
            document.getElementById('editor').innerText = event.data;
        };
        
        socket.onclose = () => {
            console.log('Connection closed.');
        };
        
        // Function to handle changes in the document
        const handleUpdate = () => {
            const content = document.getElementById('editor').innerText;
            socket.send(content);
        };
        
        // Event listener to update the document
        document.getElementById('editor').addEventListener('input', handleUpdate);
    </script>
{% endblock %}
{% endraw %}
```

2. Update your `views.py` file within the `editor` app to include the following:

```python
from django.shortcuts import render

def document(request, room_name):
    return render(request, 'document.html', {'room_name': room_name})
```

3. Define the necessary URL patterns in your project's `urls.py` file:

```python
from django.urls import path

from editor import views

urlpatterns = [
    path('document/<str:room_name>/', views.document, name='document'),
]
```

## Running the Application
1. Start the Django development server:

```
python manage.py runserver
```

2. Access the application in your web browser at `http://localhost:8000/document/my-room/`, where `my-room` can be any desired room name.

## Conclusion
In this tutorial, you learned how to implement a real-time collaborative document editor using websockets in Django. Now, multiple users can simultaneously edit a document, and the changes are propagated in real-time to other connected users. This functionality opens up a range of possibilities for building collaborative web applications. Happy coding!

## #Django #WebSocket