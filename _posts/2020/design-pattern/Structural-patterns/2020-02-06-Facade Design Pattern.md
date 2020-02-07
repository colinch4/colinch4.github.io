---
layout: post
title: "[Design Pattern] Facade"
description: "Facade is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes."
date: 2020-02-06 15:05
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://refactoring.guru/design-patterns)  /  [Structural Patterns](https://refactoring.guru/design-patterns/structural-patterns)

## Intent

**Facade**  is a structural design pattern that provides a simplified interface to a library, a framework, or any other complex set of classes.

![Facade design pattern](https://refactoring.guru/images/patterns/content/facade/facade.png)

## Problem

Imagine that you must make your code work with a broad set of objects that belong to a sophisticated library or framework. Ordinarily, you’d need to initialize all of those objects, keep track of dependencies, execute methods in the correct order, and so on.

As a result, the business logic of your classes would become tightly coupled to the implementation details of 3rd-party classes, making it hard to comprehend and maintain.

## Solution

A facade is a class that provides a simple interface to a complex subsystem which contains lots of moving parts. A facade might provide limited functionality in comparison to working with the subsystem directly. However, it includes only those features that clients really care about.

Having a facade is handy when you need to integrate your app with a sophisticated library that has dozens of features, but you just need a tiny bit of its functionality.

For instance, an app that uploads short funny videos with cats to social media could potentially use a professional video conversion library. However, all that it really needs is a class with the single method  `encode(filename, format)`. After creating such a class and connecting it with the video conversion library, you’ll have your first facade.

## Real-World Analogy

![An example of taking a phone order](https://refactoring.guru/images/patterns/diagrams/facade/live-example-en.png)

Placing orders by phone.

When you call a shop to place a phone order, an operator is your facade to all services and departments of the shop. The operator provides you with a simple voice interface to the ordering system, payment gateways, and various delivery services.

## Structure

![Structure of the Facade design pattern](https://refactoring.guru/images/patterns/diagrams/facade/structure.png)

1.  The  **Facade**  provides convenient access to a particular part of the subsystem’s functionality. It knows where to direct the client’s request and how to operate all the moving parts.
    
2.  An  **Additional Facade**  class can be created to prevent polluting a single facade with unrelated features that might make it yet another complex structure. Additional facades can be used by both clients and other facades.
    
3.  The  **Complex Subsystem**  consists of dozens of various objects. To make them all do something meaningful, you have to dive deep into the subsystem’s implementation details, such as initializing objects in the correct order and supplying them with data in the proper format.
    
    Subsystem classes aren’t aware of the facade’s existence. They operate within the system and work with each other directly.
    
4.  The  **Client**  uses the facade instead of calling the subsystem objects directly.
    

## Pseudocode

In this example, the  **Facade**  pattern simplifies interaction with a complex video conversion framework.

![The structure of the Facade pattern example](https://refactoring.guru/images/patterns/diagrams/facade/example.png)

An example of isolating multiple dependencies within a single facade class.

Instead of making your code work with dozens of the framework classes directly, you create a facade class which encapsulates that functionality and hides it from the rest of the code. This structure also helps you to minimize the effort of upgrading to future versions of the framework or replacing it with another one. The only thing you’d need to change in your app would be the implementation of the facade’s methods.
```java
// These are some of the classes of a complex 3rd-party video
// conversion framework. We don't control that code, therefore
// can't simplify it.

class VideoFile
// ...

class OggCompressionCodec
// ...

class MPEG4CompressionCodec
// ...

class CodecFactory
// ...

class BitrateReader
// ...

class AudioMixer
// ...

// We create a facade class to hide the framework's complexity
// behind a simple interface. It's a trade-off between
// functionality and simplicity.
class VideoConverter is
    method convert(filename, format):File is
        file = new VideoFile(filename)
        sourceCodec = new CodecFactory.extract(file)
        if (format == "mp4")
            destinationCodec = new MPEG4CompressionCodec()
        else
            destinationCodec = new OggCompressionCodec()
        buffer = BitrateReader.read(filename, sourceCodec)
        result = BitrateReader.convert(buffer, destinationCodec)
        result = (new AudioMixer()).fix(result)
        return new File(result)

// Application classes don't depend on a billion classes
// provided by the complex framework. Also, if you decide to
// switch frameworks, you only need to rewrite the facade class.
class Application is
    method main() is
        convertor = new VideoConverter()
        mp4 = convertor.convert("funny-cats-video.ogg", "mp4")
        mp4.save()
```

## Applicability

Use the Facade pattern when you need to have a limited but straightforward interface to a complex subsystem.

Often, subsystems get more complex over time. Even applying design patterns typically leads to creating more classes. A subsystem may become more flexible and easier to reuse in various contexts, but the amount of configuration and boilerplate code it demands from a client grows ever larger. The Facade attempts to fix this problem by providing a shortcut to the most-used features of the subsystem which fit most client requirements.

Use the Facade when you want to structure a subsystem into layers.

Create facades to define entry points to each level of a subsystem. You can reduce coupling between multiple subsystems by requiring them to communicate only through facades.

For example, let’s return to our video conversion framework. It can be broken down into two layers: video- and audio-related. For each layer, you can create a facade and then make the classes of each layer communicate with each another via those facades. This approach looks very similar to the  [Mediator](https://refactoring.guru/design-patterns/mediator)  pattern.

## How to Implement

1.  Check whether it’s possible to provide a simpler interface than what an existing subsystem already provides. You’re on the right track if this interface makes the client code independent from many of the subsystem’s classes.
    
2.  Declare and implement this interface in a new facade class. The facade should redirect the calls from the client code to appropriate objects of the subsystem. The facade should be responsible for initializing the subsystem and managing its further life cycle unless the client code already does this.
    
3.  To get the full benefit from the pattern, make all the client code communicate with the subsystem only via the facade. Now the client code is protected from any changes in the subsystem code. For example, when a subsystem gets upgraded to a new version, you will only need to modify the code in the facade.
    
4.  If the facade becomes  [too big](https://refactoring.guru/smells/large-class), consider extracting part of its behavior to a new, refined facade class.
    

## Pros and Cons

-   You can isolate your code from the complexity of a subsystem.

-   A facade can become  [a god object](https://refactoring.guru/antipatterns/god-object)  coupled to all classes of an app.

## Relations with Other Patterns

-   [Facade](https://refactoring.guru/design-patterns/facade)  defines a new interface for existing objects, whereas  [Adapter](https://refactoring.guru/design-patterns/adapter)  tries to make the existing interface usable.  _Adapter_  usually wraps just one object, while  _Facade_  works with an entire subsystem of objects.
    
-   [Abstract Factory](https://refactoring.guru/design-patterns/abstract-factory)  can serve as an alternative to  [Facade](https://refactoring.guru/design-patterns/facade)  when you only want to hide the way the subsystem objects are created from the client code.
    
-   [Flyweight](https://refactoring.guru/design-patterns/flyweight)  shows how to make lots of little objects, whereas  [Facade](https://refactoring.guru/design-patterns/facade)  shows how to make a single object that represents an entire subsystem.
    
-   [Facade](https://refactoring.guru/design-patterns/facade)  and  [Mediator](https://refactoring.guru/design-patterns/mediator)  have similar jobs: they try to organize collaboration between lots of tightly coupled classes.
    
    -   _Facade_  defines a simplified interface to a subsystem of objects, but it doesn’t introduce any new functionality. The subsystem itself is unaware of the facade. Objects within the subsystem can communicate directly.
    -   _Mediator_  centralizes communication between components of the system. The components only know about the mediator object and don’t communicate directly.
-   A  [Facade](https://refactoring.guru/design-patterns/facade)  class can often be transformed into a  [Singleton](https://refactoring.guru/design-patterns/singleton)  since a single facade object is sufficient in most cases.
    
-   [Facade](https://refactoring.guru/design-patterns/facade)  is similar to  [Proxy](https://refactoring.guru/design-patterns/proxy)  in that both buffer a complex entity and initialize it on its own. Unlike  _Facade_,  _Proxy_  has the same interface as its service object, which makes them interchangeable.

## Code Example
**Facade**  is a structural design pattern that provides a simplified (but limited) interface to a complex system of classes, library or framework.

While Facade decreases the overall complexity of the application, it also helps to move unwanted dependencies to one place.

[Learn more about Facade](https://refactoring.guru/design-patterns/facade)

## Usage of the pattern in Java

**Complexity:**

**Popularity:**

**Usage examples:**  The Facade pattern is commonly used in apps written in Java. It’s especially handy when working with complex libraries and APIs.

Here are some Facade examples in core Java libs:

-   [`javax.faces.context.FacesContext`](http://docs.oracle.com/javaee/7/api/javax/faces/context/FacesContext.html)  uses  [`LifeCycle`](http://docs.oracle.com/javaee/7/api/javax/faces/lifecycle/Lifecycle.html),  [`ViewHandler`](http://docs.oracle.com/javaee/7/api/javax/faces/application/ViewHandler.html),  [`NavigationHandler`](http://docs.oracle.com/javaee/7/api/javax/faces/application/NavigationHandler.html)  classes under the hood, but most clients aren’t aware of that.
    
-   [`javax.faces.context.ExternalContext`](http://docs.oracle.com/javaee/7/api/javax/faces/context/ExternalContext.html)  uses  [`ServletContext`](http://docs.oracle.com/javaee/7/api/javax/servlet/ServletContext.html),  [`HttpSession`](http://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpSession.html),  [`HttpServletRequest`](http://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpServletRequest.html),  [`HttpServletResponse`](http://docs.oracle.com/javaee/7/api/javax/servlet/http/HttpServletResponse.html)  and others inside.
    

**Identification:**  Facade can be recognized in a class that has a simple interface, but delegates most of the work to other classes. Usually, facades manage full life cycle of objects they use.

## Simple interface for a complex video conversion library

In this example, the Facade simplifies communication with a complex video conversion framework.

The Facade provides a single class with a single method that handles all the complexity of configuring the right classes of the framework and retrieving result in a correct format.

## [](https://refactoring.guru/design-patterns/facade/java/example#example-0--some_complex_media_library)**some_complex_media_library:**  Complex video conversion library

#### [](https://refactoring.guru/design-patterns/facade/java/example#example-0--some_complex_media_library-VideoFile-java)**some_complex_media_library/VideoFile.java**
```java
package refactoring_guru.facade.example.some_complex_media_library;

public class VideoFile {
    private String name;
    private String codecType;

    public VideoFile(String name) {
        this.name = name;
        this.codecType = name.substring(name.indexOf(".") + 1);
    }

    public String getCodecType() {
        return codecType;
    }

    public String getName() {
        return name;
    }
}
```
#### [](https://refactoring.guru/design-patterns/facade/java/example#example-0--some_complex_media_library-Codec-java)**some_complex_media_library/Codec.java**
```java
package refactoring_guru.facade.example.some_complex_media_library;

public interface Codec {
}

#### [](https://refactoring.guru/design-patterns/facade/java/example#example-0--some_complex_media_library-MPEG4CompressionCodec-java)**some_complex_media_library/MPEG4CompressionCodec.java**

package refactoring_guru.facade.example.some_complex_media_library;

public class MPEG4CompressionCodec implements Codec {
    public String type = "mp4";

}
```
#### [](https://refactoring.guru/design-patterns/facade/java/example#example-0--some_complex_media_library-OggCompressionCodec-java)**some_complex_media_library/OggCompressionCodec.java**
```java
package refactoring_guru.facade.example.some_complex_media_library;

public class OggCompressionCodec implements Codec {
    public String type = "ogg";
}
```
#### [](https://refactoring.guru/design-patterns/facade/java/example#example-0--some_complex_media_library-CodecFactory-java)**some_complex_media_library/CodecFactory.java**
```java
package refactoring_guru.facade.example.some_complex_media_library;

public class CodecFactory {
    public static Codec extract(VideoFile file) {
        String type = file.getCodecType();
        if (type.equals("mp4")) {
            System.out.println("CodecFactory: extracting mpeg audio...");
            return new MPEG4CompressionCodec();
        }
        else {
            System.out.println("CodecFactory: extracting ogg audio...");
            return new OggCompressionCodec();
        }
    }
}
```
#### [](https://refactoring.guru/design-patterns/facade/java/example#example-0--some_complex_media_library-BitrateReader-java)**some_complex_media_library/BitrateReader.java**
```java
package refactoring_guru.facade.example.some_complex_media_library;

public class BitrateReader {
    public static VideoFile read(VideoFile file, Codec codec) {
        System.out.println("BitrateReader: reading file...");
        return file;
    }

    public static VideoFile convert(VideoFile buffer, Codec codec) {
        System.out.println("BitrateReader: writing file...");
        return buffer;
    }
}
```
#### [](https://refactoring.guru/design-patterns/facade/java/example#example-0--some_complex_media_library-AudioMixer-java)**some_complex_media_library/AudioMixer.java**
```java
package refactoring_guru.facade.example.some_complex_media_library;

import java.io.File;

public class AudioMixer {
    public File fix(VideoFile result){
        System.out.println("AudioMixer: fixing audio...");
        return new File("tmp");
    }
}
```
## [](https://refactoring.guru/design-patterns/facade/java/example#example-0--facade)**facade**

#### [](https://refactoring.guru/design-patterns/facade/java/example#example-0--facade-VideoConversionFacade-java)**facade/VideoConversionFacade.java:**  Facade provides simple interface of video conversion
```java
package refactoring_guru.facade.example.facade;

import refactoring_guru.facade.example.some_complex_media_library.*;

import java.io.File;

public class VideoConversionFacade {
    public File convertVideo(String fileName, String format) {
        System.out.println("VideoConversionFacade: conversion started.");
        VideoFile file = new VideoFile(fileName);
        Codec sourceCodec = CodecFactory.extract(file);
        Codec destinationCodec;
        if (format.equals("mp4")) {
            destinationCodec = new OggCompressionCodec();
        } else {
            destinationCodec = new MPEG4CompressionCodec();
        }
        VideoFile buffer = BitrateReader.read(file, sourceCodec);
        VideoFile intermediateResult = BitrateReader.convert(buffer, destinationCodec);
        File result = (new AudioMixer()).fix(intermediateResult);
        System.out.println("VideoConversionFacade: conversion completed.");
        return result;
    }
}
```
#### [](https://refactoring.guru/design-patterns/facade/java/example#example-0--Demo-java)**Demo.java:**  Client code
```java
package refactoring_guru.facade.example;

import refactoring_guru.facade.example.facade.VideoConversionFacade;

import java.io.File;

public class Demo {
    public static void main(String[] args) {
        VideoConversionFacade converter = new VideoConversionFacade();
        File mp4Video = converter.convertVideo("youtubevideo.ogg", "mp4");
        // ...
    }
}
```
#### [](https://refactoring.guru/design-patterns/facade/java/example#example-0--OutputDemo-txt)**OutputDemo.txt:**  Execution result
```java
VideoConversionFacade: conversion started.
CodecFactory: extracting ogg audio...
BitrateReader: reading file...
BitrateReader: writing file...
AudioMixer: fixing audio...
VideoConversionFacade: conversion completed.
```