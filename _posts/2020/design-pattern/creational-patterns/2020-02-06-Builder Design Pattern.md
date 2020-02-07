---
layout: post
title: "[Design Pattern] Builder"
description: "Builder is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code."
date: 2020-02-06 13:03
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://algamza.github.io/2020-02-06/Design-Patterns)  /  [Creational Patterns](https://algamza.github.io/2020-02-06/Creational-Design-patterns)


## Intent

**Builder**  is a creational design pattern that lets you construct complex objects step by step. The pattern allows you to produce different types and representations of an object using the same construction code.

![Builder design pattern](https://refactoring.guru/images/patterns/content/builder/builder.png)

## Problem

Imagine a complex object that requires laborious, step-by-step initialization of many fields and nested objects. Such initialization code is usually buried inside a monstrous constructor with lots of parameters. Or even worse: scattered all over the client code.

![Lots of subclasses create another problem](https://refactoring.guru/images/patterns/diagrams/builder/problem1.png)

You might make the program too complex by creating a subclass for every possible configuration of an object.

For example, let’s think about how to create a  `House`  object. To build a simple house, you need to construct four walls and a floor, install a door, fit a pair of windows, and build a roof. But what if you want a bigger, brighter house, with a backyard and other goodies (like a heating system, plumbing, and electrical wiring)?

The simplest solution is to extend the base  `House`  class and create a set of subclasses to cover all combinations of the parameters. But eventually you’ll end up with a considerable number of subclasses. Any new parameter, such as the porch style, will require growing this hierarchy even more.

There’s another approach that doesn’t involve breeding subclasses. You can create a giant constructor right in the base  `House`  class with all possible parameters that control the house object. While this approach indeed eliminates the need for subclasses, it creates another problem.

![The telescopic constructor](https://refactoring.guru/images/patterns/diagrams/builder/problem2.png)

The constructor with lots of parameters has its downside: not all the parameters are needed at all times.

In most cases most of the parameters will be unused, making  [the constructor calls pretty ugly](https://refactoring.guru/smells/long-parameter-list). For instance, only a fraction of houses have swimming pools, so the parameters related to swimming pools will be useless nine times out of ten.

## Solution

The Builder pattern suggests that you extract the object construction code out of its own class and move it to separate objects called  _builders_.

![Applying the Builder pattern](https://refactoring.guru/images/patterns/diagrams/builder/solution1.png)

The Builder pattern lets you construct complex objects step by step. The Builder doesn’t allow other objects to access the product while it’s being built.

The pattern organizes object construction into a set of steps (`buildWalls`,  `buildDoor`, etc.). To create an object, you execute a series of these steps on a builder object. The important part is that you don’t need to call all of the steps. You can call only those steps that are necessary for producing a particular configuration of an object.

Some of the construction steps might require different implementation when you need to build various representations of the product. For example, walls of a cabin may be built of wood, but the castle walls must be built with stone.

In this case, you can create several different builder classes that implement the same set of building steps, but in a different manner. Then you can use these builders in the construction process (i.e., an ordered set of calls to the building steps) to produce different kinds of objects.

![](https://refactoring.guru/images/patterns/content/builder/builder-comic-1-en.png)

Different builders execute the same task in various ways.

For example, imagine a builder that builds everything from wood and glass, a second one that builds everything with stone and iron and a third one that uses gold and diamonds. By calling the same set of steps, you get a regular house from the first builder, a small castle from the second and a palace from the third. However, this would only work if the client code that calls the building steps is able to interact with builders using a common interface.

#### Director

You can go further and extract a series of calls to the builder steps you use to construct a product into a separate class called  _director_. The director class defines the order in which to execute the building steps, while the builder provides the implementation for those steps.

![](https://refactoring.guru/images/patterns/content/builder/builder-comic-2-en.png)

The director knows which building steps to execute to get a working product.

Having a director class in your program isn’t strictly necessary. You can always call the building steps in a specific order directly from the client code. However, the director class might be a good place to put various construction routines so you can reuse them across your program.

In addition, the director class completely hides the details of product construction from the client code. The client only needs to associate a builder with a director, launch the construction with the director, and get the result from the builder.

## Structure

![Structure of the Builder design pattern](https://refactoring.guru/images/patterns/diagrams/builder/structure.png)

1.  The  **Builder**  interface declares product construction steps that are common to all types of builders.
    
2.  **Concrete Builders**  provide different implementations of the construction steps. Concrete builders may produce products that don’t follow the common interface.
    
3.  **Products**  are resulting objects. Products constructed by different builders don’t have to belong to the same class hierarchy or interface.
    
4.  The  **Director**  class defines the order in which to call construction steps, so you can create and reuse specific configurations of products.
    
5.  The  **Client**  must associate one of the builder objects with the director. Usually, it’s done just once, via parameters of the director’s constructor. Then the director uses that builder object for all further construction. However, there’s an alternative approach for when the client passes the builder object to the production method of the director. In this case, you can use a different builder each time you produce something with the director.
    

## Pseudocode

This example of the  **Builder**  pattern illustrates how you can reuse the same object construction code when building different types of products, such as cars, and create the corresponding manuals for them.

![The structure of the Builder pattern example](https://refactoring.guru/images/patterns/diagrams/builder/example.png)

The example of step-by-step construction of cars and the user guides that fit those car models.

A car is a complex object that can be constructed in a hundred different ways. Instead of bloating the  `Car`  class with a huge constructor, we extracted the car assembly code into a separate car builder class. This class has a set of methods for configuring various parts of a car.

If the client code needs to assemble a special, fine-tuned model of a car, it can work with the builder directly. On the other hand, the client can delegate the assembly to the director class, which knows how to use a builder to construct several of the most popular models of cars.

You might be shocked, but every car needs a manual (seriously, who reads them?). The manual describes every feature of the car, so the details in the manuals vary across the different models. That’s why it makes sense to reuse an existing construction process for both real cars and their respective manuals. Of course, building a manual isn’t the same as building a car, and that’s why we must provide another builder class that specializes in composing manuals. This class implements the same building methods as its car-building sibling, but instead of crafting car parts, it describes them. By passing these builders to the same director object, we can construct either a car or a manual.

The final part is fetching the resulting object. A metal car and a paper manual, although related, are still very different things. We can’t place a method for fetching results in the director without coupling the director to concrete product classes. Hence, we obtain the result of the construction from the builder which performed the job.

```java
// Using the Builder pattern makes sense only when your products
// are quite complex and require extensive configuration. The
// following two products are related, although they don't have
// a common interface.
class Car is
    // A car can have a GPS, trip computer and some number of
    // seats. Different models of cars (sports car, SUV,
    // cabriolet) might have different features installed or
    // enabled.

class Manual is
    // Each car should have a user manual that corresponds to
    // the car's configuration and describes all its features.

// The builder interface specifies methods for creating the
// different parts of the product objects.
interface Builder is
    method reset()
    method setSeats(...)
    method setEngine(...)
    method setTripComputer(...)
    method setGPS(...)

// The concrete builder classes follow the builder interface and
// provide specific implementations of the building steps. Your
// program may have several variations of builders, each
// implemented differently.
class CarBuilder implements Builder is
    private field car:Car

    // A fresh builder instance should contain a blank product
    // object which it uses in further assembly.
    constructor CarBuilder() is
        this.reset()

    // The reset method clears the object being built.
    method reset() is
        this.car = new Car()

    // All production steps work with the same product instance.
    method setSeats(...) is
        // Set the number of seats in the car.

    method setEngine(...) is
        // Install a given engine.

    method setTripComputer(...) is
        // Install a trip computer.

    method setGPS(...) is
        // Install a global positioning system.

    // Concrete builders are supposed to provide their own
    // methods for retrieving results. That's because various
    // types of builders may create entirely different products
    // that don't all follow the same interface. Therefore such
    // methods can't be declared in the builder interface (at
    // least not in a statically-typed programming language).
    //
    // Usually, after returning the end result to the client, a
    // builder instance is expected to be ready to start
    // producing another product. That's why it's a usual
    // practice to call the reset method at the end of the
    // `getProduct` method body. However, this behavior isn't
    // mandatory, and you can make your builder wait for an
    // explicit reset call from the client code before disposing
    // of the previous result.
    method getProduct():Car is
        product = this.car
        this.reset()
        return product

// Unlike other creational patterns, builder lets you construct
// products that don't follow the common interface.
class CarManualBuilder implements Builder is
    private field manual:Manual

    constructor CarManualBuilder() is
        this.reset()

    method reset() is
        this.manual = new Manual()

    method setSeats(...) is
        // Document car seat features.

    method setEngine(...) is
        // Add engine instructions.

    method setTripComputer(...) is
        // Add trip computer instructions.

    method setGPS(...) is
        // Add GPS instructions.

    method getProduct():Manual is
        // Return the manual and reset the builder.

// The director is only responsible for executing the building
// steps in a particular sequence. It's helpful when producing
// products according to a specific order or configuration.
// Strictly speaking, the director class is optional, since the
// client can control builders directly.
class Director is
    private field builder:Builder

    // The director works with any builder instance that the
    // client code passes to it. This way, the client code may
    // alter the final type of the newly assembled product.
    method setBuilder(builder:Builder)
        this.builder = builder

    // The director can construct several product variations
    // using the same building steps.
    method constructSportsCar(builder: Builder) is
        builder.reset()
        builder.setSeats(2)
        builder.setEngine(new SportEngine())
        builder.setTripComputer(true)
        builder.setGPS(true)

    method constructSUV(builder: Builder) is
        // ...

// The client code creates a builder object, passes it to the
// director and then initiates the construction process. The end
// result is retrieved from the builder object.
class Application is

    method makeCar() is
        director = new Director()

        CarBuilder builder = new CarBuilder()
        director.constructSportsCar(builder)
        Car car = builder.getProduct()

        CarManualBuilder builder = new CarManualBuilder()
        director.constructSportsCar(builder)

        // The final product is often retrieved from a builder
        // object since the director isn't aware of and not
        // dependent on concrete builders and products.
        Manual manual = builder.getProduct()
```

## Applicability

Use the Builder pattern to get rid of a “telescopic constructor”.

Say you have a constructor with ten optional parameters. Calling such a beast is very inconvenient; therefore, you overload the constructor and create several shorter versions with fewer parameters. These constructors still refer to the main one, passing some default values into any omitted parameters.
```java
class Pizza {
    Pizza(int size) { ... }
    Pizza(int size, boolean cheese) { ... }
    Pizza(int size, boolean cheese, boolean pepperoni) { ... }
    // ...
```
Creating such a monster is only possible in languages that support method overloading, such as C# or Java.

The Builder pattern lets you build objects step by step, using only those steps that you really need. After implementing the pattern, you don’t have to cram dozens of parameters into your constructors anymore.

Use the Builder pattern when you want your code to be able to create different representations of some product (for example, stone and wooden houses).

The Builder pattern can be applied when construction of various representations of the product involves similar steps that differ only in the details.

The base builder interface defines all possible construction steps, and concrete builders implement these steps to construct particular representations of the product. Meanwhile, the director class guides the order of construction.

Use the Builder to construct  [Composite](https://algamza.github.io/2020-02-06/Composite-Design-Pattern)  trees or other complex objects.

The Builder pattern lets you construct products step-by-step. You could defer execution of some steps without breaking the final product. You can even call steps recursively, which comes in handy when you need to build an object tree.

A builder doesn’t expose the unfinished product while running construction steps. This prevents the client code from fetching an incomplete result.

## How to Implement

1.  Make sure that you can clearly define the common construction steps for building all available product representations. Otherwise, you won’t be able to proceed with implementing the pattern.
    
2.  Declare these steps in the base builder interface.
    
3.  Create a concrete builder class for each of the product representations and implement their construction steps.
    
    Don’t forget about implementing a method for fetching the result of the construction. The reason why this method can’t be declared inside the builder interface is that various builders may construct products that don’t have a common interface. Therefore, you don’t know what would be the return type for such a method. However, if you’re dealing with products from a single hierarchy, the fetching method can be safely added to the base interface.
    
4.  Think about creating a director class. It may encapsulate various ways to construct a product using the same builder object.
    
5.  The client code creates both the builder and the director objects. Before construction starts, the client must pass a builder object to the director. Usually, the client does this only once, via parameters of the director’s constructor. The director uses the builder object in all further construction. There’s an alternative approach, where the builder is passed directly to the construction method of the director.
    
6.  The construction result can be obtained directly from the director only if all products follow the same interface. Otherwise, the client should fetch the result from the builder.
    

## Pros and Cons

-   You can construct objects step-by-step, defer construction steps or run steps recursively.
-   You can reuse the same construction code when building various representations of products.
-   _Single Responsibility Principle_. You can isolate complex construction code from the business logic of the product.

-   The overall complexity of the code increases since the pattern requires creating multiple new classes.

## Relations with Other Patterns

-   Many designs start by using  [Factory Method](https://algamza.github.io/2020-02-06/Factory-Method-Design-Pattern)  (less complicated and more customizable via subclasses) and evolve toward  [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern),  [Prototype](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern), or  [Builder](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  (more flexible, but more complicated).
    
-   [Builder](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  focuses on constructing complex objects step by step.  [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern)  specializes in creating families of related objects.  _Abstract Factory_  returns the product immediately, whereas  _Builder_  lets you run some additional construction steps before fetching the product.
    
-   You can use  [Builder](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  when creating complex  [Composite](https://algamza.github.io/2020-02-06/Composite-Design-Pattern)  trees because you can program its construction steps to work recursively.
    
-   You can combine  [Builder](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  with  [Bridge](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern): the  _director_  class plays the role of the abstraction, while different  _builders_  act as  _implementations_.
    
-   [Abstract Factories](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern),  [Builders](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  and  [Prototypes](https://algamza.github.io/2020-02-06/Prototype-Design-Pattern)  can all be implemented as  [Singletons](https://algamza.github.io/2020-02-06/Singleton-Design-Pattern).

## Code Example

**Builder**  is a creational design pattern, which allows constructing complex objects step by step.

Unlike other creational patterns, Builder doesn’t require products to have a common interface. That makes it possible to produce different products using the same construction process.

[Learn more about Builder](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)

## Usage of the pattern in Java

**Complexity:**

**Popularity:**

**Usage examples:**  The Builder pattern is a well-known pattern in Java world. It’s especially useful when you need to create an object with lots of possible configuration options.

Builder is widely used in Java core libraries:

-   [`java.lang.StringBuilder#append()`](http://docs.oracle.com/javase/8/docs/api/java/lang/StringBuilder.html#append-boolean-)  (`unsynchronized`)
-   [`java.lang.StringBuffer#append()`](http://docs.oracle.com/javase/8/docs/api/java/lang/StringBuffer.html#append-boolean-)  (`synchronized`)
-   [`java.nio.ByteBuffer#put()`](http://docs.oracle.com/javase/8/docs/api/java/nio/ByteBuffer.html#put-byte-)  (also in  [`CharBuffer`](http://docs.oracle.com/javase/8/docs/api/java/nio/CharBuffer.html#put-char-),  [`ShortBuffer`](http://docs.oracle.com/javase/8/docs/api/java/nio/ShortBuffer.html#put-short-),  [`IntBuffer`](http://docs.oracle.com/javase/8/docs/api/java/nio/IntBuffer.html#put-int-),  [`LongBuffer`](http://docs.oracle.com/javase/8/docs/api/java/nio/LongBuffer.html#put-long-),  [`FloatBuffer`](http://docs.oracle.com/javase/8/docs/api/java/nio/FloatBuffer.html#put-float-)  and  [`DoubleBuffer`](http://docs.oracle.com/javase/8/docs/api/java/nio/DoubleBuffer.html#put-double-))
-   [`javax.swing.GroupLayout.Group#addComponent()`](http://docs.oracle.com/javase/8/docs/api/javax/swing/GroupLayout.Group.html#addComponent-java.awt.Component-)
-   All implementations  [`java.lang.Appendable`](http://docs.oracle.com/javase/8/docs/api/java/lang/Appendable.html)

**Identification:**  The Builder pattern can be recognized in class, which has a single creation method and several methods to configure the resulting object. Builder methods often support chaining (for example,  `someBuilder->setValueA(1)->setValueB(2)->create()`).

## Step-by-step car production

In this example, the Builder pattern allows step by step construction of different car models.

The example also shows how Builder produces products of different kinds (car manual) using the same building steps.

The Director controls the order of the construction. It knows which building steps to call to produce this or that car model. It works with builders only via their common interface. This allows passing different types of builders to the director.

The end result is retrieved from the builder object because the director can’t know the type of resulting product. Only the Builder object knows what exactly does it builds.

## [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--builders)**builders**

#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--builders-Builder-java)**builders/Builder.java:**  Common builder interface
```java
package algamza.builder.example.builders;

import algamza.builder.example.cars.Type;
import algamza.builder.example.components.Engine;
import algamza.builder.example.components.GPSNavigator;
import algamza.builder.example.components.Transmission;
import algamza.builder.example.components.TripComputer;

/**
 * Builder interface defines all possible ways to configure a product.
 */
public interface Builder {
    void setType(Type type);
    void setSeats(int seats);
    void setEngine(Engine engine);
    void setTransmission(Transmission transmission);
    void setTripComputer(TripComputer tripComputer);
    void setGPSNavigator(GPSNavigator gpsNavigator);
}
```
#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--builders-CarBuilder-java)**builders/CarBuilder.java:**  Builder of car
```java
package algamza.builder.example.builders;

import algamza.builder.example.cars.Car;
import algamza.builder.example.cars.Type;
import algamza.builder.example.components.Engine;
import algamza.builder.example.components.GPSNavigator;
import algamza.builder.example.components.Transmission;
import algamza.builder.example.components.TripComputer;

/**
 * Concrete builders implement steps defined in the common interface.
 */
public class CarBuilder implements Builder {
    private Type type;
    private int seats;
    private Engine engine;
    private Transmission transmission;
    private TripComputer tripComputer;
    private GPSNavigator gpsNavigator;

    @Override
    public void setType(Type type) {
        this.type = type;
    }

    @Override
    public void setSeats(int seats) {
        this.seats = seats;
    }

    @Override
    public void setEngine(Engine engine) {
        this.engine = engine;
    }

    @Override
    public void setTransmission(Transmission transmission) {
        this.transmission = transmission;
    }

    @Override
    public void setTripComputer(TripComputer tripComputer) {
        this.tripComputer = tripComputer;
    }

    @Override
    public void setGPSNavigator(GPSNavigator gpsNavigator) {
        this.gpsNavigator = gpsNavigator;
    }

    public Car getResult() {
        return new Car(type, seats, engine, transmission, tripComputer, gpsNavigator);
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--builders-CarManualBuilder-java)**builders/CarManualBuilder.java:**  Builder of a car manual
```java
package algamza.builder.example.builders;

import algamza.builder.example.cars.Manual;
import algamza.builder.example.cars.Type;
import algamza.builder.example.components.Engine;
import algamza.builder.example.components.GPSNavigator;
import algamza.builder.example.components.Transmission;
import algamza.builder.example.components.TripComputer;

/**
 * Unlike other creational patterns, Builder can construct unrelated products,
 * which don't have the common interface.
 *
 * In this case we build a user manual for a car, using the same steps as we
 * built a car. This allows to produce manuals for specific car models,
 * configured with different features.
 */
public class CarManualBuilder implements Builder{
    private Type type;
    private int seats;
    private Engine engine;
    private Transmission transmission;
    private TripComputer tripComputer;
    private GPSNavigator gpsNavigator;

    @Override
    public void setType(Type type) {
        this.type = type;
    }

    @Override
    public void setSeats(int seats) {
        this.seats = seats;
    }

    @Override
    public void setEngine(Engine engine) {
        this.engine = engine;
    }

    @Override
    public void setTransmission(Transmission transmission) {
        this.transmission = transmission;
    }

    @Override
    public void setTripComputer(TripComputer tripComputer) {
        this.tripComputer = tripComputer;
    }

    @Override
    public void setGPSNavigator(GPSNavigator gpsNavigator) {
        this.gpsNavigator = gpsNavigator;
    }

    public Manual getResult() {
        return new Manual(type, seats, engine, transmission, tripComputer, gpsNavigator);
    }
}
```
## [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--cars)**cars**

#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--cars-Car-java)**cars/Car.java:**  Car product
```java
package algamza.builder.example.cars;

import algamza.builder.example.components.Engine;
import algamza.builder.example.components.GPSNavigator;
import algamza.builder.example.components.Transmission;
import algamza.builder.example.components.TripComputer;

/**
 * Car is a product class.
 */
public class Car {
    private final Type type;
    private final int seats;
    private final Engine engine;
    private final Transmission transmission;
    private final TripComputer tripComputer;
    private final GPSNavigator gpsNavigator;
    private double fuel = 0;

    public Car(Type type, int seats, Engine engine, Transmission transmission,
               TripComputer tripComputer, GPSNavigator gpsNavigator) {
        this.type = type;
        this.seats = seats;
        this.engine = engine;
        this.transmission = transmission;
        this.tripComputer = tripComputer;
        this.tripComputer.setCar(this);
        this.gpsNavigator = gpsNavigator;
    }

    public Type getType() {
        return type;
    }

    public double getFuel() {
        return fuel;
    }

    public void setFuel(double fuel) {
        this.fuel = fuel;
    }

    public int getSeats() {
        return seats;
    }

    public Engine getEngine() {
        return engine;
    }

    public Transmission getTransmission() {
        return transmission;
    }

    public TripComputer getTripComputer() {
        return tripComputer;
    }

    public GPSNavigator getGpsNavigator() {
        return gpsNavigator;
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--cars-Manual-java)**cars/Manual.java:**  Manual product
```java
package algamza.builder.example.cars;

import algamza.builder.example.components.Engine;
import algamza.builder.example.components.GPSNavigator;
import algamza.builder.example.components.Transmission;
import algamza.builder.example.components.TripComputer;

/**
 * Car manual is another product. Note that it does not have the same ancestor
 * as a Car. They are not related.
 */
public class Manual {
    private final Type type;
    private final int seats;
    private final Engine engine;
    private final Transmission transmission;
    private final TripComputer tripComputer;
    private final GPSNavigator gpsNavigator;

    public Manual(Type type, int seats, Engine engine, Transmission transmission,
                  TripComputer tripComputer, GPSNavigator gpsNavigator) {
        this.type = type;
        this.seats = seats;
        this.engine = engine;
        this.transmission = transmission;
        this.tripComputer = tripComputer;
        this.gpsNavigator = gpsNavigator;
    }

    public String print() {
        String info = "";
        info += "Type of car: " + type + "\n";
        info += "Count of seats: " + seats + "\n";
        info += "Engine: volume - " + engine.getVolume() + "; mileage - " + engine.getMileage() + "\n";
        info += "Transmission: " + transmission + "\n";
        if (this.tripComputer != null) {
            info += "Trip Computer: Functional" + "\n";
        } else {
            info += "Trip Computer: N/A" + "\n";
        }
        if (this.gpsNavigator != null) {
            info += "GPS Navigator: Functional" + "\n";
        } else {
            info += "GPS Navigator: N/A" + "\n";
        }
        return info;
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--cars-Type-java)**cars/Type.java**
```java
package algamza.builder.example.cars;

public enum Type {
    CITY_CAR, SPORTS_CAR, SUV
}
```
## [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--components)**components**

#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--components-Engine-java)**components/Engine.java:**  Product feature 1
```java
package algamza.builder.example.components;

/**
 * Just another feature of a car.
 */
public class Engine {
    private final double volume;
    private double mileage;
    private boolean started;

    public Engine(double volume, double mileage) {
        this.volume = volume;
        this.mileage = mileage;
    }

    public void on() {
        started = true;
    }

    public void off() {
        started = false;
    }

    public boolean isStarted() {
        return started;
    }

    public void go(double mileage) {
        if (started) {
            this.mileage += mileage;
        } else {
            System.err.println("Cannot go(), you must start engine first!");
        }
    }

    public double getVolume() {
        return volume;
    }

    public double getMileage() {
        return mileage;
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--components-GPSNavigator-java)**components/GPSNavigator.java:**  Product feature 2
```java
package algamza.builder.example.components;

/**
 * Just another feature of a car.
 */
public class GPSNavigator {
    private String route;

    public GPSNavigator() {
        this.route = "221b, Baker Street, London  to Scotland Yard, 8-10 Broadway, London";
    }

    public GPSNavigator(String manualRoute) {
        this.route = manualRoute;
    }

    public String getRoute() {
        return route;
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--components-Transmission-java)**components/Transmission.java:**  Product feature 3
```java
package algamza.builder.example.components;

/**
 * Just another feature of a car.
 */
public enum Transmission {
    SINGLE_SPEED, MANUAL, AUTOMATIC, SEMI_AUTOMATIC
}
```
#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--components-TripComputer-java)**components/TripComputer.java:**  Product feature 4
```java
package algamza.builder.example.components;

import algamza.builder.example.cars.Car;

/**
 * Just another feature of a car.
 */
public class TripComputer {

    private Car car;

    public void setCar(Car car) {
        this.car = car;
    }

    public void showFuelLevel() {
        System.out.println("Fuel level: " + car.getFuel());
    }

    public void showStatus() {
        if (this.car.getEngine().isStarted()) {
            System.out.println("Car is started");
        } else {
            System.out.println("Car isn't started");
        }
    }
}
```
## [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--director)**director**

#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--director-Director-java)**director/Director.java:**  Director controls builders
```java
package algamza.builder.example.director;

import algamza.builder.example.builders.Builder;
import algamza.builder.example.cars.Type;
import algamza.builder.example.components.Engine;
import algamza.builder.example.components.GPSNavigator;
import algamza.builder.example.components.Transmission;
import algamza.builder.example.components.TripComputer;

/**
 * Director defines the order of building steps. It works with a builder object
 * through common Builder interface. Therefore it may not know what product is
 * being built.
 */
public class Director {

    public void constructSportsCar(Builder builder) {
        builder.setType(Type.SPORTS_CAR);
        builder.setSeats(2);
        builder.setEngine(new Engine(3.0, 0));
        builder.setTransmission(Transmission.SEMI_AUTOMATIC);
        builder.setTripComputer(new TripComputer());
        builder.setGPSNavigator(new GPSNavigator());
    }

    public void constructCityCar(Builder builder) {
        builder.setType(Type.CITY_CAR);
        builder.setSeats(2);
        builder.setEngine(new Engine(1.2, 0));
        builder.setTransmission(Transmission.AUTOMATIC);
        builder.setTripComputer(new TripComputer());
        builder.setGPSNavigator(new GPSNavigator());
    }

    public void constructSUV(Builder builder) {
        builder.setType(Type.SUV);
        builder.setSeats(4);
        builder.setEngine(new Engine(2.5, 0));
        builder.setTransmission(Transmission.MANUAL);
        builder.setGPSNavigator(new GPSNavigator());
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--Demo-java)**Demo.java:**  Client code
```java
package algamza.builder.example;

import algamza.builder.example.builders.CarBuilder;
import algamza.builder.example.builders.CarManualBuilder;
import algamza.builder.example.cars.Car;
import algamza.builder.example.cars.Manual;
import algamza.builder.example.director.Director;

/**
 * Demo class. Everything comes together here.
 */
public class Demo {

    public static void main(String[] args) {
        Director director = new Director();

        // Director gets the concrete builder object from the client
        // (application code). That's because application knows better which
        // builder to use to get a specific product.
        CarBuilder builder = new CarBuilder();
        director.constructSportsCar(builder);

        // The final product is often retrieved from a builder object, since
        // Director is not aware and not dependent on concrete builders and
        // products.
        Car car = builder.getResult();
        System.out.println("Car built:\n" + car.getType());


        CarManualBuilder manualBuilder = new CarManualBuilder();

        // Director may know several building recipes.
        director.constructSportsCar(manualBuilder);
        Manual carManual = manualBuilder.getResult();
        System.out.println("\nCar manual built:\n" + carManual.print());
    }

}
```
#### [](https://algamza.github.io/2020-02-06/Builder-Design-Pattern/java/example#example-0--OutputDemo-txt)**OutputDemo.txt:**  Execution results
```java
Car built:
SPORTS_CAR

Car manual built:
Type of car: SPORTS_CAR
Count of seats: 2
Engine: volume - 3.0; mileage - 0.0
Transmission: SEMI_AUTOMATIC
Trip Computer: Functional
GPS Navigator: Functional
```