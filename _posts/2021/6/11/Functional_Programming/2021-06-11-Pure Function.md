---
layout: post
title: "[함수형프로그래밍] Pure Function"
description: " "
date: 2021-06-11
tags: [swift]
comments: true
share: true
---


## Pure Function

* 이 글은 `곰튀김`님의 `Swift로 함수형 프로그래밍 시작하기` 강의를 보고 정리한 것임을 알려드립니다.

### 1. 순수 함수란?

* 특정 Input에 대하여 **항상 동일한 Output값을 반환**하는 함수
  * 함수의 수행과정에 외부에 있는 값을 변경하지도 않으므로 **부수효과(side-effect)** 가 없다.

### 2. 예제들

```swift
var name = "kimdo"
var greeting = ""
func setGreeting() {
    greeting = "hello, \(name)"
}
```

위의 코드는 외부 변수를 사용하고 있고, 또 외부 변수를 바꾸고 있으므로 순수 함수가 아니고 `side-effect`가 존재한다. (외부 변수를 바꾸는 다는 것 자체가 side-effect가 있다는 뜻이다.)

이를 순수함수로 바꾸면 다음과 같다. 
```swift
func greeting(_ name: String) -> String {
    return "hello, \(name)"
}
```
=> 외부의 값에 영향을 받지 않고, 파리미터 값(input 값)에 따라 항상 동일한 값을 반환하므로 `순수 함수`가 맞다.

```swift
let greet = "hello"
func greeting(_ name: String) -> String {
    return "\(greet), \(name)"
}
```
=> 위 소스코드 또한 **순수함수다.** 왜냐하면 외부 변수 `greet`은 `let`으로 선언되어 있어 변경이 불가능하므로, **결국 이 함수도 input값에 따라 동일한 output값이 반환되기 때문이다.** 
그리고 `greet`처럼 변경이 불가능한 데이터를 `immutable data`라고 한다.

```swift
func add(_ a: Int) -> Int {
    return Int.random(in: 0...100) + a
}
```
=> 위 소스 코드는 순수 함수일까? 얼핏 보면 외부 값을 사용하거나 변경하지 않으므로, 순수 함수가 맞는 것처럼 보인다. 
하지만, random 함수를 호출하므로 `특정 input 값에 대해 동일한 output값을 반환`하지 않음을 알 수 있다. 즉, 동일한 input값이어도 매번 다른 결과가 나타나므로 위의 함수는 **순수 함수가 아니다.** 