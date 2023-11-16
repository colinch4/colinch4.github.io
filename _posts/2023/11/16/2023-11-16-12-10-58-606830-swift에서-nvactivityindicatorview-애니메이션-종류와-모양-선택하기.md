---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 종류와 모양 선택하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 강력한 애니메이션 라이브러리입니다. 이 라이브러리를 사용하면 다양한 종류와 모양의 애니메이션을 만들 수 있습니다. 이번 글에서는 NVActivityIndicatorView를 사용하여 애니메이션의 종류와 모양을 선택하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 애니메이션을 구현하기 위한 라이브러리로, 많은 종류와 모양의 애니메이션을 제공합니다. 이 라이브러리는 CocoaPods를 통해 설치할 수 있습니다.

```swift
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 애니메이션 종류 선택하기

NVActivityIndicatorView는 다양한 종류의 애니메이션을 제공합니다. 이 애니메이션 종류는 다음과 같습니다:

- BallPulse
- BallGridPulse
- BallClipRotate
- ...

애니메이션 종류는 NVActivityIndicatorType 열거형으로 선택할 수 있습니다. 애니메이션을 생성할 때 해당 열거형 값을 지정하면 됩니다. 예를 들어, BallPulse 형태의 애니메이션을 생성하려면 다음과 같이 코드를 작성합니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse)
```

## NVActivityIndicatorView 애니메이션 모양 선택하기

NVActivityIndicatorView는 각 애니메이션 종류에 대해 다양한 모양을 제공합니다. 이 모양은 NVActivityIndicatorShape 열거형으로 선택할 수 있습니다. 예를 들어, Circle 모양의 애니메이션을 생성하려면 다음과 같이 코드를 작성합니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .gray, padding: nil, displayTimeThreshold: nil, minimumDisplayTime: nil, fadeInAnimation: nil, fadeOutAnimation: nil, size: CGSize(width: 50, height: 50), fadeOutDelay: nil, fadeOutDuration: nil, maxFadeOutDelay: nil, shape: .circle)
```

## 참고 자료

- [NVActivityIndicatorView Github 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)

이제 NVActivityIndicatorView를 사용하여 원하는 종류와 모양의 애니메이션을 Swift 프로젝트에 적용할 수 있습니다. 다양한 종류와 모양을 시도해보고, 원하는 결과를 얻으세요.