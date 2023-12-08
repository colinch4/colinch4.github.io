---
layout: post
title: "[go] 문자열에서 특정 문자 세기 (Counting Specific Character in String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

Go 언어를 사용하여 문자열에서 특정 문자의 발생 횟수를 세는 방법에 대해 알아보겠습니다.

## strings.Count 함수 사용하기

Go 언어의 `strings` 패키지에는 문자열에서 특정 부분 문자열이 발생하는 횟수를 세는 함수인 `Count`가 있습니다. 이 함수를 사용하여 특정 문자의 발생 횟수를 쉽게 구할 수 있습니다.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "hello, world"
	character := "l"
	count := strings.Count(str, character)
	fmt.Printf("Character '%s' appears %d times in the string\n", character, count)
}
```

위의 예제 코드에서는 `strings.Count` 함수를 사용하여 문자열 "hello, world"에서 문자 'l'의 발생 횟수를 세고, 그 결과를 출력합니다.

이제 당신도 Go 언어를 사용하여 문자열에서 특정 문자를 세는 방법을 알게 되었습니다!