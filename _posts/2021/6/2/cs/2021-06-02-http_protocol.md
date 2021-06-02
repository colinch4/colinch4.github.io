---
layout: post
title: "[cs] HTTP 프로토콜 완벽 정리"
description: " "
date: 2021-06-02
tags: [cs]
comments: true
share: true
---

# HTTP 프로토콜 완벽 정리

1. [HTTP 프로토콜 이란?](##-http-프로토콜-이란?)
2. [HTTP 기반 시스템의 구성 요소](##-http-기반-시스템의-구성-요소)
3. [HTTP의 기초적인 측면](##-HTTP의-기초적인-측면)
4. [HTTP 메세지의 구조](##-http-메세지의-구조)
5. [HTTP 헤더](##-http-헤더)
6. [HTTP 처리 방식](##-http-처리-방식)
7. [HTTP Status Code](##-http-status-code)
8. [URL](##-url)

<br>

## HTTP 프로토콜 이란?

웹 서버와 웹 클라이언트 사이에서 데이터를 주고받기 위해 사용하는 통신 방식으로, TCP/IP 프로토콜 위에서 동작합니다. 즉, 우리가 웹을 이용하려면 웹서버와 웹 클라이언트는 각각 TCP/IP 동작에 필수적인 IP 주소를 가져야 한다는 의미이다.

- HTTP는 HTML이나 XML 과 같은 하이퍼 텍스트 뿐만 아니라 이미지, 음성, 동영상, 자바스크립트, PDF와 각종 도큐먼트 파일 등 컴퓨터에서 다룰 수 있는 데이터라면 무엇이든 전송할 수 있다.
- 예를 들어, 주소창에 `[www.google.com](http://www.google.com)` 을 입력하고 `Enter` 를 누르면 웹 클라이언트와 웹 서버 사이에 HTTP 연결이 맺어지고, 웹 클라이언트는 웹 서버에 HTTP 요청 메시지를 보내게 된다. 웹 서버는 요청에 따른 처리를 진행한 후 그 결과를 웹 클라이언트에게 HTTP 응답 메시지로 보냅니다. 이런 방식으로 요청 메시지와 응답 메시지가 반복적으로 오가면서 웹을 사용하게 되는 것이다.

<br>

![http](https://user-images.githubusercontent.com/58774316/111725057-ab511380-88a9-11eb-80da-68cc9bf45d5f.png)

<br>

## HTTP 기반 시스템의 구성 요소

- HTTP는 클라이언트-서버 프로토콜이다
- 요청은 하나의 개체, 사용자 에이전트(또는 그것을 대신하는 프록시)에 의해 전송된다.
- 대부분의 경우, 사용자 에이전트는 브라우저지만, 무엇이든 될 수 있다. ex) 검색 엔진 인덱스를 채워 넣고 유지하기 위해 웹을 돌아다니는 로봇

> 각각의 개별적인 요청들은 서버로 보내지며, 서버는 요청을 처리하고 response라고 불리는 응답을 제공하고, 이 요청과 응답 사이에는 여러 개체들이 있다. 예를 들면 다양한 작업을 수행하는 게이트웨이 또는 캐시 역할을 하는 프록시등이 있다.

![proxy](https://user-images.githubusercontent.com/58774316/112080451-61c43980-8bc5-11eb-8405-965ba58b35f4.png)

실제로는 브라우저와 요청을 처리하는 서버 사이에는 좀 더 많은 컴퓨터들이 존재합니다.(라우터, 모뎀 등)

웹의 계층적인 설계 덕분에, 이들은 네트워크와 전송 계층 내로 숨겨집니다. HTTP는 애플리케이션 계층의 최상위에 있다.

### 클라이언트: 사용자 에이전트

사용자 에이전트는 사용자를 대신하여 동작하는 모든 도구입니다. 이 역할은 주로 **브라우저**에 의해 수행됩니다; 엔지니어들과 자신들의 애플리케이션을 디버그하는 웹 개발자들이 사용하는 프로그램들은 예외입니다.

브라우저는 **항상** 요청을 보내는 개체입니다. 그것은 결코 서버가 될 수 없습니다.

웹 페이지를 표시하기 위해, 브라우저는 페이지의 HTML 문서를 가져오기 위한 요청을 전송한 뒤, 파일을 구문 분석하여 실행해야 할 스크립트 그리고 페이지 내 포함된 하위 리소스들(보통 이미지와 비디오)을 잘 표시하기 위한 레이아웃 정보(CSS)에 대응하는 추가적인 요청들을 가져옵니다. 그런 뒤에 브라우저는 완전한 문서인 웹 페이지를 표시하기 위해 그런 리소스들을 혼합합니다. 브라우저에 의해 실행된 스크립트는 이후 단계에서 좀 더 많은 리소스들을 가져올 수 있으며 브라우저는 그에 따라 웹 페이지를 갱신하게 됩니다.

웹 페이지는 하이퍼텍스트 문서로, 표시된 텍스트의 일부는 사용자가 사용자 에이전트를 제어하고 웹을 돌아다닐 수 있도록 새로운 웹 페이지를 가져오기 위해 실행(보통 마우스 클릭에 의해)될 수 있는 링크임을 뜻합니다. 브라우저는 HTTP 요청 내에서 이런 지시 사항들을 변환하고 HTTP 응답을 해석하여 사용자에게 명확한 응답을 표시합니다.

### 웹 서버

통신 채널의 반대편에는 클라이언트에 의한 요청에 대한 문서를 *제공*하는 서버가 존재합니다. 서버는 사실 상 논리적으로 단일 기계입니다.이는 로드(로드 밸런싱) 혹은 그때 그때 다른 컴퓨터(캐시, DB 서버, e-커머스 서버 등과 같은)들의 정보를 얻고 완전하게 혹은 부분적으로 문서를 생성하는 소프트웨어의 복잡한 부분을 공유하는 서버들의 집합일 수도 있기 때문입니다.

서버는 반드시 단일 머신일 필요는 없지만, 여러 개의 서버를 동일한 머신 위에서 호스팅 할 수는 있습니다. HTTP/1.1과 `[Host](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Host)` 헤더를 이용하여, 동일한 IP 주소를 공유할 수도 있습니다.

### 프록시

웹 브라우저와 서버 사이에서는 수많은 컴퓨터와 머신이 HTTP 메시지를 이어 받고 전달합니다. 여러 계층으로 이루어진 웹 스택 구조에서 이러한 컴퓨터/머신들은 대부분은 전송, 네트워크 혹은 물리 계층에서 동작하며, 성능에 상당히 큰 영향을 주지만 HTTP 계층에서는 이들이 어떻게 동작하는지 눈에 보이지 않습니다. 이러한 컴퓨터/머신 중에서도 애플리케이션 계층에서 동작하는 것들을 일반적으로 **프록시**라고 부릅니다. 프록시는 눈에 보이거나 그렇지 않을 수도 있으며(프록시를 통해 요청이 변경되거나 변경되지 않는 경우를 말함) 다양한 기능들을 수행할 수 있습니다:

- 캐싱 (캐시는 공개 또는 비공개가 될 수 있습니다 (예: 브라우저 캐시))
- 필터링 (바이러스 백신 스캔, 유해 컨텐츠 차단(자녀 보호) 기능)
- 로드 밸런싱 (여러 서버들이 서로 다른 요청을 처리하도록 허용)
- 인증 (다양한 리소스에 대한 접근 제어)
- 로깅 (이력 정보를 저장)

<br>

## HTTP의 기초적인 측면

### Simple

- HTTP는 사람이 읽을 수 있으며 간단하게 고안되었습니다.
- 심지어 HTTP/2가 다소 더 복잡해졌지만 여전히 HTTP 메세지를 프레임별로 캡슐화하여 간결함을 유지하였습니다.
- HTTP 메시지들은 사람이 읽고 이해할 수 있어, 테스트하기 쉽고 초심자의 진입장벽을 낮췄습니다.

### Scalable (확장 가능)

- HTTP/1.0에서 소개된, HTTP 헤더는 HTTP를 확장하고 실험하기 쉽게 만들어주었습니다.
- 클라이언트와 서버가 새로운 헤더의 시맨틱에 대해 간단한 합의만 한다면, 언제든지 새로운 기능을 추가할 수 있습니다.

### There is no status, but there is a session.

- HTTP는 상태를 저장하지 않습니다(Stateless). 동일한 연결 상에서 연속하여 전달된 두 개의 요청 사이에는 연결고리가 없습니다. 이는 e-커머스 쇼핑 바구니처럼, 일관된 방식으로 사용자가 페이지와 상호작용하길 원할 때 문제가 됩니다.
- 하지만, HTTP의 핵심은 상태가 없는 것이지만 HTTP 쿠키는 상태가 있는 세션을 만들도록 해줍니다.헤더 확장성을 사용하여, 동일한 컨텍스트 또는 동일한 상태를 공유하기 위해 각각의 요청들에 세션을 만들도록 HTTP 쿠키가 추가됩니다.

### Connect to HTTP

- 연결은 전송 계층에서 제어되므로 근본적으로 HTTP 영역 밖입니다. HTTP는 연결될 수 있도록 하는 근본적인 전송 프로토콜을 요구하지 않습니다; 다만 그저 신뢰할 수 있거나 메시지 손실이 없는(최소한의 오류는 표시) 연결을 요구할 뿐입니다. 인터넷 상의 가장 일반적인 두 개의 전송 프로토콜 중에서 TCP는 신뢰할 수 있으며 UDP는 그렇지 않습니다. 그러므로 HTTP는 연결이 필수는 아니지만 연결 기반인 TCP 표준에 의존합니다.
- 클라이언트와 서버가 HTTP를 요청/응답으로 교환하기 전에 여러 왕복이 필요한 프로세스인 TCP 연결을 설정해야 합니다. HTTP/1.0의 기본 동작은 각 요청/응답에 대해 별도의 TCP 연결을 여는 것입니다. 이 동작은 여러 요청을 연속해서 보내는 경우에는 단일 TCP 연결을 공유하는 것보다 효율적이지 못합니다.
- 이러한 결함을 개선하기 위해, HTTP/1.1은 (구현하기 어렵다고 입증된) 파이프라이닝 개념과 지속적인 연결의 개념을 도입했습니다: 기본적인 TCP 연결은 `[Connection](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Connection)` 헤더를 사용해 부분적으로 제어할 수 있습니다. HTTP/2는 연결을 좀 더 지속되고 효율적으로 유지하는데 도움이 되도록, 단일 연결 상에서 메시지를 다중 전송(multiplex)하여 한 걸음 더 나아갔습니다.

<br>

## HTTP 메세지의 구조

HTTP 메시지는 클라이언트에서 서버로 보내는 요청 메시지와 서버에서 클라이언트로 보내는 응답 메시지 2가지가 있다.

![message](https://user-images.githubusercontent.com/58774316/111723207-87d89980-88a6-11eb-9c1b-36f28e3b41a8.png)

<br>

**시작줄 / 헤더 / 바디** 로 나눌 수 있다.

- **시작줄**
  - Request 시, 메서드와 요청 URL, HTTP version ( GET /exam/help.txt HTTP/1.1 )
  - Response 시, HTTP version, 상태 코드 및 사유 구절 ( HTTP/1.1 200 OK )
- **헤더**
  - 요청과 응답 메세지에 대한 추가적인 정보를 담고 있다.
  - Key/Value 형식으로 나타냄
- **바디**

  - 전송하고 싶은 실질적인 데이터를 나타냄
  - 헤더를 마치고 \n(CRLF : 공백) 후에 나타남.

<br>
<br>

- 요청 메세지 예제

```cpp
GET /hello.txt HTTP/1.1 		// 요청메서드 / 자원주소 / HTTP 버전
User-Agent: curl/7.16.3 libcurl/7.16.3 OpenSSL/0.9.7l zlib/1.2.3	// 헤더
Host: www.example.com												// 헤더
Accept-Language: en, mi
```

- 응답 메세지 예제

```cpp
HTTP/1.1 200 OK         // HTTP 버전 / 응답코드 및 사유
Date: Mon, 27 Jul 2009 12:28:53 GMT    // 바디까지 주욱 헤더
Server: Apache
Last-Modified: Wed, 22 Jul 2009 19:15:56 GMT
ETag: "34aa387-d-1568eb00"
Accept-Ranges: bytes
Content-Length: 51
Vary: Accept-Encoding
Content-Type: text/plain

Hello World! My payload includes a trailing CRLF.	// 바디
```

<br>

## HTTP 헤더

- Request header 와 Response header 둘다 동일한 구조를 가지고 있다.

### HTTP Request header

- General 헤더: `[Via](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Via)`와 같은 *헤더는* 메시지 전체에 적용됩니다.
- Request 헤더: [User-Agent (en-US)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent), `[Accept-Type](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Accept-Type)`와 같은 헤더는 요청의 내용을 좀 더 구체화 시키고(`[Accept-Language](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Accept-Language)`), 컨텍스를 제공하기도 하며(`[Referer](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Referer)`), 조건에 따른 제약 사항을 가하기도 하면서(`[If-None](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/If-None)`) 요청 내용을 수정합니다.
- Entity 헤더: `[Content-Length](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Content-Length)`와 같은 헤더는 요청 본문에 적용됩니다. 당연히 요청 내에 본문이 없는 경우 entity 헤더는 전송되지 않습니다.

![request_header](https://user-images.githubusercontent.com/58774316/112080484-70aaec00-8bc5-11eb-9545-3b7f607e2ade.png)

### HTTP Response header

- General 헤더: `[Via](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Via)`와 같은 *헤더는* 메시지 전체에 적용됩니다.
- Response 헤더: `[Vary](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Vary)`와 `[Accept-Ranges](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Accept-Ranges)`와 같은 헤더는 상태 줄에 미처 들어가지 못했던 서버에 대한 추가 정보를 제공합니다.
- Entity 헤더: `[Content-Length](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Content-Length)`와 같은 헤더는 요청 본문에 적용됩니다. 당연히 요청 내에 본문이 없는 경우 entity 헤더는 전송되지 않습니다.

![response_header](https://user-images.githubusercontent.com/58774316/112080506-76a0cd00-8bc5-11eb-8aee-8229abb0b108.png)

### 공통 헤더

---

- **Date** : 현재시간 (Sat, 23 Mat 2019 GMT)
- **Pragma** : 캐시제어 (no-cache), HTTP/1.0에서 쓰던 것으로 HTTP/1.1에서는 Cache-Control이 쓰인다.
- **Cache-Control** : 캐시 제어

  - no-store : 캐시를 저장하지 않겠다.

  - no-cache : 모든 캐시를 쓰기 전에 서버에 해당 캐시를 사용해도 되는지 확인하겠다.

  - must-revalidate : 만료된 캐시만 서버에 확인하겠다.

  - public : 공유 캐시에 저장해도 된다.

  - private : '브라우저' 같은 특정 사용자 환경에만 저장하겠다.

  - max-age : 캐시의 유효시간을 명시하겠다.

- **Transfer-Encoding** : body 내용 자체 압축 방식 지정

  'chunked'면 본문의 내용이 동적으로 생성되어 길이를 모르기 때문에 나눠서 보낸다는 의미다.

  본문에 데이터 길이가 나와서 야금야금 브라우저가 해석해서 화면에 뿌려줄 때 이 기능을 사용한다.

- **Upgrade** : 프로토콜 변경시 사용 ex) HTTP/2.0
- **Via** : 중계(프록시)서버의 이름, 버전, 호스트명
- **Content-Encoding** : 본문의 리소스 압축 방식 (transfer-encoding은 body 자체이므로 다름)
- **Content-type** : 본문의 미디어 타입(MIME) ex) application/json, text/html
- **Content-Length** : 본문의 길이
- **Content-language** : 본문을 이해하는데 가장 적절한 언어 ex) ko

  한국사이트여도 본문을 이해하는데 영어가 제일 적절하면 영어로 지정된다.

- **Expires** : 자원의 만료 일자
- **Allow** : 사용이 가능한 HTTP 메소드 방식 ex) GET, HEAD, POST
- **Last-Modified** : 최근에 수정된 날짜
- **ETag** : 캐시 업데이트 정보를 위한 임의의 식별 숫자
- **Connection** : 클라이언트와 서버의 연결 방식 설정 HTTP/1.1은 kepp-alive 로 연결 유지하는게 디폴트.

### 요청 헤더

---

- **Host** : 요청하려는 서버 호스트 이름과 포트번호
- **User-agent** : 클라이언트 프로그램 정보 ex) Mozilla/4.0, Windows NT5.1

  이 정보를 통해서 서버는 클라이언트 프로그램(브라우저)에 맞는 최적의 데이터를 보내줄 수 있다.

- **Referer** : 바로 직전에 머물렀던 웹 링크 주소(해당 요청을 할 수 있게된 페이지)
- **Accept** : 클라이언트가 처리 가능한 미디어 타입 종류 나열 ex) _/_ - 모든 타입 처리 가능, application/json - json데이터 처리 가능.
- **Accept-charset** : 클라이언트가 지원가능한 문자열 인코딩 방식
- **Accept-language** : 클라이언트가 지원가능한 언어 나열
- **Accept-encoding** : 클라이언트가 해석가능한 압축 방식 지정 ex) gzip, deflate

  압축이 되어있다면 content-length와 content-encoding으로 압축을 해제한다.

- **Content-location** : 해당 개체의 실제 위치
- **Content-disposition** : 응답 메세지를 브라우저가 어떻게 처리할지 알려줌. ex) inline, attachment; filename='jeong-pro.xlsx'
- **Content-Security-Policy** : 다른 외부 파일을 불러오는 경우 차단할 리소스와 불러올 리소스 명시

  ex) default-src https -> https로만 파일을 가져옴

  ex) default-src 'self' -> 자기 도메인에서만 가져옴

  ex) default-src 'none' -> 외부파일은 가져올 수 없음

- **If-Modified-Since** : 여기에 쓰여진 시간 이후로 변경된 리소스 취득. 페이지가 수정되었으면 최신 페이지로 교체하기 위해 사용된다.
- **Authorization** : 인증 토큰을 서버로 보낼 때 쓰이는 헤더
- **Origin** : 서버로 Post 요청을 보낼 때 요청이 어느 주소에서 시작되었는지 나타내는 값

  이 값으로 요청을 보낸 주소와 받는 주소가 다르면 CORS 에러가 난다.

- **Cookie** : 쿠기 값 key-value로 표현된다. ex) attr1=value1; attr2=value2

### 응답 헤더

---

- **Location** : 301, 302 상태코드일 떄만 볼 수 있는 헤더로 서버의 응답이 다른 곳에 있다고 알려주면서 해당 위치(URI)를 지정한다.
- **Server** : 웹서버의 종류 ex) nginx
- **Age** : max-age 시간내에서 얼마나 흘렀는지 초 단위로 알려주는 값
- **Referrer-policy** : 서버 referrer 정책을 알려주는 값 ex) origin, no-referrer, unsafe-url
- **WWW-Authenticate** : 사용자 인증이 필요한 자원을 요구할 시, 서버가 제공하는 인증 방식
- **Proxy-Authenticate** : 요청한 서버가 프록시 서버인 경우 유저 인증을 위한 값

### 참고자료 - 알아둬야 할 HTTP 공통 & 요청 헤더

[(HTTP) 알아둬야 할 HTTP 공통 & 요청 헤더](https://www.zerocho.com/category/HTTP/post/5b3ba2d0b3dabd001b53b9db)

<br>

## HTTP 처리 방식

위에서 살펴본 URL을 이용하여 우리는 서버에게 자원을 요청 할 수 있는데요, 이 때(요청할때) 데이터에게 특정 동작을 수행하고 싶을 때 HTTP Request Methods를 이용합니다.

일반적으로 HTTP 요청 메소드는 HTTP Verbs라고도 불리우며 아래와 같이 주요 메서드를 갖고 있습니다.

<br>

| Method Name |               의미               | CRUD와 매핑되는 역활 |
| :---------: | :------------------------------: | :------------------: |
|     GET     |    존재하는 자원에 대한 요청     |         READ         |
|    POST     |        새로운 자원을 생성        |        Create        |
|     PUT     |    존재하는 자원에 대한 변경     |        Update        |
|   DELETE    |    존재하는 자원에 대한 삭제     |        Delete        |
|    HEAD     |  리소스의 헤더(메타데이터) 취득  |                      |
|   OPTIONS   | 서버 옵션들을 확인하기 위한 요청 |                      |
|    TRACE    |        루프백 시험에 사용        |                      |
|   CONNECT   | 프록시 동작의 터널 접속으로 변경 |                      |

<br>

위의 정의한 바와 같이 데이터에 대한 조회, 생성, 변경, 삭제 동작을 HTTP 요청 메소드로 이용할 수 있습니다. 참고로 때에 따라서는 POST 메서드로 PUT, DELETE의 동작도 수행할 수 있습니다.

<br>

## HTTP Status Code

위에서 살펴본 HTTP 요청 메서드가 클라이언트에서 설정하는 정보라면 HTTP 상태 코드는 클라이언트에서 요청을 받아 응답(Response)을 해주기 위해 설정해주는 코드 입니다.

### 2xx - 성공

200번대의 상태 코드는 대부분 성공을 의미합니다.

- 200 : GET 요청에 대한 성공
- 204 : No Content. 성공했으나 응답 본문에 데이터가 없음
- 205 : Reset Content. 성공했으나 클라이언트의 화면을 새로 고침하도록 권고
- 206 : Partial Conent. 성공했으나 일부 범위의 데이터만 반환

### 3xx - 리다이렉션

300번대의 상태 코드는 대부분 클라이언트가 이전 주소로 데이터를 요청하여 서버에서 새 URL로 리다이렉트를 유도하는 경우입니다.

- 301 : Moved Permanently, 요청한 자원이 새 URL에 존재
- 303 : See Other, 요청한 자원이 임시 주소에 존재
- 304 : Not Modified, 요청한 자원이 변경되지 않았으므로 클라이언트에서 캐싱된 자원을 사용하도록 권고. [ETag](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag)와 같은 정보를 활용하여 변경 여부를 확인

### 4xx - 클라이언트 에러

400번대 상태 코드는 대부분 클라이언트의 코드가 잘못된 경우입니다. 유효하지 않은 자원을 요청했거나 요청이나 권한이 잘못된 경우 발생합니다. 가장 익숙한 상태 코드는 404 코드입니다. 요청한 자원이 서버에 없다는 의미죠.

- 400 : Bad Request, 잘못된 요청
- 401 : Unauthorized, 권한 없이 요청. Authorization 헤더가 잘못된 경우
- 403 : Forbidden, 서버에서 해당 자원에 대해 접근 금지
- 405 : Method Not Allowed, 허용되지 않은 요청 메서드
- 409 : Conflict, 최신 자원이 아닌데 업데이트하는 경우. ex) 파일 업로드 시 버전 충돌

### 5xx - 서버 에러

500번대 상태 코드는 서버 쪽에서 오류가 난 경우입니다.

- 501 : Not Implemented, 요청한 동작에 대해 서버가 수행할 수 없는 경우
- 503 : Service Unavailable, 서버가 과부하 또는 유지 보수로 내려간 경우

<br>

## HTTP 프로토콜 특징

HTTP의 특징으로는 **상태가 없는(stateless**) 프로토콜입니다. 여기서 상태가 없다라는 말은 각각의 데이터 주고받기를 위한 요청이 서로 독립 적으로 관리가 된다는 말입니다. 좀 더 쉽게 말해서 이전 데이터요청과 다음 데이터 요청이 서로 관련이 없다는 말이죠.

- 이러한 특징 덕분에 서버는 세션과 같은 별도의 추가 정보를 관리하지 않아도 되고, 다수의 요청 처리 및 서버의 부하를 줄일 수 있는 성능 상의 이점이 생깁니다.

- 하지만 연결을 끊어버리기 때문에, 클라이언트의 이전 상태를 알 수가 없다. 이러한 HTTP의 stateless 특성으로 Connectionless 로 부터 파생되는 특징이라고 할 수 있다. 클라이언트의 이전 상태 정보를 알 수 없게 되면, 웹 서비스를 하는데 당장에 문제가 생긴다.
  클라이언트가 과거에 로그인을 성공하더라도 로그 정보를 유지할 수가 없다. HTTP는 cookie를 이용해서 이 문제를 해결하고 있다.

- Cookie는 클라이언트와 서버의 상태 정보를 담고 있는 정보조각이다. 로그인을 예로 들자면, 클라이언트가 로그인에 성공하면, 서버는 로그인 정보를 자신의 데이터베이스에 저장하고 동일한 값을 cookie형태로 클라이언트에 보낸다.

첫 요청 시 :

- 클라이언트 로그인 성공 then 서버 로그인정보를 자신의 DB에 저장 (서버는 cookie를 키로하는 값을 데이터베이스에 저장하는 방식으로 "세션"을 유지한다) and then return 쿠키 to 클라이언트
- 클라이언트는 다음 번 요청때 cookie를 서버에 보내는데, 서버는 cookie 값으로 자신의 데이터베이스를 조회해서 로그인 여부를 확인할 수 있다.

두번쨰 요청 시 :

- 클라이언트 request(cookie) to server then 서버는 자신의 DB 조회 and then 로그인여부 확인

<br>

## URL

URL(Uniform Resource Locators)은 서버에 자원을 요청하기 위한 주소입니다.

구조로는 밑에 보이시는 것과 같습니다.

![url](https://user-images.githubusercontent.com/58774316/111725108-cc196900-88a9-11eb-93a8-75c12922659a.png)
