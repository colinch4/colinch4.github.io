---
layout: post
title: "[go] 문자열에서 특정 단어 추출 (Word Extraction from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

언어: Go

인기있는 프로그래밍 언어인 Go는 문자열에서 특정 단어를 추출하는데 사용하기 편리한 기능을 제공합니다.

## 문자열에서 단어 추출하기

Go에서 문자열을 단어로 나누고 추출하는 방법은 `strings` 패키지의 `Split` 함수를 사용하는 것입니다. 이 함수는 문자열을 특정 구분자를 기준으로 나누어 문자열의 조각으로 만들어주는데 사용됩니다. 

다음은 문자열에서 단어를 추출하는 예제 코드입니다.


```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	sentence := "This is a sample sentence"
	words := strings.Split(sentence, " ")
	for _, word := range words {
		fmt.Println(word)
	}
}
```

위 코드는 주어진 문장을 공백을 기준으로 단어로 분리하고, 각 단어를 출력합니다.

## 결과

```plaintext
This
is
a
sample
sentence
```

위 결과는 입력된 문장을 공백을 기준으로 단어로 분리한 결과를 나타냅니다.

다음과 같은 방법으로 Go를 사용하여 문자열에서 특정 단어를 추출할 수 있습니다. 

이를 통해 Go 언어를 사용하면 문자열을 다룰 때 간편하게 단어를 추출하고 다양한 작업에 활용할 수 있습니다.

## 참고 자료
- Go 표준 라이브러리: https://pkg.go.dev/std

위의 예제 코드 및 설명은 Go 표준 라이브러리에 대한 이해와 같은 참고 자료를 참조하여 작성되었습니다.