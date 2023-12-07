---
layout: post
title: "[go] 구조체(struct)의 암시적 타입 변환(Implicit type conversion)"
description: " "
date: 2023-12-07
tags: [go]
comments: true
share: true
---

Go 언어에서는 구조체(struct) 간의 타입 변환이 가능합니다. 이를 암시적 타입 변환이라고도 부릅니다. 구조체의 필드가 같고 순서도 같다면 두 구조체는 호환 가능하며, 암시적으로 타입 변환이 이루어집니다.

예를 들어서, 다음과 같이 두 개의 구조체 타입이 있다고 가정해봅시다.

```go
type Person struct {
    name    string
    age     int
    address string
}

type Employee struct {
    name    string
    age     int
    address string
    position string
}
```

위의 구조체 `Person`과 `Employee`는 `name`, `age`, `address` 필드를 갖고 있습니다. `Employee` 구조체에는 추가적으로 `position` 필드가 포함되어 있습니다.

이때, 다음과 같이 구조체 변수를 선언하고 값을 할당하면, 구조체 간에 암시적 타입 변환이 이루어집니다.

```go
var person Person
var employee Employee

person = employee // 암시적 타입 변환
```

위의 코드에서 `employee` 변수는 `Person` 타입의 `person` 변수에 할당되었습니다. 이는 `Person` 구조체와 `Employee` 구조체가 동일한 필드를 가지고 있으므로 암시적으로 타입 변환이 가능한 것입니다.

하지만, 반대로 `Person` 구조체에 `Employee` 구조체를 할당하는 것은 불가능합니다. `Employee`는 `position` 필드가 추가로 있기 때문에 `Person`에 할당할 수 없습니다.

구조체의 암시적 타입 변환은 유용한 기능으로 활용될 수 있습니다. 예를 들어, 다양한 타입의 구조체를 사용하는 함수에 동일한 로직을 적용할 때, 암시적 타입 변환이 도움이 될 수 있습니다.

# 참고 자료
- Go 공식 문서: [Types](https://golang.org/ref/spec#Types)
- Go 플레이그라운드: [Try Go](https://play.golang.org/)