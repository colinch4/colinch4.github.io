---
layout: post
title: "[go] 문자열에서 고유한 값 추출 (Unique Values Extraction from String)"
description: " "
date: 2023-12-08
tags: [go]
comments: true
share: true
---

일부 경우에는 문자열에서 중복되지 않는 고유한 값을 추출해야 할 때가 있습니다. 이를 위해 Go 언어에서는 `map`을 사용하여 간단하고 효율적으로 고유한 값들을 추출할 수 있습니다. 예를 들어, 주어진 문자열에서 중복되지 않는 모든 문자를 추출하는 방법을 다음과 같이 살펴볼 수 있습니다.

```go
package main

import "fmt"

func uniqueValues(input string) []rune {
    uniqueMap := make(map[rune]bool)
    result := []rune{}

    for _, value := range input {
        if _, ok := uniqueMap[value]; !ok {
            result = append(result, value)
            uniqueMap[value] = true
        }
    }

    return result
}

func main() {
    input := "hello world"
    unique := uniqueValues(input)
    fmt.Println(string(unique))
}
```

위의 예제에서 `uniqueValues` 함수는 주어진 문자열에서 중복되지 않는 고유한 문자들을 추출하는 역할을 합니다. 결과를 확인하기 위해 `hello world` 문자열로 테스트해봤습니다.

이제, 위의 코드를 실행하면 `helo wrd`가 출력됩니다. 따라서 **고유한 값인 `h`, `e`, `l`, `o`, `w`, `r`, `d`**가 추출되었습니다.

이러한 방식으로 Go 언어를 사용하여 문자열에서 중복되지 않는 고유한 값을 추출할 수 있습니다.

고유한 값 추출에 대한 추가적인 정보는 [Effective Go](https://golang.org/doc/effective_go.html)를 참고하시기 바랍니다.