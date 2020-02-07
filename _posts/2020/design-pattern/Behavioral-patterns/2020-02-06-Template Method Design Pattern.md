---
layout: post
title: "[Design Pattern] Template Method"
description: "Template Method is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure."
date: 2020-02-06 14:09
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://algamza.github.io/2020-02-06/Design-Patterns)  /  [Behavioral Patterns](https://algamza.github.io/2020-02-06/Behavioral-Design-Patterns)

## Intent

**Template Method**  is a behavioral design pattern that defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps of the algorithm without changing its structure.

![Template method design pattern](https://refactoring.guru/images/patterns/content/template-method/template-method.png)

## Problem

Imagine that you’re creating a data mining application that analyzes corporate documents. Users feed the app documents in various formats (PDF, DOC, CSV), and it tries to extract meaningful data from these docs in a uniform format.

The first version of the app could work only with DOC files. In the following version, it was able to support CSV files. A month later, you “taught” it to extract data from PDF files.

![Data mining classes contained a lot of duplicate code](https://refactoring.guru/images/patterns/diagrams/template-method/problem.png)

Data mining classes contained a lot of duplicate code.

At some point, you noticed that all three classes have a lot of similar code. While the code for dealing with various data formats was entirely different in all classes, the code for data processing and analysis is almost identical. Wouldn’t it be great to get rid of the code duplication, leaving the algorithm structure intact?

There was another problem related to client code that used these classes. It had lots of conditionals that picked a proper course of action depending on the class of the processing object. If all three processing classes had a common interface or a base class, you’d be able to eliminate the conditionals in client code and use polymorphism when calling methods on a processing object.

## Solution

The Template Method pattern suggests that you break down an algorithm into a series of steps, turn these steps into methods, and put a series of calls to these methods inside a single “template method.” The steps may either be  `abstract`, or have some default implementation. To use the algorithm, the client is supposed to provide its own subclass, implement all abstract steps, and override some of the optional ones if needed (but not the template method itself).

Let’s see how this will play out in our data mining app. We can create a base class for all three parsing algorithms. This class defines a template method consisting of a series of calls to various document-processing steps.

![Template method defines the skeleton of the algorithm](https://refactoring.guru/images/patterns/diagrams/template-method/solution-en.png)

Template method breaks the algorithm into steps, allowing subclasses to override these steps but not the actual method.

At first, we can declare all steps  `abstract`, forcing the subclasses to provide their own implementations for these methods. In our case, subclasses already have all necessary implementations, so the only thing we might need to do is adjust signatures of the methods to match the methods of the superclass.

Now, let’s see what we can do to get rid of the duplicate code. It looks like the code for opening/closing files and extracting/parsing data is different for various data formats, so there’s no point in touching those methods. However, implementation of other steps, such as analyzing the raw data and composing reports, is very similar, so it can be pulled up into the base class, where subclasses can share that code.

As you can see, we’ve got two types of steps:

-   _abstract steps_  must be implemented by every subclass
-   _optional steps_  already have some default implementation, but still can be overridden if needed

There’s another type of step, called  _hooks_. A hook is an optional step with an empty body. A template method would work even if a hook isn’t overridden. Usually, hooks are placed before and after crucial steps of algorithms, providing subclasses with additional extension points for an algorithm.

## Real-World Analogy

![Mass housing construction](https://refactoring.guru/images/patterns/diagrams/template-method/live-example.png)

A typical architectural plan can be slightly altered to better fit the client’s needs.

The template method approach can be used in mass housing construction. The architectural plan for building a standard house may contain several extension points that would let a potential owner adjust some details of the resulting house.

Each building step, such as laying the foundation, framing, building walls, installing plumbing and wiring for water and electricity, etc., can be slightly changed to make the resulting house a little bit different from others.

## Structure

![Structure of the Template Method design pattern](https://refactoring.guru/images/patterns/diagrams/template-method/structure.png)

1.  The  **Abstract Class**  declares methods that act as steps of an algorithm, as well as the actual template method which calls these methods in a specific order. The steps may either be declared  `abstract`  or have some default implementation.
    
2.  **Concrete Classes**  can override all of the steps, but not the template method itself.
    

## Pseudocode

In this example, the  **Template Method**  pattern provides a “skeleton” for various branches of artificial intelligence in a simple strategy video game.

![Structure of the Template Method pattern example](https://refactoring.guru/images/patterns/diagrams/template-method/example.png)

AI classes of a simple video game.

All races in the game have almost the same types of units and buildings. Therefore you can reuse the same AI structure for various races, while being able to override some of the details. With this approach, you can override the orcs’ AI to make it more aggressive, make humans more defense-oriented, and make monsters unable to build anything. Adding a new race to the game would require creating a new AI subclass and overriding the default methods declared in the base AI class.

```java
// The abstract class defines a template method that contains a
// skeleton of some algorithm composed of calls, usually to
// abstract primitive operations. Concrete subclasses implement
// these operations, but leave the template method itself
// intact.
class GameAI is
    // The template method defines the skeleton of an algorithm.
    method turn() is
        collectResources()
        buildStructures()
        buildUnits()
        attack()

    // Some of the steps may be implemented right in a base
    // class.
    method collectResources() is
        foreach (s in this.builtStructures) do
            s.collect()

    // And some of them may be defined as abstract.
    abstract method buildStructures()
    abstract method buildUnits()

    // A class can have several template methods.
    method attack() is
        enemy = closestEnemy()
        if (enemy == null)
            sendScouts(map.center)
        else
            sendWarriors(enemy.position)

    abstract method sendScouts(position)
    abstract method sendWarriors(position)

// Concrete classes have to implement all abstract operations of
// the base class but they must not override the template method
// itself.
class OrcsAI extends GameAI is
    method buildStructures() is
        if (there are some resources) then
            // Build farms, then barracks, then stronghold.

    method buildUnits() is
        if (there are plenty of resources) then
            if (there are no scouts)
                // Build peon, add it to scouts group.
            else
                // Build grunt, add it to warriors group.

    // ...

    method sendScouts(position) is
        if (scouts.length > 0) then
            // Send scouts to position.

    method sendWarriors(position) is
        if (warriors.length > 5) then
            // Send warriors to position.

// Subclasses can also override some operations with a default
// implementation.
class MonstersAI extends GameAI is
    method collectResources() is
        // Monsters don't collect resources.

    method buildStructures() is
        // Monsters don't build structures.

    method buildUnits() is
        // Monsters don't build units.
```

## Applicability

Use the Template Method pattern when you want to let clients extend only particular steps of an algorithm, but not the whole algorithm or its structure.

The Template Method lets you turn a monolithic algorithm into a series of individual steps which can be easily extended by subclasses while keeping intact the structure defined in a superclass.

Use the pattern when you have several classes that contain almost identical algorithms with some minor differences. As a result, you might need to modify all classes when the algorithm changes.

When you turn such an algorithm into a template method, you can also pull up the steps with similar implementations into a superclass, eliminating code duplication. Code that varies between subclasses can remain in subclasses.

## How to Implement

1.  Analyze the target algorithm to see whether you can break it into steps. Consider which steps are common to all subclasses and which ones will always be unique.
    
2.  Create the abstract base class and declare the template method and a set of abstract methods representing the algorithm’s steps. Outline the algorithm’s structure in the template method by executing corresponding steps. Consider making the template method  `final`  to prevent subclasses from overriding it.
    
3.  It’s okay if all the steps end up being abstract. However, some steps might benefit from having a default implementation. Subclasses don’t have to implement those methods.
    
4.  Think of adding hooks between the crucial steps of the algorithm.
    
5.  For each variation of the algorithm, create a new concrete subclass. It  _must_  implement all of the abstract steps, but  _may_  also override some of the optional ones.
    

## Pros and Cons

-   You can let clients override only certain parts of a large algorithm, making them less affected by changes that happen to other parts of the algorithm.
-   You can pull the duplicate code into a superclass.

-   Some clients may be limited by the provided skeleton of an algorithm.
-   You might violate the  _Liskov Substitution Principle_  by suppressing a default step implementation via a subclass.
-   Template methods tend to be harder to maintain the more steps they have.

## Relations with Other Patterns

-   [Factory Method](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern)  is a specialization of  [Template Method](https://algamza.github.io/2020-02-06/Template-Method-Design-Pattern). At the same time, a  _Factory Method_  may serve as a step in a large  _Template Method_.
    
-   [Template Method](https://algamza.github.io/2020-02-06/Template-Method-Design-Pattern)  is based on inheritance: it lets you alter parts of an algorithm by extending those parts in subclasses.  [Strategy](https://algamza.github.io/2020-02-06/Stategy-Design-Pattern)  is based on composition: you can alter parts of the object’s behavior by supplying it with different strategies that correspond to that behavior.  _Template Method_  works at the class level, so it’s static.  _Strategy_  works on the object level, letting you switch behaviors at runtime.

## Code Example
**Template Method**  is a behavioral design pattern that allows you to defines a skeleton of an algorithm in a base class and let subclasses override the steps without changing the overall algorithm’s structure.

[Learn more about Template Method](https://algamza.github.io/2020-02-06/Template-Method-Design-Pattern)

## Usage of the pattern in Java

**Complexity:**

**Popularity:**

**Usage examples:**  The Template Method pattern is quite common in Java frameworks. Developers often use it to provide framework users with a simple means of extending standard functionality using inheritance.

Here are some examples of Template Methods in core Java libraries:

-   All non-abstract methods of  [`java.io.InputStream`](http://docs.oracle.com/javase/8/docs/api/java/io/InputStream.html),  [`java.io.OutputStream`](http://docs.oracle.com/javase/8/docs/api/java/io/OutputStream.html),  [`java.io.Reader`](http://docs.oracle.com/javase/8/docs/api/java/io/Reader.html)  and  [`java.io.Writer`](http://docs.oracle.com/javase/8/docs/api/java/io/Writer.html).
    
-   All non-abstract methods of  [`java.util.AbstractList`](http://docs.oracle.com/javase/8/docs/api/java/util/AbstractList.html),  [`java.util.AbstractSet`](http://docs.oracle.com/javase/8/docs/api/java/util/AbstractSet.html)  and  [`java.util.AbstractMap`](http://docs.oracle.com/javase/8/docs/api/java/util/AbstractMap.html).
    
-   [`javax.servlet.http.HttpServlet`](http://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpServlet.html), all the  `doXXX()`  methods by default send a HTTP 405 “Method Not Allowed” error as a response. You’re free to override any of them.
    

**Identification:**  Template Method can be recognized by behavioral methods that already have a “default” behavior defined by the base class.

## Overriding standard steps of an algorithm

In this example, the Template Method pattern defines an algorithm of working with a social network. Subclasses that match a particular social network, implement these steps according to the API provided by the social network.

## [](https://algamza.github.io/2020-02-06/Template-Method-Design-Pattern/java/example#example-0--networks)**networks**

#### [](https://algamza.github.io/2020-02-06/Template-Method-Design-Pattern/java/example#example-0--networks-Network-java)**networks/Network.java:**  Base social network class
```java
package refactoring_guru.template_method.example.networks;

/**
 * Base class of social network.
 */
public abstract class Network {
    String userName;
    String password;

    Network() {}

    /**
     * Publish the data to whatever network.
     */
    public boolean post(String message) {
        // Authenticate before posting. Every network uses a different
        // authentication method.
        if (logIn(this.userName, this.password)) {
            // Send the post data.
            boolean result =  sendData(message.getBytes());
            logOut();
            return result;
        }
        return false;
    }

    abstract boolean logIn(String userName, String password);
    abstract boolean sendData(byte[] data);
    abstract void logOut();
}
```
#### [](https://algamza.github.io/2020-02-06/Template-Method-Design-Pattern/java/example#example-0--networks-Facebook-java)**networks/Facebook.java:**  Concrete social network
```java
package refactoring_guru.template_method.example.networks;

/**
 * Class of social network
 */
public class Facebook extends Network {
    public Facebook(String userName, String password) {
        this.userName = userName;
        this.password = password;
    }

    public boolean logIn(String userName, String password) {
        System.out.println("\nChecking user's parameters");
        System.out.println("Name: " + this.userName);
        System.out.print("Password: ");
        for (int i = 0; i < this.password.length(); i++) {
            System.out.print("*");
        }
        simulateNetworkLatency();
        System.out.println("\n\nLogIn success on Facebook");
        return true;
    }

    public boolean sendData(byte[] data) {
        boolean messagePosted = true;
        if (messagePosted) {
            System.out.println("Message: '" + new String(data) + "' was posted on Facebook");
            return true;
        } else {
            return false;
        }
    }

    public void logOut() {
        System.out.println("User: '" + userName + "' was logged out from Facebook");
    }

    private void simulateNetworkLatency() {
        try {
            int i = 0;
            System.out.println();
            while (i < 10) {
                System.out.print(".");
                Thread.sleep(500);
                i++;
            }
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Template-Method-Design-Pattern/java/example#example-0--networks-Twitter-java)**networks/Twitter.java:**  One more social network
```java
package refactoring_guru.template_method.example.networks;

/**
 * Class of social network
 */
public class Twitter extends Network {

    public Twitter(String userName, String password) {
        this.userName = userName;
        this.password = password;
    }

    public boolean logIn(String userName, String password) {
        System.out.println("\nChecking user's parameters");
        System.out.println("Name: " + this.userName);
        System.out.print("Password: ");
        for (int i = 0; i < this.password.length(); i++) {
            System.out.print("*");
        }
        simulateNetworkLatency();
        System.out.println("\n\nLogIn success on Twitter");
        return true;
    }

    public boolean sendData(byte[] data) {
        boolean messagePosted = true;
        if (messagePosted) {
            System.out.println("Message: '" + new String(data) + "' was posted on Twitter");
            return true;
        } else {
            return false;
        }
    }

    public void logOut() {
        System.out.println("User: '" + userName + "' was logged out from Twitter");
    }

    private void simulateNetworkLatency() {
        try {
            int i = 0;
            System.out.println();
            while (i < 10) {
                System.out.print(".");
                Thread.sleep(500);
                i++;
            }
        } catch (InterruptedException ex) {
            ex.printStackTrace();
        }
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Template-Method-Design-Pattern/java/example#example-0--Demo-java)**Demo.java:**  Client code
```java
package refactoring_guru.template_method.example;

import refactoring_guru.template_method.example.networks.Facebook;
import refactoring_guru.template_method.example.networks.Network;
import refactoring_guru.template_method.example.networks.Twitter;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Demo class. Everything comes together here.
 */
public class Demo {
    public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        Network network = null;
        System.out.print("Input user name: ");
        String userName = reader.readLine();
        System.out.print("Input password: ");
        String password = reader.readLine();

        // Enter the message.
        System.out.print("Input message: ");
        String message = reader.readLine();

        System.out.println("\nChoose social network for posting message.\n" +
                "1 - Facebook\n" +
                "2 - Twitter");
        int choice = Integer.parseInt(reader.readLine());

        // Create proper network object and send the message.
        if (choice == 1) {
            network = new Facebook(userName, password);
        } else if (choice == 2) {
            network = new Twitter(userName, password);
        }
        network.post(message);
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Template-Method-Design-Pattern/java/example#example-0--OutputDemo-txt)**OutputDemo.txt:**  Execution result
```java
Input user name: Jhonatan
Input password: qswe
Input message: Hello, World!

Choose social network for posting message.
1 - Facebook
2 - Twitter
2

Checking user's parameters
Name: Jhonatan
Password: ****
..........

LogIn success on Twitter
Message: 'Hello, World!' was posted on Twitter
User: 'Jhonatan' was logged out from Twitter
```