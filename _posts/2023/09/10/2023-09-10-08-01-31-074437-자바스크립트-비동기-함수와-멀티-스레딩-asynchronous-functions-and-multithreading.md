---
layout: post
title: "자바스크립트 비동기 함수와 멀티 스레딩 (Asynchronous Functions and Multithreading)"
description: " "
date: 2023-09-10
tags: [javascript]
comments: true
share: true
---

JavaScript is a single-threaded language, meaning it can only execute one task at a time. However, with the introduction of asynchronous functions and the concept of multithreading, JavaScript developers are now able to handle multiple tasks simultaneously, improving performance and responsiveness.

## 비동기 함수 (Asynchronous Functions)

In traditional programming, functions execute synchronously, which means that each line of code is executed one after the other, sequentially. This can cause performance issues when dealing with time-consuming tasks, such as making network requests or loading large amounts of data.

To overcome this limitation, JavaScript introduced asynchronous functions. With asynchronous functions, instead of waiting for a task to complete before moving to the next line, the function can continue executing while the task runs in the background. This allows the program to remain responsive and perform other tasks while waiting for the asynchronous task to complete.

### 콜백 함수 (Callback Functions)

The most common way to work with asynchronous functions in JavaScript is through the use of callback functions. A callback function is a function passed as an argument to another function, which will be executed once the asynchronous task is complete.

```javascript
function doSomethingAsync(callback) {
  // Simulating an asynchronous task
  setTimeout(function() {
    console.log("Async task complete");
    callback();
  }, 1000);
}

console.log("Start");
doSomethingAsync(function() {
  console.log("Callback executed");
});
console.log("End");
```

In the example above, `doSomethingAsync` is an asynchronous function that simulates a time delay with the `setTimeout` function. The callback function is passed as an argument and will be executed after 1 second. The output would be:

```
Start
End
Async task complete
Callback executed
```

Notice that the program doesn't wait for the asynchronous task to complete before continuing with the next line of code. This is what allows JavaScript to handle multiple tasks simultaneously.

### 프로미스 (Promises)

While callback functions are widely used, they can lead to callback hell and make the code difficult to read and maintain, especially when chaining multiple asynchronous tasks. To address this issue, JavaScript introduced promises.

A promise is an object representing the eventual completion or failure of an asynchronous operation. Instead of passing a callback function directly, asynchronous functions return a promise object that can be chained with `.then()` to handle successful completion or `.catch()` to handle errors.

```javascript
function doSomethingAsync() {
  return new Promise(function(resolve, reject) {
    setTimeout(function() {
      console.log("Async task complete");
      resolve();
    }, 1000);
  });
}

console.log("Start");
doSomethingAsync()
  .then(function() {
    console.log("Promise resolved");
  })
  .catch(function(error) {
    console.error("Promise rejected:", error);
  });
console.log("End");
```

In this example, the asynchronous function `doSomethingAsync` returns a promise object that resolves after 1 second. The `.then()` and `.catch()` methods are used to handle the successful completion and errors, respectively. The output would be the same as the previous example.

Promises provide a more structured and readable way to handle asynchronous operations, making the code easier to work with.

## 멀티 스레딩 (Multithreading)

Even though JavaScript is single-threaded, there are ways to leverage multiple threads using techniques such as Web Workers. Web Workers allow JavaScript code to be executed in the background, separate from the main thread, enabling true multitasking.

Web Workers are well-suited for computationally expensive or time-consuming tasks that don't require direct interaction with the DOM. Using Web Workers, developers can offload these tasks to separate threads, keeping the main thread responsive and improving overall performance.

Here's an example of using a Web Worker to calculate Fibonacci numbers:

```javascript
// main.js
const worker = new Worker("worker.js");

worker.onmessage = function(event) {
  console.log("Fibonacci result:", event.data);
};

worker.postMessage(40);

// worker.js
function fibonacci(n) {
  if (n <= 1) {
    return n;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}

self.onmessage = function(event) {
  const result = fibonacci(event.data);
  self.postMessage(result);
}
```

In this example, `main.js` creates a new Web Worker from the `worker.js` file and sends a message to it with the number 40. The `worker.js` file calculates the Fibonacci sequence recursively and sends the result back to the main thread using the `postMessage` method. The result is then logged in the console.

Web Workers provide a way to handle computationally intensive tasks without blocking the main thread, leading to a more responsive user interface.

## 결론 (Conclusion)

Asynchronous functions and multithreading techniques greatly enhance the capabilities of JavaScript, allowing developers to build more efficient and responsive applications. By leveraging callbacks, promises, and Web Workers, JavaScript developers can handle time-consuming tasks while keeping the main thread free to handle other operations, resulting in improved performance and user experience.