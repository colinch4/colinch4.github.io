---
layout: post
title: "[swift] Swift의 SwiftyAttributes 개요"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

[SwiftyAttributes](https://github.com/eddiekaiger/SwiftyAttributes)는 Swift에서 NSAttributedString을 쉽게 생성하고 편집할 수 있도록 도와주는 유용한 라이브러리입니다.

NSAttributedString은 텍스트에 서로 다른 스타일을 적용할 수 있는 기능을 제공합니다. 그러나 Swift에서 기본적으로 제공되는 NSAttributedString을 다루는 것은 번거롭고 복잡할 수 있습니다. SwiftyAttributes는 이런 불편함을 해결하고자 만들어진 라이브러리로, 간단하고 직관적인 문법을 제공합니다.

## 주요 기능

SwiftyAttributes는 다음과 같은 주요 기능을 제공합니다:

### 1. 텍스트 스타일링

SwiftyAttributes를 사용하면 텍스트에 다양한 스타일을 손쉽게 적용할 수 있습니다. 예를 들어, 다음과 같이 특정 부분만 볼드체로 표시할 수 있습니다:

```swift
let string = "Hello, SwiftyAttributes!"
let attributedString = string.attributedString
    .font(.boldSystemFont(ofSize: 16))
    .range(of: "SwiftyAttributes")
    .font(.italicSystemFont(ofSize: 16))
    .build()
```

### 2. 텍스트 색상 지정

SwiftyAttributes를 사용하여 텍스트에 원하는 색상을 지정할 수 있습니다. 아래 예시 코드에서는 특정 부분의 텍스트 색상을 파란색으로 지정합니다:

```swift
let string = "Hello, SwiftyAttributes!"
let attributedString = string.attributedString
    .range(of: "SwiftyAttributes")
    .foregroundColor(.blue)
    .build()
```

### 3. 배경색 지정

SwiftyAttributes를 사용하여 텍스트의 배경색을 지정할 수도 있습니다. 아래 예시 코드에서는 특정 부분의 배경색을 노란색으로 지정합니다:

```swift
let string = "Hello, SwiftyAttributes!"
let attributedString = string.attributedString
    .range(of: "SwiftyAttributes")
    .backgroundColor(.yellow)
    .build()
```

## 결론

SwiftyAttributes은 Swift에서 NSAttributedString을 다루기 쉽게 만들어주는 유용한 라이브러리입니다. 간편한 문법과 다양한 스타일링 옵션을 제공하여 텍스트를 보다 쉽게 편집할 수 있도록 도와줍니다. 프로젝트에서 NSAttributedString을 다루어야 할 때 SwiftyAttributes을 사용해 보는 것을 추천드립니다.

### 참고 자료

- [SwiftyAttributes GitHub 레포지토리](https://github.com/eddiekaiger/SwiftyAttributes)