---
layout: post
title: "Prototype Design Pattern"
description: "Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype. Co-opt one instance of a class for use as a breeder of all future instances. The  new  operator considered harmful."
date: 2020-02-06 13:07
tags: [디자인패턴]
comments: true
share: true
---

/ [Design Patterns](../2020-02-06-Design%20Patterns.md) / [Creational patterns](./2020-02-06-Creational%20patterns.md)

### Intent

-   Specify the kinds of objects to create using a prototypical instance, and create new objects by copying this prototype.
-   Co-opt one instance of a class for use as a breeder of all future instances.
-   The  `new`  operator considered harmful.

### Problem

Application "hard wires" the class of object to create in each "new" expression.

### Discussion

Declare an abstract base class that specifies a pure virtual "clone" method, and, maintains a dictionary of all "cloneable" concrete derived classes. Any class that needs a "polymorphic constructor" capability: derives itself from the abstract base class, registers its prototypical instance, and implements the  `clone()`  operation.

The client then, instead of writing code that invokes the "new" operator on a hard-wired class name, calls a "clone" operation on the abstract base class, supplying a string or enumerated data type that designates the particular concrete derived class desired.

### Structure

The Factory knows how to find the correct Prototype, and each Product knows how to spawn new instances of itself.

![Scheme of Prototype](https://sourcemaking.com/files/v2/content/patterns/Prototype.png)

### Example

The Prototype pattern specifies the kind of objects to create using a prototypical instance. Prototypes of new products are often built prior to full production, but in this example, the prototype is passive and does not participate in copying itself. The mitotic division of a cell - resulting in two identical cells - is an example of a prototype that plays an active role in copying itself and thus, demonstrates the Prototype pattern. When a cell splits, two cells of identical genotype result. In other words, the cell clones itself.

![Example of Prototype](https://sourcemaking.com/files/v2/content/patterns/Prototype_example1.png)

### Check list

1.  Add a  `clone()`  method to the existing "product" hierarchy.
2.  Design a "registry" that maintains a cache of prototypical objects. The registry could be encapsulated in a new  `Factory`  class, or in the base class of the "product" hierarchy.
3.  Design a factory method that: may (or may not) accept arguments, finds the correct prototype object, calls  `clone()`  on that object, and returns the result.
4.  The client replaces all references to the  `new`  operator with calls to the factory method.

### Rules of thumb

-   Sometimes creational patterns are competitors: there are cases when either Prototype or Abstract Factory could be used properly. At other times they are complementary: Abstract Factory might store a set of Prototypes from which to clone and return product objects. Abstract Factory, Builder, and Prototype can use Singleton in their implementations.
-   Abstract Factory classes are often implemented with Factory Methods, but they can be implemented using Prototype.
-   Factory Method: creation through inheritance. Prototype: creation through delegation.
-   Often, designs start out using Factory Method (less complicated, more customizable, subclasses proliferate) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, more complex) as the designer discovers where more flexibility is needed.
-   Prototype doesn't require subclassing, but it does require an "initialize" operation. Factory Method requires subclassing, but doesn't require Initialize.
-   Designs that make heavy use of the Composite and Decorator patterns often can benefit from Prototype as well.
-   Prototype co-opts one instance of a class for use as a breeder of all future instances.
-   Prototypes are useful when object initialization is expensive, and you anticipate few variations on the initialization parameters. In this context, Prototype can avoid expensive "creation from scratch", and support cheap cloning of a pre-initialized prototype.
-   Prototype is unique among the other creational patterns in that it doesn't require a class – only an object. Object-oriented languages like Self and Omega that do away with classes completely rely on prototypes for creating new objects.

### Code

#### Prototype design pattern

1.  Create a "contract" with  `clone()`  and  `getName()`  entries
2.  Design a "registry" that maintains a cache of prototypical objects
3.  Populate the registry with an  `initializePrototypes()`  function
4.  The registry has a  `findAndClone()`  "virtual constructor" that can transform a String into its correct object (it calls  `clone()`  which then calls "new")
5.  All classes relate themselves to the  `clone()`  contract
6.  Client uses the  `findAndClone()`  virtual ctor instead of the "new" operator

```java
// 1. The clone() contract
interface Prototype {
    Prototype clone();
    String getName();
    void execute();
}

class PrototypeModule {
    // 2. "registry" of prototypical objs
    private static List<Prototype> prototypes = new ArrayList<>();

    // Adds a feature to the Prototype attribute of the PrototypesModule class
    // obj  The feature to be added to the Prototype attribute
    public static void addPrototype(Prototype p) {
        prototypes.add(p);
    }

    public static Prototype createPrototype(String name) {
        // 4. The "virtual ctor"
        for (Prototype p : prototypes) {
            if (p.getName().equals(name)) {
                return p.clone();
            }
        }
        System.out.println(name + ": doesn't exist");
        return null;
    }
}

// 5. Sign-up for the clone() contract.
// Each class calls "new" on itself FOR the client.
class PrototypeAlpha implements Prototype {
    private String name = "AlphaVersion";

    @Override
    public Prototype clone() {
        return new PrototypeAlpha();
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void execute() {
        System.out.println(name + ": does something");
    }
}

class PrototypeBeta implements Prototype {
    private String name = "BetaVersion";

    @Override
    public Prototype clone() {
        return new PrototypeBeta();
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void execute() {
        System.out.println(name + ": does something");
    }
}

class ReleasePrototype implements Prototype {
    private String name = "ReleaseCandidate";
    @Override
    public Prototype clone() {
        return new ReleasePrototype();
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void execute() {
        System.out.println(name + ": does real work");
    }
}

public class PrototypeDemo {
    public static void main(String[] args) {
        if (args.length > 0) {
            initializePrototypes();
            List<Prototype> prototypes = new ArrayList<>();
            // 6. Client does not use "new"
            for (String protoName : args) {
                Prototype prototype = PrototypeModule.createPrototype(protoName);
                if (prototype != null) {
                    prototypes.add(prototype);
                }
            }
            for (Prototype p : prototypes) {
                p.execute();
            }
        } else {
            System.out.println("Run again with arguments of command string ");
        }
    }

    // 3. Populate the "registry"
    public static void initializePrototypes() {
        PrototypeModule.addPrototype(new PrototypeAlpha());
        PrototypeModule.addPrototype(new PrototypeBeta());
        PrototypeModule.addPrototype(new ReleasePrototype());
    }
}
```

Abstract Factory might store a set of Prototypes from which to clone and return product objects.
```java
interface Person {
    Person clone();
}

class Tom implements Person {
    private final String NAME = "Tom";

    @Override
    public Person clone() {
        return new Tom();
    }

    @Override
    public String toString() {
        return NAME;
    }
}

class Dick implements Person {
    private final String NAME = "Dick";

    @Override
    public Person clone() {
        return new Dick();
    }

    @Override
    public String toString() {
        return NAME;
    }
}

class Harry implements Person {
    private final String NAME = "Harry";

    @Override
    public Person clone() {
        return new Harry();
    }

    @Override
    public String toString() {
        return NAME;
    }
}

class Factory {
    private static final Map<String, Person> prototypes = new HashMap<>();

    static {
        prototypes.put("tom", new Tom());
        prototypes.put("dick", new Dick());
        prototypes.put("harry", new Harry());
    }

    public static Person getPrototype(String type) {
        try {
            return prototypes.get(type).clone();
        } catch (NullPointerException ex) {
            System.out.println("Prototype with name: " + type + ", doesn't exist");
            return null;
        }
    }
}

public class PrototypeFactory {
    public static void main(String[] args) {
        if (args.length > 0) {
            for (String type : args) {
                Person prototype = Factory.getPrototype(type);
                if (prototype != null) {
                    System.out.println(prototype);
                }
            }
        } else {
            System.out.println("Run again with arguments of command string ");
        }
    }
}
```