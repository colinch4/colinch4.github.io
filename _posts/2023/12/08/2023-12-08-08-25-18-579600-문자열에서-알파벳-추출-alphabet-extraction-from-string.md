---
layout: post
title: "[go] 문자열에서 알파벳 추출 (Alphabet Extraction from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

문자열에서 알파벳 문자만을 추출해야 하는 경우가 종종 있습니다. 이를 처리할 수 있는 여러 가지 방법이 있지만, 다음은 Go 언어에서 문자열에서 알파벳 문자만을 추출하는 방법에 대한 예시 코드입니다.

## strings 패키지 활용

`strings` 패키지를 사용하여 문자열에서 알파벳 문자를 추출해 봅시다.
```go
package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	str := "Hello123World456"
	alphabetStr := ""

	for _, char := range str {
		if unicode.IsLetter(char) {
			alphabetStr += string(char)
		}
	}
	fmt.Println(alphabetStr) // Output: HelloWorld
}
```

위의 코드는 `Hello123World456` 문자열에서 숫자를 제외한 알파벳 문자만을 추출하여 `HelloWorld`를 출력합니다.

이는 `strings` 패키지의 `IsLetter` 함수를 활용하여 문자가 알파벳 문자인지 여부를 확인하고, 알파벳 문자인 경우에만 결과 문자열에 추가하는 방식으로 동작합니다.

이 방법을 사용하여 Go 언어에서 문자열에서 알파벳 문자만을 추출할 수 있습니다.