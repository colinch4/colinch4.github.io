---
layout: post
title: "[go] 문자열에서 특정 문자열 인덱스 찾기 (Finding Index of Specific String in String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

문자열에서 특정 문자열이 나타나는 위치를 찾아야 하는 경우가 있습니다. 이럴 때 Go 언어에서는 `strings` 패키지의 `Index` 함수를 사용하여 간단하게 특정 문자열의 인덱스를 찾을 수 있습니다.

## `Index` 함수 사용하기

`Index` 함수는 주어진 문자열에서 지정된 부분 문자열의 첫 번째 인덱스를 반환합니다. 만약 부분 문자열이 존재하지 않는다면 `-1`을 반환합니다.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, World!"
	substr := "World"

	index := strings.Index(str, substr)
	fmt.Println(index) // Output: 7
}
```

위의 예제에서 `Index` 함수를 사용하여 `substr`인 "World"의 인덱스를 찾고 있습니다.

이제 Go 언어에서 문자열에서 특정 문자열의 위치를 찾는 방법에 대해 이해하셨습니다. 더 많은 정보는 [Go 문자열 패키지 문서](https://golang.org/pkg/strings/)를 참고하세요.