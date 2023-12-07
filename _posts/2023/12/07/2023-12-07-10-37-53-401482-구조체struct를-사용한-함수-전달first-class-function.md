---
layout: post
title: "[go] 구조체(struct)를 사용한 함수 전달(First-class Function)"
description: " "
date: 2023-12-07
tags: [go]
comments: true
share: true
---

Go는 First-class Function을 지원하는 언어로서 함수를 값으로 다룰 수 있습니다. 이는 구조체를 사용하여 함수를 다른 함수에 전달하고 반환할 수 있음을 의미합니다. 

## 구조체를 사용한 함수 전달 예제

```go
package main

import "fmt"

type MathFunc func(int, int) int

func add(x, y int) int {
    return x + y
}

func subtract(x, y int) int {
    return x - y
}

func multiply(x, y int) int {
    return x * y
}

func calculate(x, y int, mathFunc MathFunc) int {
    return mathFunc(x, y)
}

func main() {
    var a, b int = 10, 5

    result := calculate(a, b, add) // add 함수 전달
    fmt.Println("Addition:", result)

    result = calculate(a, b, subtract) // subtract 함수 전달
    fmt.Println("Subtraction:", result)

    result = calculate(a, b, multiply) // multiply 함수 전달
    fmt.Println("Multiplication:", result)
}
```

위 예제에서는 구조체 `MathFunc`를 선언하여 함수 시그니처를 정의합니다. 그리고 `add`, `subtract`, `multiply` 함수를 구현한 후, `calculate` 함수에서 전달된 구조체를 사용하여 결과를 계산합니다.

`calculate` 함수에서는 `mathFunc` 매개변수를 통해 전달된 함수를 호출하여 결과를 반환합니다. `main` 함수에서는 `calculate` 함수에 각각의 함수와 인자를 전달하고 반환된 결과를 출력합니다.

## 실행 결과

```
Addition: 15
Subtraction: 5
Multiplication: 50
```

위 예제를 실행하면 세 가지 연산을 수행한 결과가 출력됩니다. 각 연산은 `calculate` 함수 내부에서 전달된 함수에 의해 처리되고 결과가 반환됩니다.

## 결론

Go에서 구조체를 사용하여 함수를 First-class Function으로 다룰 수 있습니다. 이를 통해 함수를 값으로 전달하고 반환할 수 있어 유연하고 동적인 프로그래밍이 가능해집니다. 이 기능을 사용하여 다양한 함수를 전달하고 활용할 수 있습니다.