---
layout: post
title: " Root Name Server"
description: " "
date: 2021-06-11
tags: [cs]
comments: true
share: true
---

## Root Name Server

* Root Name Server 는 **교통정리**를 한다. 
<br>=> 쿼리가 오면 자기가 하는 것(Do Not Resolution)이 아니라, 쿼리를 알것 같은 TLD 서버에 연결해준다.  ( TLD 서버의 주소를 알려주거나(iterative) 자신이 TLD에 쿼리 메시지를 날리거나(recursive))

> 13 root name servers worldwide (in 2019)

![root_name_servers](https://user-images.githubusercontent.com/38216027/71320499-8e376480-24ef-11ea-9876-6f142d1ddd52.png)

* Local DNS server는 13 개의 Root Name Server에 **Anycast** 한다. 
<br>=> 가장 빨리 응답오는 Root Name Server와 연결한다.   

## 애니 캐스트 (Anycast)

> 애니캐스트(anycast)는 단일 송신자로부터의 인터넷 상 트래픽인 데이터그램들을 인터넷상의 경로가되는 토폴로지 상의 잠재적인 수신자 그룹 안에서 **가장 가까운 노드**로 연결시키는, 네트워크 어드레싱 및 라우팅 방식으로, 여러 개의 노드들에 전송될 수 있고 이 노드들 모두 동일한 목적 주소로 식별된다.

