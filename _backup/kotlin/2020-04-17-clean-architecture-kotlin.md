---
layout: post
title: "Kotlin Clean Architecture"
date: 2020-04-17 09:49
category: kotlin
author: kskim2
tags: [kotlin]
description: "A strong base architecture is extremely important for an app to scale and meet the expectation of the user base. I got a task of replacement of API with new updated and optimized API structure. For integrating this kind of change made me kind of rewrite the whole app."
summary: 
---


![](https://miro.medium.com/max/772/0*sfCDEb571WD-7EfP.jpg)

A strong base architecture is extremely important for an app to scale and meet the expectation of the user base. I got a task of replacement of API with new updated and optimized API structure. For integrating this kind of change made me kind of rewrite the whole app.

Why? Because the code was  **deeply coupled**  with response data models. At this time, I didn’t want to make the same mistakes over and over again. For resolving this problem, Clean architecture came to the rescue. It is a bit pain in the starting but might be the best option for a large app with many features and  **SOLID**  approach. Let’s just try by questioning every aspect of architecture and break down into simpler bits.

[](https://github.com/rakshit444/news-sample-app)

## news-sample-app

### Contribute to news-sample-app development by creating an account on GitHub.

#### github.com

This architecture was proposed in 2012 by Robert C. Martin(Uncle Bob) in  [clean code blog](http://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).

## **Why the cleaner approach?**

1.  Separation of code in different layers with  **assigned responsibilities**  making it easier for further modification.
2.  High level of  **abstraction**
3.  **Loose coupling**  between the code
4.  **Testing**  of code is painless

> “Clean code always looks like it was written by someone who cares.”
> 
> — Michael Feathers

## **What are the Layers?**

![](https://miro.medium.com/max/56/1*a5UQUjgYu5SZAbmkNELI_A.png?q=20)

![](https://miro.medium.com/max/476/1*a5UQUjgYu5SZAbmkNELI_A.png)

Dependency Flow

**Domain layer:**  Would execute business logic which is independent of any layer and is just a pure kotlin package with no android specific dependency.

**Data layer:**  Would dispense the required data for the application to the domain layer by implementing interface exposed by the domain

**Presentation layer:** Would include both domain and data layer and is android specific which executes the UI logic.

## **What is Domain Layer?**

This will be the most generic layer of the three. It will connect the presentation layer with the data layer. This is the layer where app-related business logic will be executed.

![](https://miro.medium.com/max/60/1*m06XFPa5OTvOF6zGPC7Q0w.png?q=20)

![](https://miro.medium.com/max/568/1*m06XFPa5OTvOF6zGPC7Q0w.png)

The domain layer structure of the application

## **UseCases**

Use cases are the application logic executor. As the name depicts each functionality can have its separate use case. With more granularity of the use case creation, it can be reused more often.

Sample UseCase

This use case returns Flowable which can be modified according to the required observer. There are two parameters to it. One of them is  _transformers_  or  [ObservableTransformer](http://reactivex.io/RxJava/javadoc/io/reactivex/ObservableTransformer.html)  which control what thread to execute the logic and the other parameter  _repository_, is the interface for the data layer. If any data has to be passed to the data layer then HashMap can be used.

## Repositories

It specifies the functionalities required by the use cases which is implemented by the data layer.

## What is Data Layer?

This layer is responsible for providing the data required by the application. Data layer should be designed such data it can be re-used by any application without modification in their presentation logic.

![](https://miro.medium.com/max/60/1*KbdhwDpsxspHEz7QInpbhA.png?q=20)

![](https://miro.medium.com/max/398/1*KbdhwDpsxspHEz7QInpbhA.png)

The data layer structure of the application

**API** provides remote networking implementation. Any networking library can be integrated into this like retrofit, volley etc. Similarly,  **DB** provides local database implementation.

In Repository, we have an implementation of the local, remote or any kind of data provider and above class NewsRepositoryImpl.kt implements the interface exposed by the domain layer. It acts as a single point of access to the data layer.

**What is the presentation layer?**

The presentation layer provides the UI implementation of the application. It is the dumb layer which only performs instruction with no logic in it. This layer internally implements architecture like MVC, MVP, MVVM, MVI etc. This is the layer where everything connects.

![](https://miro.medium.com/max/60/1*4UH3LeLcGg8tjp1BmPm1jw.png?q=20)

![](https://miro.medium.com/max/514/1*4UH3LeLcGg8tjp1BmPm1jw.png)

The presentation layer structure of the application

**DI** folder provides the injection all the dependencies at the start of an app like network related, View Models, Use Cases etc. DI in android can be implemented with dagger, kodein, koin or by just using the service locator pattern. It just depends upon the application like for complex app di can be pretty helpful. I chose koin just because it was much easy to understand and implement than dagger.

**Why using ViewModels?**

As per the android documentation  [ViewModel](https://developer.android.com/topic/libraries/architecture/viewmodel):

> _Store and manage UI-related data in a lifecycle conscious way. It allows data to survive configuration changes such as screen rotations._

So, ViewModel retains the data on configuration change. In MVP, Presenter was bind to the view with the interface which makes it difficult to test but in ViewModel, there is no interface because of the architectural aware components.

Base View Model is using  [CompositeDisposable](http://reactivex.io/RxJava/javadoc/io/reactivex/disposables/CompositeDisposable.html)  for adding all the observables and removing all them on @OnCleared of the lifecycle.

A data wrapper class is used onto the LiveData as a helper class so that view gets to know about the status of the request i.e if it has been started, successful or any concerned state about the data.

**How all the layers are connected?**

Each layer has its own  _entities_  which are specific to that package. Mapper is used for conversion of one layer entities to another. We are having different entities for each layer so that the layer becomes purely independent and only the required data gets passed to the subsequent layer.

## Application Flow

![](https://miro.medium.com/max/54/1*a-AUcEVdyRJhIepo9JyJBw.png?q=20)

![](https://miro.medium.com/max/1258/1*a-AUcEVdyRJhIepo9JyJBw.png)

----------

This would be the end of the post, Let me know if I missed anything. Let me conclude by:

> _Base architecture defines the solidarity of the app and yes, It depends upon the app for the appropriate architecture BUT why not just pick the most apt architecture_ ahead of time _which could be scalable, robust, testable so that you don’t have to take pain in future_

Thanks for reading :)