---
layout: post
title: "[Design Pattern] Composite"
description: "Composite is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects."
date: 2020-02-06 15:03
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://algamza.github.io/2020-02-06/Design-Patterns)  /  [Structural Patterns](https://algamza.github.io/2020-02-06/Structural-Design-Patterns)

#### Also known as:  Object Tree

## Intent

**Composite**  is a structural design pattern that lets you compose objects into tree structures and then work with these structures as if they were individual objects.

![Composite design pattern](https://refactoring.guru/images/patterns/content/composite/composite.png)

## Problem

Using the Composite pattern makes sense only when the core model of your app can be represented as a tree.

For example, imagine that you have two types of objects:  `Products`  and  `Boxes`. A  `Box`  can contain several  `Products`  as well as a number of smaller  `Boxes`. These little  `Boxes`  can also hold some  `Products`  or even smaller  `Boxes`, and so on.

Say you decide to create an ordering system that uses these classes. Orders could contain simple products without any wrapping, as well as boxes stuffed with products...and other boxes. How would you determine the total price of such an order?

![Structure of a complex order](https://refactoring.guru/images/patterns/diagrams/composite/problem-en.png)

An order might comprise various products, packaged in boxes, which are packaged in bigger boxes and so on. The whole structure looks like an upside down tree.

You could try the direct approach: unwrap all the boxes, go over all the products and then calculate the total. That would be doable in the real world; but in a program, it’s not as simple as running a loop. You have to know the classes of  `Products`  and  `Boxes`  you’re going through, the nesting level of the boxes and other nasty details beforehand. All of this makes the direct approach either too awkward or even impossible.

## Solution

The Composite pattern suggests that you work with  `Products`  and  `Boxes`  through a common interface which declares a method for calculating the total price.

How would this method work? For a product, it’d simply return the product’s price. For a box, it’d go over each item the box contains, ask its price and then return a total for this box. If one of these items were a smaller box, that box would also start going over its contents and so on, until the prices of all inner components were calculated. A box could even add some extra cost to the final price, such as packaging cost.

![Solution suggested by the Composite pattern](https://refactoring.guru/images/patterns/content/composite/composite-comic-1-en.png)

The Composite pattern lets you run a behavior recursively over all components of an object tree.

The greatest benefit of this approach is that you don’t need to care about the concrete classes of objects that compose the tree. You don’t need to know whether an object is a simple product or a sophisticated box. You can treat them all the same via the common interface. When you call a method, the objects themselves pass the request down the tree.

## Real-World Analogy

![An example of a military structure](https://refactoring.guru/images/patterns/diagrams/composite/live-example.png)

An example of a military structure.

Armies of most countries are structured as hierarchies. An army consists of several divisions; a division is a set of brigades, and a brigade consists of platoons, which can be broken down into squads. Finally, a squad is a small group of real soldiers. Orders are given at the top of the hierarchy and passed down onto each level until every soldier knows what needs to be done.

## Structure

![Structure of the Composite design pattern](https://refactoring.guru/images/patterns/diagrams/composite/structure-en.png)

1.  The  **Component**  interface describes operations that are common to both simple and complex elements of the tree.
    
2.  The  **Leaf**  is a basic element of a tree that doesn’t have sub-elements.
    
    Usually, leaf components end up doing most of the real work, since they don’t have anyone to delegate the work to.
    
3.  The  **Container**  (aka  _composite_) is an element that has sub-elements: leaves or other containers. A container doesn’t know the concrete classes of its children. It works with all sub-elements only via the component interface.
    
    Upon receiving a request, a container delegates the work to its sub-elements, processes intermediate results and then returns the final result to the client.
    
4.  The  **Client**  works with all elements through the component interface. As a result, the client can work in the same way with both simple or complex elements of the tree.
    

## Pseudocode

In this example, the  **Composite**  pattern lets you implement stacking of geometric shapes in a graphical editor.

![Structure of the Composite example](https://refactoring.guru/images/patterns/diagrams/composite/example.png)

The geometric shapes editor example.

The  `CompoundGraphic`  class is a container that can comprise any number of sub-shapes, including other compound shapes. A compound shape has the same methods as a simple shape. However, instead of doing something on its own, a compound shape passes the request recursively to all its children and “sums up” the result.

The client code works with all shapes through the single interface common to all shape classes. Thus, the client doesn’t know whether it’s working with a simple shape or a compound one. The client can work with very complex object structures without being coupled to concrete classes that form that structure.

```java
// The component interface declares common operations for both
// simple and complex objects of a composition.
interface Graphic is
    method move(x, y)
    method draw()

// The leaf class represents end objects of a composition. A
// leaf object can't have any sub-objects. Usually, it's leaf
// objects that do the actual work, while composite objects only
// delegate to their sub-components.
class Dot implements Graphic is
    field x, y

    constructor Dot(x, y) { ... }

    method move(x, y) is
        this.x += x, this.y += y

    method draw() is
        // Draw a dot at X and Y.

// All component classes can extend other components.
class Circle extends Dot is
    field radius

    constructor Circle(x, y, radius) { ... }

    method draw() is
        // Draw a circle at X and Y with radius R.

// The composite class represents complex components that may
// have children. Composite objects usually delegate the actual
// work to their children and then "sum up" the result.
class CompoundGraphic implements Graphic is
    field children: array of Graphic

    // A composite object can add or remove other components
    // (both simple or complex) to or from its child list.
    method add(child: Graphic) is
        // Add a child to the array of children.

    method remove(child: Graphic) is
        // Remove a child from the array of children.

    method move(x, y) is
        foreach (child in children) do
            child.move(x, y)

    // A composite executes its primary logic in a particular
    // way. It traverses recursively through all its children,
    // collecting and summing up their results. Since the
    // composite's children pass these calls to their own
    // children and so forth, the whole object tree is traversed
    // as a result.
    method draw() is
        // 1. For each child component:
        //     - Draw the component.
        //     - Update the bounding rectangle.
        // 2. Draw a dashed rectangle using the bounding
        // coordinates.

// The client code works with all the components via their base
// interface. This way the client code can support simple leaf
// components as well as complex composites.
class ImageEditor is
    method load() is
        all = new CompoundGraphic()
        all.add(new Dot(1, 2))
        all.add(new Circle(5, 3, 10))
        // ...

    // Combine selected components into one complex composite
    // component.
    method groupSelected(components: array of Graphic) is
        group = new CompoundGraphic()
        group.add(components)
        all.remove(components)
        all.add(group)
        // All components will be drawn.
        all.draw()
```

## Applicability

Use the Composite pattern when you have to implement a tree-like object structure.

The Composite pattern provides you with two basic element types that share a common interface: simple leaves and complex containers. A container can be composed of both leaves and other containers. This lets you construct a nested recursive object structure that resembles a tree.

Use the pattern when you want the client code to treat both simple and complex elements uniformly.

All elements defined by the Composite pattern share a common interface. Using this interface, the client doesn’t have to worry about the concrete class of the objects it works with.

## How to Implement

1.  Make sure that the core model of your app can be represented as a tree structure. Try to break it down into simple elements and containers. Remember that containers must be able to contain both simple elements and other containers.
    
2.  Declare the component interface with a list of methods that make sense for both simple and complex components.
    
3.  Create a leaf class to represent simple elements. A program may have multiple different leaf classes.
    
4.  Create a container class to represent complex elements. In this class, provide an array field for storing references to sub-elements. The array must be able to store both leaves and containers, so make sure it’s declared with the component interface type.
    
    While implementing the methods of the component interface, remember that a container is supposed to be delegating most of the work to sub-elements.
    
5.  Finally, define the methods for adding and removal of child elements in the container.
    
    Keep in mind that these operations can be declared in the component interface. This would violate the  _Interface Segregation Principle_  because the methods will be empty in the leaf class. However, the client will be able to treat all the elements equally, even when composing the tree.
    

## Pros and Cons

-   You can work with complex tree structures more conveniently: use polymorphism and recursion to your advantage.
-   _Open/Closed Principle_. You can introduce new element types into the app without breaking the existing code, which now works with the object tree.

-   It might be difficult to provide a common interface for classes whose functionality differs too much. In certain scenarios, you’d need to overgeneralize the component interface, making it harder to comprehend.

## Relations with Other Patterns

-   You can use  [Builder](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  when creating complex  [Composite](https://algamza.github.io/2020-02-06/Composite-Design-Pattern)  trees because you can program its construction steps to work recursively.
    
-   [Chain of Responsibility](https://algamza.github.io/2020-02-06/Chain-of-Responsibility-Design-Pattern)  is often used in conjunction with  [Composite](https://algamza.github.io/2020-02-06/Composite-Design-Pattern). In this case, when a leaf component gets a request, it may pass it through the chain of all of the parent components down to the root of the object tree.
    
-   You can use  [Iterators](https://algamza.github.io/2020-02-06/Iterator-Design-Pattern)  to traverse  [Composite](https://algamza.github.io/2020-02-06/Composite-Design-Pattern)  trees.
    
-   You can use  [Visitor](https://algamza.github.io/2020-02-06/Visitor-Design-Pattern)  to execute an operation over an entire  [Composite](https://algamza.github.io/2020-02-06/Composite-Design-Pattern)  tree.
    
-   You can implement shared leaf nodes of the  [Composite](https://algamza.github.io/2020-02-06/Composite-Design-Pattern)  tree as  [Flyweights](https://algamza.github.io/2020-02-06/Flyweight-Design-Pattern)  to save some RAM.
    
-   [Composite](https://algamza.github.io/2020-02-06/Composite-Design-Pattern)  and  [Decorator](https://algamza.github.io/2020-02-06/Decorator-Design-Pattern)  have similar structure diagrams since both rely on recursive composition to organize an open-ended number of objects.
    
    A  _Decorator_  is like a  _Composite_  but only has one child component. There’s another significant difference:  _Decorator_  adds additional responsibilities to the wrapped object, while  _Composite_  just “sums up” its children’s results.
    
    However, the patterns can also cooperate: you can use  _Decorator_  to extend the behavior of a specific object in the  _Composite_  tree.
    
-   Designs that make heavy use of  [Composite](https://algamza.github.io/2020-02-06/Composite-Design-Pattern)  and  [Decorator](https://algamza.github.io/2020-02-06/Decorator-Design-Pattern)  can often benefit from using  [Prototype](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern). Applying the pattern lets you clone complex structures instead of re-constructing them from scratch.

## Code Example
**Composite**  is a structural design pattern that allows composing objects into a tree-like structure and work with the it as if it was a singular object.

Composite became a pretty popular solution for the most problems that require building a tree structure. Composite’s great feature is the ability to run methods recursively over the whole tree structure and sum up the results.

[Learn more about Composite](https://algamza.github.io/2020-02-06/Composite-Design-Pattern)

## Usage of the pattern in Java

**Complexity:**

**Popularity:**

**Usage examples:**  The Composite pattern is pretty common in Java code. It’s often used to represent hierarchies of user interface components or the code that works with graphs.

Here are some composite examples from standard Java libraries:

-   [`java.awt.Container#add(Component)`](http://docs.oracle.com/javase/8/docs/api/java/awt/Container.html#add-java.awt.Component-)  (practically all over Swing components)
    
-   [`javax.faces.component.UIComponent#getChildren()`](http://docs.oracle.com/javaee/7/api/javax/faces/component/UIComponent.html#getChildren--)  (practically all over JSF UI components)
    

**Identification:**  The composite is easy to recognize by behavioral methods taking an instance of the same abstract/interface type into a tree structure.

## Simple and compound graphical shapes

This example shows how to create complex graphical shapes, composed of simpler shapes and treat both of them uniformly.

## [](https://algamza.github.io/2020-02-06/Composite-Design-Pattern/java/example#example-0--shapes)**shapes**

#### [](https://algamza.github.io/2020-02-06/Composite-Design-Pattern/java/example#example-0--shapes-Shape-java)**shapes/Shape.java:**  Common shape interface
```java
package refactoring_guru.composite.example.shapes;

import java.awt.*;

public interface Shape {
    int getX();
    int getY();
    int getWidth();
    int getHeight();
    void move(int x, int y);
    boolean isInsideBounds(int x, int y);
    void select();
    void unSelect();
    boolean isSelected();
    void paint(Graphics graphics);
}
```
#### [](https://algamza.github.io/2020-02-06/Composite-Design-Pattern/java/example#example-0--shapes-BaseShape-java)**shapes/BaseShape.java:**  Abstract shape with basic functionality
```java
package refactoring_guru.composite.example.shapes;

import java.awt.*;

abstract class BaseShape implements Shape {
    public int x;
    public int y;
    public Color color;
    private boolean selected = false;

    BaseShape(int x, int y, Color color) {
        this.x = x;
        this.y = y;
        this.color = color;
    }

    @Override
    public int getX() {
        return x;
    }

    @Override
    public int getY() {
        return y;
    }

    @Override
    public int getWidth() {
        return 0;
    }

    @Override
    public int getHeight() {
        return 0;
    }

    @Override
    public void move(int x, int y) {
        this.x += x;
        this.y += y;
    }

    @Override
    public boolean isInsideBounds(int x, int y) {
        return x > getX() && x < (getX() + getWidth()) &&
                y > getY() && y < (getY() + getHeight());
    }

    @Override
    public void select() {
        selected = true;
    }

    @Override
    public void unSelect() {
        selected = false;
    }

    @Override
    public boolean isSelected() {
        return selected;
    }

    void enableSelectionStyle(Graphics graphics) {
        graphics.setColor(Color.LIGHT_GRAY);

        Graphics2D g2 = (Graphics2D) graphics;
        float dash1[] = {2.0f};
        g2.setStroke(new BasicStroke(1.0f,
                BasicStroke.CAP_BUTT,
                BasicStroke.JOIN_MITER,
                2.0f, dash1, 0.0f));
    }

    void disableSelectionStyle(Graphics graphics) {
        graphics.setColor(color);
        Graphics2D g2 = (Graphics2D) graphics;
        g2.setStroke(new BasicStroke());
    }


    @Override
    public void paint(Graphics graphics) {
        if (isSelected()) {
            enableSelectionStyle(graphics);
        }
        else {
            disableSelectionStyle(graphics);
        }

        // ...
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Composite-Design-Pattern/java/example#example-0--shapes-Dot-java)**shapes/Dot.java:**  A dot
```java
package refactoring_guru.composite.example.shapes;

import java.awt.*;

public class Dot extends BaseShape {
    private final int DOT_SIZE = 3;

    public Dot(int x, int y, Color color) {
        super(x, y, color);
    }

    @Override
    public int getWidth() {
        return DOT_SIZE;
    }

    @Override
    public int getHeight() {
        return DOT_SIZE;
    }

    @Override
    public void paint(Graphics graphics) {
        super.paint(graphics);
        graphics.fillRect(x - 1, y - 1, getWidth(), getHeight());
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Composite-Design-Pattern/java/example#example-0--shapes-Circle-java)**shapes/Circle.java:**  A circle
```java
package refactoring_guru.composite.example.shapes;

import java.awt.*;

public class Circle extends BaseShape {
    public int radius;

    public Circle(int x, int y, int radius, Color color) {
        super(x, y, color);
        this.radius = radius;
    }

    @Override
    public int getWidth() {
        return radius * 2;
    }

    @Override
    public int getHeight() {
        return radius * 2;
    }

    public void paint(Graphics graphics) {
        super.paint(graphics);
        graphics.drawOval(x, y, getWidth() - 1, getHeight() - 1);
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Composite-Design-Pattern/java/example#example-0--shapes-Rectangle-java)**shapes/Rectangle.java:**  A rectangle
```java
package refactoring_guru.composite.example.shapes;

import java.awt.*;

public class Rectangle extends BaseShape {
    public int width;
    public int height;

    public Rectangle(int x, int y, int width, int height, Color color) {
        super(x, y, color);
        this.width = width;
        this.height = height;
    }

    @Override
    public int getWidth() {
        return width;
    }

    @Override
    public int getHeight() {
        return height;
    }

    @Override
    public void paint(Graphics graphics) {
        super.paint(graphics);
        graphics.drawRect(x, y, getWidth() - 1, getHeight() - 1);
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Composite-Design-Pattern/java/example#example-0--shapes-CompoundShape-java)**shapes/CompoundShape.java:**  Compound shape, which consists of other shape objects
```java
package refactoring_guru.composite.example.shapes;

import java.awt.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CompoundShape extends BaseShape {
    protected List<Shape> children = new ArrayList<>();

    public CompoundShape(Shape... components) {
        super(0, 0, Color.BLACK);
        add(components);
    }

    public void add(Shape component) {
        children.add(component);
    }

    public void add(Shape... components) {
        children.addAll(Arrays.asList(components));
    }

    public void remove(Shape child) {
        children.remove(child);
    }

    public void remove(Shape... components) {
        children.removeAll(Arrays.asList(components));
    }

    public void clear() {
        children.clear();
    }

    @Override
    public int getX() {
        if (children.size() == 0) {
            return 0;
        }
        int x = children.get(0).getX();
        for (Shape child : children) {
            if (child.getX() < x) {
                x = child.getX();
            }
        }
        return x;
    }

    @Override
    public int getY() {
        if (children.size() == 0) {
            return 0;
        }
        int y = children.get(0).getY();
        for (Shape child : children) {
            if (child.getY() < y) {
                y = child.getY();
            }
        }
        return y;
    }

    @Override
    public int getWidth() {
        int maxWidth = 0;
        int x = getX();
        for (Shape child : children) {
            int childsRelativeX = child.getX() - x;
            int childWidth = childsRelativeX + child.getWidth();
            if (childWidth > maxWidth) {
                maxWidth = childWidth;
            }
        }
        return maxWidth;
    }

    @Override
    public int getHeight() {
        int maxHeight = 0;
        int y = getY();
        for (Shape child : children) {
            int childsRelativeY = child.getY() - y;
            int childHeight = childsRelativeY + child.getHeight();
            if (childHeight > maxHeight) {
                maxHeight = childHeight;
            }
        }
        return maxHeight;
    }

    @Override
    public void move(int x, int y) {
        for (Shape child : children) {
            child.move(x, y);
        }
    }

    @Override
    public boolean isInsideBounds(int x, int y) {
        for (Shape child : children) {
            if (child.isInsideBounds(x, y)) {
                return true;
            }
        }
        return false;
    }

    @Override
    public void unSelect() {
        super.unSelect();
        for (Shape child : children) {
            child.unSelect();
        }
    }

    public boolean selectChildAt(int x, int y) {
        for (Shape child : children) {
            if (child.isInsideBounds(x, y)) {
                child.select();
                return true;
            }
        }
        return false;
    }

    @Override
    public void paint(Graphics graphics) {
        if (isSelected()) {
            enableSelectionStyle(graphics);
            graphics.drawRect(getX() - 1, getY() - 1, getWidth() + 1, getHeight() + 1);
            disableSelectionStyle(graphics);
        }

        for (refactoring_guru.composite.example.shapes.Shape child : children) {
            child.paint(graphics);
        }
    }
}
```
## [](https://algamza.github.io/2020-02-06/Composite-Design-Pattern/java/example#example-0--editor)**editor**

#### [](https://algamza.github.io/2020-02-06/Composite-Design-Pattern/java/example#example-0--editor-ImageEditor-java)**editor/ImageEditor.java:**  Shape editor
```java
package refactoring_guru.composite.example.editor;

import refactoring_guru.composite.example.shapes.CompoundShape;
import refactoring_guru.composite.example.shapes.Shape;

import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class ImageEditor {
    private EditorCanvas canvas;
    private CompoundShape allShapes = new CompoundShape();

    public ImageEditor() {
        canvas = new EditorCanvas();
    }

    public void loadShapes(Shape... shapes) {
        allShapes.clear();
        allShapes.add(shapes);
        canvas.refresh();
    }

    private class EditorCanvas extends Canvas {
        JFrame frame;

        private static final int PADDING = 10;

        EditorCanvas() {
            createFrame();
            refresh();
            addMouseListener(new MouseAdapter() {
                @Override
                public void mousePressed(MouseEvent e) {
                    allShapes.unSelect();
                    allShapes.selectChildAt(e.getX(), e.getY());
                    e.getComponent().repaint();
                }
            });
        }

        void createFrame() {
            frame = new JFrame();
            frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
            frame.setLocationRelativeTo(null);

            JPanel contentPanel = new JPanel();
            Border padding = BorderFactory.createEmptyBorder(PADDING, PADDING, PADDING, PADDING);
            contentPanel.setBorder(padding);
            frame.setContentPane(contentPanel);

            frame.add(this);
            frame.setVisible(true);
            frame.getContentPane().setBackground(Color.LIGHT_GRAY);
        }

        public int getWidth() {
            return allShapes.getX() + allShapes.getWidth() + PADDING;
        }

        public int getHeight() {
            return allShapes.getY() + allShapes.getHeight() + PADDING;
        }

        void refresh() {
            this.setSize(getWidth(), getHeight());
            frame.pack();
        }

        public void paint(Graphics graphics) {
            allShapes.paint(graphics);
        }
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Composite-Design-Pattern/java/example#example-0--Demo-java)**Demo.java:**  Client code
```java
package refactoring_guru.composite.example;

import refactoring_guru.composite.example.editor.ImageEditor;
import refactoring_guru.composite.example.shapes.Circle;
import refactoring_guru.composite.example.shapes.CompoundShape;
import refactoring_guru.composite.example.shapes.Dot;
import refactoring_guru.composite.example.shapes.Rectangle;

import java.awt.*;

public class Demo {
    public static void main(String[] args) {
        ImageEditor editor = new ImageEditor();

        editor.loadShapes(
                new Circle(10, 10, 10, Color.BLUE),

                new CompoundShape(
                    new Circle(110, 110, 50, Color.RED),
                    new Dot(160, 160, Color.RED)
                ),

                new CompoundShape(
                        new Rectangle(250, 250, 100, 100, Color.GREEN),
                        new Dot(240, 240, Color.GREEN),
                        new Dot(240, 360, Color.GREEN),
                        new Dot(360, 360, Color.GREEN),
                        new Dot(360, 240, Color.GREEN)
                )
        );
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Composite-Design-Pattern/java/example#example-0--OutputDemo-png)**OutputDemo.png:**  Execution result

![](https://refactoring.guru/images/patterns/examples/java/composite/OutputDemo.png)