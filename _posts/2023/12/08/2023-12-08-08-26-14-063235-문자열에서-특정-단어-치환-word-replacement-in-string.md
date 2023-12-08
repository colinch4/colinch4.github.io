---
layout: post
title: "[go] 문자열에서 특정 단어 치환 (Word Replacement in String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

Go 언어로 문자열에서 특정 단어를 다른 단어로 치환하는 방법을 알아보겠습니다.

## strings 패키지 활용

Go에서는 `strings` 패키지를 활용하여 문자열에서 원하는 단어를 치환할 수 있습니다. 예를 들어, `strings` 패키지의 `Replace` 함수를 사용하여 문자열에서 특정 단어를 원하는 단어로 치환할 수 있습니다.

다음은 `strings` 패키지를 사용하여 문자열에서 특정 단어를 치환하는 간단한 예제입니다.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, world!"
	newStr := strings.Replace(str, "Hello", "Hi", -1)
	fmt.Println(newStr)
}
```

위의 예제에서는 `Hello, world!`라는 문자열에서 `Hello`를 `Hi`로 치환한 결과를 출력합니다.

Go 언어에서는 `strings` 패키지를 활용하여 문자열 처리를 간편하게 할 수 있습니다.

이제 `strings` 패키지의 `Replace` 함수를 통해 문자열에서 특정 단어를 치환하거나 변형하는 방법을 이해하셨습니다.

**참고 문헌**: [Go 문자열 함수 (Go by Example)](https://gobyexample.com/string-functions)

이상으로 Go 언어에서 문자열에서 특정 단어 치환을 다루는 방법에 대해 알아보았습니다.