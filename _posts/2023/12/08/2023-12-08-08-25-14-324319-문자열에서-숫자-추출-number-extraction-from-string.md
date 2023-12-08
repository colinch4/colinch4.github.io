---
layout: post
title: "[go] 문자열에서 숫자 추출 (Number Extraction from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

일반적으로 프로그래밍에서, 문자열에서 숫자를 추출해야 하는 경우가 있습니다. 예를 들어, 사용자가 입력한 문자열에서 숫자만을 추출하거나, 특정 패턴에 맞는 숫자를 찾아야 할 때가 있습니다. 이번 블로그에서는 Go 언어를 사용하여 문자열에서 숫자를 추출하는 방법에 대해 알아보겠습니다.

## 방법 1: 정규표현식 사용

Go 언어에서는 정규표현식 패키지를 사용하여 문자열에서 숫자를 추출할 수 있습니다. 아래 예제는 정규표현식을 사용하여 문자열에서 모든 숫자를 추출하는 방법을 보여줍니다.

```go
package main

import (
	"fmt"
	"regexp"
)

func main() {
	str := "I have 2 apples and 3 oranges"
	re := regexp.MustCompile("\\d+")
	nums := re.FindAllString(str, -1)
	for _, num := range nums {
		fmt.Println(num)
	}
}
```

위 예제에서 `\\d+`는 하나 이상의 숫자에 해당하는 정규표현식을 나타냅니다. `FindAllString` 함수를 사용하여 해당 정규표현식에 일치하는 모든 숫자를 찾아냅니다.

## 방법 2: 루프를 사용하여 숫자 추출

정규표현식을 사용하지 않고도 문자열에서 숫자를 추출할 수 있습니다. 아래 예제는 문자열을 반복하면서 각 문자가 숫자인지 확인하여 숫자를 추출하는 방법을 보여줍니다.

```go
package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	str := "The price is $15.99"
	var numStr string
	for _, char := range str {
		if unicode.IsDigit(char) {
			numStr += string(char)
		}
	}
	fmt.Println(numStr)
}
```

위 예제는 문자열을 반복하면서 `unicode.IsDigit` 함수를 사용하여 숫자를 찾아냅니다.

## 결론

이번 글에서는 Go 언어를 사용하여 문자열에서 숫자를 추출하는 두 가지 방법을 살펴보았습니다. 정규표현식을 사용하는 방법과 루프를 이용하는 방법이 있으며, 각각의 상황에 맞게 적절한 방법을 선택하면 됩니다.

더 많은 정보는 [Go 언어 공식 문서](https://golang.org/pkg/)에서 확인할 수 있습니다.

**참고 문헌:**
- https://golang.org/pkg/
- https://pkg.go.dev/regexp

이상으로 문자열에서 숫자를 추출하는 방법에 대해 알아보았습니다. 감사합니다!