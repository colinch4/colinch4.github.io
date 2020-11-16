---
layout: post
title: "18. 참조, Retain Cycle"
description: " "
date: 2020-07-30
tags: [swift]
comments: true
share: true
---

### Retain Cycle 
- 인스턴스 참조 시, 서로 strong 참조를 하게 되는 강한 참조가 생기는 경우. 해제되지 않는 문제 발생

### weak keyword
- 약한 참조
- weak var 

### unowned
- 참조 대상이 되는 인스터스가 참조하고 있는 것과 같은 생명주기를 갖거나 더 긴 갱애 주기를 가질 때 사용한다. 

### 클로저에서의 강한 순환 참조 해결
- self를 캡쳐(unowned or weak)

```swift
lazy var someClosure: (Int, String) -> String = {
    [unowned self, weak delegate = self.delegate!] (index: Int, stringToProcess: String) -> String in
    // closure body goes here
}


// 추론에 의한 생략 시
lazy var someClosure: () -> String = {
    [unowned self, weak delegate = self.delegate!] in
    // closure body goes here
}
```
