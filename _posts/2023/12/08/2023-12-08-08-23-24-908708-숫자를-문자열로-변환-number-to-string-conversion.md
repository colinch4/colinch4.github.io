---
layout: post
title: "[go] 숫자를 문자열로 변환 (Number to String Conversion)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

어떤 이유로든 **Go 언어**에서 **숫자를 문자열로** 변환해야할 때가 있습니다. 이 블로그 포스트에서는 **Go 언어**에서 **숫자를 문자열로 변환하는** 여러 가지 방법에 대해 알아보겠습니다.

1. **fmt 패키지** 사용
2. **strconv 패키지** 사용
3. **strconv.Itoa 함수** 사용

## 1. fmt 패키지 사용
**fmt 패키지**는 **포맷된 문자열**을 생성하기 위한 함수를 제공합니다. 아래의 예제는 **fmt.Sprintf 함수**를 사용하여 숫자를 문자열로 변환하는 방법을 보여줍니다.

```go
package main

import "fmt"

func main() {
    num := 42
    str := fmt.Sprintf("%d", num)
    fmt.Println(str)
}
```

## 2. strconv 패키지 사용
**strconv 패키지**는 **문자열과 숫자**간의 변환을 제공합니다. **strconv.Itoa 함수**를 사용하여 **정수를 문자열로** 변환할 수 있습니다.

```go
package main

import (
    "fmt"
    "strconv"
)

func main() {
    num := 42
    str := strconv.Itoa(num)
    fmt.Println(str)
}
```

## 3. strconv.Itoa 함수 사용
**strconv.Itoa 함수**는 **정수를 문자열로** 변환하는 간단한 방법을 제공합니다.

```go
package main

import (
    "fmt"
    "strconv"
)

func main() {
    num := 42
    str := strconv.Itoa(num)
    fmt.Println(str)
}
```

이러한 방법을 사용하여 **Go 언어**에서 **숫자를 문자열로** 변환할 수 있습니다. 선택한 방법에 따라 코드의 가독성과 성능을 고려하여 적절한 방법을 선택하시면 됩니다.

**참고 자료**:
- [Go 언어 공식 문서 - fmt 패키지](https://golang.org/pkg/fmt/)
- [Go 언어 공식 문서 - strconv 패키지](https://golang.org/pkg/strconv/)