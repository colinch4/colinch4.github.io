---
layout: post
title: "자바스크립트 비동기 함수와 멀티 스레딩 (Asynchronous Functions and Multithreading)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

JavaScript is a single-threaded programming language, which means it can only execute one task at a time. However, it also provides mechanisms for handling asynchronous operations and achieving concurrency through asynchronous functions and multithreading concepts.

## Asynchronous Functions

**Asynchronous functions** in JavaScript allow the execution of tasks to continue without waiting for a previous task to complete. This is particularly useful when dealing with time-consuming operations like fetching data from a server or performing computations that could potentially block the main thread.

In JavaScript, asynchronous functions can be achieved through various mechanisms such as Promises, async/await, and callbacks. Let's take a look at an example of using promises:

```javascript
// Promise example
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Data fetched successfully");
    }, 2000);
  });
}

console.log("Before fetching data");

fetchData()
  .then((data) => {
    console.log(data);
  })
  .catch((error) => {
    console.error(error);
  });

console.log("After fetching data");
```

In the above example, the `fetchData` function returns a Promise object that resolves with the fetched data after a delay of 2 seconds. The `then` and `catch` methods are then used to handle the resolved value or any error that might occur.

The output of the above code will be:

```
Before fetching data
After fetching data
Data fetched successfully
```

As you can see, the code continues to execute even before the data is fetched, demonstrating the asynchronous nature of the function.

## Multithreading

JavaScript, being a single-threaded language, does not inherently support multithreading. However, with the introduction of technologies like Web Workers, it is possible to achieve multithreading-like functionality in JavaScript.

**Web Workers** allow you to run JavaScript code in a separate background thread, parallel to the main thread. This enables the execution of heavy computations or time-consuming tasks without blocking the main thread and impacting the user experience.

Here's an example of using a Web Worker to perform a time-consuming calculation:

```javascript
// Create a new web worker
const worker = new Worker("worker.js");

// Listen for messages from the worker
worker.onmessage = function (event) {
  console.log("Result:", event.data);
};

// Send a message to the worker
worker.postMessage(10);

console.log("Calculating...");

// worker.js
onmessage = function (event) {
  const number = event.data;
  const result = performCalculation(number);
  postMessage(result);
};

function performCalculation(number) {
  // Time-consuming calculation
  let result = 0;
  for (let i = 0; i < number; i++) {
    result += i;
  }
  return result;
}
```

In this example, the main thread creates a Web Worker (`worker.js`) and communicates with it using messages. The Web Worker receives a number, performs a time-consuming calculation, and sends the result back to the main thread.

Using Web Workers allows JavaScript to offload heavy computations to a separate thread, improving performance and responsiveness.

## Conclusion

JavaScript's asynchronous functions and the concept of multithreading with Web Workers provide powerful tools for managing time-consuming operations and achieving concurrency. By leveraging these features, you can enhance the performance and responsiveness of your JavaScript applications.