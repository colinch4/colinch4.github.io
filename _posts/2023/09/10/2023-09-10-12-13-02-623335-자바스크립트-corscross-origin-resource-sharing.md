---
layout: post
title: "자바스크립트 CORS(Cross-Origin Resource Sharing)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

CORS (Cross-Origin Resource Sharing) is a mechanism that allows resources (such as fonts, JavaScript, or AJAX requests) on a web page to be requested from a domain other than the one which the resource originated from. In other words, it enables secure cross-origin data sharing between different domains.

## Why CORS?

The same-origin policy is a fundamental security concept in web browsers that prevents a web page from making requests to a different domain. This policy helps to protect users from malicious scripts that could access sensitive data from different domains. However, it also poses a challenge when web applications need to interact with resources on different domains.

CORS comes into play to relax the same-origin policy and allow controlled access to resources from different origins, *origin* being defined as the combination of *protocol*, *domain*, and *port*.

## How CORS Works

The CORS mechanism enforces permissions for cross-origin requests through the use of HTTP headers. When a browser makes a cross-origin request, it includes an *Origin* header that specifies the origin of the request. The server then responds with an appropriate set of headers to allow or deny the request based on the policy defined by the server.

The key headers involved in CORS are:
- **Access-Control-Allow-Origin**: Specifies which domains are allowed to access the resource.
- **Access-Control-Allow-Methods**: Specifies the HTTP methods (e.g., GET, POST, PUT, DELETE) allowed for the resource.
- **Access-Control-Allow-Headers**: Specifies which headers are allowed for the request.
- **Access-Control-Allow-Credentials**: Specifies if the resource can be accessed with credentials (e.g., cookies, HTTP authentication).

## Implementing CORS in JavaScript

To enable CORS in JavaScript, you need to configure the server to include the necessary CORS headers in the response. Additionally, on the client-side, you can use the `XMLHttpRequest` or the newer `fetch` API to make cross-origin requests.

Here's an example of making a cross-origin request using `fetch`:

```javascript
fetch('https://api.example.com/data', {
  method: 'GET',
  headers: {
    'Origin': 'https://example.com'
  }
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

In the above example, the `Origin` header is set to `https://example.com`. The server is responsible for validating this origin and responding with the appropriate CORS headers. If the request is allowed, the response is converted to JSON and logged to the console.

When making cross-origin requests with credentials (e.g., cookies), you'll need to set the `credentials` option to `'include'`:

```javascript
fetch('https://api.example.com/data', {
  method: 'GET',
  headers: {
    'Origin': 'https://example.com'
  },
  credentials: 'include'
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

## Conclusion

CORS in JavaScript allows web applications to securely interact with resources from different origins. By configuring the server to include the appropriate CORS headers and using the appropriate client-side APIs, you can safely access cross-origin resources and enhance the functionality of your web applications. Remember to take necessary precautions and understand the security implications when enabling cross-origin resource sharing.