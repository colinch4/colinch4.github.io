---
layout: post
title: "[go] 구조체(struct)를 사용한 패턴 매칭(Pattern Matching) 방법"
description: " "
date: 2023-12-07
tags: [go]
comments: true
share: true
---

패턴 매칭(Pattern Matching)은 프로그래밍에서 많이 사용되는 기법 중 하나로, 특정 패턴에 맞는 값들을 추출하거나 조건에 따라 다른 동작을 수행하는데 사용됩니다. 이번 글에서는 Go 언어에서 구조체(struct)를 사용하여 패턴 매칭을 구현하는 방법을 알아보겠습니다.

## 구조체(struct)란?

구조체는 필드들을 묶어 하나의 새로운 데이터 타입을 정의하는 기능을 제공하는데, 일반적으로 연관된 데이터를 묶을 때 사용됩니다. 각 필드는 이름과 타입을 가지며, 구조체는 그 필드들의 집합입니다. 예를 들면 다음과 같은 코드로 구조체를 정의할 수 있습니다.

```go
type Person struct {
    Name string
    Age int
}
```

위 코드에서 `Person`은 구조체의 이름이고, `Name`과 `Age`는 필드의 이름입니다. `string`과 `int`는 각 필드의 타입을 나타냅니다.

## 패턴 매칭(Pattern Matching) 구현하기

Go 언어에는 패턴 매칭을 직접적으로 지원하는 기능은 없지만, 구조체를 활용하여 패턴 매칭과 유사한 효과를 구현할 수 있습니다. 다음은 구조체를 사용하여 패턴 매칭을 구현하는 예시입니다.

```go
func matchPattern(person Person) {
    switch {
    case person.Age > 20:
        fmt.Println(person.Name, "is an adult")
    case person.Age < 20:
        fmt.Println(person.Name, "is a teenager")
    default:
        fmt.Println(person.Name, "is of unknown age")
    }
}
```

위 코드에서 `matchPattern` 함수는 `Person` 구조체를 입력받아 해당하는 패턴에 따라 동작을 수행합니다. 패턴은 `switch`문을 사용하여 구현되었습니다. `Age` 필드를 기준으로 판단하여 적절한 메시지를 출력합니다.

## 패턴 매칭을 활용한 활용 예시

구조체를 사용한 패턴 매칭은 다양한 상황에서 유용하게 활용될 수 있습니다. 예를 들어, 다음과 같은 상태 변화에 따라 다른 동작을 수행하는 예시를 살펴보겠습니다.

```go
type EntityState struct {
    State string
}

func ProcessStateChange(entity EntityState) {
    switch entity.State {
    case "created":
        fmt.Println("Entity is created")
    case "updated":
        fmt.Println("Entity is updated")
    case "deleted":
        fmt.Println("Entity is deleted")
    default:
        fmt.Println("Unknown entity state")
    }
}
```

위 코드에서는 `EntityState` 구조체를 입력받아 `State` 필드를 기준으로 동작을 분기합니다. 해당하는 패턴에 따라 적절한 메시지를 출력합니다.

## 결론

Go 언어에서 구조체(struct)를 사용하여 패턴 매칭을 구현하는 방법을 살펴보았습니다. 구조체를 활용하면 연관된 데이터를 묶고, 패턴에 따라 다른 동작을 수행할 수 있습니다. 패턴 매칭은 다양한 상황에서 유용하게 활용될 수 있으며, 코드의 가독성과 유지보수성을 향상시킬 수 있습니다.

참고 자료:
- [Go 언어 공식 문서](https://golang.org)
- [A Tour of Go (한국어)](https://go-tour-kr.appspot.com/)