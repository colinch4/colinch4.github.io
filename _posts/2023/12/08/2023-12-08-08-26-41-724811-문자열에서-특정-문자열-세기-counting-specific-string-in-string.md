---
layout: post
title: "[go] 문자열에서 특정 문자열 세기 (Counting Specific String in String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

여러분 안녕하세요! 오늘은 Go 언어를 사용하여 문자열에서 특정 문자열을 세는 방법을 알아보겠습니다.

문자열에서 특정 문자열을 세는 것은 Go에서 간단하게 할 수 있습니다. ```strings``` 패키지를 사용하여 이 작업을 수행할 수 있습니다.

다음은 문자열에서 특정 문자열을 세는 방법을 코드로 표현한 예제입니다.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "hello hello world hello"
	substr := "hello"

	count := strings.Count(str, substr)
	fmt.Printf("The count of '%s' in '%s' is: %d", substr, str, count)
}
```

위의 예제 코드에서는 `strings` 패키지의 `Count` 함수를 사용하여 문자열 `str`에서 `substr`의 개수를 세고 그 값을 출력합니다.

이제 코드를 실행해 보면, "hello"라는 문자열이 "hello hello world hello"에서 3번 등장하는 것을 확인할 수 있습니다.

Go에서는 문자열을 다루는데 많은 유용한 함수들을 제공하기 때문에 특정 문자열을 세는 것 또한 간단한 작업으로 수행할 수 있습니다.

이상으로 Go 언어에서 문자열에서 특정 문자열을 세는 방법에 대해 알아보았습니다. 감사합니다!

참고:
- [Go 언어 공식 문서 - strings 패키지](https://golang.org/pkg/strings/)