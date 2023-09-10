---
layout: post
title: "자바스크립트 CORS(Cross-Origin Resource Sharing)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

In this blog post, we will explore **CORS (Cross-Origin Resource Sharing)**, which is an important mechanism that allows resources (such as fonts, images, scripts, etc.) on a web page to be requested from a different-origin domain. CORS helps in protecting the web application from *cross-site scripting* attacks and provides controlled access to resources.

## What is CORS?

CORS is a security feature implemented in web browsers that allows a web page to make requests to a different domain than the one it originates from. By default, web browsers enforce [*same-origin policy*](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy), which restricts the access to resources from different origins. CORS relaxes this policy by adding HTTP headers to the requests and responses exchanged between the client and server, indicating allowed origins, methods, and headers.

### The CORS Flow

1. **Preflight Request**: When an XMLHttpRequest or Fetch API request is made from a web page to a different-origin domain, the browser first sends a preflight request with the *OPTIONS* method to check if the server allows the actual request.
   
2. **Server Validation**: The server checks the Origin header in the preflight request and verifies if it is allowed to access its resources. It responds with the appropriate CORS headers (*Access-Control-Allow-Origin*, *Access-Control-Allow-Methods*, etc.) in the response.
   
3. **Actual Request**: If the preflight request is successful, the browser sends the actual request (GET, POST, PUT, DELETE, etc.) along with the relevant CORS headers.
   
4. **Server Response**: The server processes the actual request and responds with the requested resource or an error message.

## How to Handle CORS Requests in JavaScript?

In JavaScript, we can handle CORS requests using the Fetch API or the XMLHttpRequest object. Here's an example of making a GET request to a different-origin API using Fetch API:

```javascript
fetch('https://api.example.com/data', {
  method: 'GET',
  mode: 'cors',
  credentials: 'same-origin'
})
  .then(response => response.json())
  .then(data => {
    // Process the received data
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });
```

In the above code snippet:
- The URL `https://api.example.com/data` is the endpoint from a different-origin domain.
- The **`mode`** option is set to `'cors'` to enable CORS.
- The **`credentials`** option is set to `'same-origin'` to include credentials (cookies, HTTP authentication, etc.) in the request.

## CORS Server Configuration

To allow CORS requests on the server side, the backend needs to respond with the appropriate CORS headers. Here's an example of setting CORS headers in a Node.js Express application:

```javascript
const express = require('express');
const app = express();

app.use((req, res, next) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization');
  next();
});

// Define your API routes here

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
```

In the above code snippet, we set the following headers:
- **`Access-Control-Allow-Origin`**: Allow requests from all origins. You can set specific domains instead of '*' to allow requests only from those domains.
- **`Access-Control-Allow-Methods`**: Specify the allowed HTTP methods (GET, POST, PUT, DELETE, etc.).
- **`Access-Control-Allow-Headers`**: Specify the allowed request headers.

## Conclusion

CORS plays a crucial role in enabling communication between web applications hosted on different origins. It provides a secure way to control resource sharing and protects against unauthorized access. Understanding CORS is fundamental when building web applications that interact with external APIs or resources.

Remember to configure your server-side application to handle CORS requests properly and utilize JavaScript's Fetch API or XMLHttpRequest to handle CORS requests on the client-side.