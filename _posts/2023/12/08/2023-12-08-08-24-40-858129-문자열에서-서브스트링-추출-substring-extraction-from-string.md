---
layout: post
title: "[go] 문자열에서 서브스트링 추출 (Substring Extraction from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

Go 언어에서 문자열의 일부를 추출하여 사용해야 할 때가 있습니다. 예를 들어, 특정 위치부터 일정 길이의 서브스트링을 추출하거나 특정 문자열을 포함하는 서브스트링을 찾아야 할 때가 있습니다. Go 언어에서는 이러한 작업을 수행할 수 있는 다양한 방법이 있습니다.

## 특정 위치에서 서브스트링 추출

만약 문자열에서 특정 위치부터 일정 길이의 서브스트링을 추출하고 싶다면 `substring` 함수를 사용할 수 있습니다. 아래는 이를 수행하는 간단한 예시 코드입니다.

```go
package main

import "fmt"

func main() {
    str := "Hello, World"
    substr := str[7:12]
    fmt.Println(substr) // Output: World
}
```

위 예시에서 `str[7:12]`는 `str` 문자열의 7번째 위치부터 12번째 위치 이전까지의 서브스트링을 추출합니다.

## 특정 문자열을 포함하는 서브스트링 찾기

Go 언어에서는 `strings` 패키지를 사용하여 특정 문자열을 포함하는 서브스트링을 찾을 수 있습니다. 아래는 이를 수행하는 예시 코드입니다.

```go
package main

import (
    "fmt"
    "strings"
)

func main() {
    str := "Hello, World"
    if strings.Contains(str, "World") {
        fmt.Println("Found!") // Output: Found!
    }
}
```

위 예시에서 `strings.Contains` 함수는 `str` 문자열에 "World" 문자열이 포함되어 있는지 확인합니다.

## 결론

Go 언어에서는 문자열에서 서브스트링을 추출하거나 특정 문자열을 포함하는 서브스트링을 찾는 다양한 방법을 제공합니다. 이러한 기능들을 활용하여 다양한 상황에서 문자열 작업을 보다 편리하게 수행할 수 있습니다.