---
layout: post
title: "[go] 문자열에서 특정 패턴의 값 추출 (Value Extraction based on String Pattern)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

이번에는 Golang에서 문자열에서 정규 표현식을 사용하여 **특정 패턴**의 값 추출하는 방법에 대해 알아보겠습니다.

## 1. 정규 표현식 패턴 정의
먼저, 추출하고자 하는 값의 패턴을 정의해야 합니다. 예를 들어, 전화번호나 이메일 주소와 같은 특정 형식의 값이 있다면 해당 값의 패턴을 정의합니다.

```go
// 전화번호 패턴 정의
phoneNumberPattern := `\d{3}-\d{4}-\d{4}`
```

## 2. 정규 표현식으로 값 추출
정의한 패턴을 사용하여 문자열에서 값을 추출할 수 있습니다.

```go
package main

import (
    "fmt"
    "regexp"
)

func main() {
    input := "제 전화번호는 010-1234-5678입니다."
    phoneNumberPattern := `\d{3}-\d{4}-\d{4}`

    re := regexp.MustCompile(phoneNumberPattern)
    phoneNumber := re.FindString(input)

    fmt.Println(phoneNumber)
}
```

## 3. 값 추출
위 코드를 실행하면, **010-1234-5678** 이라는 전화번호가 추출되어 출력될 것입니다.

이와 같이 Golang의 `regexp` 패키지를 사용하여 문자열에서 정규 표현식에 맞는 값을 추출할 수 있습니다. 이를 응용하여 다양한 형식의 값도 추출할 수 있습니다.

## 참고 자료
- [Golang 정규 표현식 패키지 - regexp](https://pkg.go.dev/regexp)
- [정규 표현식 사용하기](https://wikidocs.net/19240)

Golang에서의 문자열 패턴 인식 및 값 추출에 대해 알아보았습니다. 원하는 패턴을 정의하고 `regexp` 패키지를 사용하여 값을 추출해 보세요.