---
layout: post
title: "[linux] Message Passing"
description: " "
date: 2021-06-11
tags: [linux]
comments: true
share: true
---

> Message Passing

: 메세지 패싱은 프로세스가 다른 프로세스에 메세지((data)를 커널을 통해 전달하는 방식을 말한다.<br> 

* Message system 
: 프로세스 사이에 공유 변수(shared variable)를 일체 사용하지 않고 통신하는 시스템<br>
: 프로세스 A가 메세지를 프로세스 B에게 보낼 때, OS에게 System call하여 커널을 통해 메세지를 보낸다.<br>
: 메세지를 A 프로세스가 커널에게 주고 커널이 B 프로세스에게 준다. 
