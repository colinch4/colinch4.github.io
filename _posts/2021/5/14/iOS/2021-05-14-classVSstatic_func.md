---
layout: post
title: "[iOS] class func vs staticfunc"
description: " "
date: 2021-05-14
tags: [ios]
comments: true
share: true
---


## class func vs staticfunc

스위프트에는 세가지 함수 종류가 있습니다. 앞에 붙는 키워드에 따라서 instance / class/ static으로 나타냅니다.

```swift
class Sample {
    // 1. Instance 함수
    func myUnstanceFunc() {}

    // 2. class 함수
    class func myClassFunc() {}

    // 3. static 함수
    static func myStaticFunc() {}
}
```

**공통점**

static과 class 메소드는 타입 메소드라 불린다. 모두 class 객체보다는 class 자체와 연관되어 있습니다. () 생성자를 통해서 인스턴스를 생성하지 않더라도 접근이 가능하다

```swift
Sample.myClassFunc()
Sample.myStaticFunc()
```

**차이점**

차이점은 해당 class를 상속 받은 subclass에서 나타난다

class 함수 - override 가능

static 함수 - override 불가능

```swift
class SubSample : Sample {

    // Compile Ok
    override class func myClassFunc() {}

    // Compile Error
    ouverride static func myStaticFunc() {}

}
```
