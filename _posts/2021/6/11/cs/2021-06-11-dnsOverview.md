---
layout: post
title: "DNS Overview "
description: " "
date: 2021-06-11
tags: [cs]
comments: true
share: true
---

# DNS Overview 

> 도메인이란 ? 

ip는 사람이 이해하고 기억하기 어렵기 때문에 이를 위해서 각 ip에 이름을 부여할 수 있게 했는데, 이것을 도메인이라고 한다.

## DNS (Domain Name System)

* RFC 1034 and RFC 1035
  * updated in several additional RFCs
* application-layer protocol 
  * client-server model 
* used to resolve host names to IP addresses
  * host name -> IP address
  * IP address -> host name translation

=> **보통 자신이 알고있는 host name의 ip 주소를 구하려고 사용하는 프로토콜**  

* UDP를 사용하고 port 53번을 사용하는 프로토콜

> nslookup

* nslookup 명령어로 자신이 찾고자하는 도메인의 ip address 를 구할수 있다. 

![nslookup](https://user-images.githubusercontent.com/38216027/71318053-9b902700-24ce-11ea-9b0d-e34ab32a63c6.png)

