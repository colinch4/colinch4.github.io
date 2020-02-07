---
layout: post
title: "Abstract Factory Design Pattern"
description: "Provide an interface for creating families of related or dependent objects without specifying their concrete classes. A hierarchy that encapsulates: many possible "platforms", and the construction of a suite of "products". The  `new`  operator considered harmful."
date: 2020-02-06 13:00
tags: [디자인패턴]
comments: true
share: true
---

/ [Design Patterns](../2020-02-06-Design%20Patterns.md) / [Creational patterns](./2020-02-06-Creational%20patterns.md)

### Intent

-   Provide an interface for creating families of related or dependent objects without specifying their concrete classes.
-   A hierarchy that encapsulates: many possible "platforms", and the construction of a suite of "products".
-   The  `new`  operator considered harmful.

### Problem

If an application is to be portable, it needs to encapsulate platform dependencies. These "platforms" might include: windowing system, operating system, database, etc. Too often, this encapsulation is not engineered in advance, and lots of  `#ifdef`  case statements with options for all currently supported platforms begin to procreate like rabbits throughout the code.

### Discussion

Provide a level of indirection that abstracts the creation of families of related or dependent objects without directly specifying their concrete classes. The "factory" object has the responsibility for providing creation services for the entire platform family. Clients never create platform objects directly, they ask the factory to do that for them.

This mechanism makes exchanging product families easy because the specific class of the factory object appears only once in the application - where it is instantiated. The application can wholesale replace the entire family of products simply by instantiating a different concrete instance of the abstract factory.

Because the service provided by the factory object is so pervasive, it is routinely implemented as a Singleton.

### Structure

The Abstract Factory defines a Factory Method per product. Each Factory Method encapsulates the  `new`  operator and the concrete, platform-specific, product classes. Each "platform" is then modeled with a Factory derived class.

![Scheme of Abstract Factory](https://sourcemaking.com/files/v2/content/patterns/Abstract_Factory.png)

### Example

The purpose of the Abstract Factory is to provide an interface for creating families of related objects, without specifying concrete classes. This pattern is found in the sheet metal stamping equipment used in the manufacture of Japanese automobiles. The stamping equipment is an Abstract Factory which creates auto body parts. The same machinery is used to stamp right hand doors, left hand doors, right front fenders, left front fenders, hoods, etc. for different models of cars. Through the use of rollers to change the stamping dies, the concrete classes produced by the machinery can be changed within three minutes.

![Example of Abstract Factory](https://sourcemaking.com/files/v2/content/patterns/Abstract_Factory_example1.png)

### Check list

1.  Decide if "platform independence" and creation services are the current source of pain.
2.  Map out a matrix of "platforms" versus "products".
3.  Define a factory interface that consists of a factory method per product.
4.  Define a factory derived class for each platform that encapsulates all references to the  `new`  operator.
5.  The client should retire all references to  `new`, and use the factory methods to create the product objects.

### Rules of thumb

-   Sometimes creational patterns are competitors: there are cases when either Prototype or Abstract Factory could be used profitably. At other times they are complementary: Abstract Factory might store a set of Prototypes from which to clone and return product objects, Builder can use one of the other patterns to implement which components get built. Abstract Factory, Builder, and Prototype can use Singleton in their implementation.
-   Abstract Factory, Builder, and Prototype define a factory object that's responsible for knowing and creating the class of product objects, and make it a parameter of the system. Abstract Factory has the factory object producing objects of several classes. Builder has the factory object building a complex product incrementally using a correspondingly complex protocol. Prototype has the factory object (aka prototype) building a product by copying a prototype object.
-   Abstract Factory classes are often implemented with Factory Methods, but they can also be implemented using Prototype.
-   Abstract Factory can be used as an alternative to Facade to hide platform-specific classes.
-   Builder focuses on constructing a complex object step by step. Abstract Factory emphasizes a family of product objects (either simple or complex). Builder returns the product as a final step, but as far as the Abstract Factory is concerned, the product gets returned immediately.
-   Often, designs start out using Factory Method (less complicated, more customizable, subclasses proliferate) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, more complex) as the designer discovers where more flexibility is needed.


### Code 


Abstract Factory classes are often implemented with Factory Methods, but they can also be implemented using Prototype. Abstract Factory might store a set of Prototypes from which to clone and return product objects.

-   Factory Method: creation through inheritance.
-   Prototype: creation through delegation.
-   Virtual constructor: defer choice of object to create until run-time.
```java
class Expression implements Cloneable{
    public String str;

    public Expression(String str) {
        this.str = str;
    }

    @Override
    public Expression clone() {
        Expression clone = null;
        try {
            clone = (Expression)super.clone();
        } catch (CloneNotSupportedException ex) {
            ex.printStackTrace();
        }
        return clone;
    }

    @Override
    public String toString() {
        return str;
    }
}

abstract class AbstractFactory {
    public Expression prototype;

    public Expression makePhase() {
        return prototype.clone();
    }

    public abstract Expression makeCompromise();

    public abstract Expression makeGrade();
}

class PCFactory extends AbstractFactory {

    public PCFactory() {
        prototype = new PCPhase();
    }

    @Override
    public Expression makeCompromise() {
        return new Expression("\"do it your way, any way, or no way\"");
    }

    @Override
    public Expression makeGrade() {
        return new Expression("\"you pass, self-esteem intact\"");
    }
}

class PCPhase extends Expression {
    private static int next = 0;
    private static final String[] list = {"\"animal companion\"", "\"vertically challenged\"",
            "\"factually inaccurate\"", "\"chronologically gifted\""};

    public PCPhase() {
        super(list[next]);
        next = (next + 1) % list.length;
    }

    @Override
    public Expression clone() {
        return new PCPhase();
    }
}

class NotPCPhase extends Expression {
    private static int next = 0;
    private static final String[] list = {"\"pet\"", "\"short\"", "\"lie\"", "\"old\""};

    public NotPCPhase() {
        super(list[next]);
        next = (next + 1) % list.length;
    }

    @Override
    public Expression clone() {
        return new NotPCPhase();
    }
}

class NotPCFactory extends AbstractFactory {

    public NotPCFactory() {
        prototype = new NotPCPhase();
    }

    @Override
    public Expression makeGrade() {
        return new Expression("\"my way, or the highway\"");
    }

    @Override
    public Expression makeCompromise() {
        return new Expression("\"take test, deal with the results\"");
    }
}

public class FactoryFmProto {
    public static void main(String[] args) {
        AbstractFactory factory;
        if (args.length  > 0) {
            factory = new PCFactory();
        } else {
            factory = new NotPCFactory();
        }
        for (int i = 0; i < 3; i++) {
            System.out.print(factory.makePhase() + " ");
        }
        System.out.println();
        System.out.println(factory.makeCompromise());
        System.out.println(factory.makeGrade());
    }
}
```

```java
// class CPU
abstract class CPU {}

// class EmberCPU
class EmberCPU extends CPU {}

// class EnginolaCPU
class EnginolaCPU extends CPU {}

// class MMU
abstract class MMU {}

// class EmberMMU
class EmberMMU extends MMU {}

// class EnginolaMMU
class EnginolaMMU extends MMU {}

// class EmberFactory
class EmberToolkit extends AbstractFactory {
    @Override
    public CPU createCPU() {
        return new EmberCPU();
    }

    @Override
    public MMU createMMU() {
        return new EmberMMU();
    }
}

// class EnginolaFactory
class EnginolaToolkit extends AbstractFactory {
    @Override
    public CPU createCPU() {
        return new EnginolaCPU();
    }

    @Override
    public MMU createMMU() {
        return new EnginolaMMU();
    }
}

enum Architecture {
    ENGINOLA, EMBER
}

abstract class AbstractFactory {
    private static final EmberToolkit EMBER_TOOLKIT = new EmberToolkit();
    private static final EnginolaToolkit ENGINOLA_TOOLKIT = new EnginolaToolkit();

    // Returns a concrete factory object that is an instance of the
    // concrete factory class appropriate for the given architecture.
    static AbstractFactory getFactory(Architecture architecture) {
        AbstractFactory factory = null;
        switch (architecture) {
            case ENGINOLA:
                factory = ENGINOLA_TOOLKIT;
                break;
            case EMBER:
                factory = EMBER_TOOLKIT;
                break;
        }
        return factory;
    }

    public abstract CPU createCPU();

    public abstract MMU createMMU();
}

public class Client {
    public static void main(String[] args) {
        AbstractFactory factory = AbstractFactory.getFactory(Architecture.EMBER);
        CPU cpu = factory.createCPU();
    }
}
```