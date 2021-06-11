---
layout: post
title: "[socket] A stream socket"
description: " "
date: 2021-06-11
tags: [socket]
comments: true
share: true
---

## A stream socket

* two-way, sequenced, reliable flow of data. The socket type is SOCK\_STREAM, which, in the internet domain, uses Transmission Control Protocol(TCP)

* TCP 프로토콜을 사용한다. TCP 프로토콜은 양방향, 순서가 있는, 신뢰적인 프로토콜 방식이고 stream socket은 TCP 프로토콜을 사용한다.  
* TCP 프로토콜은 상대방이 데이터를 제대로 받았는지 안받았는지(Ack/Nak) 확인할 수 있기 때문에 **신뢰성이 보장**된다.

* TCP는 상대방이 제대로 데이터를 못받을 경우, 제대로 받을때까지 데이터를 재전송한다. 따라서 재전송하는 동안 **시간이 걸리는 단점이 있다. (신속하지 못하다.)**

TCP는 **신뢰성 보장!**

TCP는 데이터 통신에 쓰인다. 

## A datagram socket

* The socket type is SOCK\_DGRAM, which, in the Internet domain, uses User Datagram Protocol(UDP).

* UDP 프로토콜은 상대방이 데이터를 제대로 받았는 지 안받았는지 확인할 수 없어 **신뢰성이 보장되지 않는다.** 

* UDP는 확인을 하지 않아 재전송하지 않기 때문에 데이터가 제대로 보내지지 않을 위험은 있어도 **빠르게 데이터를 전송할 수 있다는 장점이 있다.(신속하다.)**

UDP는 **신뢰성이 보장되지 않는다!**<br>

실시간 데이터(예: 스트리밍)은 재전송보단 신속함이 중요한 데이터이므로 TCP 말고 주로 UDP를 사용한다.<br>

다운로드 -> TCP <br>
스트리밍 -> UDP <br>

## A sequential packet socket
## A raw socket
=> 두개는 많이 안쓴다. 
