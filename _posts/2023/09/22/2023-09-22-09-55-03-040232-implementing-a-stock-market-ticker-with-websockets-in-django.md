---
layout: post
title: "Implementing a stock market ticker with websockets in Django"
description: " "
date: 2023-09-22
tags: [websockets, DjangoChannels]
comments: true
share: true
---

In this blog post, we will explore how to implement a real-time stock market ticker using websockets in Django. Websockets provide a powerful mechanism for bidirectional communication between clients and servers, allowing us to push real-time updates to the user interface without the need for constant polling.

## Prerequisites

Before we begin, make sure you have the following installed on your system:

- Python and pip
- Django
- Django Channels (a third-party library that adds websocket support to Django)

## Setting up the project

To get started, create a new Django project and application by running the following commands:

```shell
$ django-admin startproject stock_ticker
$ cd stock_ticker
$ python manage.py startapp ticker
```

Next, add `'channels'` to the `INSTALLED_APPS` list in the `settings.py` file:

```python
INSTALLED_APPS = [
    ...
    'channels',
    ...
]
```

## Creating a websocket consumer

A websocket consumer is responsible for handling websocket connections and processing incoming and outgoing messages. Create a new file called `consumers.py` inside the `ticker` application directory:

```python
from channels.generic.websocket import AsyncWebsocketConsumer

class StockTickerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        pass
```

## Configuring routing

To handle websocket connections, we need to configure the Django Channels routing. Create a new file called `routing.py` inside the `stock_ticker` project directory:

```python
from django.urls import path
from .consumers import StockTickerConsumer

websocket_urlpatterns = [
    path('ws/ticker/', StockTickerConsumer.as_asgi()),
]
```

In the project's `asgi.py` file, add the following lines to the `application` variable:

```python
from django.urls import re_path
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
from stock_ticker import routing

application = ProtocolTypeRouter({
    'http': AsgiHandler(),
    'websocket': URLRouter(routing.websocket_urlpatterns),
})
```

## Adding Websocket handling to your views

Now that we have our consumer and routing configured, we need to connect them to our views. Open the `views.py` file in the `ticker` application and add the following code:

```python
from django.shortcuts import render, redirect
from django.views import View

class TickerView(View):
    template_name = 'ticker.html'

    def get(self, request):
        return render(request, self.template_name)
```

Next, create a new `urls.py` file inside the `ticker` application and add the following lines:

```python
from django.urls import path

from . import views

urlpatterns = [
    path('', views.TickerView.as_view(), name='ticker'),
]
```

## Creating the template

Create a new file called `ticker.html` inside the `templates` directory of the `ticker` application. Add the following HTML code:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Stock Market Ticker</title>
  </head>
  <body>
    <h1>Stock Market Ticker</h1>

    <script>
      const socket = new WebSocket('ws://localhost:8000/ws/ticker/');

      socket.onmessage = function(event) {
        const data = JSON.parse(event.data);
        // Handle the received data and update the ticker UI
      };
    </script>
  </body>
</html>
```

## Running the application

Finally, start the development server by running the following command:

```shell
$ python manage.py runserver
```

Visit `http://localhost:8000` in your web browser, and you should see the Stock Market Ticker page. The websocket connection is established, and now you can implement the logic to update the ticker with real-time stock data.

## Conclusion

In this blog post, we have learned how to implement a stock market ticker using websockets in Django. Websockets provide an efficient way of updating the UI in real-time without the need for constant polling. Utilizing Django Channels, we established a websocket connection in our project and created a basic consumer to handle incoming messages. Now you can extend this implementation to fetch stock data and update the ticker accordingly. Happy coding!

#websockets #DjangoChannels