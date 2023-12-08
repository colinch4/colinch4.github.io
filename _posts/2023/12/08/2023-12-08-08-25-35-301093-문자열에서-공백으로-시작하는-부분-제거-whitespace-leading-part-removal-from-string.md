---
layout: post
title: "[go] 문자열에서 공백으로 시작하는 부분 제거 (Whitespace-leading Part Removal from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---
- [소개](#introduction)
- [해결책: Go를 사용한 문자열 앞의 공백 제거](#solution-removing-leading-whitespace-in-go)
- [예제 코드](#example-code)
- [결론](#conclusion)
- [참고 자료](#references)

## 소개 {#introduction}
문자열에서 공백으로 시작하는 부분을 제거하는 것은 종종 발생하는 작업입니다. 특히 Go 언어에서는 문자열 처리를 위해 이를 수행하는 방법을 알고 있는 것이 중요합니다.

본 문서에서는 Go 언어를 사용하여 문자열에서 앞에 있는 공백을 제거하는 방법에 대해 알아보겠습니다.

## 해결책: Go를 사용한 문자열 앞의 공백 제거 {#solution-removing-leading-whitespace-in-go}
Go 언어에서 앞에 있는 공백을 제거하는 가장 간단한 방법은 `strings` 패키지의 `TrimLeft` 함수를 사용하는 것입니다. 이 함수는 문자열의 앞쪽에서 지정된 문자 집합에 속하는 모든 문자를 제거한 결과를 반환합니다.

`TrimLeft` 함수는 다음과 같은 방식으로 사용할 수 있습니다.
```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "   Hello, world!"
	trimmedStr := strings.TrimLeft(str, " ")

	fmt.Println(trimmedStr) // Output: "Hello, world!"
}
```
위 예제에서 `TrimLeft` 함수는 문자열 `str`의 시작 부분에서 공백을 모두 제거하고, 결과로 "Hello, world!"를 반환합니다.

## 예제 코드 {#example-code}
다음은 `TrimLeft` 함수를 사용하여 문자열의 앞에 있는 공백을 제거하는 예제 코드입니다.
```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "   Hello, world!"
	trimmedStr := strings.TrimLeft(str, " ")

	fmt.Println(trimmedStr) // Output: "Hello, world!"
}
```

## 결론 {#conclusion}
Go 언어에서는 `strings` 패키지의 `TrimLeft` 함수를 사용하여 문자열의 앞에 있는 공백을 손쉽게 제거할 수 있습니다. 이를 통해 문자열을 다루는 과정에서 발생하는 불필요한 공백을 간편하게 처리할 수 있습니다.

위의 예제 코드를 참고하여, Go 언어에서 문자열의 앞에 있는 공백을 효과적으로 제거해보시기 바랍니다.

## 참고 자료 {#references}
- [Go Strings Package Documentation](https://pkg.go.dev/strings)