---
layout: post
title: "[Design Pattern] Bridge"
description: "Bridge is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other."
date: 2020-02-06 15:02
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://algamza.github.io/2020-02-06/Design-Patterns)  /  [Structural Patterns](https://algamza.github.io/2020-02-06/Structural-Design-Patterns)

## Intent

**Bridge**  is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

![Bridge design pattern](https://refactoring.guru/images/patterns/content/bridge/bridge.png)

## Problem

_Abstraction?_  _Implementation?_  Sound scary? Stay calm and let’s consider a simple example.

Say you have a geometric  `Shape`  class with a pair of subclasses:  `Circle`  and  `Square`. You want to extend this class hierarchy to incorporate colors, so you plan to create  `Red`  and  `Blue`  shape subclasses. However, since you already have two subclasses, you’ll need to create four class combinations such as  `BlueCircle`  and  `RedSquare`.

![Bridge pattern problem](https://refactoring.guru/images/patterns/diagrams/bridge/problem.png)

Number of class combinations grows in geometric progression.

Adding new shape types and colors to the hierarchy will grow it exponentially. For example, to add a triangle shape you’d need to introduce two subclasses, one for each color. And after that, adding a new color would require creating three subclasses, one for each shape type. The further we go, the worse it becomes.

## Solution

This problem occurs because we’re trying to extend the shape classes in two independent dimensions: by form and by color. That’s a very common issue with class inheritance.

The Bridge pattern attempts to solve this problem by switching from inheritance to the object composition. What this means is that you extract one of the dimensions into a separate class hierarchy, so that the original classes will reference an object of the new hierarchy, instead of having all of its state and behaviors within one class.

![Solution suggested by the Bridge pattern](https://refactoring.guru/images/patterns/diagrams/bridge/solution-en.png)

You can prevent the explosion of a class hierarchy by transforming it into several related hierarchies.

Following this approach, we can extract the color-related code into its own class with two subclasses:  `Red`  and  `Blue`. The  `Shape`  class then gets a reference field pointing to one of the color objects. Now the shape can delegate any color-related work to the linked color object. That reference will act as a bridge between the  `Shape`  and  `Color`  classes. From now on, adding new colors won’t require changing the shape hierarchy, and vice versa.

#### Abstraction and Implementation

The GoF book introduces the terms  _Abstraction_  and  _Implementation_  as part of the Bridge definition. In my opinion, the terms sound too academic and make the pattern seem more complicated than it really is. Having read the simple example with shapes and colors, let’s decipher the meaning behind the GoF book’s scary words.

_Abstraction_  (also called  _interface_) is a high-level control layer for some entity. This layer isn’t supposed to do any real work on its own. It should delegate the work to the  _implementation_  layer (also called  _platform_).

Note that we’re not talking about  _interfaces_  or  _abstract classes_  from your programming language. These aren’t the same things.

When talking about real applications, the abstraction can be represented by a graphical user interface (GUI), and the implementation could be the underlying operating system code (API) which the GUI layer calls in response to user interactions.

Generally speaking, you can extend such an app in two independent directions:

-   Have several different GUIs (for instance, tailored for regular customers or admins).
-   Support several different APIs (for example, to be able to launch the app under Windows, Linux, and MacOS).

In a worst-case scenario, this app might look like a giant spaghetti bowl, where hundreds of conditionals connect different types of GUI with various APIs all over the code.

![Managing changes is much easier in modular code](https://refactoring.guru/images/patterns/content/bridge/bridge-3-en.png)

Making even a simple change to a monolithic codebase is pretty hard because you must understand the  _entire thing_  very well. Making changes to smaller, well-defined modules is much easier.

You can bring order to this chaos by extracting the code related to specific interface-platform combinations into separate classes. However, soon you’ll discover that there are  _lots_  of these classes. The class hierarchy will grow exponentially because adding a new GUI or supporting a different API would require creating more and more classes.

Let’s try to solve this issue with the Bridge pattern. It suggests that we divide the classes into two hierarchies:

-   Abstraction: the GUI layer of the app.
-   Implementation: the operating systems’ APIs.

![Cross-platform architecture](https://refactoring.guru/images/patterns/content/bridge/bridge-2-en.png)

One of the ways to structure a cross-platform application.

The abstraction object controls the appearance of the app, delegating the actual work to the linked implementation object. Different implementations are interchangeable as long as they follow a common interface, enabling the same GUI to work under Windows and Linux.

As a result, you can change the GUI classes without touching the API-related classes. Moreover, adding support for another operating system only requires creating a subclass in the implementation hierarchy.

## Structure

![Bridge design pattern](https://refactoring.guru/images/patterns/diagrams/bridge/structure-en.png)

1.  The  **Abstraction**  provides high-level control logic. It relies on the implementation object to do the actual low-level work.
    
2.  The  **Implementation**  declares the interface that’s common for all concrete implementations. An abstraction can only communicate with an implementation object via methods that are declared here.
    
    The abstraction may list the same methods as the implementation, but usually the abstraction declares some complex behaviors that rely on a wide variety of primitive operations declared by the implementation.
    
3.  **Concrete Implementations**  contain platform-specific code.
    
4.  **Refined Abstractions**  provide variants of control logic. Like their parent, they work with different implementations via the general implementation interface.
    
5.  Usually, the  **Client**  is only interested in working with the abstraction. However, it’s the client’s job to link the abstraction object with one of the implementation objects.
    

## Pseudocode

This example illustrates how the  **Bridge**  pattern can help divide the monolithic code of an app that manages devices and their remote controls. The  `Device`  classes act as the implementation, whereas the  `Remote`s act as the abstraction.

![Structure of the Bridge pattern example](https://refactoring.guru/images/patterns/diagrams/bridge/example-en.png)

The original class hierarchy is divided into two parts: devices and remote controls.

The base remote control class declares a reference field that links it with a device object. All remotes work with the devices via the general device interface, which lets the same remote support multiple device types.

You can develop the remote control classes independently from the device classes. All that’s needed is to create a new remote subclass. For example, a basic remote control might only have two buttons, but you could extend it with additional features, such as an extra battery or a touchscreen.

The client code links the desired type of remote control with a specific device object via the remote’s constructor.

```java
// The "abstraction" defines the interface for the "control"
// part of the two class hierarchies. It maintains a reference
// to an object of the "implementation" hierarchy and delegates
// all of the real work to this object.
class RemoteControl is
    protected field device: Device
    constructor RemoteControl(device: Device) is
        this.device = device
    method togglePower() is
        if (device.isEnabled()) then
            device.disable()
        else
            device.enable()
    method volumeDown() is
        device.setVolume(device.getVolume() - 10)
    method volumeUp() is
        device.setVolume(device.getVolume() + 10)
    method channelDown() is
        device.setChannel(device.getChannel() - 1)
    method channelUp() is
        device.setChannel(device.getChannel() + 1)

// You can extend classes from the abstraction hierarchy
// independently from device classes.
class AdvancedRemoteControl extends RemoteControl is
    method mute() is
        device.setVolume(0)

// The "implementation" interface declares methods common to all
// concrete implementation classes. It doesn't have to match the
// abstraction's interface. In fact, the two interfaces can be
// entirely different. Typically the implementation interface
// provides only primitive operations, while the abstraction
// defines higher-level operations based on those primitives.
interface Device is
    method isEnabled()
    method enable()
    method disable()
    method getVolume()
    method setVolume(percent)
    method getChannel()
    method setChannel(channel)

// All devices follow the same interface.
class Tv implements Device is
    // ...

class Radio implements Device is
    // ...

// Somewhere in client code.
tv = new Tv()
remote = new RemoteControl(tv)
remote.togglePower()

radio = new Radio()
remote = new AdvancedRemoteControl(radio)
```

## Applicability

Use the Bridge pattern when you want to divide and organize a monolithic class that has several variants of some functionality (for example, if the class can work with various database servers).

The bigger a class becomes, the harder it is to figure out how it works, and the longer it takes to make a change. The changes made to one of the variations of functionality may require making changes across the whole class, which often results in making errors or not addressing some critical side effects.

The Bridge pattern lets you split the monolithic class into several class hierarchies. After this, you can change the classes in each hierarchy independently of the classes in the others. This approach simplifies code maintenance and minimizes the risk of breaking existing code.

Use the pattern when you need to extend a class in several orthogonal (independent) dimensions.

The Bridge suggests that you extract a separate class hierarchy for each of the dimensions. The original class delegates the related work to the objects belonging to those hierarchies instead of doing everything on its own.

Use the Bridge if you need to be able to switch implementations at runtime.

Although it’s optional, the Bridge pattern lets you replace the implementation object inside the abstraction. It’s as easy as assigning a new value to a field.

_By the way, this last item is the main reason why so many people confuse the Bridge with the  [Strategy](https://algamza.github.io/2020-02-06/Stategy-Design-Pattern)  pattern. Remember that a pattern is more than just a certain way to structure your classes. It may also communicate intent and a problem being addressed._

## How to Implement

1.  Identify the orthogonal dimensions in your classes. These independent concepts could be: abstraction/platform, domain/infrastructure, front-end/back-end, or interface/implementation.
    
2.  See what operations the client needs and define them in the base abstraction class.
    
3.  Determine the operations available on all platforms. Declare the ones that the abstraction needs in the general implementation interface.
    
4.  For all platforms in your domain create concrete implementation classes, but make sure they all follow the implementation interface.
    
5.  Inside the abstraction class, add a reference field for the implementation type. The abstraction delegates most of the work to the implementation object that’s referenced in that field.
    
6.  If you have several variants of high-level logic, create refined abstractions for each variant by extending the base abstraction class.
    
7.  The client code should pass an implementation object to the abstraction’s constructor to associate one with the other. After that, the client can forget about the implementation and work only with the abstraction object.
    

## Pros and Cons

-   You can create platform-independent classes and apps.
-   The client code works with high-level abstractions. It isn’t exposed to the platform details.
-   _Open/Closed Principle_. You can introduce new abstractions and implementations independently from each other.
-   _Single Responsibility Principle_. You can focus on high-level logic in the abstraction and on platform details in the implementation.

-   You might make the code more complicated by applying the pattern to a highly cohesive class.

## Relations with Other Patterns

-   [Bridge](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern)  is usually designed up-front, letting you develop parts of an application independently of each other. On the other hand,  [Adapter](https://algamza.github.io/2020-02-06/Adapter-Design-Pattern)  is commonly used with an existing app to make some otherwise-incompatible classes work together nicely.
    
-   [Bridge](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern),  [State](https://algamza.github.io/2020-02-06/State-Design-Pattern),  [Strategy](https://algamza.github.io/2020-02-06/Stategy-Design-Pattern)  (and to some degree  [Adapter](https://algamza.github.io/2020-02-06/Adapter-Design-Pattern)) have very similar structures. Indeed, all of these patterns are based on composition, which is delegating work to other objects. However, they all solve different problems. A pattern isn’t just a recipe for structuring your code in a specific way. It can also communicate to other developers the problem the pattern solves.
    
-   You can use  [Abstract Factory](https://algamza.github.io/2020-02-06/Abstract-Factory-Design-Pattern)  along with  [Bridge](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern). This pairing is useful when some abstractions defined by  _Bridge_  can only work with specific implementations. In this case,  _Abstract Factory_  can encapsulate these relations and hide the complexity from the client code.
    
-   You can combine  [Builder](https://algamza.github.io/2020-02-06/Builder-Design-Pattern)  with  [Bridge](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern): the  _director_  class plays the role of the abstraction, while different  _builders_  act as  _implementations_.

## Code Example
**Bridge**  is a structural design pattern that divides business logic or huge class into separate class hierarchies that can be developed independently.

One of these hierarchies (often called the Abstraction) will get a reference to an object of the second hierarchy (Implementation). The abstraction will be able to delegate some (sometimes, most) of its calls to the implementations object. Since all implementations will have a common interface, they’d be interchangeable inside the abstraction.

[Learn more about Bridge](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern)

## Usage of the pattern in Java

**Complexity:**

**Popularity:**

**Usage examples:**  The Bridge pattern is especially useful when dealing with cross-platform apps, supporting multiple types of database servers or working with several API providers of a certain kind (for example, cloud platforms, social networks, etc.)

**Identification:**  Bridge can be recognized by a clear distinction between some controlling entity and several different platforms that it relies on.

## Bridge between devices and remote controls

This example shows separation between the classes of remotes and devices that they control.

Remotes act as abstractions, and devices are their implementations. Thanks to the common interfaces, the same remotes can work with different devices and vice versa.

The Bridge pattern allows changing or even creating new classes without touching the code of the opposite hierarchy.

## [](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern/java/example#example-0--devices)**devices**

#### [](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern/java/example#example-0--devices-Device-java)**devices/Device.java:**  Common interface of all devices
```java
package algamza.bridge.example.devices;

public interface Device {
    boolean isEnabled();

    void enable();

    void disable();

    int getVolume();

    void setVolume(int percent);

    int getChannel();

    void setChannel(int channel);

    void printStatus();
}
```
#### [](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern/java/example#example-0--devices-Radio-java)**devices/Radio.java:**  Radio
```java
package algamza.bridge.example.devices;

public class Radio implements Device {
    private boolean on = false;
    private int volume = 30;
    private int channel = 1;

    @Override
    public boolean isEnabled() {
        return on;
    }

    @Override
    public void enable() {
        on = true;
    }

    @Override
    public void disable() {
        on = false;
    }

    @Override
    public int getVolume() {
        return volume;
    }

    @Override
    public void setVolume(int volume) {
        if (volume > 100) {
            this.volume = 100;
        } else if (volume < 0) {
            this.volume = 0;
        } else {
            this.volume = volume;
        }
    }

    @Override
    public int getChannel() {
        return channel;
    }

    @Override
    public void setChannel(int channel) {
        this.channel = channel;
    }

    @Override
    public void printStatus() {
        System.out.println("------------------------------------");
        System.out.println("| I'm radio.");
        System.out.println("| I'm " + (on ? "enabled" : "disabled"));
        System.out.println("| Current volume is " + volume + "%");
        System.out.println("| Current channel is " + channel);
        System.out.println("------------------------------------\n");
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern/java/example#example-0--devices-Tv-java)**devices/Tv.java:**  TV
```java
package algamza.bridge.example.devices;

public class Tv implements Device {
    private boolean on = false;
    private int volume = 30;
    private int channel = 1;

    @Override
    public boolean isEnabled() {
        return on;
    }

    @Override
    public void enable() {
        on = true;
    }

    @Override
    public void disable() {
        on = false;
    }

    @Override
    public int getVolume() {
        return volume;
    }

    @Override
    public void setVolume(int volume) {
        if (volume > 100) {
            this.volume = 100;
        } else if (volume < 0) {
            this.volume = 0;
        } else {
            this.volume = volume;
        }
    }

    @Override
    public int getChannel() {
        return channel;
    }

    @Override
    public void setChannel(int channel) {
        this.channel = channel;
    }

    @Override
    public void printStatus() {
        System.out.println("------------------------------------");
        System.out.println("| I'm TV set.");
        System.out.println("| I'm " + (on ? "enabled" : "disabled"));
        System.out.println("| Current volume is " + volume + "%");
        System.out.println("| Current channel is " + channel);
        System.out.println("------------------------------------\n");
    }
}
```
## [](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern/java/example#example-0--remotes)**remotes**

#### [](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern/java/example#example-0--remotes-Remote-java)**remotes/Remote.java:**  Common interface for all remotes
```java
package algamza.bridge.example.remotes;

public interface Remote {
    void power();

    void volumeDown();

    void volumeUp();

    void channelDown();

    void channelUp();
}
```
#### [](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern/java/example#example-0--remotes-BasicRemote-java)**remotes/BasicRemote.java:**  Basic remote control
```java
package algamza.bridge.example.remotes;

import algamza.bridge.example.devices.Device;

public class BasicRemote implements Remote {
    protected Device device;

    public BasicRemote() {}

    public BasicRemote(Device device) {
        this.device = device;
    }

    @Override
    public void power() {
        System.out.println("Remote: power toggle");
        if (device.isEnabled()) {
            device.disable();
        } else {
            device.enable();
        }
    }

    @Override
    public void volumeDown() {
        System.out.println("Remote: volume down");
        device.setVolume(device.getVolume() - 10);
    }

    @Override
    public void volumeUp() {
        System.out.println("Remote: volume up");
        device.setVolume(device.getVolume() + 10);
    }

    @Override
    public void channelDown() {
        System.out.println("Remote: channel down");
        device.setChannel(device.getChannel() - 1);
    }

    @Override
    public void channelUp() {
        System.out.println("Remote: channel up");
        device.setChannel(device.getChannel() + 1);
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern/java/example#example-0--remotes-AdvancedRemote-java)**remotes/AdvancedRemote.java:**  Advanced remote control
```java
package algamza.bridge.example.remotes;

import algamza.bridge.example.devices.Device;

public class AdvancedRemote extends BasicRemote {

    public AdvancedRemote(Device device) {
        super.device = device;
    }

    public void mute() {
        System.out.println("Remote: mute");
        device.setVolume(0);
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern/java/example#example-0--Demo-java)**Demo.java:**  Client code
```java
package algamza.bridge.example;

import algamza.bridge.example.devices.Device;
import algamza.bridge.example.devices.Radio;
import algamza.bridge.example.devices.Tv;
import algamza.bridge.example.remotes.AdvancedRemote;
import algamza.bridge.example.remotes.BasicRemote;

public class Demo {
    public static void main(String[] args) {
        testDevice(new Tv());
        testDevice(new Radio());
    }

    public static void testDevice(Device device) {
        System.out.println("Tests with basic remote.");
        BasicRemote basicRemote = new BasicRemote(device);
        basicRemote.power();
        device.printStatus();

        System.out.println("Tests with advanced remote.");
        AdvancedRemote advancedRemote = new AdvancedRemote(device);
        advancedRemote.power();
        advancedRemote.mute();
        device.printStatus();
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Bridge-Design-Pattern/java/example#example-0--OutputDemo-txt)**OutputDemo.txt:**  Execution result
```java
Tests with basic remote.
Remote: power toggle
------------------------------------
| I'm TV set.
| I'm enabled
| Current volume is 30%
| Current channel is 1
------------------------------------

Tests with advanced remote.
Remote: power toggle
Remote: mute
------------------------------------
| I'm TV set.
| I'm disabled
| Current volume is 0%
| Current channel is 1
------------------------------------

Tests with basic remote.
Remote: power toggle
------------------------------------
| I'm radio.
| I'm enabled
| Current volume is 30%
| Current channel is 1
------------------------------------

Tests with advanced remote.
Remote: power toggle
Remote: mute
------------------------------------
| I'm radio.
| I'm disabled
| Current volume is 0%
| Current channel is 1
------------------------------------
```