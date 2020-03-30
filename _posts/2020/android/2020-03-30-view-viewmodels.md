---
layout: post
title: "ViewModels and LiveData: Patterns + AntiPatterns"
date: 2020-03-30 10:10
category: 
author: kskim2
tags: [architecture, mvvm]
summary: 
description: "Ideally, ViewModels shouldn’t know anything about Android. This improves testability, leak safety and modularity. A general rule of thumb is to make sure there are no android.* imports in your ViewModels (with exceptions like android.arch.*). The same applies to presenters."
comments: true
share: true
---


# Views and ViewModels

## Distributing responsibilities

![](https://miro.medium.com/max/60/1*I9WPcnpGNuI4CjxxrkP0-g.png?q=20)

![](https://miro.medium.com/max/803/1*I9WPcnpGNuI4CjxxrkP0-g.png)

_Typical interaction of entities in an app built with Architecture Components_

Ideally, ViewModels shouldn’t know anything about Android. This improves testability, leak safety and modularity. A general rule of thumb is to make sure there are no  `android.*`  imports in your ViewModels (with exceptions like `android.arch.*`). The same applies to presenters.

> ❌  Don’t let ViewModels (and Presenters) know about Android framework classes

Conditional statements, loops and general decisions should be done in ViewModels or other layers of an app, not in the Activities or Fragments. The View is usually not unit tested (unless you use  [Robolectric](http://robolectric.org/)) so the fewer lines of code the better. Views should only know how to display data and send user events to the ViewModel (or Presenter). This is called the  [_Passive_  _View_](https://martinfowler.com/eaaDev/PassiveScreen.html)  pattern.

> ✅ Keep the logic in Activities and Fragments to a minimum

## View references in ViewModels

[ViewModels](https://developer.android.com/topic/libraries/architecture/viewmodel.html)  have different scopes than activities or fragments. While a ViewModel is alive and running, an activity can be in any of its  [lifecycle states](https://developer.android.com/guide/components/activities/activity-lifecycle.html). Activities and fragments can be destroyed and created again while the ViewModel is unaware.

![](https://miro.medium.com/max/60/1*86RjXnTJucJMkW4Xi4kUlA.png?q=20)

![](https://miro.medium.com/max/1280/1*86RjXnTJucJMkW4Xi4kUlA.png)

ViewModels persist configuration changes

Passing a reference of the View (activity or fragment) to the ViewModel is a  **serious risk**. Let’s assume the ViewModel requests data from the network and the data comes back some time later. At that moment, the View reference might be destroyed or might be an old activity that is no longer visible, generating a memory leak and, possibly, a crash.

> ❌ Avoid references to Views in ViewModels.

The recommended way to communicate between ViewModels and Views is the observer pattern, using LiveData or observables from other libraries.

## Observer Pattern

![](https://miro.medium.com/max/60/1*hjvCDY_2W4PpK7HQoHsS2Q.png?q=20)

![](https://miro.medium.com/max/412/1*hjvCDY_2W4PpK7HQoHsS2Q.png)

A very convenient way to design the presentation layer in Android is to have the View (activity or fragment) observe (_subscribe to changes in_) the ViewModel. Since the ViewModel doesn’t know about Android, it doesn’t know how Android likes to kill Views frequently. This has some advantages:

1.  ViewModels are persisted over configuration changes, so there’s no need to re-query an external source for data (such as a database or the network) when a rotation happens.
2.  When long-running operations finish, the observables in the ViewModel are updated. It doesn’t matter if the data is being observed or not. No null pointer exceptions happen when trying to update the nonexistent View.
3.  ViewModels don’t reference views so there’s less risk of memory leaks.

Typical subscription from an activity or fragment.

> ✅ Instead of pushing data to the UI, let the UI observe changes to it.

# Fat ViewModels

Whatever lets you separate concerns is a good idea. If your ViewModel is holding too much code or has too many responsibilities consider:

-   Moving some logic out to a presenter, with the same scope as the ViewModel. It will communicate with other parts of your app and update the LiveData holders in the ViewModel.
-   Adding a Domain layer and adopting  [Clean Architecture](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html). This leads to a very testable and maintainable architecture. It also facilitates getting off the main thread quickly. There’s a Clean Architecture sample in  [Architecture Blueprints](https://github.com/googlesamples/android-architecture).

> ✅ Distribute responsibilities, add a domain layer if needed.

# Using a data repository

As seen in the  [Guide to App Architecture](https://developer.android.com/topic/libraries/architecture/guide.html)  most apps have multiple data sources, such as:

1.  Remote: network or the Cloud
2.  Local: database or file
3.  In-memory cache

It’s a good idea to have a data layer in your app, completely unaware of your presentation layer. Algorithms to keep cache and database in sync with the network are not trivial. Having a separate repository class as a single point of entry that deals with this complexity is recommended.

If you have multiple and very different data models, consider adding multiple repositories.

> ✅ Add a data repository as the single-point entry to your data

# Dealing with data state

Consider this scenario: you’re observing a LiveData exposed by a ViewModel that contains a list of items to display. How can the View diferentiate between data being loaded, a network error and an empty list?

-   You could expose a  `LiveData<MyDataState>`  from the ViewModel. For example,  `MyDataState`  could contain information about whether the data is currently loading, has loaded successfully or failed.

![](https://miro.medium.com/max/60/1*Hj8ChdU7pakjcM3kxj_Fzg.png?q=20)

![](https://miro.medium.com/max/506/1*Hj8ChdU7pakjcM3kxj_Fzg.png)

You can wrap the data in a class that has a state and other metadata like an error message. See the  [Resource](https://developer.android.com/topic/libraries/architecture/guide.html#addendum)  class in our samples.

> ✅ Expose information about the state of your data using a wrapper or another LiveData.

# Saving activity state

Activity state is the information you need to recreate a screen if an activity is gone, meaning the activity was destroyed or the process was killed. Rotation is the most obvious case and we’ve got that covered with ViewModels. State is safe if it’s kept in the ViewModel.

However, you might need to restore state in other scenarios where the ViewModels are also gone: when the OS is low on resources and kills your process for example.

To efficiently save and restore UI state, use a combination of persistence,  `onSaveInstanceState()`and ViewModels.

For an example, see:  [ViewModels: Persistence, onSaveInstanceState(), Restoring UI State and Loaders](https://medium.com/google-developers/viewmodels-persistence-onsaveinstancestate-restoring-ui-state-and-loaders-fc7cc4a6c090)

# Events

An event is something that happens once. ViewModels expose data, but what about events? For example, navigation events or showing Snackbar messages are actions that should only be executed once.

The concept of an Event doesn’t fit perfectly with how LiveData stores and restore data. Consider a ViewModel with the following field:

LiveData<String> snackbarMessage = new MutableLiveData<>();

An activity starts observing this and the ViewModel finishes an operation so it needs to update the message:

snackbarMessage.setValue("Item saved!");

The activity receives the value and shows the Snackbar. It works, apparently.

However, if the user rotates the phone, the new activity is created and starts observing. When LiveData observation starts, the activity immediately receives the old value, which causes the message to show again!

Instead of trying to solve this with libraries or extensions to the Architecture Components, it should be faced as a design problem. **We recommend you treat your events as part of your state**.

> ✅ Design events as part of your state. For more details read  [LiveData with SnackBar, Navigation and other events (the SingleLiveEvent case)](https://medium.com/google-developers/livedata-with-snackbar-navigation-and-other-events-the-singleliveevent-case-ac2622673150).

# Leaking ViewModels

The reactive paradigm works well in Android because it allows for a convenient connection between UI and the rest of the layers of your app. LiveData is the key component of this structure so normally your activities and fragments will observe LiveData instances.

How ViewModels communicate with other components is up to you, but watch out for leaks and edge cases. Consider this diagram where the Presentation layer is using the observer pattern and the Data Layer is using callbacks:

![](https://miro.medium.com/max/60/1*0BaDp6eyWAEkUwmprKC9Rg.png?q=20)

![](https://miro.medium.com/max/796/1*0BaDp6eyWAEkUwmprKC9Rg.png)

Observer pattern in the UI and callbacks in the data layer

If the user exits the app, the View will be gone so the ViewModel is not observed anymore. If the repository is a singleton or otherwise scoped to the application, **the repository will not be destroyed until the process is killed**. This will only happen when the system needs resources or the user manually kills the app. If the repository is holding a reference to a callback in the ViewModel, the ViewModel will be temporarily leaked

![](https://miro.medium.com/max/60/1*OYyXV-qPtgmAlbDjI640KA.png?q=20)

![](https://miro.medium.com/max/809/1*OYyXV-qPtgmAlbDjI640KA.png)

The activity is finished but the ViewModel is still around

This leak is not a big deal if the ViewModel is light or the operation is guaranteed to finish quickly. However, this is not always the case. Ideally, ViewModels should be free to go whenever they don’t have any Views observing them:

![](https://miro.medium.com/max/60/1*y1Zimc4SFMentSLsk6VCcQ.png?q=20)

![](https://miro.medium.com/max/798/1*y1Zimc4SFMentSLsk6VCcQ.png)

You have many options to achieve this:

-   **With ViewModel.onCleared()**  you can tell the repository to drop the callback to the ViewModel.
-   In the repository you can use a  **WeakReference**  or you can use an  **Event Bus**  (both easy to misuse and even considered harmful).
-   Use the LiveData to communicate between the Repository and ViewModel in a similar way to using LiveData between the View and the ViewModel.

> ✅ Consider edge cases, leaks and how long-running operations can affect the instances in your architecture.
> 
> ❌ Don’t put logic in the ViewModel that is critical to saving clean state or related to data. Any call you make from a ViewModel can be the last one.

# LiveData in repositories

To avoid leaking ViewModels and  _callback hell_, repositories can be observed like this:

![](https://miro.medium.com/max/60/1*Ptw2Z3PyvOKCamvRHQsyCQ.png?q=20)

![](https://miro.medium.com/max/890/1*Ptw2Z3PyvOKCamvRHQsyCQ.png)

When the ViewModel is cleared or when the lifecycle of the view is finished, the subscription is cleared:

![](https://miro.medium.com/max/60/1*y1Zimc4SFMentSLsk6VCcQ.png?q=20)

![](https://miro.medium.com/max/798/1*y1Zimc4SFMentSLsk6VCcQ.png)

There’s a catch if you try this approach: how do you subscribe to the Repository from the ViewModel if you don’t have access to the LifecycleOwner? Using  [Transformations](https://developer.android.com/topic/libraries/architecture/livedata#transform_livedata)  is a very convenient way to solve this.  `Transformations.switchMap`  lets you create a new LiveData that reacts to changes of other LiveData instances. It also allows carrying over the observer Lifecycle information across the chain:

Transformations example [[_source_](https://github.com/googlesamples/android-architecture-components/blob/master/GithubBrowserSample/app/src/main/java/com/android/example/github/ui/repo/RepoViewModel.java)]

In this example, when the trigger gets an update, the function is applied and the result is dispatched downstream. An activity would observe  `repo`  and the same LifecycleOwner would be used for the  `repository.loadRepo(id)`  call.

> ✅ Whenever you think you need a  [Lifecycle](https://developer.android.com/reference/android/arch/lifecycle/Lifecycle.html)  object inside a  [ViewModel](https://developer.android.com/reference/android/arch/lifecycle/ViewModel.html), a  [Transformation](https://developer.android.com/topic/libraries/architecture/livedata#transform_livedata)  is probably the solution.

# Extending LiveData

The most common use case for LiveData is using  `MutableLiveData`  in ViewModels and exposing them as  `LiveData`  to make them immutable from the observers.

If you need more functionality, extending LiveData will let you know when there are active observers. This is useful when you want to start listening to a location or sensor service, for example.

## When not to extend LiveData

You could also use  `onActive()`  to start some service that loads data, but unless you have a good reason for it, you don’t need to wait for the LiveData to be observed. Some common patterns:

-   Add a  `start()`  method to the ViewModel and call it as soon as possible [See  [Blueprints example](https://github.com/googlesamples/android-architecture/blob/dev-todo-mvvm-live/todoapp/app/src/main/java/com/example/android/architecture/blueprints/todoapp/addedittask/AddEditTaskFragment.java#L64)]
-   Set a property that kicks off the load [See  [GithubBrowserExample](https://github.com/googlesamples/android-architecture-components/blob/master/GithubBrowserSample/app/src/main/java/com/android/example/github/ui/repo/RepoFragment.kt)].

> ❌ You don’t usually extend LiveData. Let your activity or fragment tell the ViewModel when it’s time to start loading data.

----------

Do you need guidance (or opinions) on any other topic related to the Architecture Components? Let us know in the comments.