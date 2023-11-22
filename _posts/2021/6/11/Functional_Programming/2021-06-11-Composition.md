---
layout: post
title: "[함수형프로그래밍] Composition"
description: " "
date: 2021-06-11
tags: [swift]
comments: true
share: true
---

## Composition

> 이 글은 `곰튀김`님의 `Swift로 함수형 프로그래밍 시작하기` 강의를 보고 정리한 것임을 알려드립니다.

* 함수의 반환값이 다른 함수의 입력값으로 사용되는 것을 함수의 합성(composition)이라고 한다. **당연히 한 함수의 반환값의 타입과 또 다른 함수의 입력값의 타입은 같아야 한다.(f1: A -> B, f2: B -> C 에서 반환값과 입력값의 타입이 B로 같다.)**  

```swift 
func double(_ num: Int) -> Int {
    return num * 2
}

func description(_ num: Int) -> String {
    return String(num)
}

let result = description(double(1)) // "2"
```

* 함수는 **1급 객체로서 사용되기 때문에** 두 개의 함수를 합성하는 함수도 만들 수 있다.  

```swift
// 함수들을 합성해서 사용할 수도 있다.
func composition(f1: @escaping (Int) -> Int, f2: @escaping (Int) -> String) -> (Int) -> String {
    return { num in
        return f2(f1(num))
    }
}
let composedFunction = composition(f1: double, f2: description(_:))
```

* Generic을 이용해서도 두 개의 함수를 합성하는 함수를 만들 수 있다.  

```swift 
func composition<A, B, C>(f1: @escaping (A) -> B, f2: @escaping (B) -> C) -> (A) -> C {
    return { i in
        return f2(f1(i))
    }
}

let composedFunction = composition(f1: { 2 * $0 }, f2: { String($0)})
let result: String = composedFunction(2) // "4"
```

이는 **RxSwift** 의 기본 디자인이다. 