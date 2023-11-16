---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 종류 선택하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift에서 NVActivityIndicatorView 라이브러리는 로딩 애니메이션을 쉽게 추가할 수 있는 좋은 도구입니다. 이 라이브러리를 사용하여 다양한 종류의 애니메이션을 적용할 수 있습니다. 이번 블로그에서는 Swift에서 NVActivityIndicatorView에서 애니메이션 종류를 선택하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 소개

NVActivityIndicatorView는 iOS 앱에서 사용되는 로딩 인디케이터를 간편하게 구현할 수 있는 Swift 라이브러리입니다. 다양한 종류의 애니메이션을 제공하며, 커스터마이징도 가능합니다.

## 애니메이션 종류 선택하기

NVActivityIndicatorView에서 제공하는 다양한 애니메이션 종류 중 하나를 선택하려면 `NVActivityIndicatorType` 열거형을 사용하면 됩니다. `NVActivityIndicatorView` 인스턴스를 만들 때 이 열거형의 한 종류를 매개변수로 전달하면 됩니다.

예를 들어, 다음과 같이 NVActivityIndicatorView를 만들면서 애니메이션 종류를 선택할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(
    frame: CGRect(x: 0, y: 0, width: 50, height: 50),
    type: .ballScaleRipple, // 애니메이션 종류 선택
    color: .white,
    padding: nil
)
```

위의 코드에서 `.ballScaleRipple`은 NVActivityIndicatorView에서 제공하는 하나의 애니메이션 종류입니다. 여러 다른 종류의 애니메이션을 사용하고 싶다면 `NVActivityIndicatorType` 열거형의 다른 값을 전달하면 됩니다.

## 애니메이션 커스터마이징하기

NVActivityIndicatorView의 애니메이션은 기본값으로 제공되는 디자인을 사용할 수도 있지만, 원하는 경우에는 커스터마이징도 가능합니다. 애니메이션의 크기, 색상, 패딩 등을 조정할 수 있습니다.

애니메이션을 커스터마이징한 예를 들면, 다음과 같이 할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(
    frame: CGRect(x: 0, y: 0, width: 50, height: 50),
    type: .ballSpinFadeLoader,
    color: .red,
    padding: 20 // 패딩 값 조정
)
```

`frame`은 애니메이션의 크기와 위치를 설정하는 것이고, `color`는 애니메이션의 색상을 설정하는 것입니다. `padding`은 패딩 값을 설정하는 것으로, 애니메이션 사이의 간격을 조절할 수 있습니다.

## 결론

Swift에서 NVActivityIndicatorView를 사용하여 로딩 애니메이션을 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView에서 제공하는 다양한 애니메이션 종류 중 하나를 선택하고, 필요에 따라 커스터마이징하여 원하는 로딩 인디케이터를 만들 수 있습니다.