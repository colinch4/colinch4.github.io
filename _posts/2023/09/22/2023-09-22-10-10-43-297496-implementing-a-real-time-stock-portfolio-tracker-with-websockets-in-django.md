---
layout: post
title: "Implementing a real-time stock portfolio tracker with websockets in Django"
description: " "
date: 2023-09-22
tags: [stock, stock]
comments: true
share: true
---

In this tutorial, we will learn how to build a real-time stock portfolio tracker using websockets in the Django framework. Websockets allow us to establish a persistent connection between the client and the server, enabling real-time updates without the need for continuous HTTP requests.

## Prerequisites

To follow along with this tutorial, you should have the following:

- Basic knowledge of Python and Django
- A working installation of Django
- familiarity with websockets and Django Channels

## Setting up the Project

First, let's create a new Django project and app:

```shell
$ django-admin startproject stock_portfolio_tracker
$ cd stock_portfolio_tracker
$ python manage.py startapp portfolio
```

We also need to install Django Channels:

```shell
$ pip install django channels
```

Next, we need to configure Django Channels in our project. Update the `stock_portfolio_tracker/settings.py` file with the following:

```python
...
INSTALLED_APPS = [
    ...
    'channels',
    'portfolio',
]
...
ASGI_APPLICATION = 'stock_portfolio_tracker.routing.application'
...
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}
```

Now, create a new file called `routing.py` in the same directory as `manage.py` with the following content:

```python
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
from portfolio import consumers

application = ProtocolTypeRouter({
    'websocket': URLRouter([
        re_path(r'ws/stocks/', consumers.StockConsumer.as_asgi()),
    ]),
})
```

## Creating a Stock Consumer

Next, let's create a consumer to handle the real-time updates. Create a new file called `consumers.py` inside the `portfolio` app with the following content:

```python
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class StockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        stock_symbol = text_data_json['symbol']

        # Fetch stock data for the given symbol
        # Update the stock information in the database

        # Send updated stock information back to the client
        await self.send(json.dumps({
            'symbol': stock_symbol,
            'price': 100.0,  # Dummy data for demonstration
            'change': 2.5,   # Dummy data for demonstration
        }))
```

## Displaying Real-Time Stock Updates on the Frontend

Now, let's create a basic HTML template `stock.html` to display the real-time stock updates:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Stock Portfolio Tracker</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
    <script>
        const socket = new WebSocket('ws://' + window.location.host + '/ws/stocks/');
        
        socket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            updateStockInfo(data);
        };
        
        function updateStockInfo(data) {
            // Update the stock information on the webpage
            $('#stock-symbol').text(data.symbol);
            $('#stock-price').text(data.price);
            $('#stock-change').text(data.change);
        }
    </script>
</head>
<body>
    <h1>Stock Portfolio Tracker</h1>
    
    <h2>Stock Information</h2>
    <p>Symbol: <span id="stock-symbol"></span></p>
    <p>Price: $<span id="stock-price"></span></p>
    <p>Change: <span id="stock-change"></span>%</p>
</body>
</html>
```

## Finalizing the Project

To complete the project, we need to create a Django view to render the `stock.html` template. Update `portfolio/views.py` with the following code:

```python
from django.shortcuts import render

def stock_view(request):
    return render(request, 'stock.html')
```

Finally, update `portfolio/urls.py` with the following code:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('stocks/', views.stock_view, name='stock_view'),
]
```

## Conclusion

In this tutorial, we learned how to implement a real-time stock portfolio tracker using websockets in Django. We created a stock consumer to handle real-time updates, displayed the stock information on the frontend, and updated the information using websockets. With this functionality, users can see live updates of their stock portfolio without the need for continuous page refreshes.

#websockets #Django