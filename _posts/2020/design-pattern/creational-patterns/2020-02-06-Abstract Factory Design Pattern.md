---
layout: post
title: "[Design Pattern] Abstract Factory"
description: "Abstract Factory is a creational design pattern that lets you produce families of related objects without specifying their concrete classes."
date: 2020-02-06 13:02
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://algamza.github.io/2020-02-06/Design-Patterns)  /  [Creational Patterns](https://algamza.github.io/2020-02-06/Creational-Design-patterns)

## Intent

**Abstract Factory**  is a creational design pattern that lets you produce families of related objects without specifying their concrete classes.

![Abstract Factory pattern](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory.png)

## Problem

Imagine that you’re creating a furniture shop simulator. Your code consists of classes that represent:

1.  A family of related products, say:  `Chair`  +  `Sofa`  +  `CoffeeTable`.
    
2.  Several variants of this family. For example, products  `Chair`  +  `Sofa`  +  `CoffeeTable`  are available in these variants:  `Modern`,  `Victorian`,  `ArtDeco`.
    

![Product families and their variants.](https://refactoring.guru/images/patterns/diagrams/abstract-factory/problem-en.png)

Product families and their variants.

You need a way to create individual furniture objects so that they match other objects of the same family. Customers get quite mad when they receive non-matching furniture.

![](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-comic-1-en.png)

A Modern-style sofa doesn’t match Victorian-style chairs.

Also, you don’t want to change existing code when adding new products or families of products to the program. Furniture vendors update their catalogs very often, and you wouldn’t want to change the core code each time it happens.

## Solution

The first thing the Abstract Factory pattern suggests is to explicitly declare interfaces for each distinct product of the product family (e.g., chair, sofa or coffee table). Then you can make all variants of products follow those interfaces. For example, all chair variants can implement the  `Chair`  interface; all coffee table variants can implement the  `CoffeeTable`  interface, and so on.

![The Chairs class hierarchy](https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution1.png)

All variants of the same object must be moved to a single class hierarchy.

The next move is to declare the  _Abstract Factory_—an interface with a list of creation methods for all products that are part of the product family (for example,  `createChair`,  `createSofa`  and  `createCoffeeTable`). These methods must return  **abstract**  product types represented by the interfaces we extracted previously:  `Chair`,  `Sofa`,  `CoffeeTable`  and so on.

![The _Factories_ class hierarchy](https://refactoring.guru/images/patterns/diagrams/abstract-factory/solution2.png)

Each concrete factory corresponds to a specific product variant.

Now, how about the product variants? For each variant of a product family, we create a separate factory class based on the  `AbstractFactory`  interface. A factory is a class that returns products of a particular kind. For example, the  `ModernFurnitureFactory`  can only create  `ModernChair`,  `ModernSofa`  and  `ModernCoffeeTable`  objects.

The client code has to work with both factories and products via their respective abstract interfaces. This lets you change the type of a factory that you pass to the client code, as well as the product variant that the client code receives, without breaking the actual client code.

![](https://refactoring.guru/images/patterns/content/abstract-factory/abstract-factory-comic-2-en.png)

The client shouldn’t care about the concrete class of the factory it works with.

Say the client wants a factory to produce a chair. The client doesn’t have to be aware of the factory’s class, nor does it matter what kind of chair it gets. Whether it’s a Modern model or a Victorian-style chair, the client must treat all chairs in the same manner, using the abstract  `Chair`  interface. With this approach, the only thing that the client knows about the chair is that it implements the  `sitOn`  method in some way. Also, whichever variant of the chair is returned, it’ll always match the type of sofa or coffee table produced by the same factory object.

There’s one more thing left to clarify: if the client is only exposed to the abstract interfaces, what creates the actual factory objects? Usually, the application creates a concrete factory object at the initialization stage. Just before that, the app must select the factory type depending on the configuration or the environment settings.

## Structure

![Abstract Factory design pattern](https://refactoring.guru/images/patterns/diagrams/abstract-factory/structure.png)

1.  **Abstract Products**  declare interfaces for a set of distinct but related products which make up a product family.
    
2.  **Concrete Products**  are various implementations of abstract products, grouped by variants. Each abstract product (chair/sofa) must be implemented in all given variants (Victorian/Modern).
    
3.  The  **Abstract Factory**  interface declares a set of methods for creating each of the abstract products.
    
4.  **Concrete Factories**  implement creation methods of the abstract factory. Each concrete factory corresponds to a specific variant of products and creates only those product variants.
    
5.  Although concrete factories instantiate concrete products, signatures of their creation methods must return corresponding  _abstract_  products. This way the client code that uses a factory doesn’t get coupled to the specific variant of the product it gets from a factory. The  **Client**  can work with any concrete factory/product variant, as long as it communicates with their objects via abstract interfaces.
    

## Pseudocode

This example illustrates how the  **Abstract Factory**  pattern can be used for creating cross-platform UI elements without coupling the client code to concrete UI classes, while keeping all created elements consistent with a selected operating system.

![The class diagram for the Abstract Factory pattern example](https://refactoring.guru/images/patterns/diagrams/abstract-factory/example.png)

The cross-platform UI classes example.

The same UI elements in a cross-platform application are expected to behave similarly, but look a little bit different under different operating systems. Moreover, it’s your job to make sure that the UI elements match the style of the current operating system. You wouldn’t want your program to render macOS controls when it’s executed in Windows.

The Abstract Factory interface declares a set of creation methods that the client code can use to produce different types of UI elements. Concrete factories correspond to specific operating systems and create the UI elements that match that particular OS.

It works like this: when an application launches, it checks the type of the current operating system. The app uses this information to create a factory object from a class that matches the operating system. The rest of the code uses this factory to create UI elements. This prevents the wrong elements from being created.

With this approach, the client code doesn’t depend on concrete classes of factories and UI elements as long as it works with these objects via their abstract interfaces. This also lets the client code support other factories or UI elements that you might add in the future.

As a result, you don’t need to modify the client code each time you add a new variation of UI elements to your app. You just have to create a new factory class that produces these elements and slightly modify the app’s initialization code so it selects that class when appropriate.

```java
// The abstract factory interface declares a set of methods that
// return different abstract products. These products are called
// a family and are related by a high-level theme or concept.
// Products of one family are usually able to collaborate among
// themselves. A family of products may have several variants,
// but the products of one variant are incompatible with the
// products of another variant.
interface GUIFactory is
    method createButton():Button
    method createCheckbox():Checkbox

// Concrete factories produce a family of products that belong
// to a single variant. The factory guarantees that the
// resulting products are compatible. Signatures of the concrete
// factory's methods return an abstract product, while inside
// the method a concrete product is instantiated.
class WinFactory implements GUIFactory is
    method createButton():Button is
        return new WinButton()
    method createCheckbox():Checkbox is
        return new WinCheckbox()

// Each concrete factory has a corresponding product variant.
class MacFactory implements GUIFactory is
    method createButton():Button is
        return new MacButton()
    method createCheckbox():Checkbox is
        return new MacCheckbox()

// Each distinct product of a product family should have a base
// interface. All variants of the product must implement this
// interface.
interface Button is
    method paint()

// Concrete products are created by corresponding concrete
// factories.
class WinButton implements Button is
    method paint() is
        // Render a button in Windows style.

class MacButton implements Button is
    method paint() is
        // Render a button in macOS style.

// Here's the base interface of another product. All products
// can interact with each other, but proper interaction is
// possible only between products of the same concrete variant.
interface Checkbox is
    method paint()

class WinCheckbox implements Checkbox is
    method paint() is
        // Render a checkbox in Windows style.

class MacCheckbox implements Checkbox is
    method paint() is
        // Render a checkbox in macOS style.

// The client code works with factories and products only
// through abstract types: GUIFactory, Button and Checkbox. This
// lets you pass any factory or product subclass to the client
// code without breaking it.
class Application is
    private field factory: GUIFactory
    private field button: Button
    constructor Application(factory: GUIFactory) is
        this.factory = factory
    method createUI() is
        this.button = factory.createButton()
    method paint() is
        button.paint()

// The application picks the factory type depending on the
// current configuration or environment settings and creates it
// at runtime (usually at the initialization stage).
class ApplicationConfigurator is
    method main() is
        config = readApplicationConfigFile()

        if (config.OS == "Windows") then
            factory = new WinFactory()
        else if (config.OS == "Mac") then
            factory = new MacFactory()
        else
            throw new Exception("Error!  Unknown  operating  system.")

        Application app = new Application(factory)
```

## Applicability

Use the Abstract Factory when your code needs to work with various families of related products, but you don’t want it to depend on the concrete classes of those products—they might be unknown beforehand or you simply want to allow for future extensibility.

The Abstract Factory provides you with an interface for creating objects from each class of the product family. As long as your code creates objects via this interface, you don’t have to worry about creating the wrong variant of a product which doesn’t match the products already created by your app.

-   Consider implementing the Abstract Factory when you have a class with a set of  [Factory Methods](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern)  that blur its primary responsibility.
    
-   In a well-designed program  _each class is responsible only for one thing_. When a class deals with multiple product types, it may be worth extracting its factory methods into a stand-alone factory class or a full-blown Abstract Factory implementation.
    

## How to Implement

1.  Map out a matrix of distinct product types versus variants of these products.
    
2.  Declare abstract product interfaces for all product types. Then make all concrete product classes implement these interfaces.
    
3.  Declare the abstract factory interface with a set of creation methods for all abstract products.
    
4.  Implement a set of concrete factory classes, one for each product variant.
    
5.  Create factory initialization code somewhere in the app. It should instantiate one of the concrete factory classes, depending on the application configuration or the current environment. Pass this factory object to all classes that construct products.
    
6.  Scan through the code and find all direct calls to product constructors. Replace them with calls to the appropriate creation method on the factory object.
    

## Pros and Cons

-   You can be sure that the products you’re getting from a factory are compatible with each other.
-   You avoid tight coupling between concrete products and client code.
-   _Single Responsibility Principle_. You can extract the product creation code into one place, making the code easier to support.
-   _Open/Closed Principle_. You can introduce new variants of products without breaking existing client code.

-   The code may become more complicated than it should be, since a lot of new interfaces and classes are introduced along with the pattern.

## Relations with Other Patterns

-   Many designs start by using  [Factory Method](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern)  (less complicated and more customizable via subclasses) and evolve toward  [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern),  [Prototype](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern), or  [Builder](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  (more flexible, but more complicated).
    
-   [Builder](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  focuses on constructing complex objects step by step.  [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern)  specializes in creating families of related objects.  _Abstract Factory_  returns the product immediately, whereas  _Builder_  lets you run some additional construction steps before fetching the product.
    
-   [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern)  classes are often based on a set of  [Factory Methods](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern), but you can also use  [Prototype](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern)  to compose the methods on these classes.
    
-   [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern)  can serve as an alternative to  [Facade](https://algamza.github.io/2020-02-06/Facade-Design-Pattern)  when you only want to hide the way the subsystem objects are created from the client code.
    
-   You can use  [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern)  along with  [Bridge](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern). This pairing is useful when some abstractions defined by  _Bridge_  can only work with specific implementations. In this case,  _Abstract Factory_  can encapsulate these relations and hide the complexity from the client code.
    
-   [Abstract Factories](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern),  [Builders](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  and  [Prototypes](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern)  can all be implemented as  [Singletons](https://algamza.github.io/2020-02-06/Singleton-Design-Pattern).


## Code Example

**Abstract Factory**  is a creational design pattern, which solves the problem of creating entire product families without specifying their concrete classes.

Abstract Factory defines an interface for creating all distinct products but leaves the actual product creation to concrete factory classes. Each factory type corresponds to a certain product variety.

The client code calls the creation methods of a factory object instead of creating products directly with a constructor call (`new`  operator). Since a factory corresponds to a single product variant, all its products will be compatible.

Client code works with factories and products only through their abstract interfaces. It allows the same client code to work with different products. You just create a new concrete factory class and pass it to the client code.

> -   If you can’t figure out the difference between various factory patterns and concepts, then read our  [Factory Comparison](https://algamza.github.io/2020-02-06/Factory-Comparison).


[Learn more about Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern)

## Usage of the pattern in Java

**Complexity:**

**Popularity:**

**Usage examples:**  The Abstract Factory pattern is pretty common in Java code. Many frameworks and libraries use it to provide a way to extend and customize their standard components.

Here are some examples from core Java libraries:

-   [`javax.xml.parsers.DocumentBuilderFactory#newInstance()`](http://docs.oracle.com/javase/8/docs/api/javax/xml/parsers/DocumentBuilderFactory.html#newInstance--)
    
-   [`javax.xml.transform.TransformerFactory#newInstance()`](http://docs.oracle.com/javase/8/docs/api/javax/xml/transform/TransformerFactory.html#newInstance--)
    
-   [`javax.xml.xpath.XPathFactory#newInstance()`](http://docs.oracle.com/javase/8/docs/api/javax/xml/xpath/XPathFactory.html#newInstance--)
    

**Identification:**  The pattern is easy to recognize by methods, which return a factory object. Then, the factory is used for creating specific sub-components.

## Families of cross-platform GUI components and their production

In this example, buttons and checkboxes will act as products. They have two variants: macOS and Windows.

The abstract factory defines an interface for creating buttons and checkboxes. There are two concrete factories, which return both products in a single variant.

Client code works with factories and products using abstract interfaces. It makes the same client code working with many product variants, depending on the type of factory object.

## [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--buttons)**buttons:**  First product hierarchy

#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--buttons-Button-java)**buttons/Button.java**
```java
package algamza.abstract_factory.example.buttons;

/**
 * Abstract Factory assumes that you have several families of products,
 * structured into separate class hierarchies (Button/Checkbox). All products of
 * the same family have the common interface.
 *
 * This is the common interface for buttons family.
 */
public interface Button {
    void paint();
}
```
#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--buttons-MacOSButton-java)**buttons/MacOSButton.java**
```java
package algamza.abstract_factory.example.buttons;

/**
 * All products families have the same varieties (MacOS/Windows).
 *
 * This is a MacOS variant of a button.
 */
public class MacOSButton implements Button {

    @Override
    public void paint() {
        System.out.println("You have created MacOSButton.");
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--buttons-WindowsButton-java)**buttons/WindowsButton.java**
```java
package algamza.abstract_factory.example.buttons;

/**
 * All products families have the same varieties (MacOS/Windows).
 *
 * This is another variant of a button.
 */
public class WindowsButton implements Button {

    @Override
    public void paint() {
        System.out.println("You have created WindowsButton.");
    }
}
```
## [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--checkboxes)**checkboxes:**  Second product hierarchy

#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--checkboxes-Checkbox-java)**checkboxes/Checkbox.java**
```java
package algamza.abstract_factory.example.checkboxes;

/**
 * Checkboxes is the second product family. It has the same variants as buttons.
 */
public interface Checkbox {
    void paint();
}
```
#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--checkboxes-MacOSCheckbox-java)**checkboxes/MacOSCheckbox.java**
```java
package algamza.abstract_factory.example.checkboxes;

/**
 * All products families have the same varieties (MacOS/Windows).
 *
 * This is a variant of a checkbox.
 */
public class MacOSCheckbox implements Checkbox {

    @Override
    public void paint() {
        System.out.println("You have created MacOSCheckbox.");
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--checkboxes-WindowsCheckbox-java)**checkboxes/WindowsCheckbox.java**
```java
package algamza.abstract_factory.example.checkboxes;

/**
 * All products families have the same varieties (MacOS/Windows).
 *
 * This is another variant of a checkbox.
 */
public class WindowsCheckbox implements Checkbox {

    @Override
    public void paint() {
        System.out.println("You have created WindowsCheckbox.");
    }
}
```
## [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--factories)**factories**

#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--factories-GUIFactory-java)**factories/GUIFactory.java:**  Abstract factory
```java
package algamza.abstract_factory.example.factories;

import algamza.abstract_factory.example.buttons.Button;
import algamza.abstract_factory.example.checkboxes.Checkbox;

/**
 * Abstract factory knows about all (abstract) product types.
 */
public interface GUIFactory {
    Button createButton();
    Checkbox createCheckbox();
}
```
#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--factories-MacOSFactory-java)**factories/MacOSFactory.java:**  Concrete factory (macOS)
```java
package algamza.abstract_factory.example.factories;

import algamza.abstract_factory.example.buttons.Button;
import algamza.abstract_factory.example.buttons.MacOSButton;
import algamza.abstract_factory.example.checkboxes.Checkbox;
import algamza.abstract_factory.example.checkboxes.MacOSCheckbox;

/**
 * Each concrete factory extends basic factory and responsible for creating
 * products of a single variety.
 */
public class MacOSFactory implements GUIFactory {

    @Override
    public Button createButton() {
        return new MacOSButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new MacOSCheckbox();
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--factories-WindowsFactory-java)**factories/WindowsFactory.java:**  Concrete factory (Windows)
```java
package algamza.abstract_factory.example.factories;

import algamza.abstract_factory.example.buttons.Button;
import algamza.abstract_factory.example.buttons.WindowsButton;
import algamza.abstract_factory.example.checkboxes.Checkbox;
import algamza.abstract_factory.example.checkboxes.WindowsCheckbox;

/**
 * Each concrete factory extends basic factory and responsible for creating
 * products of a single variety.
 */
public class WindowsFactory implements GUIFactory {

    @Override
    public Button createButton() {
        return new WindowsButton();
    }

    @Override
    public Checkbox createCheckbox() {
        return new WindowsCheckbox();
    }
}
```
## [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--app)**app**

#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--app-Application-java)**app/Application.java:**  Client code
```java
package algamza.abstract_factory.example.app;

import algamza.abstract_factory.example.buttons.Button;
import algamza.abstract_factory.example.checkboxes.Checkbox;
import algamza.abstract_factory.example.factories.GUIFactory;

/**
 * Factory users don't care which concrete factory they use since they work with
 * factories and products through abstract interfaces.
 */
public class Application {
    private Button button;
    private Checkbox checkbox;

    public Application(GUIFactory factory) {
        button = factory.createButton();
        checkbox = factory.createCheckbox();
    }

    public void paint() {
        button.paint();
        checkbox.paint();
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--Demo-java)**Demo.java:**  App configuration
```java
package algamza.abstract_factory.example;

import algamza.abstract_factory.example.app.Application;
import algamza.abstract_factory.example.factories.GUIFactory;
import algamza.abstract_factory.example.factories.MacOSFactory;
import algamza.abstract_factory.example.factories.WindowsFactory;

/**
 * Demo class. Everything comes together here.
 */
public class Demo {

    /**
     * Application picks the factory type and creates it in run time (usually at
     * initialization stage), depending on the configuration or environment
     * variables.
     */
    private static Application configureApplication() {
        Application app;
        GUIFactory factory;
        String osName = System.getProperty("os.name").toLowerCase();
        if (osName.contains("mac")) {
            factory = new MacOSFactory();
            app = new Application(factory);
        } else {
            factory = new WindowsFactory();
            app = new Application(factory);
        }
        return app;
    }

    public static void main(String[] args) {
        Application app = configureApplication();
        app.paint();
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern/java/example#example-0--OutputDemo-txt)**OutputDemo.txt:**  Execution results
```java
You create WindowsButton.
You created WindowsCheckbox.
```