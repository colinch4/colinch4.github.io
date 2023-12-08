---
layout: post
title: "[go] 문자열에서 소문자 추출 (Lowercase Extraction from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

이번에는 **Go** 언어에서 문자열에서 소문자를 추출하는 방법에 대해 알아보겠습니다.

## strings 패키지 사용하기

Go 언어에서는 `strings` 패키지를 사용하여 문자열을 다룰 수 있습니다. 이 패키지에는 문자열에서 소문자를 추출하는 함수가 포함되어 있습니다.

다음은 `strings` 패키지의 `ToLower` 함수를 사용하여 문자열에서 소문자를 추출하는 예제 코드입니다.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello World"
	lowercaseStr := strings.ToLower(str)
	fmt.Println("Lowercase: ", lowercaseStr)
}
```

위의 코드는 "Hello World"라는 문자열을 모두 소문자로 변환하여 출력하는 예제입니다.

## 결론

Go 언어에서는 `strings` 패키지를 활용하여 문자열에서 소문자를 추출할 수 있습니다. 이를 통해 문자열을 손쉽게 다룰 수 있습니다.

더 많은 자세한 내용은 [공식 Go 언어 문서](https://golang.org/pkg/strings/)를 참고할 수 있습니다.