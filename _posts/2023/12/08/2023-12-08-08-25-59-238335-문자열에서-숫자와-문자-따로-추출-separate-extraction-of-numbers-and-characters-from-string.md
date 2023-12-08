---
layout: post
title: "[go] 문자열에서 숫자와 문자 따로 추출 (Separate Extraction of Numbers and Characters from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

여러분은 문자열에서 숫자와 문자를 따로 추출하는 방법을 찾고 계시나요? 예를 들어, "abc123def456"이라는 문자열에서 숫자만 추출하거나, 문자만 추출해야 하는 경우가 있을 것입니다. 이번 글에서는 Go 언어를 사용하여 문자열에서 숫자와 문자를 따로 추출하는 방법에 대해 알아보겠습니다.

## 문자열에서 숫자 추출

먼저, 문자열에서 숫자만 추출하는 방법을 살펴보겠습니다. 이를 위해서는 `unicode` 패키지와 `strings` 패키지를 사용할 수 있습니다. 다음은 숫자만을 추출하는 함수의 예시 코드입니다.

```go
package main

import (
	"fmt"
	"strings"
	"unicode"
)

func extractNumbers(s string) string {
	var result string
	for _, r := range s {
		if unicode.IsDigit(r) {
			result += string(r)
		}
	}
	return result
}

func main() {
	input := "abc123def456"
	numbers := extractNumbers(input)
	fmt.Println("Extracted Numbers:", numbers) // Output: Extracted Numbers: 123456
}
```

위의 코드에서 `extractNumbers` 함수는 문자열을 받아 숫자만을 추출하여 반환합니다. `unicode.IsDigit` 함수를 사용하여 해당 문자가 숫자인지를 확인하고, 숫자일 경우 `result` 변수에 추가합니다.

## 문자열에서 문자 추출

이번에는 문자열에서 문자만 추출하는 방법을 알아보겠습니다. 다음은 문자만을 추출하는 함수의 예시 코드입니다.

```go
func extractLetters(s string) string {
	var result string
	for _, r := range s {
		if unicode.IsLetter(r) {
			result += string(r)
		}
	}
	return result
}
```

위의 코드에서는 `unicode.IsLetter` 함수를 사용하여 해당 문자가 영문자인지를 확인하고, 영문자일 경우 `result` 변수에 추가합니다.

## 결론

이제 여러분은 Go 언어를 사용하여 문자열에서 숫자와 문자를 따로 추출하는 방법을 알게 되었습니다. 위의 예시 코드를 참고하여 원하는 문자열에서 숫자와 문자를 추출해 보세요!