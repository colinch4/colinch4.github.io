---
layout: post
title: "[swift] Swift의 제네릭 타입 매개변수(Generics type parameters)에 대해 설명해 주세요."
description: " "
date: 2023-12-15
tags: [swift]
comments: true
share: true
---

Swift는 제네릭(Generics)을 지원하는 언어로, 제네릭을 사용하면 유연하고 재사용 가능한 함수와 타입을 정의할 수 있습니다. 제네릭을 사용하면 코드의 중복을 줄이고, 안정성을 높일 수 있습니다. Swift에서 제네릭은 함수, 메서드, 클래스, 열거형 등 여러 곳에서 사용할 수 있습니다.

## 제네릭 타입 매개변수

제네릭을 사용하려면, 함수나 타입을 정의할 때 *타입 매개변수(type parameter)* 를 사용합니다. 타입 매개변수는 `<>` 내부에 선언되며, 해당 함수나 타입이 실제로 사용될 때 실제 타입으로 대체됩니다.

예를 들어, 배열을 정렬하는 함수를 제네릭으로 만들어보겠습니다. 이때 정렬 대상의 타입은 제네릭으로 받아들이도록 구현할 수 있습니다.

```swift
func customSort<T>(_ array: [T]) -> [T] where T: Comparable {
    return array.sorted()
}
```

위 코드에서 `<T>`는 타입 매개변수를 나타내며, 호출될 때 실제 타입으로 대체됩니다. `where T: Comparable` 는 `T`가 `Comparable` 프로토콜을 따르는 타입이라는 제약 조건을 추가한 것입니다.

## 제네릭 타입 사용

이제 위에서 정의한 `customSort` 함수를 사용해보겠습니다.

```swift
let unsortedArray = [5, 3, 9, 1, 2, 7]
let sortedArray = customSort(unsortedArray)
print(sortedArray) // 출력: [1, 2, 3, 5, 7, 9]
```

위의 예시에서 `customSort` 함수는 정수형 배열을 대상으로 정렬하는데 사용되었습니다. 이때 `T`는 호출 시점에 실제로 `Int`로 대체됩니다.

제네릭을 사용하면 함수나 타입을 보다 유연하게 정의할 수 있으며, 강력한 코드 재사용성을 얻을 수 있습니다.

## 요약

제네릭을 사용하면 코드를 보다 유연하고 재사용 가능하게 만들 수 있습니다. Swift에서는 제네릭을 활용하여 함수와 타입을 정의할 때 타입 매개변수를 사용하고, 강력한 제네릭 시스템을 통해 안전성과 유연성을 확보할 수 있습니다.

참고문헌:
- [Swift 공식 문서 - Generics](https://docs.swift.org/swift-book/LanguageGuide/Generics.html)