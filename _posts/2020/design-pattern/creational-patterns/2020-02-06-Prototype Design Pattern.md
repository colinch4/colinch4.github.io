---
layout: post
title: "[Design Pattern] Prototype"
description: "Prototype is a creational design pattern that lets you copy existing objects without making your code dependent on their classes."
date: 2020-02-06 13:04
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://algamza.github.io/2020-02-06/Design-Patterns)  /  [Creational Patterns](https://algamza.github.io/2020-02-06/Creational-Design-patterns)

#### Also known as:  Clone

## Intent

**Prototype**  is a creational design pattern that lets you copy existing objects without making your code dependent on their classes.

![Prototype Design Pattern](https://refactoring.guru/images/patterns/content/prototype/prototype.png)

## Problem

Say you have an object, and you want to create an exact copy of it. How would you do it? First, you have to create a new object of the same class. Then you have to go through all the fields of the original object and copy their values over to the new object.

Nice! But there’s a catch. Not all objects can be copied that way because some of the object’s fields may be private and not visible from outside of the object itself.

![Pre-built prototypes](https://refactoring.guru/images/patterns/content/prototype/prototype-comic-1-en.png)
Copying an object “from the outside” [isn’t](https://refactoring.guru/cargo-cult) always possible.

There’s one more problem with the direct approach. Since you have to know the object’s class to create a duplicate, your code becomes dependent on that class. If the extra dependency doesn’t scare you, there’s another catch. Sometimes you only know the interface that the object follows, but not its concrete class, when, for example, a parameter in a method accepts any objects that follow some interface.

## Solution

The Prototype pattern delegates the cloning process to the actual objects that are being cloned. The pattern declares a common interface for all objects that support cloning. This interface lets you clone an object without coupling your code to the class of that object. Usually, such an interface contains just a single  `clone`  method.

The implementation of the  `clone`  method is very similar in all classes. The method creates an object of the current class and carries over all of the field values of the old object into the new one. You can even copy private fields because most programming languages let objects access private fields of other objects that belong to the same class.

An object that supports cloning is called a  _prototype_. When your objects have dozens of fields and hundreds of possible configurations, cloning them might serve as an alternative to subclassing.

![Pre-built prototypes](https://refactoring.guru/images/patterns/content/prototype/prototype-comic-2-en.png)

Pre-built prototypes can be an alternative to subclassing.

Here’s how it works: you create a set of objects, configured in various ways. When you need an object like the one you’ve configured, you just clone a prototype instead of constructing a new object from scratch.

## Real-World Analogy

In real life, prototypes are used for performing various tests before starting mass production of a product. However, in this case, prototypes don’t participate in any actual production, playing a passive role instead.

![The cell division](https://refactoring.guru/images/patterns/content/prototype/prototype-comic-3-en.png)

The division of a cell.

Since industrial prototypes don’t really copy themselves, a much closer analogy to the pattern is the process of mitotic cell division (biology, remember?). After mitotic division, a pair of identical cells is formed. The original cell acts as a prototype and takes an active role in creating the copy.

## Structure

#### Basic implementation

![The structure of the Prototype design pattern](https://refactoring.guru/images/patterns/diagrams/prototype/structure.png)

1.  The  **Prototype**  interface declares the cloning methods. In most cases, it’s a single  `clone`  method.
    
2.  The  **Concrete Prototype**  class implements the cloning method. In addition to copying the original object’s data to the clone, this method may also handle some edge cases of the cloning process related to cloning linked objects, untangling recursive dependencies, etc.
    
3.  The  **Client**  can produce a copy of any object that follows the prototype interface.
    

#### Prototype registry implementation

![The prototype registry](https://refactoring.guru/images/patterns/diagrams/prototype/structure-prototype-cache.png)

1.  The  **Prototype Registry**  provides an easy way to access frequently-used prototypes. It stores a set of pre-built objects that are ready to be copied. The simplest prototype registry is a  `name → prototype`  hash map. However, if you need better search criteria than a simple name, you can build a much more robust version of the registry.
    

## Pseudocode

In this example, the  **Prototype**  pattern lets you produce exact copies of geometric objects, without coupling the code to their classes.

![The structure of the Prototype pattern example](https://refactoring.guru/images/patterns/diagrams/prototype/example.png)

Cloning a set of objects that belong to a class hierarchy.

All shape classes follow the same interface, which provides a cloning method. A subclass may call the parent’s cloning method before copying its own field values to the resulting object.

```java
// Base prototype.
abstract class Shape is
    field X: int
    field Y: int
    field color: string

    // A regular constructor.
    constructor Shape() is
        // ...

    // The prototype constructor. A fresh object is initialized
    // with values from the existing object.
    constructor Shape(source: Shape) is
        this()
        this.X = source.X
        this.Y = source.Y
        this.color = source.color

    // The clone operation returns one of the Shape subclasses.
    abstract method clone():Shape

// Concrete prototype. The cloning method creates a new object
// and passes it to the constructor. Until the constructor is
// finished, it has a reference to a fresh clone. Therefore,
// nobody has access to a partly-built clone. This keeps the
// cloning result consistent.
class Rectangle extends Shape is
    field width: int
    field height: int

    constructor Rectangle(source: Rectangle) is
        // A parent constructor call is needed to copy private
        // fields defined in the parent class.
        super(source)
        this.width = source.width
        this.height = source.height

    method clone():Shape is
        return new Rectangle(this)

class Circle extends Shape is
    field radius: int

    constructor Circle(source: Circle) is
        super(source)
        this.radius = source.radius

    method clone():Shape is
        return new Circle(this)

// Somewhere in the client code.
class Application is
    field shapes: array of Shape

    constructor Application() is
        Circle circle = new Circle()
        circle.X = 10
        circle.Y = 10
        circle.radius = 20
        shapes.add(circle)

        Circle anotherCircle = circle.clone()
        shapes.add(anotherCircle)
        // The `anotherCircle` variable contains an exact copy
        // of the `circle` object.

        Rectangle rectangle = new Rectangle()
        rectangle.width = 10
        rectangle.height = 20
        shapes.add(rectangle)

    method businessLogic() is
        // Prototype rocks because it lets you produce a copy of
        // an object without knowing anything about its type.
        Array shapesCopy = new Array of Shapes.

        // For instance, we don't know the exact elements in the
        // shapes array. All we know is that they are all
        // shapes. But thanks to polymorphism, when we call the
        // `clone` method on a shape the program checks its real
        // class and runs the appropriate clone method defined
        // in that class. That's why we get proper clones
        // instead of a set of simple Shape objects.
        foreach (s in shapes) do
            shapesCopy.add(s.clone())

        // The `shapesCopy` array contains exact copies of the
        // `shape` array's children.
```

## Applicability

Use the Prototype pattern when your code shouldn’t depend on the concrete classes of objects that you need to copy.

This happens a lot when your code works with objects passed to you from 3rd-party code via some interface. The concrete classes of these objects are unknown, and you couldn’t depend on them even if you wanted to.

The Prototype pattern provides the client code with a general interface for working with all objects that support cloning. This interface makes the client code independent from the concrete classes of objects that it clones.

Use the pattern when you want to reduce the number of subclasses that only differ in the way they initialize their respective objects. Somebody could have created these subclasses to be able to create objects with a specific configuration.

The Prototype pattern lets you use a set of pre-built objects, configured in various ways, as prototypes.

Instead of instantiating a subclass that matches some configuration, the client can simply look for an appropriate prototype and clone it.

## How to Implement

1.  Create the prototype interface and declare the  `clone`  method in it. Or just add the method to all classes of an existing class hierarchy, if you have one.
    
2.  A prototype class must define the alternative constructor that accepts an object of that class as an argument. The constructor must copy the values of all fields defined in the class from the passed object into the newly created instance. If you’re changing a subclass, you must call the parent constructor to let the superclass handle the cloning of its private fields.
    
    If your programming language doesn’t support method overloading, you may define a special method for copying the object data. The constructor is a more convenient place to do this because it delivers the resulting object right after you call the  `new`  operator.
    
3.  The cloning method usually consists of just one line: running a  `new`  operator with the prototypical version of the constructor. Note, that every class must explicitly override the cloning method and use its own class name along with the  `new`  operator. Otherwise, the cloning method may produce an object of a parent class.
    
4.  Optionally, create a centralized prototype registry to store a catalog of frequently used prototypes.
    
    You can implement the registry as a new factory class or put it in the base prototype class with a static method for fetching the prototype. This method should search for a prototype based on search criteria that the client code passes to the method. The criteria might either be a simple string tag or a complex set of search parameters. After the appropriate prototype is found, the registry should clone it and return the copy to the client.
    
    Finally, replace the direct calls to the subclasses’ constructors with calls to the factory method of the prototype registry.
    

## Pros and Cons

-   You can clone objects without coupling to their concrete classes.
-   You can get rid of repeated initialization code in favor of cloning pre-built prototypes.
-   You can produce complex objects more conveniently.
-   You get an alternative to inheritance when dealing with configuration presets for complex objects.

-   Cloning complex objects that have circular references might be very tricky.

## Relations with Other Patterns

-   Many designs start by using  [Factory Method](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern)  (less complicated and more customizable via subclasses) and evolve toward  [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern),  [Prototype](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern), or  [Builder](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  (more flexible, but more complicated).
    
-   [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern)  classes are often based on a set of  [Factory Methods](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern), but you can also use  [Prototype](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern)  to compose the methods on these classes.
    
-   [Prototype](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern)  can help when you need to save copies of  [Commands](https://algamza.github.io/2020-02-06/Command-Design-Pattern)  into history.
    
-   Designs that make heavy use of  [Composite](https://algamza.github.io/2020-02-06/Composite-Design-Pattern)  and  [Decorator](https://algamza.github.io/2020-02-06/Decorator-Design-Pattern)  can often benefit from using  [Prototype](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern). Applying the pattern lets you clone complex structures instead of re-constructing them from scratch.
    
-   [Prototype](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern)  isn’t based on inheritance, so it doesn’t have its drawbacks. On the other hand,  _Prototype_  requires a complicated initialization of the cloned object.  [Factory Method](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern)  is based on inheritance but doesn’t require an initialization step.
    
-   Sometimes  [Prototype](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern)  can be a simpler alternative to  [Memento](https://algamza.github.io/2020-02-06/Memento-Design-Pattern). This works if the object, the state of which you want to store in the history, is fairly straightforward and doesn’t have links to external resources, or the links are easy to re-establish.
    
-   [Abstract Factories](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern),  [Builders](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  and  [Prototypes](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern)  can all be implemented as  [Singletons](https://algamza.github.io/2020-02-06/Singleton-Design-Pattern).

## Code Example

**Prototype**  is a creational design pattern that allows cloning objects, even complex ones, without coupling to their specific classes.

All prototype classes should have a common interface that makes it possible to copy objects even if their concrete classes are unknown. Prototype objects can produce full copies since objects of the same class can access each other’s private fields.

[Learn more about Prototype](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern)

## Usage of the pattern in Java

**Complexity:**

**Popularity:**

**Usage examples:**  The Prototype pattern is available in Java out of the box with a  `Cloneable`  interface.

Any class can implement this interface to become cloneable.

-   [`java.lang.Object#clone()`](http://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)  (class should implement the  [`java.lang.Cloneable`](http://docs.oracle.com/javase/8/docs/api/java/lang/Cloneable.html)  interface)

**Identification:**  The prototype can be easily recognized by a  `clone`  or  `copy`  methods, etc.

## Copying graphical shapes

Let’s take a look at how the Prototype can be implemented without the standard  `Cloneable`  interface.

## [](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern/java/example#example-0--shapes)**shapes:**  Shape list

#### [](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern/java/example#example-0--shapes-Shape-java)**shapes/Shape.java:**  Common shape interface
```java
package refactoring_guru.prototype.example.shapes;

import java.util.Objects;

public abstract class Shape {
    public int x;
    public int y;
    public String color;

    public Shape() {
    }

    public Shape(Shape target) {
        if (target != null) {
            this.x = target.x;
            this.y = target.y;
            this.color = target.color;
        }
    }

    public abstract Shape clone();

    @Override
    public boolean equals(Object object2) {
        if (!(object2 instanceof Shape)) return false;
        Shape shape2 = (Shape) object2;
        return shape2.x == x && shape2.y == y && Objects.equals(shape2.color, color);
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern/java/example#example-0--shapes-Circle-java)**shapes/Circle.java:**  Simple shape
```java
package refactoring_guru.prototype.example.shapes;

public class Circle extends Shape {
    public int radius;

    public Circle() {
    }

    public Circle(Circle target) {
        super(target);
        if (target != null) {
            this.radius = target.radius;
        }
    }

    @Override
    public Shape clone() {
        return new Circle(this);
    }

    @Override
    public boolean equals(Object object2) {
        if (!(object2 instanceof Circle) || !super.equals(object2)) return false;
        Circle shape2 = (Circle) object2;
        return shape2.radius == radius;
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern/java/example#example-0--shapes-Rectangle-java)**shapes/Rectangle.java:**  Another shape
```java
package refactoring_guru.prototype.example.shapes;

public class Rectangle extends Shape {
    public int width;
    public int height;

    public Rectangle() {
    }

    public Rectangle(Rectangle target) {
        super(target);
        if (target != null) {
            this.width = target.width;
            this.height = target.height;
        }
    }

    @Override
    public Shape clone() {
        return new Rectangle(this);
    }

    @Override
    public boolean equals(Object object2) {
        if (!(object2 instanceof Rectangle) || !super.equals(object2)) return false;
        Rectangle shape2 = (Rectangle) object2;
        return shape2.width == width && shape2.height == height;
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern/java/example#example-0--Demo-java)**Demo.java:**  Cloning example
```java
package refactoring_guru.prototype.example;

import refactoring_guru.prototype.example.shapes.Circle;
import refactoring_guru.prototype.example.shapes.Rectangle;
import refactoring_guru.prototype.example.shapes.Shape;

import java.util.ArrayList;
import java.util.List;

public class Demo {
    public static void main(String[] args) {
        List<Shape> shapes = new ArrayList<>();
        List<Shape> shapesCopy = new ArrayList<>();

        Circle circle = new Circle();
        circle.x = 10;
        circle.y = 20;
        circle.radius = 15;
        circle.color = "red";
        shapes.add(circle);

        Circle anotherCircle = (Circle) circle.clone();
        shapes.add(anotherCircle);

        Rectangle rectangle = new Rectangle();
        rectangle.width = 10;
        rectangle.height = 20;
        circle.color = "blue";
        shapes.add(rectangle);

        cloneAndCompare(shapes, shapesCopy);
    }

    private static void cloneAndCompare(List<Shape> shapes, List<Shape> shapesCopy) {
        for (Shape shape : shapes) {
            shapesCopy.add(shape.clone());
        }

        for (int i = 0; i < shapes.size(); i++) {
            if (shapes.get(i) != shapesCopy.get(i)) {
                System.out.println(i + ": Shapes are different objects (yay!)");
                if (shapes.get(i).equals(shapesCopy.get(i))) {
                    System.out.println(i + ": And they are identical (yay!)");
                } else {
                    System.out.println(i + ": But they are not identical (booo!)");
                }
            } else {
                System.out.println(i + ": Shape objects are the same (booo!)");
            }
        }
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern/java/example#example-0--OutputDemo-txt)**OutputDemo.txt:**  Execution results
```java
0: Shapes are different objects (yay!)
0: And they are identical (yay!)
1: Shapes are different objects (yay!)
1: And they are identical (yay!)
2: Shapes are different objects (yay!)
2: And they are identical (yay!)
```
#### Prototype registry

You could implement a centralized prototype registry (or factory), which would contain a set of pre-defined prototype objects. This way you could retrieve new objects from the factory by passing its name or other parameters. The factory would search for an appropriate prototype, clone it and return you a copy.

## [](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern/java/example#example-0--cache)**cache**

#### [](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern/java/example#example-0--cache-BundledShapeCache-java)**cache/BundledShapeCache.java:**  Prototype factory
```java
package refactoring_guru.prototype.caching.cache;

import refactoring_guru.prototype.example.shapes.Circle;
import refactoring_guru.prototype.example.shapes.Rectangle;
import refactoring_guru.prototype.example.shapes.Shape;

import java.util.HashMap;
import java.util.Map;

public class BundledShapeCache {
    private Map<String, Shape> cache = new HashMap<>();

    public BundledShapeCache() {
        Circle circle = new Circle();
        circle.x = 5;
        circle.y = 7;
        circle.radius = 45;
        circle.color = "Green";

        Rectangle rectangle = new Rectangle();
        rectangle.x = 6;
        rectangle.y = 9;
        rectangle.width = 8;
        rectangle.height = 10;
        rectangle.color = "Blue";

        cache.put("Big green circle", circle);
        cache.put("Medium blue rectangle", rectangle);
    }

    public Shape put(String key, Shape shape) {
        cache.put(key, shape);
        return shape;
    }

    public Shape get(String key) {
        return cache.get(key).clone();
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern/java/example#example-0--Demo-java)**Demo.java:**  Cloning example
```java
package refactoring_guru.prototype.caching;

import refactoring_guru.prototype.caching.cache.BundledShapeCache;
import refactoring_guru.prototype.example.shapes.Shape;

public class Demo {
    public static void main(String[] args) {
        BundledShapeCache cache = new BundledShapeCache();

        Shape shape1 = cache.get("Big green circle");
        Shape shape2 = cache.get("Medium blue rectangle");
        Shape shape3 = cache.get("Medium blue rectangle");

        if (shape1 != shape2 && !shape1.equals(shape2)) {
            System.out.println("Big green circle != Medium blue rectangle (yay!)");
        } else {
            System.out.println("Big green circle == Medium blue rectangle (booo!)");
        }

        if (shape2 != shape3) {
            System.out.println("Medium blue rectangles are two different objects (yay!)");
            if (shape2.equals(shape3)) {
                System.out.println("And they are identical (yay!)");
            } else {
                System.out.println("But they are not identical (booo!)");
            }
        } else {
            System.out.println("Rectangle objects are the same (booo!)");
        }
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern/java/example#example-0--OutputDemo-txt)**OutputDemo.txt:**  Execution results
```java
Big green circle != Medium blue rectangle (yay!)
Medium blue rectangles are two different objects (yay!)
And they are identical (yay!)
```