---
layout: post
title: "[cs] 네트워크와 데이터"
description: " "
date: 2021-06-02
tags: [cs]
comments: true
share: true
---

1. [네트워크와 데이터](#-네트워크와-데이터)
2. [서버 인프라](#-서버-인프라)
3. [서버 사이드 언어](#-서버-사이드-언어)

# 네트워크와 데이터

## 클라이언트-서버 모델

- 컴퓨터가 네트워크 상에서 통신을 하는 방법을 정의한 구조
- 결국엔 1:1 통신이나, 요청을 받아주는 쪽이 정해져 있다.
- 클라이언트 서버 구조가 필요한 이유
  - 중앙집중방식의 대표적인 사례
  - 직관적이고, 서비스 구조를 공개할 필요도 없고, 변경도 용이
- 모든 서버는 요청/질의(request) - 응답(response)으로 동작
  - 서버는 프로토콜에서 정해진 기능을 제공
  - 새로운 프로토콜로 서버를 만들 수 있을까?

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/be5cf79c-e76b-4adc-8827-dae0360d5d79/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/be5cf79c-e76b-4adc-8827-dae0360d5d79/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210318T021817Z&X-Amz-Expires=86400&X-Amz-Signature=4f49f3f644686b9c97f73f26b9c6ac7d9da0427032f5a9b2ed138a47d1efe75f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

## 소켓 프로그래밍

- 소켓(소켓 API)는 네트워크 상에서 메세지를 전송할 때 사용
- ARPANET이 시초이며, 1983년 BSD 리눅스에서 API화
- 초창기 웹서버는 단순히 소켓 통신을 이용하는 프로그램이었다.
- **소켓 : 통신을 위한 기본 단위**
- 소켓 프로그래밍이란 : 내가 원하는 포트로 상대방의 열려있는 포트로 대화를 시도하는 것

## 소켓 유형

- 스트림 소켓 : 네트워크 신뢰가 보장되는 상황을 가정 (TCP)
- 데이터그램 소켓 : 네트워크 신뢰 여부에 상관없음 (UDP)
- 로우 소켓 : 특수한 목적으로 사용하는 임의의 프로토콜 기반
- 순서를 가지는 패킷 소켓

## 서버 프로그래밍

- bind()를 호출해 포트를 열고 listen()으로 연결을 대기
- 해당 포트로 연결이 들어오면 연결을 수락 accept()
- 클라이언트로부터 요청 데이터를 받고 read()
- **서버는 요청 데이터에 맞는 작업을 처리하고**
- **클라이언트에게 전달할 응답 데이터를 생성**
- 클라이언트에게 응답 데이터를 전송 write()

# 서버 인프라

## 서버(Server)

- 네트워크를 통해 클라이언트에게 서비스를 제공하는 프로그램
- 서버를 만들기 위한 준비물
  - 컴퓨터 : 데스크탑, 워크스테이션, 서버 제품, 호스팅 서비스, 클라우드
  - 네트워크 : 고정 IP 주소를 가지고, 인터넷에서 접근 가능해야 함
  - 운영체제 : 윈도우, 리눅스, 유닉스
  - 프로그래밍 언어 : 소켓 프로그래밍을 지원하는 모든 언어
  - **(프레임워크) : 조금 더 일관되고, 확장 가능한 서버 개발에 도움**

## 프레임워크(Framework)

- 소프트웨어 설계와 구현을 재사용 가능하도록 해주는 뼈대
- 소프트웨어의 특정 문제를 해결하기 위해 상호 협력하는 클래스와 인터페이스의 집합(기능/데이터 덩어리)
- 프레임워크(가 중심) vs 라이브러리(를 호출하는 쪽이 중심)

## 웹 서버 vs WAS(Web Application Server)

### 웹 서버

- 클라이언트로부터 받은 HTTP 요청을 처리 후 결과를 반환하는 서버
- 정적(static) 컨텐츠(html, js, css)를 제공하는 ㅓ버
- ex) apache, nginx, IIS

### WAS

- 동적 컨텐츠를 제공하기 위한 애플리케이션 서버(DB 연결)
- 컨테이너, 웹 컨테이너, 서블릿 컨테이너
- 서버에서 동적 데이터 처리를 넘겨 받아 처리 후 서버에 반환
- ex) Tomcat(JAVA), Unicorn(Ruby), uWSGI(Python)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b2340356-bcc7-4fc8-93bc-893d404cea48/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b2340356-bcc7-4fc8-93bc-893d404cea48/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210318T021929Z&X-Amz-Expires=86400&X-Amz-Signature=b98f460025ec790e02c481a3055675678d3e55a15aaf754d84e08588f7570f7a&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

## 서버별 핵심 기능

- HTTP 서버 : 요청 데이터를 페이지에 담아 반환
- FTP 서버 : 데이터를 보관하고, 요청 데이터 반환
- Telnet(SSH) 서버 : 명령어를 실행한 결과를 반환(실시간)
- DNS 서버 : 도메인 주소에 해당하는 IP주소를 반환
- DHCP 서버 : IP 주소 요청 시 주소를 할당하고 반환
- SMTP 서버 : 메일을 받아 목적지 서버로 전달

## 서버 아키텍처

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5910ef25-0aa6-4c32-a9b1-a41d4ddb3f79/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/5910ef25-0aa6-4c32-a9b1-a41d4ddb3f79/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210318T022016Z&X-Amz-Expires=86400&X-Amz-Signature=7ab585466680514de5faa54ae86b2793acd1ee09040dea5e681c3d490c15945c&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc8084d8-80d7-4232-a6ff-32667b453d58/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/cc8084d8-80d7-4232-a6ff-32667b453d58/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210318T022039Z&X-Amz-Expires=86400&X-Amz-Signature=144bbc7339d8ee1995aa01c61f19f556a6b89325044a5d99a5daed63b78f638d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b4832819-c49a-4454-8ebb-ad41cb71a781/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b4832819-c49a-4454-8ebb-ad41cb71a781/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210318T022114Z&X-Amz-Expires=86400&X-Amz-Signature=f6a2f2fe3e1bcaf0a236b9eeac97483c23fa1514c9fbfaa5728a391ddc9bd60e&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b5af6f6a-2dad-4a99-a889-2763991af360/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b5af6f6a-2dad-4a99-a889-2763991af360/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210318T022138Z&X-Amz-Expires=86400&X-Amz-Signature=9ef1a3e47c901a734ab41011cbb77e651d33bf2badef9d192cfe392005998271&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/25d1d76e-4343-41e5-84b9-15a9be6d283b/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/25d1d76e-4343-41e5-84b9-15a9be6d283b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210318T022155Z&X-Amz-Expires=86400&X-Amz-Signature=c505b43c7f6e2290e24f6095ae3221ce8e06af30b7cf18735ddef75c78a9dece&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

## 서버 인프라

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1945eae9-5159-4c58-a5b9-281ebc54a31e/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/1945eae9-5159-4c58-a5b9-281ebc54a31e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210318T022219Z&X-Amz-Expires=86400&X-Amz-Signature=5bab80ed1d723eaa1a04161547fea388ce26b8b023a92fbdc1f7223e0747f3f8&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a38c2b8f-9a26-45f9-9f37-54dce72ef7c7/Untitled.png](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/a38c2b8f-9a26-45f9-9f37-54dce72ef7c7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210318T022303Z&X-Amz-Expires=86400&X-Amz-Signature=b1f4aed9b4ab9a7dc41b60bec1d9df0cb47eca2789991e36fb310153a184b067&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

<br>

<br>

# 서버 사이드 언어

### 웹 서버에서 중요한 것은 웹 데이터!

- 웹 데이터는 HTTP 프로토콜 안에 담겨 있다
- 웹데이터 처리에 초점을 맞추자
  - 네트워크 데이터 처리는 서버에 맡기자 : apache, nginx, IIS
  - 우리는 진짜 중요한 웹 데이터 처리만 하자 : PHP, ASP, JSP

### 서버측(Server-side) 언어

- 프로그램 코드를 노출하지 않고 처리 결과만 반환
- 코드 실행 시 웹 브라우저에 영향을 받지 않음
- 실시간으로 빠르게 처리해야 하는 작업에는 적합하지 않다.

### PHP - Hypertext Preprocessor

- 1995년 최초로 공개
- 중-소규모 웹 제작 쉽고 빠른 개발이 가능하다 : C-like 문법
- 개인 웹페이지를 위해 만들어진 언어(인터프리터)
- 대표 프레임워크 : Codeigniter, Laravel
- 워드프레스, 페이스북, 제로보드, 미디어위키등
- **속도 개선과 협업이 힘들고, 구조와 설계가 안정적이지 않다.**

### JSP - Java Server Pages ( + Java ) : 템플릿

- 자바 기반 서버 사이드 스크립트 언어
- 대규모 기업용 시스템 구축에 사용(J2EE)
- 웹 서버 프로그램 이외에도 톰캣과 함께 설치해야 한다.
- 안정적이고, 유지보수가 쉽다 / 무겁고 속도가 느리다(JVM)
- JSP 페이지 = 하나의 Java 클래스
- 서블릿 = HTTP 클라이언트 요청과 응답 표준을 정해놓은 것
- 서블릿 컨테이너(톰캣) : JSP 파일을 서블릿 클래스로 변환하고 실행시켜주는 프로그램

### ASP - Active Server Pages( +.NET )

- IIS에서 동적 웹 페이지 생성 용도로 사용하려고 만든 엔진
- PHP, JSP와 달리 기존 언어를 웹에 쓸 수 있도록 도와주는 기술(vbscript, .NET)
- 2002년에 ASP.NET으로 대체됨
- ASP.NET는 C# 윈폼의 웹 버전
- **국내에서는 거의 안 쓴다....**

### Node.js

- 크롬 V8 자바스크립트 엔진으로 빌드된 자바스크립트 런타임
- 자바스크립트는 브라우저 위에서만(Client-side) 동작하는 언어로, 서버에 필요한 소켓 프로그래밍을 지원하지 않는다.
- Node.js - 자바스크립트로 서버를 만들 수 있도록 지원
- Event-driven, Non blocking I/O, Single Thread
- 웹 서버가 내장되어 있으나, 별도로 설치하는 것도 가능하다.
- **하나의 언어로 서버 개발이 가능하고, 호환성이 높지만 부하가 크거나 성능이 중요한 환경에는 적합하지 않다.**

### 정적 페이지 vs 동적 페이지

- **정적 페이지**

  - 누가, 언제 요청하더라도 항상 같은 내용을 표시하는 웹 페이지
  - html, javascript, css 이미지 만으로 구성된 페이지
  - 서버는 단순히 요청에 해당하는 내용을 반환
  - DB가 필요 없음, 속도 빠름, 서버에 영향 X, 백업과 복원이 쉽다.

- **동적 페이지**
  - 누가, 언제, 어떻게 요청한지에 따라 다른 내용을 반환하는 페이지
  - 서버측에서 요청을 분석해 적절한 응답 페이지를 생성한 후 반환
  - 데이터베이스와 연동 작업이 필요
  - 회원 관리 페이지, 현재

### CGI - Common Gateway Interface

- /cgi-bin/
- 웹 서버와 독립적인 프로그램 사이에 정보를 주고받는 규격
- 서버 언어가 아닌 다른 언어로 만든 프로그램을 직접 호출
- 유지보수가 불편하고, **메모리 부하가 큼**(별도의 프로세스 생성)

### CGI의 대안

- CGI 프로그램을 서버측 언어로 작성하고, 엔진을 서버에 내장
- CGI 프로그램을 데몬으로 가동시켜 놓은 후 요청을 처리

### 웹 애플리케이션 서버(WAS)

- 정적 페이지와 동적 페이지 처리를 분리
- 웹 서버의 기능 = 서버 본연의 기능에 집중 = 정적 페이지 처리, 캐시, 프록시, 요청관리, 인증 제어등
