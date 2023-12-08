---
layout: post
title: "[go] 문자열을 숫자로 변환 (String to Number Conversion)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

## 개요
이번 글에서는 Go 언어에서 **문자열을 숫자로 변환하는 방법**에 대해 알아보겠습니다. Go 언어는 기본적으로 문자열을 숫자로 변환하는 내장된 기능을 제공하기 때문에 간단한 방법으로 변환이 가능합니다.

## strconv 패키지 활용
Go 언어에서 문자열을 숫자로 변환하기 위해서는 `strconv` 패키지의 `Atoi` 또는 `ParseFloat` 함수를 사용하면 됩니다.

### 문자열을 정수로 변환하기
아래는 문자열을 정수로 변환하는 예제 코드입니다.
```go
package main

import (
	"fmt"
	"strconv"
)

func main() {
	str := "123"
	num, err := strconv.Atoi(str)
	if err != nil {
		fmt.Println("변환 에러:", err)
		return
	}
	fmt.Println("정수로 변환 결과:", num)
}
```

### 문자열을 부동소수점으로 변환하기
아래는 문자열을 부동소수점으로 변환하는 예제 코드입니다.
```go
package main

import (
	"fmt"
	"strconv"
)

func main() {
	str := "3.14"
	num, err := strconv.ParseFloat(str, 64)
	if err != nil {
		fmt.Println("변환 에러:", err)
		return
	}
	fmt.Println("부동소수점으로 변환 결과:", num)
}
```

## 결론
Go 언어에서 문자열을 숫자로 변환하기 위해서는 `strconv` 패키지의 함수를 사용하면 간단하게 변환할 수 있습니다. 올바른 에러 처리를 통해 안정적으로 변환을 할 수 있도록 주의해야 합니다.

더 많은 정보는 [Go 공식 문서](https://golang.org/pkg/strconv/)를 참조하세요.