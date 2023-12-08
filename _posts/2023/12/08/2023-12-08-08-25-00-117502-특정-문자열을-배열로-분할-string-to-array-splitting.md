---
layout: post
title: "[go] 특정 문자열을 배열로 분할 (String to Array Splitting)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

문자열을 배열로 분할하는 방법에는 다양한 방법이 있습니다. 이 포스트에서는 Go 언어에서 문자열을 배열로 분할하는 방법을 살펴보겠습니다.

## strings 패키지의 Split 함수 사용

Go 언어의 strings 패키지에는 문자열을 분할하는데 사용할 수 있는 Split 함수가 있습니다. Split 함수는 지정한 구분자를 기준으로 문자열을 분할하여 배열로 반환합니다.

예를 들어, 다음은 공백을 기준으로 문자열을 분할하여 배열로 만드는 예제 코드입니다.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello World"
	arr := strings.Split(str, " ")
	
	for _, val := range arr {
		fmt.Println(val)
	}
}
```

위의 코드는 "Hello World"라는 문자열을 공백을 기준으로 분할하여 "Hello"와 "World"라는 두 개의 요소를 가지는 배열을 만들고, 각 요소를 출력하는 예제입니다.

## 결과

위의 예제 코드를 실행하면 다음과 같은 결과가 출력됩니다.

```
Hello
World
```

문자열을 배열로 분할하는 또 다른 방법으로는 정규표현식을 사용하는 것이 있습니다. 필요에 따라 적합한 방법을 선택하여 문자열을 배열로 분할할 수 있습니다.

## 참고 자료

- [Go 언어 strings 패키지 문서](https://pkg.go.dev/strings)