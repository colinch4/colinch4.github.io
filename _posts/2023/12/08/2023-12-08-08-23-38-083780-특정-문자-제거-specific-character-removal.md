---
layout: post
title: "[go] 특정 문자 제거 (Specific Character Removal)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

특정 문자를 제거할 때 Go 언어에서는 `strings` 패키지의 `ReplaceAll` 함수를 사용할 수 있습니다. 이 함수를 사용하면 문자열에서 특정 문자를 다른 문자로 교체하거나 제거할 수 있습니다.

예를 들어, 주어진 문자열에서 모든 공백을 제거하려면 다음과 같이 `ReplaceAll` 함수를 사용할 수 있습니다:

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "This is a sample sentence with spaces"
	newStr := strings.ReplaceAll(str, " ", "")
	fmt.Println(newStr)
}
```

위의 예제에서는 `strings.ReplaceAll` 함수를 사용하여 `str` 문자열에서 공백을 모두 제거했습니다. 실행 결과는 "Thisisasamplesentencewithspaces"가 될 것입니다.

이와 같이 `strings.ReplaceAll` 함수를 사용하여 특정 문자를 제거하거나 교체할 수 있습니다.

더 자세한 내용은 [Go 공식 문서](https://golang.org/pkg/strings/#ReplaceAll)를 참조하세요.