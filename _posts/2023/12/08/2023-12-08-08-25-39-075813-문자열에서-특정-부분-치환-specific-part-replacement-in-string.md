---
layout: post
title: "[go] 문자열에서 특정 부분 치환 (Specific Part Replacement in String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

일부 문자열을 변경하고 싶을 때가 있습니다. 예를 들어, "Hello, [name]! How are you?" 라는 문자열이 있을 때, "[name]" 부분을 사용자의 실제 이름으로 변경하고 싶을 수 있습니다. 이런 경우 Go에서는 `strings.Replace` 함수를 사용하여 간단하게 처리할 수 있습니다.

다음은 `strings.Replace` 함수의 예제 코드입니다.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, [name]! How are you?"
	replacedStr := strings.Replace(str, "[name]", "Alice", -1)
	fmt.Println(replacedStr)
}
```

위의 코드에서 `strings.Replace` 함수는 다음과 같은 형식을 갖습니다.

```go
strings.Replace(원본문자열, 대상문자열, 치환할문자열, 치환횟수)
```

위의 코드는 "Hello, [name]! How are you?" 문자열에서 "[name]" 부분을 "Alice"로 치환하여 출력합니다.

더 자세한 내용은 [Go 언어 공식 문서](https://golang.org/pkg/strings/#Replace) 를 참고해 주세요.