---
layout: post
title: "[kotlin] 코틀린에서 제네릭을 사용하여 함수형 프로그래밍(Functional Programming)을 다루는 방법은 어떻게 되는가?"
description: " "
date: 2023-12-15
tags: [kotlin]
comments: true
share: true
---

함수형 프로그래밍은 함수를 일급 시민으로 취급하는 패러다임으로, 코틀린에서도 제네릭을 통해 이를 지원합니다. 제네릭은 타입을 인자로 받는 클래스나 함수를 만들 수 있게 해줍니다.

## 제네릭 함수 정의하기

제네릭 함수를 정의하기 위해서는 함수 이름 뒤에 `<T>`와 같이 꺽쇠 괄호 안에 타입 매개변수를 지정합니다. 

예를 들어, 다음은 제네릭 함수를 사용하여 리스트의 각 요소에 절대값을 취하는 예시입니다:

```kotlin
fun <T: Number> absoluteValue(input: T): T {
    return if (input.toDouble() < 0) -input else input
}
```

위의 코드에서 `fun <T: Number>` 부분은 제네릭 함수를 선언하는 부분이며, `T`는 함수에 전달되는 인자의 타입을 나타냅니다. 

## 제네릭 함수 사용하기

제네릭 함수를 사용할 때에는 명시적으로 타입을 지정하거나, 컴파일러가 타입을 추론하도록 할 수 있습니다.

예를 들어, 앞서 정의한 `absoluteValue` 함수를 사용하여 정수형과 실수형에 대해 각각 호출한 예시 코드입니다:

```kotlin
val intResult = absoluteValue<Int>(-10)  // intResult에는 10이 할당됨
val doubleResult = absoluteValue(-5.5)  // doubleResult에는 5.5가 할당됨
```

`absoluteValue<Int>`와 같이 타입을 명시적으로 지정하여 호출할 수 있고, 타입을 생략하고 호출할 수도 있습니다.

이렇게 제네릭 함수를 활용하면 함수형 프로그래밍에서 필요한 다양한 타입을 대응하는 함수를 유연하게 정의하고 사용할 수 있습니다.

코틀린에서 제네릭을 활용한 함수형 프로그래밍에 대한 간단한 소개였습니다. 제네릭을 통해 타입 안전성을 유지하면서 함수형 프로그래밍을 지원하기 때문에, 코틀린은 함수형 프로그래밍에 매우 적합한 언어 중 하나입니다.