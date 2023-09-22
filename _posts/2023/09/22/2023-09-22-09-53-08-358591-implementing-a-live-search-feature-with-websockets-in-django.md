---
layout: post
title: "Implementing a live search feature with websockets in Django"
description: " "
date: 2023-09-22
tags: [django, websockets]
comments: true
share: true
---

Websockets have gained popularity for building real-time applications and live features. In this blog post, we will explore how to implement a live search feature using websockets in Django. By leveraging websockets, we can provide instant search results to users as they type, improving their search experience.

## Prerequisites
Before diving into the implementation, make sure you have the following set up:

- Django installed on your system
- Basic knowledge of Django's views and templates
- Basic knowledge of JavaScript and websockets

## Setting up the Project
Let's start by creating a new Django project and app. Open up your terminal and run the following commands:

```bash
$ django-admin startproject live_search
$ cd live_search
$ python manage.py startapp search
```

Now, let's create a simple view and template for our search app. Open `search/views.py` and add the following code:

```python
from django.shortcuts import render

def search_view(request):
    return render(request, 'search.html')
```

Next, create a `templates` directory in the `search` app and then create a new file called `search.html` inside the `templates` directory. In `search.html`, add the following code:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Live Search</title>
</head>
<body>
    <h1>Live Search</h1>
    <input type="text" id="search-input" placeholder="Type to search...">
    <div id="search-results"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.3.1/socket.io.js"></script>
    <script>
        // Your JavaScript code will go here
    </script>
</body>
</html>
```

## Implementing the Websocket Connection
### Setting up Django Channels
To handle websockets in Django, we need to use Django Channels. Install Django Channels by running the following command:

```bash
$ pip install channels
```

Next, add `'channels'` to the `INSTALLED_APPS` list in your project's `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'channels',
    ...
]
```

In the same file, add the following code at the end:

```python
ASGI_APPLICATION = 'live_search.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    }
}
```

### Creating a Consumer
In Django Channels, a consumer is responsible for handling incoming websocket connections. Create a new file called `consumers.py` inside the `search` app directory and add the following code:

```python
from channels.generic.websocket import AsyncJsonWebsocketConsumer

class SearchConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive_json(self, content, **kwargs):
        # Handle search logic and send search results back to the client
        search_term = content.get('search_term')
        search_results = self.search(search_term)
        await self.send_json({
            'search_results': search_results
        })

    async def disconnect(self, code):
        # Clean up any resources, if needed
        pass

    def search(self, search_term):
        # Implement your search logic here
        # Return search results as a list or dictionary
        pass
```

### Routing Websockets
To handle websocket connections, we need to set up the routing configuration. Create a new file called `routing.py` in your project's root directory and add the following code:

```python
from django.urls import re_path

from search.consumers import SearchConsumer

websocket_urlpatterns = [
    re_path(r'ws/search/$', SearchConsumer.as_asgi()),
]
```

Next, open `live_search/asgi.py` and modify it as follows:

```python
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

from .routing import websocket_urlpatterns

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(websocket_urlpatterns),
})
```

## Connecting the Frontend with Websockets
With the backend set up, we can now make the necessary changes in our template to establish a websocket connection and handle search events. Replace the commented JavaScript code in `search.html` with the following code:

```javascript
<script>
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    const socket = io();

    searchInput.addEventListener('input', (event) => {
        const searchQuery = event.target.value;
        socket.send(JSON.stringify({
            'search_term': searchQuery
        }));
    });

    socket.on('message', (data) => {
        const { search_results } = JSON.parse(data);
        searchResults.innerHTML = '';
        search_results.forEach(result => {
            const resultElement = document.createElement('div');
            resultElement.innerText = result;
            searchResults.appendChild(resultElement);
        });
    });
</script>
```

## Start the Server
Let's run the Django development server to see our live search feature in action. In the terminal, run the following command from the project's root directory:

```bash
$ python manage.py runserver
```

Now, open your browser and go to `http://localhost:8000/search/`. You should see the live search page with a search input field. As you start typing in the input field, the search results should appear below it in real-time.

## Conclusion
In this blog post, we explored how to implement a live search feature using websockets in Django. By combining Django Channels with JavaScript, we were able to create an instant search experience for our users. This functionality can be extended and customized according to the specific needs of your application.

#django #websockets