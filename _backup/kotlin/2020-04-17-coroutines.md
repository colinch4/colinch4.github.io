---
layout: post
title: "[Kotlin] Experimenting with Coroutines"
date: 2020-04-17 09:46
category: kotlin
author: kskim2
tags: [kotlin]
description: "Coroutines are getting quite popular and I’ve been reading quite a lot of articles lately of opting Coroutine instead of RxJava. First of all, let me be clear, RxJava is a humongous library with a rich set of operators and Coroutines is a kotlin language feature. It all depends upon what is the end goal, If it’s complex manipulation of data or use of streams, RxJava would be preferred any time else for achieving asynchronous nature then coroutine would be great!."
summary: 
---


Coroutines are getting quite popular and I’ve been reading quite a lot of articles lately of opting Coroutine instead of RxJava. First of all, let me be clear, RxJava is a humongous library with a rich set of operators and Coroutines is a kotlin language feature. It all depends upon what is the end goal, If it’s complex manipulation of data or use of streams, RxJava would be preferred any time else for achieving asynchronous nature then coroutine would be great!.

I’ll be replacing RxJava implemented in Clean Architecture with coroutines. If you haven't gone through Clean Architecture then please refer:

[](https://medium.com/@rjain.jain444/kotlin-clean-architecture-1ad42fcd97fa)

## Kotlin Clean Architecture

### A strong base architecture is extremely important for an app to scale and meet the expectation of the user base. I got…

#### medium.com

Implementation of coroutine with clean architecture can be found at:

[](https://github.com/rakshit444/news-sample-app/tree/wip/coroutines)

## rakshit444/news-sample-app

### A sample news app which demonstrates clean architecture and best practices for developing android app …

#### github.com

Let’s go through some of the basics of coroutines :

## What are Coroutines?

Coroutines help’s you in achieving  **asynchronous implementation**  which is  _Elegant_,  _Easy_  and empowers app with  _rich performance._

> Coroutines provide a way to avoid blocking a thread and replace it with a cheaper and more controllable operation: suspension of a coroutine

It is a simple way of handling thread management by reducing callback hell/Channing. Yes, It converts asynchronous coding in a  _synchronous_  or  _sequential manner_  but it really depends upon your end goal. Let’s get deep dive into it and understand what it really meant.

**How to start?**

A bridge has to be created between the regular code which on the current/parent thread to the  **coroutine world**  for which suspending functions are introduced. Suspend functions are at the core for the implementation of the coroutine.

For running a coroutine, First of all,  _the code is suspended from the main thread and the rest of the code will get executed at some later point on the parent context_. You can think it like having callbacks where we get the desired result but in a coroutine, this work is done by the compiler and we just have to write one line. For the execution of suspending function, it has to be called from a coroutine which is created with  **coroutine builders**

## Coroutine builders

They are used to create a coroutine. A coroutine can be created simply by:

Let's break it down the above coroutine creation:

i) GlobalScope specifies the application scope on which coroutine is created. It should be  **avoided**  otherwise you have to track for its lifetime and take extra overhead. It should be replaced by implementing  [Coroutine scope](https://kotlin.github.io/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/-coroutine-scope/index.html)  . We will be talking about it afterward.

ii) launch is the coroutine builder used to create a new coroutine

iii) Dispatchers define the thread on which task will be performed. If you don’t specify anything then  [default dispatcher](https://kotlinlang.org/docs/reference/coroutines/coroutine-context-and-dispatchers.html)  is used which internally creates a thread pool.

iv) withContext is a scoping function which provides a job instance and inner block gets suspended and run on the defined dispatcher. In this case, it is used to switch to the main thread.

Coroutine builder launches on a coroutine scope. There are many types of builders but let’s discuss most commonly used:

> **_launch:_** It returns a  _job_  and does not return any resulting value. It is like a thread.
> 
> **_async:_** It returns  _Deferred_  which is just like Future in java or Promise in javascript
> 
> **_runBlocking:_**  It can be used when you just want to run suspending function in synchronous way with the parent thread.(Not recommeded at all)

That’s easy to work asynchronously :)

## **Coroutine scope**

It should be very rare that you create a coroutine globally. It should be linked with the local context be it activity, view model or a custom widget. This can be done by implementing CoroutineScope.

In the get value of coroutineContext, you can specify the custom scope for your coroutine builders and all the coroutine builder can be accessed by the extension function and does not require coroutineScope to be mentioned before.

As you can look just by writing launch it uses coroutine scope defined in the interface. This helps in cancellation of all coroutines for preventing leak when the local context is cleared and not needed just like we the usage of disposables in rx.

## Channel

A channel is created to pass information between sender and receiver

For clean architecture, a channel is to be created between each layer for the transferring stream of data. For achieving the functionality of Flowable in coroutines we have Channels. A channel implements two interfaces sendChannel and receiveChannel

A channel can be created using the factory function defined. It represents a hot stream of data emission. Once the data is consumed by the receiver it cannot be re-consumed. For further deep dive into channels, you can go through  [this](https://proandroiddev.com/part-3-transmitting-streams-of-value-with-channels-70cf8dccf2b)  article

We are mostly using Receive Channel which is created by  **produce**  coroutine builder. With produce, data items can only be sent from a single point. After creating a receive channel, consumeEach can be used for consuming every data items emitted in the channel

A basic overview of how channels have been used between the layer.

![](https://miro.medium.com/max/60/1*qGEGieL2haal1QmO5NOs2g.png?q=20)

![](https://miro.medium.com/max/841/1*qGEGieL2haal1QmO5NOs2g.png)

Replacing channels with Flowable in architecture

## Data Layer

For achieving the single truth principle flowable from the database is passed to the domain layer. In Rx, Flowable was used and mergeWith operator for combining the resulting from the remote as well.

The same implementation with coroutine will be implemented by launching two coroutines one for database and other for the remote. In return receive channel is sent and only changes from the database are sent on the channel. Let’ s break the two coroutines functionality:

i) The first coroutine is used for creating a subscription with the local database consumes every change in the database and further pushes it onto the channel subscribed by the use case.

ii) The second one is used to get the response for the remote and getNews function uses async await due to which receive will always get the result. After that, it is saved to the database.

Lets. look at the implementation for getting data from the local datastore

NewsCacheImpl using Rx

A flowable was returned from the room database which emitters data every time when it changes

NewsCacheImpl using Coroutine

As of now, channels are not supported with the room but rxjava extensions are provided by the coroutines which help in rx operators transforming to coroutines. So, mapped value is a flowable type and openSubcription() on flowable is used for returning ReceiveChannel.

## Domain Layer

For the domain layer, a major change had to be done in the base use case.

In Rx, Flowable was getting returned from the data layer and scheduling on observable was done using transformers.

When using coroutines we are getting a channel from the data layer and a new channel is being created between the domain layer and the presentation layer. sendToPresentation() is getting implemented in every use case which is used for performing any manipulation on data before sending it to the presentation layer.

## **Presentation Layer**

In Rx, use case was returning flowable and with the flat map, it is converted to the data model required for the presentation layer. Further subscription is done with the Observer.

Here the use case is returning channel and we are consuming every data emitted on the channel. Then the data is mapped to the presentation layer which is then posted with the live data on the main thread by switching the thread. Scheduling is a bit easy in coroutines with the ease in switching between thread context.

## Summary

Coroutines are easy to use but just do not just think about replacing rxjava with coroutines. Review your code, find out the places where coroutines will be helpful and not a pain point just for sake of replacing. Coroutines are still maturing and integrating it with the large app can be done with its limited use. I would suggest use coroutines for performing asynchronous operations and for manipulation on streams of data rxjava would still be the best options with its rich set of operators. It will be great if you could share your own experience with the coroutines.

Thanks for reading!!