---
layout: post
title: "Implementing a real-time voting system with websockets in Django"
description: " "
date: 2023-09-22
tags: [websockets, Django]
comments: true
share: true
---

In this blog post, we'll explore how to implement a real-time voting system using websockets in Django. Websockets provide a bi-directional communication channel between the client and the server, allowing real-time updates without the need for constant polling.

## Why Use Websockets?

Traditionally, web applications rely on making repeated HTTP requests to update data on the client-side. However, this approach introduces unnecessary latency and increases the load on the server. Websockets offer a more efficient and responsive alternative by establishing a persistent connection between the client and the server.

## Prerequisites

Before we begin, make sure you have the following installed:

- Python (3.6 or higher)
- Django (3.x)
- Channels (3.x)
- Django Channels Redis (`channels_redis`)
- Redis server (to act as a message broker)

## Setting Up

1. Start by creating a new Django project and app:

   ```bash
   $ django-admin startproject voting_system
   $ cd voting_system
   $ python manage.py startapp polling
   ```

2. Install the required packages:

   ```bash
   $ pip install channels channels_redis
   ```

3. Configure Django Channels in your project's `settings.py` file:

   ```python
   INSTALLED_APPS = [
       # ...
       'channels',
   ]

   CHANNEL_LAYERS = {
       'default': {
           'BACKEND': 'channels_redis.core.RedisChannelLayer',
           'CONFIG': {
               'hosts': [('localhost', 6379)],
           },
      },
   }

   ASGI_APPLICATION = 'voting_system.routing.application'
   ```

4. Create a new file called `routing.py` in the project directory:

   ```python
   from django.urls import path
   from channels.routing import ProtocolTypeRouter, URLRouter
   from polling.consumers import VoteConsumer

   application = ProtocolTypeRouter({
       'http': get_asgi_application(),
       'websocket': URLRouter([
           path('ws/vote/', VoteConsumer.as_asgi()),
       ]),
   })
   ```

5. Create a new file called `consumers.py` in the `polling` app directory:

   ```python
   from channels.generic.websocket import AsyncWebsocketConsumer

   class VoteConsumer(AsyncWebsocketConsumer):
       async def connect(self):
           await self.accept()

       async def receive(self, text_data):
           # Process and store the received vote
           await self.send(text_data="Vote received successfully!")

       async def disconnect(self, close_code):
           # Handle client disconnection
           pass
   ```

## Frontend Implementation

1. Create a new HTML file called `index.html` in the `templates` directory:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <!-- Include necessary CSS and JS files -->
   </head>
   <body>
       <h1>Real-Time Voting System</h1>

       <form id="vote-form">
           <input type="radio" name="vote" value="option1"> Option 1<br>
           <input type="radio" name="vote" value="option2"> Option 2<br>
           <input type="radio" name="vote" value="option3"> Option 3<br>
           <button type="submit">Submit</button>
       </form>

       <!-- Add required JavaScript code -->
   </body>
   </html>
   ```

2. Include the necessary JavaScript code to handle the form submission and send the vote using websockets:

   ```javascript
   const form = document.getElementById('vote-form');

   form.addEventListener('submit', (event) => {
       event.preventDefault();

       const vote = document.querySelector('input[name="vote"]:checked').value;
       const socket = new WebSocket('ws://' + window.location.host + '/ws/vote/');

       socket.onopen = function(event) {
           socket.send(JSON.stringify({ 'vote': vote }));
       };

       socket.onmessage = function(event) {
           const message = JSON.parse(event.data);
           console.log(message);
       };
   });
   ```

## Conclusion

By implementing a real-time voting system using websockets in Django, we have significantly improved the responsiveness of our application. With websockets, data updates are delivered in real-time, providing a more seamless and interactive user experience.

To enhance this example further, you could implement additional features such as displaying live vote counts or using Django Channels groups to handle multiple voting sessions simultaneously.

#websockets #Django