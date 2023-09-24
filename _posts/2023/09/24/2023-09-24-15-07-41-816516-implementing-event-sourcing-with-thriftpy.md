---
layout: post
title: "Implementing event sourcing with ThriftPy"
description: " "
date: 2023-09-24
tags: [hashtags, event]
comments: true
share: true
---

![ThriftPy Logo](https://example.com/images/thriftpy-logo.png)

Event sourcing is a popular architectural pattern that allows you to capture and store every change made to an application's state as a series of immutable events. Using event sourcing can help you build highly scalable and resilient systems by providing a complete audit trail of all actions performed on the application's data.

[ThriftPy](https://thriftpy.readthedocs.io/en/latest/) is a Python library for working with Thrift, a popular cross-language serialization framework for efficient communication between different systems. In this article, we will explore how we can implement event sourcing using ThriftPy.

## What is Event Sourcing?

Event sourcing is an approach to persisting application state by storing a series of events that represent changes to that state, rather than simply storing the current state itself. This allows you to recreate the state of the application at any point in time by replaying the events.

## Getting Started with ThriftPy

Before we start implementing event sourcing, let's make sure we have ThriftPy installed. You can install it using `pip`:

```shell
pip install thriftpy
```

Once ThriftPy is installed, we can create our Thrift structure and service definitions. Let's define a simple event structure and a service that can consume and append events to an event log.

```python
# event.thrift
struct Event {
    1: string id,
    2: string type,
    3: i64 timestamp,
    4: binary payload,
}

# event_service.thrift
namespace py event
service EventService {
    void consume(1: Event event),
    void append(1: Event event),
}
```

Make sure to generate the Python code from the Thrift definitions:

```shell
thrift -r --gen py event.thrift
thrift -r --gen py event_service.thrift
```

## Implementing Event Sourcing with ThriftPy

To implement event sourcing with ThriftPy, we need to create an event log that stores all the events. We can use a database, like PostgreSQL or MongoDB, to persist the events. Here, we will assume a PostgreSQL database for simplicity.

First, let's create a `PostgresEventLog` class that handles the interaction with the PostgreSQL database using the `psycopg2` library:

```python
import psycopg2

class PostgresEventLog:
    def __init__(self, database, user, password, host, port):
        self.connection = psycopg2.connect(
            database=database,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        self.cursor = self.connection.cursor()

    def consume(self, event):
        # Implement event consumption logic here

    def append(self, event):
        # Implement event appending logic here

    def close(self):
        self.cursor.close()
        self.connection.close()
```

In the `consume` method, we can process the event and update the application state accordingly. The `append` method is responsible for storing the event in the database.

Next, let's create a server that exposes the `EventService` defined in our Thrift definitions and uses the `PostgresEventLog` class:

```python
from thriftpy2.rpc import make_server
from event_service import EventService
from event.ttypes import Event

class EventServiceImpl(EventService):
    def __init__(self, event_log):
        self.event_log = event_log

    def consume(self, event):
        self.event_log.consume(event)

    def append(self, event):
        self.event_log.append(event)

# Assuming we already have a PostgresEventLog instance
event_log = PostgresEventLog(database="mydb", user="myuser", password="mypassword", host="localhost", port=5432)

# Create Thrift server
server = make_server(EventService, EventServiceImpl(event_log), host="localhost", port=9090)
server.serve()
```

Now, we can start the server and clients can consume and append events using ThriftPy.

## Conclusion

In this article, we explored how to implement event sourcing using ThriftPy. We defined our event structure and service using Thrift definitions, implemented the event log using the `PostgresEventLog` class, and created a server that exposes the `EventService` for clients to interact with.

Event sourcing can be a powerful pattern for building highly scalable and resilient applications. ThriftPy provides an easy and efficient way to work with Thrift in Python, making it a great choice for implementing event sourcing functionality.

#hashtags #event-sourcing #ThriftPy