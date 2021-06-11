---
layout: post
title: "[함수형프로그래밍] Higher Order Function (고차 함수)"
description: " "
date: 2021-06-11
tags: [함수형프로그래밍]
comments: true
share: true
---

## Higher Order Function (고차 함수)

> 이 내용은 곰튀김님 `Swift로 함수형 프로그래밍 시작하기` 강의를 보고 정리한 것임을 알려드립니다. 

* 1급 객체: 프로그래밍 언어에서 함수의 파라미터로 전달되거나 리턴값으로 전달 될 수 있는 객체
* 함수형 프로그래밍에서는 함수를 1급 객체로 취급한다.
* 고차 함수(Higher Order Function): 함수를 파라미터로 받거나 함수를 리턴하는 함수

Swift에서는 Foundation 라이브러리에서 고차함수를 지원하고 있다. 
예를 들어, Array에는 `filter`함수가 있다.

```swift
//filter 함수의 정의
func filter(_ isIncluded: (Element) throws -> Bool) rethrows -> [Element]
```

이렇게 사용된다.

```swift
let arr = [1, 2, 3, 4, 5]
func isOdd(_ number: Int) -> Bool {
    number % 2 == 1
}

let odds = arr.filter(isOdd(_:))
```

### 함수를 반환하는 함수

```swift
func divide(dividend: Int) -> (Int) -> Int {
    func divid(divisor: Int) -> Int {
        return dividend / divisor
    }
    return divid
}

let quotient = divide(10)(5) // 2
```

=> 이 함수는 함수를 반환하고 있다. 따라서 함수의 실행결과가 **함수**이기 때문에 `(10)(5)` 처럼 두 번 호출해서 최종 값을 얻는다.
<br>=> 또한, 반환값을 변수에 넣으면 그 변수를 함수와 동일하게 사용할 수 있다. 즉 함수(클로저)를 저장하므로 반환 값은 `escaping closure(탈출 클로저)`이다.

```swift
func divide(_ dividend: Int) -> (Int) -> Int {
    return { divisor in
        return dividend / divisor
    }
}
let divideTenBy = divide(10)
let quotient = divideTenBy(5) // 2
```