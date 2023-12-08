---
layout: post
title: "[go] 문자열 사이의 공백 제거 (Whitespace Removal between Strings)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

때로는 문자열을 다룰 때 불필요한 공백을 제거해야 할 때가 있습니다. 특히, 두 문자열 사이의 공백을 제거하는 작업은 텍스트 처리에서 매우 일반적입니다. 이번 포스트에서는 Go 언어로 두 문자열 사이의 공백을 제거하는 방법에 대해 알아보겠습니다.

## strings 패키지 활용

Go 언어의 `strings` 패키지는 문자열 처리에 유용한 함수들을 제공합니다. 두 문자열을 `strings.TrimSpace()` 함수를 사용하여 처리하면 됩니다. 이 함수는 주어진 문자열의 양 끝에서 모든 공백을 제거합니다.

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	str1 := "   Hello,   "
	str2 := "   World!   "

	result := strings.TrimSpace(str1) + strings.TrimSpace(str2)
	fmt.Println(result) // 출력: "Hello,World!"
}
```

위의 예제에서는 `strings.TrimSpace()` 함수를 사용하여 `str1`과 `str2`에서 공백을 제거한 후 두 문자열을 연결하여 "Hello, World!" 문자열을 얻었습니다.

두 문자열에 모두 `strings.TrimSpace()` 함수를 적용하고 나서 결합하는 대신에 두 문자열의 연결 후 `strings.TrimSpace()` 함수를 한 번만 사용할 수도 있습니다.

이 방법을 사용하면 문자열 간의 공백을 효과적으로 제거할 수 있으며, 코드를 간결하게 유지할 수 있습니다.

## 마치며

이번 포스트에서는 Go 언어를 사용하여 두 문자열 사이의 공백을 제거하는 방법에 대해 살펴보았습니다. `strings.TrimSpace()` 함수를 활용하여 문자열 처리 시 공백을 효과적으로 제거할 수 있습니다. 이를 통해 문자열 데이터를 다루는 데 있어 불필요한 공백으로 인한 문제를 효과적으로 해결할 수 있을 것입니다.