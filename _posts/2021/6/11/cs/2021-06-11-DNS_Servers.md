---
layout: post
title: "DNS Servers "
description: " "
date: 2021-06-11
tags: [cs]
comments: true
share: true
---

# DNS Servers 

* 세 개 클래스의 DNS Servers : a distributed , hierarchical database

  * Root DNS servers 
  * Top-level Domain (TLD) servers
  * Authoritative DNS servers 

* Why not centralize DNS ? 
  * single point of failure 
    <br>=> 하나의 서버만 있고 그 서버가 문제가 있으면 전체에게 영향을 주게 된다. 따라서 서버들을 분산시켜야 한다. 
  * traffic volume 
    <br>=> 하나로는 전세계의 트래픽을 커버할 수 없다.
  * distant centralized database
    <br>=> 하나만 있으면 너무 멀다. 
  * maintenance
    <br>=> 하나의 서버만 있고 그 서버를 유지보수 해야되면  전체는 그 동안 서버를 쓸 수가 없다. 따라서 서버들을 분산시켜야 한다. 

## Three classes example 

![dns_servers](https://user-images.githubusercontent.com/38216027/71319815-98a13080-24e6-11ea-8b3c-94e0ecbb61a5.png)


