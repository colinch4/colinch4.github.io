---
layout: post
title: "[Network] Proxy Server"
description: " "
date: 2021-11-19
tags: [Network]
comments: true
share: true
---


# Proxy Server
서버와 클라이언트의 연결을 중계해 주는 서버

### Table of Contents
- [Proxy Server](#proxy-server)
    - [Table of Contents](#table-of-contents)
  - [About Proxy Server](#about-proxy-server)
  - [Functions and Benefits](#functions-and-benefits)
  - [Type of Proxy Servers](#type-of-proxy-servers)


## About Proxy Server

<img width="700" alt="proxy server" src="https://user-images.githubusercontent.com/48475824/125184588-f8dafd00-e259-11eb-84f2-8d1385b5a81b.png">

프록시 서버(또는 프록시)는 내부 네트워크와 외부 네트워크를 중재해주는 기기로 사용된다.  

- **Proxy 어원**  
  Proxy 는 procuracy를 짧게 지칭하는 단어로써 16세기 부터 사용되어왔다. Procuracy 는 `the taking care of any thing for another` 라는 의미를 갖고 있다. `무언가를 대신하여 일을 처리`하는 대리의 개념이라 보면 된다.  

  단어가 함유한 의미처럼, 프록시는 다른 기기가 처리해야 할 일을 대신하여 처리해주는 컴퓨터(서버)다.

<br>

**(Client)⏤(Proxy)⏤(Server)**

한 당사자와 다른 당사자가 직접 소통(연결)하지 않고 둘 사이에 중재자(프록시)를 두는 이유는 무엇일까?  
프록시의 역할과 이를 사용함으로써 얻게 되는 이점을 아래에서 세부적으로 알아보자.

[Return to TOC](#table-of-contents)

## Functions and Benefits  
프록시는 아래와 같은 기능을 담당하며 프록시를 사용함으로 인해 `보안성` 및 `속도 향상`, `대역폭 감소` 그리고 `로그 수집`이라는 이점을 얻을 수 있다.

Function|Benefit|Detail
--------|-----:|------
Caching Machine|Speed ↑|**캐시:** 리소스를 캐시로 저장해 놓는다.  <br>내부 유저는 리소스를 얻기 위해 직접 인터넷에 접근하지 않고서도 프록시 서버를 통해 빠르게 원하는 리소스를 얻을 수 있다.
Reduce Bandwidth|Bandwidth ↓|**대역폭 감소:** 내외부적으로 트래픽을 줄임으로써 병목현상이 감소된다. <br> 필요한 데이터를 프록시 캐시로부터 얻을 수 있기 때문이다.
Traffic Control|Security ↑|**트래픽 관리:** 인바운드와 아웃바운드 트래픽을 관리하는 역할  <br><br>  회사에서 사용하는 프록시의 경우, 근무시간에 직원이 특정 사이트(SNS와 같은)에 접속하지 못하도록 금지해 놓을 수 있다. <br><br>**Inbound → Outbound:** 내부에서 외부로 유출되는 데이터를 제한해 놓을수 있다. 그로인해 중요한 데이터가 유출되지 않도록 방지해준다.  <br><br>**Inbound ← Outbound:** 외부에서 내부로 들어오는 데이터를 검증 처리를 해준다. 프록시는 악성 트래픽을 차단한다.  
Hide IP|Security ↑|**익명성 보장:** 본 IP 주소 대신 프록시의 IP 주소가 외부에 노출된다.
Collect Logs|Log ✓|**로그를 수집:** 내부 네트워크에서 방문한 웹사이트가 어디인지, 얼마나 머물렀는지의 정보를 로그로 남길 수 있다.  


[Return to TOC](#table-of-contents)

## Type of Proxy Servers  
1. Forward Proxy
1. Reverse Proxy

[Return to TOC](#table-of-contents)
