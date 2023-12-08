---
layout: post
title: "[go] 문자열에서 대문자 추출 (Uppercase Extraction from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---
1. [소개](#1-소개)
2. [예시 코드](#2-예시-코드)
3. [결론](#3-결론)
4. [참고 자료](#4-참고-자료)

## 1. 소개
이번 포스트에서는 *Go* 언어를 사용하여 주어진 문자열에서 대문자를 추출하는 방법에 대해 알아보겠습니다. 이 기술은 특히 대소문자를 구분하여 문자열을 처리해야 하는 경우에 유용합니다.

## 2. 예시 코드
다음은 *Go* 언어를 사용하여 주어진 문자열에서 대문자를 추출하는 예시 코드입니다.

```go
package main

import (
	"fmt"
	"strings"
)

func extractUppercase(input string) string {
	var result string
	for _, char := range input {
		if 'A' <= char && char <= 'Z' {
			result += string(char)
		}
	}
	return result
}

func main() {
	input := "Hello World"
	uppercaseLetters := extractUppercase(input)
	fmt.Println(uppercaseLetters) // 출력: HW
}
```

위 예시 코드에서 `extractUppercase` 함수는 입력 문자열을 순회하면서 각 문자가 대문자인지 확인하고, 대문자인 경우 결과 문자열에 추가합니다. 마지막으로 추출된 대문자가 반환됩니다.

## 3. 결론
이렇게하여, *Go* 언어를 사용하여 문자열에서 대문자를 추출하는 방법에 대해 알아보았습니다. 이 기술은 텍스트 처리 및 데이터 변환 작업에 유용하게 사용될 수 있습니다.

## 4. 참고 자료
- [Go 언어 공식 문서](https://golang.org/doc/)
- [A Tour of Go](https://tour.golang.org/)