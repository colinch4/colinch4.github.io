---
layout: post
title: "[go] 공백으로 구분된 문자열 분해 (Whitespace-separated String Parsing)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

일반적으로, 주어진 문자열을 공백으로 구분해야 하는 경우가 많습니다. 예를 들어, "Hello world"와 같은 문자열을 분해하여 "Hello"와 "world"라는 두 개의 단어로 나누는 작업이 필요할 수 있습니다.

이를 위해 Go 언어에서는 `strings.Fields()` 함수를 사용하여 문자열을 공백으로 분리할 수 있습니다.

아래는 간단한 예제 코드입니다.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	input := "Hello world"
	words := strings.Fields(input)

	for _, word := range words {
		fmt.Println(word)
	}
}
```

위 예제 코드는 "Hello world"라는 입력 문자열을 공백으로 분해하고, 분해된 각 단어를 개행하여 출력합니다.

`strings.Fields()` 함수는 문자열을 공백으로 나누어 []string 형태로 반환합니다.

**참고 자료:**
- [Go 언어 공식 문서 - strings 패키지](https://golang.org/pkg/strings/)

위와 같은 방법으로 공백으로 구분된 문자열을 분해하여 처리할 수 있습니다.