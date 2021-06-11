---
layout: post
title: "[swift] struct vs class "
description: " "
date: 2021-06-11
tags: [swift]
comments: true
share: true
---

# struct vs class 

## 구조체는 언제 사용하나? 

* 연관된 몇몇의 값들을 모아서 하나의 데이터 타입으로 표현하고 싶을 때( 이건 클래스도 마찬가지! )

* 다른 객체 또는 함수등으로 전달될 때 **참조가 아닌 복사를 원할 때** 

* 자신이 상속할 필요가 없거나, **자신이 다른 타입을 상속할 필요가 없을 때**

* Apple 프레임워크에서 프로그래밍을 할 때에는 주로 클래스를 많이 사용 

## Value vs Reference

* Value
  * 데이터를 전달할 때 값을 복사하여 전달

* Reference  
  * 데이터를 전달할 때 값의 메모리 위치를 전달 

## Data types in Swift

```swift
public struct Int

public struct Double

public struct String

public struct Dictionary<Key : Hashable, Value>

public struct Array<Element>

public struct Set<Element : Hashable> 

// => 데이터 타입들이 모두 struct 로 이루어져있다!
```

## Swift Loves Struct

* 스위프트는 구조체, 열거형 사용을 선호 
* **Apple 프레임워크는 대부분 클래스 사용** 
* **Apple 프레임워크 사용시 구조체/클래스 선택은 우리의 몫!**
