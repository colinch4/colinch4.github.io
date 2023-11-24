---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 함께 사용할 수 있는 레이아웃 UI 스타일링 팁"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

![NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView/raw/master/Resources/Loading.gif)

Swift에서 `NVActivityIndicatorView`를 사용하여 로딩 인디케이터를 구현하고자 할 때, 이를 더욱 화려하고 시각적으로 매력적인 UI로 스타일링할 수 있습니다. 이 글에서는 `NVActivityIndicatorView`를 사용하는 동안 UI를 스타일링하기 위한 몇 가지 유용한 팁을 제공하고자 합니다.

## 1. 색상 설정하기

NVActivityIndicatorView는 여러 가지 다양한 색상 옵션을 제공합니다. 로딩 인디케이터의 색상을 변경하려면, `color` 프로퍼티를 사용하면 됩니다. 예를 들어, 아래의 코드는 로딩 인디케이터를 빨강색으로 설정하는 예제입니다.

```swift
let activityIndicator = NVActivityIndicatorView(frame: frame, type: .ballClipRotate, color: .red, padding: 0)
```

## 2. 크기 조정하기

로딩 인디케이터의 크기를 조정하는 것도 가능합니다. `size` 프로퍼티를 사용하여 로딩 인디케이터의 크기를 변경할 수 있습니다. 아래의 코드는 로딩 인디케이터의 크기를 50포인트로 설정하는 예시입니다.

```swift
let activityIndicator = NVActivityIndicatorView(frame: frame, type: .ballClipRotate, color: .red, padding: 0)
activityIndicator.size = CGSize(width: 50, height: 50)
```

## 3. 배경색 설정하기

로딩 인디케이터를 감싸는 뷰의 배경색을 변경하여 시인성을 높일 수도 있습니다. 생성된 인디케이터를 감싸는 `UIView`의 배경색을 변경하려면, `backgroundColor` 프로퍼티를 사용하면 됩니다. 아래의 코드는 인디케이터를 감싸는 뷰의 배경색을 파란색으로 변경하는 예시입니다.

```swift
let containerView = UIView(frame: frame)
containerView.backgroundColor = .blue

let activityIndicator = NVActivityIndicatorView(frame: containerView.bounds, type: .ballClipRotate, color: .red, padding: 0)
containerView.addSubview(activityIndicator)
```

## 4. 애니메이션 속도 조절하기

로딩 인디케이터의 애니메이션 속도를 조절하여 원하는 효과를 낼 수도 있습니다. `animationDuration` 프로퍼티를 사용하여 애니메이션의 지속 시간을 변경할 수 있습니다. 예를 들어, 아래의 코드는 로딩 인디케이터의 애니메이션 속도를 1.5초로 지정하는 예제입니다.

```swift
let activityIndicator = NVActivityIndicatorView(frame: frame, type: .ballClipRotate, color: .red, padding: 0)
activityIndicator.animationDuration = 1.5
```

위의 팁을 활용하여 NVActivityIndicatorView를 사용하여 로딩 인디케이터를 구현할 때, 좀 더 멋진 UI를 만들어보세요. 더 자세한 정보는 [NVActivityIndicatorView GitHub 리포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.