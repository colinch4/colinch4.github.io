---
layout: post
title: "[Design Pattern] Proxy"
description: "Proxy is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object."
date: 2020-02-06 15:00
tags: [디자인패턴]
comments: true
share: true
---

/  [Design Patterns](https://algamza.github.io/2020-02-06/Design-Patterns)  /  [Structural Patterns](https://algamza.github.io/2020-02-06/Structural-Design-Patterns)

## Intent

**Proxy**  is a structural design pattern that lets you provide a substitute or placeholder for another object. A proxy controls access to the original object, allowing you to perform something either before or after the request gets through to the original object.

![Proxy design pattern](https://refactoring.guru/images/patterns/content/proxy/proxy.png)

## Problem

Why would you want to control access to an object? Here is an example: you have a massive object that consumes a vast amount of system resources. You need it from time to time, but not always.

![Problem solved by Proxy pattern](https://refactoring.guru/images/patterns/diagrams/proxy/problem.png)

Database queries can be really slow.

You could implement lazy initialization: create this object only when it’s actually needed. All of the object’s clients would need to execute some deferred initialization code. Unfortunately, this would probably cause a lot of code duplication.

In an ideal world, we’d want to put this code directly into our object’s class, but that isn’t always possible. For instance, the class may be part of a closed 3rd-party library.

## Solution

The Proxy pattern suggests that you create a new proxy class with the same interface as an original service object. Then you update your app so that it passes the proxy object to all of the original object’s clients. Upon receiving a request from a client, the proxy creates a real service object and delegates all the work to it.

![Solution with the Proxy pattern](https://refactoring.guru/images/patterns/diagrams/proxy/solution.png)

The proxy disguises itself as a database object. It can handle lazy initialization and result caching without the client or the real database object even knowing.

But what’s the benefit? If you need to execute something either before or after the primary logic of the class, the proxy lets you do this without changing that class. Since the proxy implements the same interface as the original class, it can be passed to any client that expects a real service object.

## Real-World Analogy

![A credit card is a proxy for a bundle of cash](https://refactoring.guru/images/patterns/diagrams/proxy/live-example.png)

Credit cards can be used for payments just the same as cash.

A credit card is a proxy for a bank account, which is a proxy for a bundle of cash. Both implement the same interface: they can be used for making a payment. A consumer feels great because there’s no need to carry loads of cash around. A shop owner is also happy since the income from a transaction gets added electronically to the shop’s bank account without the risk of losing the deposit or getting robbed on the way to the bank.

## Structure

![Structure of the Proxy design pattern](https://refactoring.guru/images/patterns/diagrams/proxy/structure.png)

1.  The  **Service Interface**  declares the interface of the Service. The proxy must follow this interface to be able to disguise itself as a service object.
    
2.  The  **Service**  is a class that provides some useful business logic.
    
3.  The  **Proxy**  class has a reference field that points to a service object. After the proxy finishes its processing (e.g., lazy initialization, logging, access control, caching, etc.), it passes the request to the service object.
    
    Usually, proxies manage the full lifecycle of their service objects.
    
4.  The  **Client**  should work with both services and proxies via the same interface. This way you can pass a proxy into any code that expects a service object.
    

## Pseudocode

This example illustrates how the  **Proxy**  pattern can help to introduce lazy initialization and caching to a 3rd-party YouTube integration library.

![Structure of the Proxy pattern example](https://refactoring.guru/images/patterns/diagrams/proxy/example.png)

Caching results of a service with a proxy.

The library provides us with the video downloading class. However, it’s very inefficient. If the client application requests the same video multiple times, the library just downloads it over and over, instead of caching and reusing the first downloaded file.

The proxy class implements the same interface as the original downloader and delegates it all the work. However, it keeps track of the downloaded files and returns the cached result when the app requests the same video multiple times.

```java
// The interface of a remote service.
interface ThirdPartyYoutubeLib is
    method listVideos()
    method getVideoInfo(id)
    method downloadVideo(id)

// The concrete implementation of a service connector. Methods
// of this class can request information from YouTube. The speed
// of the request depends on a user's internet connection as
// well as YouTube's. The application will slow down if a lot of
// requests are fired at the same time, even if they all request
// the same information.
class ThirdPartyYoutubeClass implements ThirdPartyYoutubeLib is
    method listVideos() is
        // Send an API request to YouTube.

    method getVideoInfo(id) is
        // Get metadata about some video.

    method downloadVideo(id) is
        // Download a video file from YouTube.

// To save some bandwidth, we can cache request results and keep
// them for some time. But it may be impossible to put such code
// directly into the service class. For example, it could have
// been provided as part of a third party library and/or defined
// as `final`. That's why we put the caching code into a new
// proxy class which implements the same interface as the
// service class. It delegates to the service object only when
// the real requests have to be sent.
class CachedYoutubeClass implements ThirdPartyYouTubeLib is
    private field service: ThirdPartyYouTubeClass
    private field listCache, videoCache
    field needReset

    constructor CachedYoutubeClass(service: ThirdPartyYouTubeLib) is
        this.service = service

    method listVideos() is
        if (listCache == null || needReset)
            listCache = service.listVideos()
        return listCache

    method getVideoInfo(id) is
        if (videoCache == null || needReset)
            videoCache = service.getVideoInfo(id)
        return videoCache

    method downloadVideo(id) is
        if (!downloadExists(id) || needReset)
            service.downloadVideo(id)

// The GUI class, which used to work directly with a service
// object, stays unchanged as long as it works with the service
// object through an interface. We can safely pass a proxy
// object instead of a real service object since they both
// implement the same interface.
class YoutubeManager is
    protected field service: ThirdPartyYouTubeLib

    constructor YoutubeManager(service: ThirdPartyYouTubeLib) is
        this.service = service

    method renderVideoPage(id) is
        info = service.getVideoInfo(id)
        // Render the video page.

    method renderListPanel() is
        list = service.listVideos()
        // Render the list of video thumbnails.

    method reactOnUserInput() is
        renderVideoPage()
        renderListPanel()

// The application can configure proxies on the fly.
class Application is
    method init() is
        aYouTubeService = new ThirdPartyYouTubeClass()
        aYouTubeProxy = new CachedYouTubeClass(aYouTubeService)
        manager = new YouTubeManager(aYouTubeProxy)
        manager.reactOnUserInput()
```

## Applicability

There are dozens of ways to utilize the Proxy pattern. Let’s go over the most popular uses.

Lazy initialization (virtual proxy). This is when you have a heavyweight service object that wastes system resources by being always up, even though you only need it from time to time.

Instead of creating the object when the app launches, you can delay the object’s initialization to a time when it’s really needed.

Access control (protection proxy). This is when you want only specific clients to be able to use the service object; for instance, when your objects are crucial parts of an operating system and clients are various launched applications (including malicious ones).

The proxy can pass the request to the service object only if the client’s credentials match some criteria.

Local execution of a remote service (remote proxy). This is when the service object is located on a remote server.

In this case, the proxy passes the client request over the network, handling all of the nasty details of working with the network.

Logging requests (logging proxy). This is when you want to keep a history of requests to the service object.

The proxy can log each request before passing it to the service.

Caching request results (caching proxy). This is when you need to cache results of client requests and manage the life cycle of this cache, especially if results are quite large.

The proxy can implement caching for recurring requests that always yield the same results. The proxy may use the parameters of requests as the cache keys.

Smart reference. This is when you need to be able to dismiss a heavyweight object once there are no clients that use it.

The proxy can keep track of clients that obtained a reference to the service object or its results. From time to time, the proxy may go over the clients and check whether they are still active. If the client list gets empty, the proxy might dismiss the service object and free the underlying system resources.

The proxy can also track whether the client had modified the service object. Then the unchanged objects may be reused by other clients.

## How to Implement

1.  If there’s no pre-existing service interface, create one to make proxy and service objects interchangeable. Extracting the interface from the service class isn’t always possible, because you’d need to change all of the service’s clients to use that interface. Plan B is to make the proxy a subclass of the service class, and this way it’ll inherit the interface of the service.
    
2.  Create the proxy class. It should have a field for storing a reference to the service. Usually, proxies create and manage the whole life cycle of their servers. In rare occasions, a service is passed to the proxy via a constructor by the client.
    
3.  Implement the proxy methods according to their purposes. In most cases, after doing some work, the proxy should delegate the work to the service object.
    
4.  Consider introducing a creation method that decides whether the client gets a proxy or a real service. This can be a simple static method in the proxy class or a full-blown factory method.
    
5.  Consider implementing lazy initialization for the service object.
    

## Pros and Cons

-   You can control the service object without clients knowing about it.
-   You can manage the lifecycle of the service object when clients don’t care about it.
-   The proxy works even if the service object isn’t ready or is not available.
-   _Open/Closed Principle_. You can introduce new proxies without changing the service or clients.

-   The code may become more complicated since you need to introduce a lot of new classes.
-   The response from the service might get delayed.

## Relations with Other Patterns

-   [Adapter](https://algamza.github.io/2020-02-06/Adapter-Design-Pattern)  provides a different interface to the wrapped object,  [Proxy](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern)  provides it with the same interface, and  [Decorator](https://algamza.github.io/2020-02-06/Decorator-Design-Pattern)  provides it with an enhanced interface.
    
-   [Facade](https://algamza.github.io/2020-02-06/Facade-Design-Pattern)  is similar to  [Proxy](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern)  in that both buffer a complex entity and initialize it on its own. Unlike  _Facade_,  _Proxy_  has the same interface as its service object, which makes them interchangeable.
    
-   [Decorator](https://algamza.github.io/2020-02-06/Decorator-Design-Pattern)  and  [Proxy](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern)  have similar structures, but very different intents. Both patterns are built on the composition principle, where one object is supposed to delegate some of the work to another. The difference is that a  _Proxy_  usually manages the life cycle of its service object on its own, whereas the composition of  _Decorators_  is always controlled by the client.

## Code Example

**Proxy**  is a structural design pattern that provides an object that acts as a substitute for a real service object used by a client. A proxy receives client requests, does some work (access control, caching, etc.) and then passes the request to a service object.

The proxy object has the same interface as a service, which makes it interchangeable with a real object when passed to a client.

[Learn more about Proxy](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern)

## Usage of the pattern in Java

**Complexity:**

**Popularity:**

**Usage examples:**  While the Proxy pattern isn’t a frequent guest in most Java applications, it’s still very handy in some special cases. It’s irreplaceable when you want to add some additional behaviors to an object of some existing class without changing the client code.

Some examples of proxies in standard Java libraries:

-   [`java.lang.reflect.Proxy`](http://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Proxy.html)
-   [`java.rmi.*`](http://docs.oracle.com/javase/8/docs/api/java/rmi/package-summary.html)
-   [`javax.ejb.EJB`](http://docs.oracle.com/javaee/7/api/javax/ejb/EJB.html)  ([see comments](http://stackoverflow.com/questions/25514361/when-using-ejb-does-each-managed-bean-get-its-own-ejb-instance))
-   [`javax.inject.Inject`](http://docs.oracle.com/javaee/7/api/javax/inject/Inject.html)  ([see comments](http://stackoverflow.com/questions/29651008/field-getobj-returns-all-nulls-on-injected-cdi-managed-beans-while-manually-i/29672591#29672591))
-   [`javax.persistence.PersistenceContext`](http://docs.oracle.com/javaee/7/api/javax/persistence/PersistenceContext.html)

**Identification:**  Proxies delegate all of the real work to some other object. Each proxy method should, in the end, refer to a service object unless the proxy is a subclass of a service.

## Caching proxy

In this example, the Proxy pattern helps to implement the lazy initialization and caching to an inefficient 3rd-party Youtube integration library.

Proxy is invaluable when you have to add some additional behaviors to a class which code you can’t change.

## [](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern/java/example#example-0--some_cool_media_library)**some_cool_media_library**

#### [](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern/java/example#example-0--some_cool_media_library-ThirdPartyYoutubeLib-java)**some_cool_media_library/ThirdPartyYoutubeLib.java:**  Remote service interface
```java
package algamza.proxy.example.some_cool_media_library;

import java.util.HashMap;

public interface ThirdPartyYoutubeLib {
    HashMap<String, Video> popularVideos();

    Video getVideo(String videoId);
}
```
#### [](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern/java/example#example-0--some_cool_media_library-ThirdPartyYoutubeClass-java)**some_cool_media_library/ThirdPartyYoutubeClass.java:**  Remote service implementation
```java
package algamza.proxy.example.some_cool_media_library;

import java.util.HashMap;

public class ThirdPartyYoutubeClass implements ThirdPartyYoutubeLib {

    @Override
    public HashMap<String, Video> popularVideos() {
        connectToServer("http://www.youtube.com");
        return getRandomVideos();
    }

    @Override
    public Video getVideo(String videoId) {
        connectToServer("http://www.youtube.com/" + videoId);
        return getSomeVideo(videoId);
    }

    // -----------------------------------------------------------------------
    // Fake methods to simulate network activity. They as slow as a real life.

    private int random(int min, int max) {
        return min + (int) (Math.random() * ((max - min) + 1));
    }

    private void experienceNetworkLatency() {
        int randomLatency = random(5, 10);
        for (int i = 0; i < randomLatency; i++) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException ex) {
                ex.printStackTrace();
            }
        }
    }

    private void connectToServer(String server) {
        System.out.print("Connecting to " + server + "... ");
        experienceNetworkLatency();
        System.out.print("Connected!" + "\n");
    }

    private HashMap<String, Video> getRandomVideos() {
        System.out.print("Downloading populars... ");

        experienceNetworkLatency();
        HashMap<String, Video> hmap = new HashMap<String, Video>();
        hmap.put("catzzzzzzzzz", new Video("sadgahasgdas", "Catzzzz.avi"));
        hmap.put("mkafksangasj", new Video("mkafksangasj", "Dog play with ball.mp4"));
        hmap.put("dancesvideoo", new Video("asdfas3ffasd", "Dancing video.mpq"));
        hmap.put("dlsdk5jfslaf", new Video("dlsdk5jfslaf", "Barcelona vs RealM.mov"));
        hmap.put("3sdfgsd1j333", new Video("3sdfgsd1j333", "Programing lesson#1.avi"));

        System.out.print("Done!" + "\n");
        return hmap;
    }

    private Video getSomeVideo(String videoId) {
        System.out.print("Downloading video... ");

        experienceNetworkLatency();
        Video video = new Video(videoId, "Some video title");

        System.out.print("Done!" + "\n");
        return video;
    }

}
```
#### [](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern/java/example#example-0--some_cool_media_library-Video-java)**some_cool_media_library/Video.java:**  Video file
```java
package algamza.proxy.example.some_cool_media_library;

public class Video {
    public String id;
    public String title;
    public String data;

    Video(String id, String title) {
        this.id = id;
        this.title = title;
        this.data = "Random video.";
    }
}
```
## [](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern/java/example#example-0--proxy)**proxy**

#### [](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern/java/example#example-0--proxy-YoutubeCacheProxy-java)**proxy/YoutubeCacheProxy.java:**  Caching proxy
```java
package algamza.proxy.example.proxy;

import algamza.proxy.example.some_cool_media_library.ThirdPartyYoutubeClass;
import algamza.proxy.example.some_cool_media_library.ThirdPartyYoutubeLib;
import algamza.proxy.example.some_cool_media_library.Video;

import java.util.HashMap;

public class YoutubeCacheProxy implements ThirdPartyYoutubeLib {
    private ThirdPartyYoutubeLib youtubeService;
    private HashMap<String, Video> cachePopular = new HashMap<String, Video>();
    private HashMap<String, Video> cacheAll = new HashMap<String, Video>();

    public YoutubeCacheProxy() {
        this.youtubeService = new ThirdPartyYoutubeClass();
    }

    @Override
    public HashMap<String, Video> popularVideos() {
        if (cachePopular.isEmpty()) {
            cachePopular = youtubeService.popularVideos();
        } else {
            System.out.println("Retrieved list from cache.");
        }
        return cachePopular;
    }

    @Override
    public Video getVideo(String videoId) {
        Video video = cacheAll.get(videoId);
        if (video == null) {
            video = youtubeService.getVideo(videoId);
            cacheAll.put(videoId, video);
        } else {
            System.out.println("Retrieved video '" + videoId + "' from cache.");
        }
        return video;
    }

    public void reset() {
        cachePopular.clear();
        cacheAll.clear();
    }
}
```
## [](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern/java/example#example-0--downloader)**downloader**

#### [](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern/java/example#example-0--downloader-YoutubeDownloader-java)**downloader/YoutubeDownloader.java:**  Media downloader app
```java
package algamza.proxy.example.downloader;

import algamza.proxy.example.some_cool_media_library.ThirdPartyYoutubeLib;
import algamza.proxy.example.some_cool_media_library.Video;

import java.util.HashMap;

public class YoutubeDownloader {
    private ThirdPartyYoutubeLib api;

    public YoutubeDownloader(ThirdPartyYoutubeLib api) {
        this.api = api;
    }

    public void renderVideoPage(String videoId) {
        Video video = api.getVideo(videoId);
        System.out.println("\n-------------------------------");
        System.out.println("Video page (imagine fancy HTML)");
        System.out.println("ID: " + video.id);
        System.out.println("Title: " + video.title);
        System.out.println("Video: " + video.data);
        System.out.println("-------------------------------\n");
    }

    public void renderPopularVideos() {
        HashMap<String, Video> list = api.popularVideos();
        System.out.println("\n-------------------------------");
        System.out.println("Most popular videos on Youtube (imagine fancy HTML)");
        for (Video video : list.values()) {
            System.out.println("ID: " + video.id + " / Title: " + video.title);
        }
        System.out.println("-------------------------------\n");
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern/java/example#example-0--Demo-java)**Demo.java:**  Initialization code
```java
package algamza.proxy.example;

import algamza.proxy.example.downloader.YoutubeDownloader;
import algamza.proxy.example.proxy.YoutubeCacheProxy;
import algamza.proxy.example.some_cool_media_library.ThirdPartyYoutubeClass;

public class Demo {

    public static void main(String[] args) {
        YoutubeDownloader naiveDownloader = new YoutubeDownloader(new ThirdPartyYoutubeClass());
        YoutubeDownloader smartDownloader = new YoutubeDownloader(new YoutubeCacheProxy());

        long naive = test(naiveDownloader);
        long smart = test(smartDownloader);
        System.out.print("Time saved by caching proxy: " + (naive - smart) + "ms");

    }

    private static long test(YoutubeDownloader downloader) {
        long startTime = System.currentTimeMillis();

        // User behavior in our app:
        downloader.renderPopularVideos();
        downloader.renderVideoPage("catzzzzzzzzz");
        downloader.renderPopularVideos();
        downloader.renderVideoPage("dancesvideoo");
        // Users might visit the same page quite often.
        downloader.renderVideoPage("catzzzzzzzzz");
        downloader.renderVideoPage("someothervid");

        long estimatedTime = System.currentTimeMillis() - startTime;
        System.out.print("Time elapsed: " + estimatedTime + "ms\n");
        return estimatedTime;
    }
}
```
#### [](https://algamza.github.io/2020-02-06/Proxy-Design-Pattern/java/example#example-0--OutputDemo-txt)**OutputDemo.txt:**  Execution result
```java
Connecting to http://www.youtube.com... Connected!
Downloading populars... Done!

-------------------------------
Most popular videos on Youtube (imagine fancy HTML)
ID: sadgahasgdas / Title: Catzzzz.avi
ID: asdfas3ffasd / Title: Dancing video.mpq
ID: 3sdfgsd1j333 / Title: Programing lesson#1.avi
ID: mkafksangasj / Title: Dog play with ball.mp4
ID: dlsdk5jfslaf / Title: Barcelona vs RealM.mov
-------------------------------

Connecting to http://www.youtube.com/catzzzzzzzzz... Connected!
Downloading video... Done!

-------------------------------
Video page (imagine fancy HTML)
ID: catzzzzzzzzz
Title: Some video title
Video: Random video.
-------------------------------

Connecting to http://www.youtube.com... Connected!
Downloading populars... Done!

-------------------------------
Most popular videos on Youtube (imagine fancy HTML)
ID: sadgahasgdas / Title: Catzzzz.avi
ID: asdfas3ffasd / Title: Dancing video.mpq
ID: 3sdfgsd1j333 / Title: Programing lesson#1.avi
ID: mkafksangasj / Title: Dog play with ball.mp4
ID: dlsdk5jfslaf / Title: Barcelona vs RealM.mov
-------------------------------

Connecting to http://www.youtube.com/dancesvideoo... Connected!
Downloading video... Done!

-------------------------------
Video page (imagine fancy HTML)
ID: dancesvideoo
Title: Some video title
Video: Random video.
-------------------------------

Connecting to http://www.youtube.com/catzzzzzzzzz... Connected!
Downloading video... Done!

-------------------------------
Video page (imagine fancy HTML)
ID: catzzzzzzzzz
Title: Some video title
Video: Random video.
-------------------------------

Connecting to http://www.youtube.com/someothervid... Connected!
Downloading video... Done!

-------------------------------
Video page (imagine fancy HTML)
ID: someothervid
Title: Some video title
Video: Random video.
-------------------------------

Time elapsed: 9354ms
Connecting to http://www.youtube.com... Connected!
Downloading populars... Done!

-------------------------------
Most popular videos on Youtube (imagine fancy HTML)
ID: sadgahasgdas / Title: Catzzzz.avi
ID: asdfas3ffasd / Title: Dancing video.mpq
ID: 3sdfgsd1j333 / Title: Programing lesson#1.avi
ID: mkafksangasj / Title: Dog play with ball.mp4
ID: dlsdk5jfslaf / Title: Barcelona vs RealM.mov
-------------------------------

Connecting to http://www.youtube.com/catzzzzzzzzz... Connected!
Downloading video... Done!

-------------------------------
Video page (imagine fancy HTML)
ID: catzzzzzzzzz
Title: Some video title
Video: Random video.
-------------------------------

Retrieved list from cache.

-------------------------------
Most popular videos on Youtube (imagine fancy HTML)
ID: sadgahasgdas / Title: Catzzzz.avi
ID: asdfas3ffasd / Title: Dancing video.mpq
ID: 3sdfgsd1j333 / Title: Programing lesson#1.avi
ID: mkafksangasj / Title: Dog play with ball.mp4
ID: dlsdk5jfslaf / Title: Barcelona vs RealM.mov
-------------------------------

Connecting to http://www.youtube.com/dancesvideoo... Connected!
Downloading video... Done!

-------------------------------
Video page (imagine fancy HTML)
ID: dancesvideoo
Title: Some video title
Video: Random video.
-------------------------------

Retrieved video 'catzzzzzzzzz' from cache.

-------------------------------
Video page (imagine fancy HTML)
ID: catzzzzzzzzz
Title: Some video title
Video: Random video.
-------------------------------

Connecting to http://www.youtube.com/someothervid... Connected!
Downloading video... Done!

-------------------------------
Video page (imagine fancy HTML)
ID: someothervid
Title: Some video title
Video: Random video.
-------------------------------

Time elapsed: 5875ms
Time saved by caching proxy: 3479ms

```