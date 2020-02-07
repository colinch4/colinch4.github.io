---
layout: post
title: "[Design Pattern] Behavioral Design Patterns"
description: "Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects."
date: 2020-02-06 14:00
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://refactoring.guru/design-patterns)  /  [Catalog](https://refactoring.guru/design-patterns/catalog)

# Behavioral Design Patterns

Behavioral design patterns are concerned with algorithms and the assignment of responsibilities between objects.

[![Chain of Responsibility](https://refactoring.guru/images/patterns/cards/chain-of-responsibility-mini.png)Chain of Responsibility](https://refactoring.guru/design-patterns/chain-of-responsibility)

Lets you pass requests along a chain of handlers. Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

[![Command](https://refactoring.guru/images/patterns/cards/command-mini.png)Command](https://refactoring.guru/design-patterns/command)

Turns a request into a stand-alone object that contains all information about the request. This transformation lets you parameterize methods with different requests, delay or queue a request's execution, and support undoable operations.

[![Iterator](https://refactoring.guru/images/patterns/cards/iterator-mini.png)Iterator](https://refactoring.guru/design-patterns/iterator)

Lets you traverse elements of a collection without exposing its underlying representation (list, stack, tree, etc.).

[![Mediator](https://refactoring.guru/images/patterns/cards/mediator-mini.png)Mediator](https://refactoring.guru/design-patterns/mediator)

Lets you reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object.

[![Memento](https://refactoring.guru/images/patterns/cards/memento-mini.png)Memento](https://refactoring.guru/design-patterns/memento)

Lets you save and restore the previous state of an object without revealing the details of its implementation.

[![Observer](https://refactoring.guru/images/patterns/cards/observer-mini.png)Observer](https://refactoring.guru/design-patterns/observer)

Lets you define a subscription mechanism to notify multiple objects about any events that happen to the object they're observing.

[![State](https://refactoring.guru/images/patterns/cards/state-mini.png)State](https://refactoring.guru/design-patterns/state)

Lets an object alter its behavior when its internal state changes. It appears as if the object changed its class.

[![Strategy](https://refactoring.guru/images/patterns/cards/strategy-mini.png)Strategy](https://refactoring.guru/design-patterns/strategy)

Lets you define a family of algorithms, put each of them into a separate class, and make their objects interchangeable.

[![Template Method](https://refactoring.guru/images/patterns/cards/template-method-mini.png)Template Method](https://refactoring.guru/design-patterns/template-method)

Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

[![Visitor](https://refactoring.guru/images/patterns/cards/visitor-mini.png)Visitor](https://refactoring.guru/design-patterns/visitor)

Lets you separate algorithms from the objects on which they operate.