---
layout: post
title: "Design Patterns"
description: "In software engineering, a design pattern is a general repeatable solution to a commonly occurring problem in software design. A design pattern isn't a finished design that can be transformed directly into code. It is a description or template for how to solve a problem that can be used in many different situations."
date: 2020-02-06 13:00
tags: [디자인패턴]
comments: true
share: true
---

In software engineering, a  **design pattern**  is a general repeatable solution to a commonly occurring problem in software design. A design pattern isn't a finished design that can be transformed directly into code. It is a description or template for how to solve a problem that can be used in many different situations.

### Uses of Design Patterns

Design patterns can speed up the development process by providing tested, proven development paradigms. Effective software design requires considering issues that may not become visible until later in the implementation. Reusing design patterns helps to prevent subtle issues that can cause major problems and improves code readability for coders and architects familiar with the patterns.

Often, people only understand how to apply certain software design techniques to certain problems. These techniques are difficult to apply to a broader range of problems. Design patterns provide general solutions, documented in a format that doesn't require specifics tied to a particular problem.

In addition, patterns allow developers to communicate using well-known, well understood names for software interactions. Common design patterns can be improved over time, making them more robust than ad-hoc designs.

### [Creational design patterns](./creational-patterns/2020-02-06-Creational%20patterns.md)

These design patterns are all about class instantiation. This pattern can be further divided into class-creation patterns and object-creational patterns. While class-creation patterns use inheritance effectively in the instantiation process, object-creation patterns use delegation effectively to get the job done.

[![Example of Abstract Factory](https://sourcemaking.com/files/v2/content/patterns/Abstract_Factory-preview.png)](./creational-patterns/2020-02-06-Abstract%20Factory%20Design%20Pattern.md)

-   [Abstract Factory](./creational-patterns/2020-02-06-Abstract%20Factory%20Design%20Pattern.md "Provides a way to encapsulate a group of individual factories that have a common theme.")  
    Creates an instance of several families of classes
-   [Builder](./creational-patterns/2020-02-06-Builder%20Design%20Pattern.md "Separate the construction of a complex object from its representation so that the same construction process can create different representations.")  
    Separates object construction from its representation
-   [Factory Method](./creational-patterns/2020-02-06-Factory%20Method%20Design%20Pattern.md "Defines a separate method for creating the objects, which subclasses can then override to specify the derived type of product that will be created.")  
    Creates an instance of several derived classes
-   [Object Pool](./creational-patterns/2020-02-06-Object%20Pool%20Design%20Pattern.md "Avoid expensive acquisition and release of resources by recycling objects that are no longer in use")  
    Avoid expensive acquisition and release of resources by recycling objects that are no longer in use
-   [Prototype](./creational-patterns/2020-02-06-Prototype%20Design%20Pattern.md "Being cloned to produce new objects.")  
    A fully initialized instance to be copied or cloned
-   [Singleton](./creational-patterns/2020-02-06-Singleton%20Design%20Pattern.md "Restricts instantiation of a class to one object.")  
    A class of which only a single instance can exist

### [Structural design patterns](https://sourcemaking.com/design_patterns/structural_patterns)

These design patterns are all about Class and Object composition. Structural class-creation patterns use inheritance to compose interfaces. Structural object-patterns define ways to compose objects to obtain new functionality.

[![](https://sourcemaking.com/files/v2/content/patterns/Decorator-preview.png)](https://sourcemaking.com/design_patterns/decorator)

-   [Adapter](https://sourcemaking.com/design_patterns/adapter "Adapts one interface for a class into one that a client expects.")  
    Match interfaces of different classes
-   [Bridge](https://sourcemaking.com/design_patterns/bridge "Decouples an abstraction from its implementation so that the two can vary independently.")  
    Separates an object’s interface from its implementation
-   [Composite](https://sourcemaking.com/design_patterns/composite "Designed as a composition of one-or-more similar objects, all exhibiting similar functionality.")  
    A tree structure of simple and composite objects
-   [Decorator](https://sourcemaking.com/design_patterns/decorator "Allows new/additional behavior to be added to an existing method of an object dynamically.")  
    Add responsibilities to objects dynamically
-   [Facade](https://sourcemaking.com/design_patterns/facade "Provides a simplified interface to a larger body of code.")  
    A single class that represents an entire subsystem
-   [Flyweight](https://sourcemaking.com/design_patterns/flyweight "When many objects must be manipulated and these cannot afford to have extraneous data, flyweight is appropriate.")  
    A fine-grained instance used for efficient sharing
-   [![](https://sourcemaking.com/files/v2/content/patterns/Proxy-preview.png)](https://sourcemaking.com/design_patterns/proxy)
    
    [Private Class Data](https://sourcemaking.com/design_patterns/private_class_data "Restricts accessor/mutator access")  
    Restricts accessor/mutator access
-   [Proxy](https://sourcemaking.com/design_patterns/proxy "Class functioning as an interface to another thing.")  
    An object representing another object

### [Behavioral design patterns](https://sourcemaking.com/design_patterns/behavioral_patterns)

These design patterns are all about Class's objects communication. Behavioral patterns are those patterns that are most specifically concerned with communication between objects.

[![](https://sourcemaking.com/files/v2/content/patterns/Interpreter-preview.png)](https://sourcemaking.com/design_patterns/interpreter)

-   [Chain of responsibility](https://sourcemaking.com/design_patterns/chain_of_responsibility "Source of command objects and a series of processing objects.")  
    A way of passing a request between a chain of objects
-   [Command](https://sourcemaking.com/design_patterns/command "Objects are used to represent actions.")  
    Encapsulate a command request as an object
-   [Interpreter](https://sourcemaking.com/design_patterns/interpreter "The basic idea is to implement a specialized computer language to rapidly solve a defined class of problems.")  
    A way to include language elements in a program
-   [Iterator](https://sourcemaking.com/design_patterns/iterator "Used to access the elements of an aggregate object sequentially without exposing its underlying representation.")  
    Sequentially access the elements of a collection
-   [Mediator](https://sourcemaking.com/design_patterns/mediator "Provides a unified interface to a set of interfaces in a subsystem.")  
    Defines simplified communication between classes
-   [Memento](https://sourcemaking.com/design_patterns/memento "Provides the ability to restore an object to its previous state.")  
    Capture and restore an object's internal state
-   [Null Object](https://sourcemaking.com/design_patterns/null_object "Designed to act as a default value of an object.")  
    Designed to act as a default value of an object
-   [Observer](https://sourcemaking.com/design_patterns/observer "Observes the state of an object in a program.")  
    A way of notifying change to a number of classes
-   [![](https://sourcemaking.com/files/v2/content/patterns/State-preview.png)](https://sourcemaking.com/design_patterns/state)
    
    [State](https://sourcemaking.com/design_patterns/state "Represent the state of an object.")  
    Alter an object's behavior when its state changes
-   [Strategy](https://sourcemaking.com/design_patterns/strategy "Algorithms can be selected on-the-fly at runtime.")  
    Encapsulates an algorithm inside a class
-   [Template method](https://sourcemaking.com/design_patterns/template_method "A template method defines the skeleton of an algorithm.")  
    Defer the exact steps of an algorithm to a subclass
-   [Visitor](https://sourcemaking.com/design_patterns/visitor "A way of separating an algorithm from an object structure.")  
    Defines a new operation to a class without change

### Criticism

The concept of design patterns has been criticized by some in the field of computer science.

#### Targets the wrong problem

The need for patterns results from using computer languages or techniques with insufficient abstraction ability. Under ideal factoring, a concept should not be copied, but merely referenced. But if something is referenced instead of copied, then there is no "pattern" to label and catalog. Paul Graham writes in the essay  [Revenge of the Nerds](http://www.paulgraham.com/icad.html).

Peter Norvig provides a similar argument. He demonstrates that 16 out of the 23 patterns in the Design Patterns book (which is primarily focused on C++) are simplified or eliminated (via direct language support) in Lisp or Dylan.

#### Lacks formal foundations

The study of design patterns has been excessively ad hoc, and some have argued that the concept sorely needs to be put on a more formal footing. At  OOPSLA 1999, the Gang of Four were (with their full cooperation) subjected to a show trial, in which they were "charged" with numerous crimes against computer science. They were "convicted" by ⅔ of the "jurors" who attended the trial.

#### Leads to inefficient solutions

The idea of a design pattern is an attempt to standardize what are already accepted best practices. In principle this might appear to be beneficial, but in practice it often results in the unnecessary duplication of code. It is almost always a more efficient solution to use a well-factored implementation rather than a "just barely good enough" design pattern.

#### Does not differ significantly from other abstractions

Some authors allege that design patterns don't differ significantly from other forms of abstraction, and that the use of new terminology (borrowed from the architecture community) to describe existing phenomena in the field of programming is unnecessary. The Model-View-Controller paradigm is touted as an example of a "pattern" which predates the concept of "design patterns" by several years. It is further argued by some that the primary contribution of the Design Patterns community (and the Gang of Four book) was the use of Alexander's pattern language as a form of documentation; a practice which is often ignored in the literature.