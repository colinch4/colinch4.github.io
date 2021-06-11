---
layout: post
title: "HTTP Overview  "
description: " "
date: 2021-06-11
tags: [cs]
comments: true
share: true
---

# HTTP Overview  

# Web Page and Objects

* Web page
  * 객체들(objects)로 구성됨.
  * 여러개의 참조된 객체(referenced objects)들을 포함하는 베이스 HTML-file로 구성된다. 
  
* Object 
  * can be HTML file, JPEG image, Java applet, audio file...

* URL (Uniform Resource Locator)
  * 각각의 객체는 주소화 될 수 있다.
  * 예를 들면 , mmcn.ajou.ac.kr/someDir/pic.gif 
    * mmcn.ajou.ac.kr 은 host name 
    * someDir/pic.gif 은 path name 

# HTTP 

* HTTP 
  * **H**yper**T**ext **T**ransfer **P**rotocol
  * **Web's** application layer protocol

* Client-Server model
  * Client(browser)
    * requests,receives,(using HTTP protocol ) and "displays" Web objects
  * Server(Web server)
    * sends (using HTTP protocol) objects in response to requests

![http_request_response](https://user-images.githubusercontent.com/38216027/71318088-24a75e00-24cf-11ea-96da-c4480922e083.png)

=> client : request 
<br>=> server : response 