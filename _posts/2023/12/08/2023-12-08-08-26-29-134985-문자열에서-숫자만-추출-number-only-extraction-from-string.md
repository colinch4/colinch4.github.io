---
layout: post
title: "[go] 문자열에서 숫자만 추출 (Number-only Extraction from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

어떤 경우에는 문자열에서 숫자만을 추출해야 하는 일이 발생합니다. 예를 들어, 사용자로부터 입력받은 문자열에서 숫자를 추출하여 계산하는 경우 등이 있습니다. 이번 글에서는 Go 언어를 사용하여 문자열에서 숫자만을 추출하는 방법에 대해 알아보겠습니다.

## 방법 1: 정규표현식 사용

정규표현식을 사용하여 문자열에서 숫자만을 추출할 수 있습니다. 다음은 이를 수행하는 코드 예시입니다.

```go
package main

import (
	"fmt"
	"regexp"
)

func main() {
	str := "abc 123 def 456 ghi"
	re := regexp.MustCompile("[0-9]+")
	nums := re.FindAllString(str, -1)
	for _, num := range nums {
		fmt.Println(num)
	}
}
```

위의 코드는 입력된 문자열에서 정규표현식 `[0-9]+`에 해당하는 숫자를 추출하여 출력합니다.

## 방법 2: 문자열 순회

또 다른 방법은 문자열을 순회하면서 숫자인지를 판별하여 추출하는 것입니다. 다음은 해당 방법의 코드 예시입니다.

```go
package main

import (
	"fmt"
)

func main() {
	str := "abc 123 def 456 ghi"
	num := ""
	for _, char := range str {
		if char >= '0' && char <= '9' {
			num += string(char)
		} else if num != "" {
			fmt.Println(num)
			num = ""
		}
	}
}
```

위의 코드는 문자열을 순회하면서 숫자를 발견하면 `num` 변수에 추가하고, 숫자가 아닌 경우에는 `num` 변수를 출력합니다.

## 결론

Go 언어로 문자열에서 숫자만을 추출하는 방법에 대해 알아보았습니다. 정규표현식을 사용하는 방법과 문자열을 순회하여 숫자를 추출하는 방법에 대해 다루었습니다.

정규표현식 방법은 더 유연하게 사용할 수 있지만, 간단한 경우에는 문자열 순회 방법을 사용하여 간단히 숫자를 추출할 수 있습니다. 각 상황에 맞게 적절한 방법을 선택하여 활용하는 것이 중요합니다.

참고 문헌: 
- [Go 언어 정규표현식 패키지](https://golang.org/pkg/regexp/)
- [Go 언어 문자열 패키지](https://golang.org/pkg/strings/)

**참고:** 본 예시 코드는 간단한 예시를 위해 입력값에 대한 유효성 검사를 수행하지 않았습니다. 실제 상황에서는 입력값에 대한 적절한 유효성 검사를 반드시 수행해야 합니다.

수정 사항을 제안하거나 추가적인 도움이 필요한 경우 언제든지 연락해주세요!