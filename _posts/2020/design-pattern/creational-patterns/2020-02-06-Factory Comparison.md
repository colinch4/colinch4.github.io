---
layout: post
title: "[Design Pattern] Factory Comparison"
description: "This article will show the difference between:"
date: 2020-02-06 13:02
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://algamza.github.io/2020-02-06/Design-Patterns)  /  [Creational Patterns](https://algamza.github.io/2020-02-06/Creational-Design-patterns)

# Factory Comparison

This article will show the difference between:

1.  Factory
2.  Creation method
3.  Static creation (or factory) method
4.  Simple factory
5.  [Factory Method](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern)
6.  [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern)

You can find references to these terms all around the web. Though they may look similar, they all have different meanings. A lot of people don’t realize that, which leads to confusion and misunderstanding.

So let’s try to figure out the difference and solve this problem once and for all.

## 1. Factory

**Factory**  is an ambiguous term that stands for a function, method or class that supposed to be producing something. Most commonly, factories produce objects. But they may also produce files, records in databases, etc.

For instance, any of these things may be casually referenced as a “factory”:

-   a function or method that creates a program’s GUI;
-   a class that creates users;
-   static method that calls a class constructor in a certain way;
-   one of the creational design patterns.

Usually, when someone says a word “factory,” the exact meaning is supposed to be clear from a context. But if you’re in doubt, just ask. There’s a chance that the author is ignorant.

## 2. Creation method

Creation method defined in the  [Refactoring To Patterns](https://refactoring.guru/ref-to-patterns-book)  book as “a method that creates objects.” This means that every result of a factory method pattern is a “creation method” but not necessarily the reverse. It also means that you can substitute the term “creation method” wherever Martin Fowler uses the term “factory method” in  [Refactoring](https://refactoring.guru/ref-book)  and wherever Joshua Bloch uses the term “static factory method” in  [Effective Java](https://refactoring.guru/effective-java-book).

In reality, the creation method is just a wrapper around a constructor call. It may just have a name that better expresses your intentions. On the other hand, it may help to isolate your code from changes to the constructor. It could even contain some particular logic that would return existing objects instead of creating new.

A lot of people would call such methods “factory method” just because it produces new objects: The logic is straightforward: the method creates objects and since all  _factories_  creates objects, this method should clearly be a  _factory method_. Naturally, there’s a lot of confusion when it comes to the real  [Factory Method](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern)  pattern.

In the following example,  `next`  is a creation method:

class Number {
    private $value;

    public function __construct($value) {
        $this->value = $value;
    }

    public function next() {
        return new Number ($this->value + 1);
    }
}

## 3. Static creation method

**Static creation method**  is a creation method declared as  `static`. In other words, it can be called on a class and doesn’t require an object to be created.

Don’t be confused when someone calls methods like this a “static factory method”. That’s just a bad habit. The  [Factory Method](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern)  is a design pattern that relies on inheritance. If you make it  `static`, you can no longer extend it in subclasses, which defeats the purpose of the pattern.

When a static creation method returns new objects it becomes an alternative constructor.

It might be useful when:

-   You have to have several different constructors that have different purposes but their signatures match. For instance, having both  `Random(int max)`  and  `Random(int min)`  is impossible in Java, C++, C#, and many other languages. And the most popular workaround is to create several static methods that call the default constructor and set appropriate values afterward.
    
-   You want to reuse existing objects, instead of instancing new ones (see, the  [Singleton](https://algamza.github.io/2020-02-06/Singleton-Design-Pattern)  pattern). Constructors in most programming languages have to return new class instances. The static creation method is a workaround to this limitation. Inside a static method, your code can decide whether to create a fresh instance by calling the constructor or return an existing object from some cache.
    

In the following example, the  `load`  method is a static factory method. It provides a convenient way to retrieve users from a database.

class User {
    private $id, $name, $email, $phone;

    public function __construct($id, $name, $email, $phone) {
        $this->id = $id;
        $this->name = $name;
        $this->email = $email;
        $this->phone = $phone;
    }

    public static function load($id) {
        list($id, $name, $email, $phone) = DB::load_data('users', 'id', 'name', 'email', 'phone');
        $user = new User($id, $name, $email, $phone);
        return $user;
    }
}

## 4.  _Simple factory_  pattern

The  **Simple factory**  pattern describes a class that has one creation method with a large conditional that based on method parameters chooses which product class to instantiate and then return.

People usually confuse  _simple factories_  with a general  _factories_  or with one of the creational design patterns. In most cases, a simple factory is an intermediate step of introducing  [Factory Method](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern)  or  [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern)  patterns.

Simple factories usually don’t have subclasses. But after extracting subclasses from a simple factory, it starts to look like a classic  _factory method_  pattern.

By the way, if you declare a simple factory  `abstract`, it doesn’t magically become the  _abstract factory_  pattern.

Here’s an example of  _simple factory_:

class UserFactory {
    public static function create($type) {
        switch ($type) {
            case 'user': return new User();
            case 'customer': return new Customer();
            case 'admin': return new Admin();
            default:
                throw new Exception('Wrong user type passed.');
        }
    }
}

## 5.  _Factory Method_  pattern

The  **Factory Method** is a creational design pattern that provides an interface for creating objects but allows subclasses to alter the type of an object that will be created.

If you have a creation method in base class and subclasses that extend it, you might be looking at the factory method.

abstract class Department {
    public abstract function createEmployee($id);

    public function fire($id) {
        $employee = $this->createEmployee($id);
        $employee->paySalary();
        $employee->dismiss();
    }
}

class ITDepartment extends Department {
    public function createEmployee($id) {
        return new Programmer($id);
    }
}

class AccountingDepartment extends Department {
    public function createEmployee($id) {
        return new Accountant($id);
    }
}

## 6.  _Abstract Factory_  pattern

The  **Abstract Factory** is a creational design pattern that allows producing families of related or dependent objects without specifying their concrete classes.

What are the "families of objects"? For instance, take this set of classes:  `Transport`  +  `Engine`  +  `Controls`. There are might be several variants of these:

1.  `Car`  +  `CombustionEngine`  +  `SteeringWheel`
2.  `Plane`  +  `JetEngine`  +  `Yoke`

If your program doesn’t operate with product families, then you don’t need an abstract factory.

And again, a lot of people mix-up the  _abstract factory_  pattern with a simple factory class declared as  `abstract`. Don’t do that!

### Afterword

Now that you know the difference, take a fresh look at the design patterns:

-   [Factory Method](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern)
-   [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern)