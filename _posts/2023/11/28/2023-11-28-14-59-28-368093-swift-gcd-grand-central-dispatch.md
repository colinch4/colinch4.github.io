---
layout: post
title: "[swift] Swift GCD (Grand Central Dispatch)"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

Grand Central Dispatch (GCD) is a powerful concurrency framework in Swift that allows you to perform multiple tasks concurrently. It helps you manage the execution of tasks in your application, making it more efficient and responsive.

## Table of Contents
- [Dispatch Queues](#dispatch-queues)
- [Concurrent and Serial Queues](#concurrent-and-serial-queues)
- [Dispatching Tasks](#dispatching-tasks)
- [Dispatch Groups](#dispatch-groups)
- [Dispatch Semaphores](#dispatch-semaphores)
- [Conclusion](#conclusion)

## Dispatch Queues

Dispatch queues are the fundamental building blocks of GCD. They define the execution context for tasks. There are two types of dispatch queues: 

- **Main Queue**: It runs tasks on the main thread of the application. This queue is responsible for updating the user interface and should be used for all UI-related tasks.
- **Global Queues**: These are concurrent queues that are provided by the system. They allow tasks to be executed in the background. There are four different priority levels: high, default, low, and background.

## Concurrent and Serial Queues

Dispatch queues can be either concurrent or serial. 

- **Concurrent Queues**: These queues can execute multiple tasks simultaneously. Tasks are executed in the order they are added to the queue.
- **Serial Queues**: These queues execute tasks one at a time in the order they are added to the queue.

## Dispatching Tasks

Dispatching tasks to queues is done using the `dispatch` method. There are several methods available depending on the type of task and queue you are using. 

Here's an example of dispatching an asynchronous task to a global queue:

```swift
DispatchQueue.global().async {
    // Perform asynchronous task here
}
```

You can also dispatch a task synchronously, which means the current thread will wait until the task is completed:

```swift
DispatchQueue.main.sync {
    // Perform synchronous task here
}
```

## Dispatch Groups

Dispatch groups allow you to group multiple tasks and get notified when they are completed. You can use them to synchronize the execution of tasks that depend on each other.

Here's an example of how to use dispatch groups:

```swift
let group = DispatchGroup()

group.enter()
DispatchQueue.global().async {
    // Perform task 1
    group.leave()
}

group.enter()
DispatchQueue.global().async {
    // Perform task 2
    group.leave()
}

group.notify(queue: .main) {
    // Called when all tasks are completed
    print("All tasks completed")
}
```

## Dispatch Semaphores

Dispatch semaphores are synchronization primitives that allow you to control access to a resource. With semaphores, you can limit the number of concurrent tasks or wait for a task to be completed before proceeding.

Here's an example of how to use dispatch semaphores:

```swift
let semaphore = DispatchSemaphore(value: 0)

DispatchQueue.global().async {
    // Perform asynchronous task here
    
    semaphore.signal() // Signal that task is completed
}

semaphore.wait() // Wait for task to be completed
```

## Conclusion

Grand Central Dispatch is an essential framework in Swift for managing concurrency and improving the performance of your applications. It provides a simple and efficient way to handle tasks asynchronously, group tasks, and control access to shared resources. Understanding how to use GCD effectively can greatly enhance the responsiveness and efficiency of your code.