---
layout: post
title: "[Design Pattern] Flyweight"
description: "Flyweight is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object."
date: 2020-02-06 15:00
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://refactoring.guru/design-patterns)  /  [Structural Patterns](https://refactoring.guru/design-patterns/structural-patterns)

#### Also known as:  Cache

## Intent

**Flyweight**  is a structural design pattern that lets you fit more objects into the available amount of RAM by sharing common parts of state between multiple objects instead of keeping all of the data in each object.

![Flyweight design pattern](https://refactoring.guru/images/patterns/content/flyweight/flyweight.png)

## Problem

To have some fun after long working hours, you decided to create a simple video game: players would be moving around a map and shooting each other. You chose to implement a realistic particle system and make it a distinctive feature of the game. Vast quantities of bullets, missiles, and shrapnel from explosions should fly all over the map and deliver a thrilling experience to the player.

Upon its completion, you pushed the last commit, built the game and sent it to your friend for a test drive. Although the game was running flawlessly on your machine, your friend wasn’t able to play for long. On his computer, the game kept crashing after a few minutes of gameplay. After spending several hours digging through debug logs, you discovered that the game crashed because of an insufficient amount of RAM. It turned out that your friend’s rig was much less powerful than your own computer, and that’s why the problem emerged so quickly on his machine.

The actual problem was related to your particle system. Each particle, such as a bullet, a missile or a piece of shrapnel was represented by a separate object containing plenty of data. At some point, when the carnage on a player’s screen reached its climax, newly created particles no longer fit into the remaining RAM, so the program crashed.

![Flyweight pattern problem](https://refactoring.guru/images/patterns/diagrams/flyweight/problem-en.png)

## Solution

On closer inspection of the  `Particle`  class, you may notice that the color and  sprite  fields consume a lot more memory than other fields. What’s worse is that these two fields store almost identical data across all particles. For example, all bullets have the same color and sprite.

![Flyweight pattern solution](https://refactoring.guru/images/patterns/diagrams/flyweight/solution1-en.png)

Other parts of a particle’s state, such as coordinates, movement vector and speed, are unique to each particle. After all, the values of these fields change over time. This data represents the always changing context in which the particle exists, while the color and sprite remain constant for each particle.

This constant data of an object is usually called the  _intrinsic state_. It lives within the object; other objects can only read it, not change it. The rest of the object’s state, often altered “from the outside” by other objects, is called the  _extrinsic state_.

The Flyweight pattern suggests that you stop storing the extrinsic state inside the object. Instead, you should pass this state to specific methods which rely on it. Only the intrinsic state stays within the object, letting you reuse it in different contexts. As a result, you’d need fewer of these objects since they only differ in the intrinsic state, which has much fewer variations than the extrinsic.

![Flyweight pattern solution](https://refactoring.guru/images/patterns/diagrams/flyweight/solution3-en.png)

Let’s return to our game. Assuming that we had extracted the extrinsic state from our particle class, only three different objects would suffice to represent all particles in the game: a bullet, a missile, and a piece of shrapnel. As you’ve probably guessed by now, an object that only stores the intrinsic state is called  a flyweight.

#### Extrinsic state storage

Where does the extrinsic state move to? Some class should still store it, right? In most cases, it gets moved to the container object, which aggregates objects before we apply the pattern.

In our case, that’s the main  `Game`  object that stores all particles in the  `particles`  field. To move the extrinsic state into this class, you need to create several array fields for storing coordinates, vectors, and speed of each individual particle. But that’s not all. You need another array for storing references to a specific flyweight that represents a particle. These arrays must be in sync so that you can access all data of a particle using the same index.

![Flyweight pattern solution](https://refactoring.guru/images/patterns/diagrams/flyweight/solution2-en.png)

A more elegant solution is to create a separate context class that would store the extrinsic state along with reference to the flyweight object. This approach would require having just a single array in the container class.

Wait a second! Won’t we need to have as many of these contextual objects as we had at the very beginning? Technically, yes. But the thing is, these objects are much smaller than before. The most memory-consuming fields have been moved to just a few flyweight objects. Now, a thousand small contextual objects can reuse a single heavy flyweight object instead of storing a thousand copies of its data.

#### Flyweight and immutability

Since the same flyweight object can be used in different contexts, you have to make sure that its state can’t be modified. A flyweight should initialize its state just once, via constructor parameters. It shouldn’t expose any setters or public fields to other objects.

#### Flyweight factory

For more convenient access to various flyweights, you can create a factory method that manages a pool of existing flyweight objects. The method accepts the intrinsic state of the desired flyweight from a client, looks for an existing flyweight object matching this state, and returns it if it was found. If not, it creates a new flyweight and adds it to the pool.

There are several options where this method could be placed. The most obvious place is a flyweight container. Alternatively, you could create a new factory class. Or you could make the factory method static and put it inside an actual flyweight class.

## Structure

![Structure of the Flyweight design pattern](https://refactoring.guru/images/patterns/diagrams/flyweight/structure.png)

1.  The Flyweight pattern is merely an optimization. Before applying it, make sure your program does have the RAM consumption problem related to having a massive number of similar objects in memory at the same time. Make sure that this problem can’t be solved in any other meaningful way.
    
2.  The  **Flyweight**  class contains the portion of the original object’s state that can be shared between multiple objects. The same flyweight object can be used in many different contexts. The state stored inside a flyweight is called “intrinsic.” The state passed to the flyweight’s methods is called “extrinsic.”
    
3.  The  **Context**  class contains the extrinsic state, unique across all original objects. When a context is paired with one of the flyweight objects, it represents the full state of the original object.
    
4.  Usually, the behavior of the original object remains in the flyweight class. In this case, whoever calls a flyweight’s method must also pass appropriate bits of the extrinsic state into the method’s parameters. On the other hand, the behavior can be moved to the context class, which would use the linked flyweight merely as a data object.
    
5.  The  **Client**  calculates or stores the extrinsic state of flyweights. From the client’s perspective, a flyweight is a template object which can be configured at runtime by passing some contextual data into parameters of its methods.
    
6.  The  **Flyweight Factory**  manages a pool of existing flyweights. With the factory, clients don’t create flyweights directly. Instead, they call the factory, passing it bits of the intrinsic state of the desired flyweight. The factory looks over previously created flyweights and either returns an existing one that matches search criteria or creates a new one if nothing is found.
    

## Pseudocode

In this example, the  **Flyweight**  pattern helps to reduce memory usage when rendering millions of tree objects on a canvas.

![Flyweight pattern example](https://refactoring.guru/images/patterns/diagrams/flyweight/example.png)

The pattern extracts the repeating intrinsic state from a main  `Tree`  class and moves it into the flyweight class  `TreeType`.

Now instead of storing the same data in multiple objects, it’s kept in just a few flyweight objects and linked to appropriate  `Tree`  objects which act as contexts. The client code creates new tree objects using the flyweight factory, which encapsulates the complexity of searching for the right object and reusing it if needed.

```java
// The flyweight class contains a portion of the state of a
// tree. These fields store values that are unique for each
// particular tree. For instance, you won't find here the tree
// coordinates. But the texture and colors shared between many
// trees are here. Since this data is usually BIG, you'd waste a
// lot of memory by keeping it in each tree object. Instead, we
// can extract texture, color and other repeating data into a
// separate object which lots of individual tree objects can
// reference.
class TreeType is
    field name
    field color
    field texture
    constructor TreeType(name, color, texture) { ... }
    method draw(canvas, x, y) is
        // 1. Create a bitmap of a given type, color & texture.
        // 2. Draw the bitmap on the canvas at X and Y coords.

// Flyweight factory decides whether to re-use existing
// flyweight or to create a new object.
class TreeFactory is
    static field treeTypes: collection of tree types
    static method getTreeType(name, color, texture) is
        type = treeTypes.find(name, color, texture)
        if (type == null)
            type = new TreeType(name, color, texture)
            treeTypes.add(type)
        return type

// The contextual object contains the extrinsic part of the tree
// state. An application can create billions of these since they
// are pretty small: just two integer coordinates and one
// reference field.
class Tree is
    field x,y
    field type: TreeType
    constructor Tree(x, y, type) { ... }
    method draw(canvas) is
        type.draw(canvas, this.x, this.y)

// The Tree and the Forest classes are the flyweight's clients.
// You can merge them if you don't plan to develop the Tree
// class any further.
class Forest is
    field trees: collection of Trees

    method plantTree(x, y, name, color, texture) is
        type = TreeFactory.getTreeType(name, color, texture)
        tree = new Tree(x, y, type)
        trees.add(tree)

    method draw(canvas) is
        foreach (tree in trees) do
            tree.draw(canvas)
```

## Applicability

Use the Flyweight pattern only when your program must support a huge number of objects which barely fit into available RAM.

The benefit of applying the pattern depends heavily on how and where it’s used. It’s most useful when:

-   an application needs to spawn a huge number of similar objects
-   this drains all available RAM on a target device
-   the objects contain duplicate states which can be extracted and shared between multiple objects

## How to Implement

1.  Divide fields of a class that will become a flyweight into two parts:
    
    -   the intrinsic state: the fields that contain unchanging data duplicated across many objects
    -   the extrinsic state: the fields that contain contextual data unique to each object
2.  Leave the fields that represent the intrinsic state in the class, but make sure they’re immutable. They should take their initial values only inside the constructor.
    
3.  Go over methods that use fields of the extrinsic state. For each field used in the method, introduce a new parameter and use it instead of the field.
    
4.  Optionally, create a factory class to manage the pool of flyweights. It should check for an existing flyweight before creating a new one. Once the factory is in place, clients must only request flyweights through it. They should describe the desired flyweight by passing its intrinsic state to the factory.
    
5.  The client must store or calculate values of the extrinsic state (context) to be able to call methods of flyweight objects. For the sake of convenience, the extrinsic state along with the flyweight-referencing field may be moved to a separate context class.
    

## Pros and Cons

-   You can save lots of RAM, assuming your program has tons of similar objects.

-   You might be trading RAM over CPU cycles when some of the context data needs to be recalculated each time somebody calls a flyweight method.
-   The code becomes much more complicated. New team members will always be wondering why the state of an entity was separated in such a way.

## Relations with Other Patterns

-   You can implement shared leaf nodes of the  [Composite](https://refactoring.guru/design-patterns/composite)  tree as  [Flyweights](https://refactoring.guru/design-patterns/flyweight)  to save some RAM.
    
-   [Flyweight](https://refactoring.guru/design-patterns/flyweight)  shows how to make lots of little objects, whereas  [Facade](https://refactoring.guru/design-patterns/facade)  shows how to make a single object that represents an entire subsystem.
    
-   [Flyweight](https://refactoring.guru/design-patterns/flyweight)  would resemble  [Singleton](https://refactoring.guru/design-patterns/singleton)  if you somehow managed to reduce all shared states of the objects to just one flyweight object. But there are two fundamental differences between these patterns:
    
    1.  There should be only one Singleton instance, whereas a  _Flyweight_  class can have multiple instances with different intrinsic states.
    2.  The  _Singleton_  object can be mutable. Flyweight objects are immutable.

## Code Example
**Flyweight**  is a structural design pattern that allows programs to support vast quantities of objects by keeping their memory consumption low.

Pattern achieves it by sharing parts of object state between multiple objects. In other words, the Flyweight saves RAM by caching the same data used by different objects.

[Learn more about Flyweight](https://refactoring.guru/design-patterns/flyweight)

## Usage of the pattern in Java

**Complexity:**

**Popularity:**

**Usage examples:**  The Flyweight pattern has a single purpose: minimizing memory intake. If your program doesn’t struggle with a shortage of RAM, then you might just ignore this pattern for a while.

Examples of Flyweight in core Java libraries:

-   [`java.lang.Integer#valueOf(int)`](http://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html#valueOf-int-)  (also  [`Boolean`](http://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html#valueOf-boolean-),  [`Byte`](http://docs.oracle.com/javase/8/docs/api/java/lang/Byte.html#valueOf-byte-),  [`Character`](http://docs.oracle.com/javase/8/docs/api/java/lang/Character.html#valueOf-char-),  [`Short`](http://docs.oracle.com/javase/8/docs/api/java/lang/Short.html#valueOf-short-),  [`Long`](http://docs.oracle.com/javase/8/docs/api/java/lang/Long.html#valueOf-long-)  and  [`BigDecimal`](https://docs.oracle.com/javase/8/docs/api/java/math/BigDecimal.html#valueOf-long-int-))

**Identification:**  Flyweight can be recognized by a creation method that returns cached objects instead of creating new.

## Rendering a forest

In this example, we’re going to render a forest (1.000.000 trees)! Each tree will be represented by its own object that has some state (coordinates, texture and so on). Although the program does its primary job, naturally, it consumes a lot of RAM.

The reason is simple: too many tree objects contain duplicate data (name, texture, color). That’s why we can apply the Flyweight pattern and store these values inside separate flyweight objects (the  `TreeType`  class). Now, instead of storing the same data in thousands of  `Tree`  objects, we’re going to reference one of the flyweight objects with a particular set of values.

The client code isn’t going to notice anything since the complexity of reusing flyweight objects is buried inside a flyweight factory.

## [](https://refactoring.guru/design-patterns/flyweight/java/example#example-0--trees)**trees**

#### [](https://refactoring.guru/design-patterns/flyweight/java/example#example-0--trees-Tree-java)**trees/Tree.java:**  Contains state unique for each tree
```java
package refactoring_guru.flyweight.example.trees;

import java.awt.*;

public class Tree {
    private int x;
    private int y;
    private TreeType type;

    public Tree(int x, int y, TreeType type) {
        this.x = x;
        this.y = y;
        this.type = type;
    }

    public void draw(Graphics g) {
        type.draw(g, x, y);
    }
}
```
#### [](https://refactoring.guru/design-patterns/flyweight/java/example#example-0--trees-TreeType-java)**trees/TreeType.java:**  Contains state shared by several trees
```java
package refactoring_guru.flyweight.example.trees;

import java.awt.*;

public class TreeType {
    private String name;
    private Color color;
    private String otherTreeData;

    public TreeType(String name, Color color, String otherTreeData) {
        this.name = name;
        this.color = color;
        this.otherTreeData = otherTreeData;
    }

    public void draw(Graphics g, int x, int y) {
        g.setColor(Color.BLACK);
        g.fillRect(x - 1, y, 3, 5);
        g.setColor(color);
        g.fillOval(x - 5, y - 10, 10, 10);
    }
}
```
#### [](https://refactoring.guru/design-patterns/flyweight/java/example#example-0--trees-TreeFactory-java)**trees/TreeFactory.java:**  Encapsulates complexity of flyweight creation
```java
package refactoring_guru.flyweight.example.trees;

import java.awt.*;
import java.util.HashMap;
import java.util.Map;

public class TreeFactory {
    static Map<String, TreeType> treeTypes = new HashMap<>();

    public static TreeType getTreeType(String name, Color color, String otherTreeData) {
        TreeType result = treeTypes.get(name);
        if (result == null) {
            result = new TreeType(name, color, otherTreeData);
            treeTypes.put(name, result);
        }
        return result;
    }
}
```
## [](https://refactoring.guru/design-patterns/flyweight/java/example#example-0--forest)**forest**

#### [](https://refactoring.guru/design-patterns/flyweight/java/example#example-0--forest-Forest-java)**forest/Forest.java:**  Forest, which we draw
```java
package refactoring_guru.flyweight.example.forest;

import refactoring_guru.flyweight.example.trees.Tree;
import refactoring_guru.flyweight.example.trees.TreeFactory;
import refactoring_guru.flyweight.example.trees.TreeType;

import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.List;

public class Forest extends JFrame {
    private List<Tree> trees = new ArrayList<>();

    public void plantTree(int x, int y, String name, Color color, String otherTreeData) {
        TreeType type = TreeFactory.getTreeType(name, color, otherTreeData);
        Tree tree = new Tree(x, y, type);
        trees.add(tree);
    }

    @Override
    public void paint(Graphics graphics) {
        for (Tree tree : trees) {
            tree.draw(graphics);
        }
    }
}
```
#### [](https://refactoring.guru/design-patterns/flyweight/java/example#example-0--Demo-java)**Demo.java:**  Client code
```java
package refactoring_guru.flyweight.example;

import refactoring_guru.flyweight.example.forest.Forest;

import java.awt.*;

public class Demo {
    static int CANVAS_SIZE = 500;
    static int TREES_TO_DRAW = 1000000;
    static int TREE_TYPES = 2;

    public static void main(String[] args) {
        Forest forest = new Forest();
        for (int i = 0; i < Math.floor(TREES_TO_DRAW / TREE_TYPES); i++) {
            forest.plantTree(random(0, CANVAS_SIZE), random(0, CANVAS_SIZE),
                    "Summer Oak", Color.GREEN, "Oak texture stub");
            forest.plantTree(random(0, CANVAS_SIZE), random(0, CANVAS_SIZE),
                    "Autumn Oak", Color.ORANGE, "Autumn Oak texture stub");
        }
        forest.setSize(CANVAS_SIZE, CANVAS_SIZE);
        forest.setVisible(true);

        System.out.println(TREES_TO_DRAW + " trees drawn");
        System.out.println("---------------------");
        System.out.println("Memory usage:");
        System.out.println("Tree size (8 bytes) * " + TREES_TO_DRAW);
        System.out.println("+ TreeTypes size (~30 bytes) * " + TREE_TYPES + "");
        System.out.println("---------------------");
        System.out.println("Total: " + ((TREES_TO_DRAW * 8 + TREE_TYPES * 30) / 1024 / 1024) +
                "MB (instead of " + ((TREES_TO_DRAW * 38) / 1024 / 1024) + "MB)");
    }

    private static int random(int min, int max) {
        return min + (int) (Math.random() * ((max - min) + 1));
    }
}
```
#### [](https://refactoring.guru/design-patterns/flyweight/java/example#example-0--OutputDemo-png)**OutputDemo.png:**  Screenshot

![](https://refactoring.guru/images/patterns/examples/java/flyweight/OutputDemo.png)

#### [](https://refactoring.guru/design-patterns/flyweight/java/example#example-0--OutputDemo-txt)**OutputDemo.txt:**  RAM usage stats
```java
1000000 trees drawn
---------------------
Memory usage:
Tree size (8 bytes) * 1000000
+ TreeTypes size (~30 bytes) * 2
---------------------
Total: 7MB (instead of 36MB)
```