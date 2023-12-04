---
layout: post
title: "[java] REST 통신에서 HTTP 메서드(GET, POST, PUT, DELETE)의 역할은 무엇인가?"
description: " "
date: 2023-12-04
tags: [java]
comments: true
share: true
---

- GET: GET 메서드는 리소스의 정보를 요청할 때 사용됩니다. GET 요청은 서버로부터 리소스의 데이터를 받아와서 클라이언트에게 반환합니다. GET 메서드는 데이터의 조회나 검색에 주로 사용됩니다.

- POST: POST 메서드는 새로운 리소스를 생성할 때 사용됩니다. 클라이언트는 POST 요청을 통해 서버에 데이터를 제출하고, 서버는 이 데이터를 처리하여 새로운 리소스를 생성합니다. 주로 회원가입, 댓글 작성 등의 기능에 사용됩니다.

- PUT: PUT 메서드는 기존의 리소스를 업데이트할 때 사용됩니다. 클라이언트는 PUT 요청을 통해 서버에 업데이트할 데이터를 제출하고, 서버는 해당 리소스를 업데이트합니다. PUT 메서드는 전체 리소스의 업데이트에 사용되며, 부분적인 업데이트를 위해서는 PATCH 메서드를 사용할 수도 있습니다.

- DELETE: DELETE 메서드는 특정 리소스를 삭제할 때 사용됩니다. 클라이언트는 DELETE 요청을 통해 서버에 특정 리소스 삭제를 요청하고, 서버는 해당 리소스를 삭제합니다.

이렇게 HTTP 메서드를 적절하게 사용하여 클라이언트와 서버 간의 효율적인 통신을 할 수 있습니다.

References:
- [MDN Web Docs - HTTP Methods](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods)
- [W3Schools - HTTP Methods](https://www.w3schools.com/tags/ref_httpmethods.asp)