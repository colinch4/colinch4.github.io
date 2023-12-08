---
layout: post
title: "[go] net/http 패키지의 request 객체와 response 객체"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

Go 언어의 `net/http` 패키지는 HTTP 클라이언트 및 서버의 구현을 제공합니다. 이 패키지를 사용하면 HTTP 요청(request)과 응답(response)을 다룰 수 있습니다. 요청 객체와 응답 객체에는 각각 다양한 속성들이 있으며, 이 두 객체를 통해 HTTP 통신을 관리할 수 있습니다. 이번 포스트에서는 Go의 `net/http` 패키지를 사용하여 요청 객체와 응답 객체를 조작하는 방법에 대해 알아보겠습니다.

## request 객체

HTTP 요청을 보내기 위해서는 요청 객체를 생성해야 합니다. Go의 `net/http` 패키지에서는 `http.Request` 구조체를 사용하여 요청 객체를 표현합니다. 요청 객체를 생성하려면 HTTP 메서드(`GET`, `POST`, `PUT` 등), URL, 요청 바디(body) 등의 정보를 설정해야 합니다.

아래는 간단한 GET 요청을 보내는 예제 코드입니다.

```go
package main

import (
	"bytes"
	"fmt"
	"net/http"
)

func main() {
	url := "https://api.example.com/data"
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		// 오류 처리
	}

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		// 오류 처리
	}

	defer resp.Body.Close()

	// 응답 처리
	fmt.Println(resp.Status)
}
```

## response 객체

서버로부터 받은 HTTP 응답은 응답 객체를 통해 다룰 수 있습니다. Go의 `net/http` 패키지에서는 `http.Response` 구조체를 사용하여 응답 객체를 표현합니다. 응답 객체에는 상태 코드, 응답 바디(body) 등의 정보가 포함되어 있습니다.

아래는 서버로부터 응답을 받아 처리하는 예제 코드입니다.

```go
package main

import (
	"fmt"
	"net/http"
)

func main() {
	resp, err := http.Get("https://api.example.com/data")
	if err != nil {
		// 오류 처리
	}

	defer resp.Body.Close()

	// 상태 코드 확인
	fmt.Println(resp.Status)
}
```

`http.Response` 구조체에는 다양한 메서드와 속성들이 있어서, 응답 객체를 다양한 방법으로 조작할 수 있습니다.

## 결론

Go의 `net/http` 패키지를 사용하여 HTTP 요청과 응답을 다룰 때, 요청 객체와 응답 객체를 적절히 활용하는 것이 중요합니다. 요청 객체에는 클라이언트가 서버로 보내는 요청 정보를 설정하고, 응답 객체에는 서버로부터 받은 응답 정보를 처리합니다. 이러한 객체들을 올바르게 다루면 안정적이고 효율적인 HTTP 통신을 구현할 수 있습니다.

이러한 HTTP 요청 객체와 응답 객체를 다루는 방법은 Go 언어를 사용하는 웹 애플리케이션 개발에 있어서 매우 중요한 부분이므로, 실제 프로젝트에 적용하기 전에 자세히 학습하고 숙지하는 것이 좋습니다.

더 많은 정보를 원하신다면 https://golang.org/pkg/net/http/ 를 확인해 보세요!