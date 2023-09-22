---
layout: post
title: "Implementing a real-time photo sharing app with websockets in Django"
description: " "
date: 2023-09-22
tags: [hashtags, Django]
comments: true
share: true
---

In this tutorial, we will walk through the process of building a real-time photo sharing app using websockets in Django. By utilizing websockets, we can achieve real-time updates and instant sharing of photos between users.

## Prerequisites
Before we begin, make sure you have the following:

- Django installed on your system
- Basic knowledge of Django models and views

## Setting up Django Channels
Django Channels is a package that provides support for handling websockets in Django. Begin by installing it using pip:

```bash
pip install channels
```

Next, make sure to add `'channels'` to your Django project's `INSTALLED_APPS` setting in `settings.py`. Add the following line:

```python
INSTALLED_APPS = [
    ...
    'channels',
    ...
]
```

## Creating the Photo model and WebSocket consumers
Create a Django model to represent the photos in your app. For simplicity, let's assume our model consists of the following fields:

```python
from django.db import models

class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

Now, let's create a WebSocket consumer to handle the real-time photo sharing functionality. Create a new file `consumers.py` in your Django app directory:

```python
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class PhotoConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Connect to the websocket
        await self.accept()

    async def disconnect(self, close_code):
        # Disconnect from the websocket
        pass

    async def receive(self, text_data):
        # Process incoming messages
        text_data_json = json.loads(text_data)
        # Handle different message types (e.g., "new_photo", "delete_photo")
        # Perform necessary operations and broadcast updates
        await self.send(text_data=json.dumps({
            'message': 'Photo has been shared successfully!'
        }))
```

## Routing WebSocket requests
Open your Django app's `routing.py` file and add a URL route to handle the WebSocket requests. Add the following code:

```python
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/photos/$', consumers.PhotoConsumer.as_asgi()),
]
```

## Updating Django settings
Update your Django project's `settings.py` file to include the required settings for using Django Channels. Add the following lines:

```python
ASGI_APPLICATION = 'your_project_name.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    }
}
```

## Testing the app
With the above steps completed, you are ready to test your real-time photo sharing app.

Start the development server by running the following command:

```bash
python manage.py runserver
```

Visit your app in a web browser and open the developer console. You can use JavaScript to connect to the websocket and send messages to perform real-time actions on the server.

## Conclusion
By combining Django, Django Channels, and websockets, we have successfully implemented a real-time photo sharing app. With websockets, users can instantly share and receive updates on shared photos. Explore further by adding authentication, notification systems, and additional features to enhance the app.

#hashtags: #Django #Websockets