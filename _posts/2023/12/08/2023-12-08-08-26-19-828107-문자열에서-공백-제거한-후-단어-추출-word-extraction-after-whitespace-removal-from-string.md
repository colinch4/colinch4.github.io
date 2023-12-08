---
layout: post
title: "[go] 문자열에서 공백 제거한 후 단어 추출 (Word Extraction after Whitespace Removal from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

이번에는 **Golang**에서 문자열에서 공백을 제거한 후 단어를 추출하는 방법에 대해 알아보겠습니다.

## 문자열에서 공백 제거하기

우선 문자열에서 공백을 제거하는 방법은 `strings` 패키지의 `Fields` 함수를 사용하는 것입니다. 예를 들어, 다음과 같이 입력할 수 있습니다:

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello,  Golang  World"
	words := strings.Fields(str)
	fmt.Println(words)
}
```

위의 예시 코드를 실행하면, 결과로 `Hello,`, `Golang`, `World`가 출력됩니다.

## 추출된 단어 사용하기

이제 공백이 제거된 문자열에서 추출된 단어를 활용하는 방법을 살펴보겠습니다. 예를 들어, 각 단어에 대해 작업을 수행하거나 단어의 개수를 세는 등의 다양한 작업을 할 수 있습니다.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello,  Golang  World"
	words := strings.Fields(str)

	for _, word := range words {
		fmt.Println(word)
	}
}
```

위의 예시 코드는 추출된 각 단어를 새로운 라인에 출력합니다.

이제 공백이 제거된 문자열에서 단어를 추출하는 방법에 대해 알게 되었습니다. 이러한 기술은 데이터 처리 및 텍스트 분석과 같은 다양한 응용 프로그램에서 유용하게 활용될 수 있습니다.

## 참고 자료
- [Golang strings 패키지 문서](https://pkg.go.dev/strings)

이상으로 공백이 제거된 문자열에서 단어를 추출하는 방법에 대해 살펴보았습니다. 도움이 되길 바랍니다!