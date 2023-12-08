---
layout: post
title: "[go] 문자열에서 고유한 문자 추출 (Unique Character Extraction from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

고유한 문자를 추출하는 것은 많은 프로그래밍 시나리오에서 유용합니다. 문자열에서 중복된 문자를 제거하거나, 각 문자가 몇 번씩 나타나는지 확인하는 등의 작업이 가능합니다. 이번 포스트에서는 Go 언어를 사용하여 문자열에서 고유한 문자를 추출하는 방법을 알아보겠습니다.

## 문자열에서 고유한 문자 추출하는 방법

```go
package main

import (
	"fmt"
)

func extractUniqueCharacters(str string) string {
	// 문자열의 각 문자를 맵에 저장
	uniqueChars := map[rune]bool{}
	for _, char := range str {
		uniqueChars[char] = true
	}

	// 맵의 키 값을 문자열로 변환
	var result string
	for char := range uniqueChars {
		result += string(char)
	}
	return result
}

func main() {
	str := "hello"
	fmt.Println("원본 문자열:", str)
	fmt.Println("고유한 문자열:", extractUniqueCharacters(str))
}
```

위의 예시 코드는 입력된 문자열에서 중복된 문자들을 제거하고 고유한 문자들만 남긴 후 반환하는 `extractUniqueCharacters` 함수를 포함하고 있습니다. 결과적으로, 이 코드는 "hello" 문자열을 받아 "helo"를 반환합니다.

## 마무리

이렇게 Go 언어에서 문자열에서 고유한 문자를 추출하는 방법에 대해 알아보았습니다. 이러한 테크닉은 데이터 처리나 문자열 조작 등의 다양한 상황에서 활용될 수 있습니다. 관련 코드를 작성하거나 API를 사용하여 더욱 강력하고 효율적인 기능으로 발전시킬 수 있을 것입니다.

참고 문헌:
- [Go 언어 공식 문서](https://golang.org/doc/)
- [Go 언어 위키백과](https://ko.wikipedia.org/wiki/Go_%EC%96%B8%EC%96%B4)

**관련 포스트:**
- [Go에서 문자열 연산 사용하기](link to the post about string operations in Go)