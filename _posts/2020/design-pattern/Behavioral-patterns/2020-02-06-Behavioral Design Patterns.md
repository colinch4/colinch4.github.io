---
layout: post
title: "[Design Pattern] Behavioral Design Patterns"
description: "Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects."
date: 2020-02-06 14:00
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://algamza.github.io/2020-02-06/Design-Patterns) 

# Behavioral Design Patterns

Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects.

[![Chain of Responsibility](https://refactoring.guru/images/patterns/cards/chain-of-responsibility-mini.png)Chain of Responsibility](https://algamza.github.io/2020-02-06/Chain-of-Responsibility-Design-Pattern)

Lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

[![Command](https://refactoring.guru/images/patterns/cards/command-mini.png)Command](https://algamza.github.io/2020-02-06/Command-Design-Pattern)

Turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request's execution, and support undoable operations.

[![Iterator](https://refactoring.guru/images/patterns/cards/iterator-mini.png)Iterator](https://algamza.github.io/2020-02-06/Iterator-Design-Pattern)

Lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

[![Mediator](https://refactoring.guru/images/patterns/cards/mediator-mini.png)Mediator](https://algamza.github.io/2020-02-06/Mediator-Design-Pattern)

Lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.

[![Memento](https://refactoring.guru/images/patterns/cards/memento-mini.png)Memento](https://algamza.github.io/2020-02-06/Memento-Design-Pattern)

Lets you save and restore the previous state of an object without revealing the details of its implementation.

[![Observer](https://refactoring.guru/images/patterns/cards/observer-mini.png)Observer](https://algamza.github.io/2020-02-06/Observer-Design-Pattern)

Lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.

[![State](https://refactoring.guru/images/patterns/cards/state-mini.png)State](https://algamza.github.io/2020-02-06/State-Design-Pattern)

Lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

[![Strategy](https://refactoring.guru/images/patterns/cards/strategy-mini.png)Strategy](https://algamza.github.io/2020-02-06/Stategy-Design-Pattern)

Lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

[![Template Method](https://refactoring.guru/images/patterns/cards/template-method-mini.png)Template Method](https://algamza.github.io/2020-02-06/Template-Method-Design-Pattern)

Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

[![Visitor](https://refactoring.guru/images/patterns/cards/visitor-mini.png)Visitor](https://algamza.github.io/2020-02-06/Visitor-Design-Pattern)

Lets you separate algorithms from the objects on which they operate.