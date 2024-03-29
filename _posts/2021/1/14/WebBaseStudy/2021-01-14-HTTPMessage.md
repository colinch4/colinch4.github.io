---
layout: post
title: "[웹] HTTP Message"
description: " "
date: 2021-01-14
tags: [network]
comments: true
share: true
---


## HTTP Message

HTTP 메세지의 형식은 다음과 같이 생겼다.

![https://mdn.mozillademos.org/files/13827/HTTPMsgStructure2.png](https://mdn.mozillademos.org/files/13827/HTTPMsgStructure2.png)

![https://68.media.tumblr.com/c1d2d09d6c686f891dce3d71453d84fe/tumblr_oowq4hCTlT1w8w3y8o1_1280.png](https://68.media.tumblr.com/c1d2d09d6c686f891dce3d71453d84fe/tumblr_oowq4hCTlT1w8w3y8o1_1280.png)

HTTP가 동작할 때, 요청/응답 과정을 거치면서 주고받는 메세지가 바로 `HTTP Message`이다.<br> 



## HTTP Method

Request의 http message를 보면, 요청 정보 행에 요청 메소드 타입인 `HTTP Method` 를 볼 수 있다. 한 개의 요청 메세지는 한 개의 HTTP메서드를 가지고 있다. 이름에서 알 수 있듯, 서버가 무슨 일을 해야 하는지 알려주는 역할을 한다.

HTTP Method에는 크게 GET, POST, PUT, DELETE가 있다.

| HTTP METHOD | 설명                                       |
| ----------- | ---------------------------------------- |
| GET         | 클라이언트가 지정한 리소스를 반환                       |
| POST        | 클라이언트의 데이터를 서버 게이트웨이 애플리케이션(웹 프로그램) 으로 보냄 |
| DELETE      | 지정한 리소스를 삭제                              |
| PUT         | 클라이언트가 전송한 데이터를 지정한 이름의 리소스로 저장          |

이 중에서 가장 흔히 쓰이고 중요한 GET,POST에 대해 조금 더 구체적으로 보자.



### GET : 클라이언트가 데이터를 요청할 때

- 주로 정보를 요청할 때 사용된다. 클라이언트가 서버에 URL이 가리키는 웹 문서의 내용을 전송하도록 요구한다.
- 요청한 내용은 서버가 회신하는 응답 메시지의 바디에 포함된다.
- 클라이언트의 입력 폼에 데이터를 입력하면, 이 데이터가 URL의 '?' 뒤에 붙기 때문에 URL에 입력 폼의 내용이 포함되는 셈이다. (따라서 지나치게 긴 데이터를 입력하기엔 무리가 있다.)
- 이 내용은 HTTP Message 중 `Request 정보 행` 에 입력 폼의 내용이 포함된다. (위의 그림 참고)



### POST : 클라이언트의 데이터를 서버에 저장하거나 서버에 저장된 데이터를 변경할 때 

- 주로 정보를 저장하거나 변경할 때 쓰인다. 클라이언트가 서버에 정보를 전송할 수 있도록 해준다.
- 보통 게시판, 방명록처럼 사용자로부터 입력된 정보를 서버에 전달하는 용도.
- 주소창에 입력 폼에 입력한 데이터가 붙지 않기 때문에, 상대적으로 더 많은 데이터를 전송할 수 있다.
- 이 내용은 HTTP Message 중 `Request 바디(본문)` 에 입력폼에 작성한 데이터의 내용이 포함된다.



## HTTP Status

클라이언트에서 데이터를 요청하고 응답(Response)을 받았을 때, 모든 HTTP 응답 메세지는 상태 코드를 갖는다.<br>클라이언트에게 이 응답의 상태가 무엇인지 알려주는 역할을 한다. 세 자리 숫자의 코드로 이루어지며, 이 코드에는 영혼의 친구(ㅋㅋ) "사유구절"이 있다.

### 100번대 코드 : 정보성 상태 코드

- 100 - Continue : 볼 일 없음ㅇㅅㅇ
- 101 - Switching Protocols : HTTP에서 Web Socket으로 프로토콜 전환 시 구경 가능



### 200번대 코드 : 성공

- 200 - OK : 서버가 요청 사항을 성공적으로 수행했고 너에게 이것을 반환한다.
- 204 - No Content : 내가 잘 처리했지만 네게 돌려줄 건 없다.



### 300번대 코드 : 옮겨짐 - 다른 주소로 Redirect했다

- 301 - Moved Permanently : 주소를 영구적으로 이동했으니 새주소로 리다이렉트. 담부터는 새주소 입력해서 와줘🙂
- 302 - Found : 잠시 사정이 생겨 주소를 옮겼으니 리다이렉트.



### 400번대 코드 : 요청 오류 (~~아 망했어요~~)

- 400 - Bad Request : 네가 보낸 요청을 이해 못하겠다...
- 401 - Unauthorized : 권한이 없다. 로그인 해주세요!
- 402 - Payment Required : 유료 페이지이니 돈내놓거라
- 403 - Forbidden : 서버 측에서 요청을 거부
- 404 - Not Found : 페이지를 찾을 수 없음. 삭제되었거나 존재하지 않는 페이지. URL을 다시 잘 보고 주소가 올바로 입력되었는지를 확인함. 



### 500번대 코드 : 서버 오류 (~~아 망했어요2~~)

- 500 - Internal Server Error : 서버 내부 오류. 웹 서버가 요청사항을 수행할 수 없을 경우에 발생함 
- 502 - Bad Gateway : 게이트웨이 상태가 나쁘거나 서버의 과부하 상태일 때 발생