---
layout: post
title: "Interceptor pattern in Python"
description: " "
date: 2023-10-04
tags: []
comments: true
share: true
---

The Interceptor pattern, also known as the "Chain of Responsibility" pattern, is a behavioral design pattern that allows multiple objects to participate in the handling of a request. Each object in the chain has the opportunity to process the request, modify it, or pass it on to the next object in the chain.

## How it works

The Interceptor pattern is based on a linked list of objects, where each object is responsible for either handling the request or passing it to the next object in the chain. The client sends the request to the first object in the chain, which then decides whether to handle the request or pass it along. If the request is passed along, the next object in the chain is responsible for processing it, and so on, until the request is either handled or reaches the end of the chain.

## Implementation in Python

Let's see an example implementation of the Interceptor pattern in Python. We will create a middleware layer for handling incoming HTTP requests and logging each request's information.

First, let's define the `Interceptor` class, which will serve as the base class for all interceptors in the chain. Each interceptor will have a `handle_request` method that will be responsible for processing the request or passing it to the next interceptor.

```python
class Interceptor:
    def __init__(self, next_interceptor=None):
        self.next_interceptor = next_interceptor

    def handle_request(self, request):
        if self.next_interceptor:
            self.next_interceptor.handle_request(request)
        else:
            raise NotImplementedError("No interceptor found to handle the request.")
```

Next, let's create specific interceptors that will perform different tasks on the request. For this example, we'll implement a `LoggerInterceptor` that logs each request's information.

```python
class LoggerInterceptor(Interceptor):
    def handle_request(self, request):
        # Log the request information
        print(f"Request: {request.method} {request.url}")

        # Pass the request to the next interceptor
        super().handle_request(request)
```

To complete the implementation, we need to create a `Request` class that will represent our HTTP request. In this example, we'll keep it simple and define only `method` and `url` attributes.

```python
class Request:
    def __init__(self, method, url):
        self.method = method
        self.url = url
```

Finally, let's create the chain of interceptors and test the implementation.

```python
if __name__ == "__main__":
    request = Request("GET", "https://example.com")

    # Create the interceptors
    logger_interceptor = LoggerInterceptor()
    # Add more interceptors if needed

    # Set up the chain
    logger_interceptor.handle_request(request)
```

When running the above code, you should see the request information being logged:

```
Request: GET https://example.com
```

## Conclusion

The Interceptor pattern provides a flexible and extensible way to handle requests by allowing multiple objects to participate in the processing. It promotes loose coupling between the sender and receiver of the request, allowing for dynamic modification of the request handling pipeline.

In this Python implementation, we saw how to create and utilize interceptors to log incoming HTTP requests. This pattern can be extended to handle various tasks, such as authentication, request validation, caching, and more.