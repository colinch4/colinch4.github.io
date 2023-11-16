---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 속도와 외관 설정 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift로 작성된 애니메이션 라이브러리입니다. 이 라이브러리를 사용하면 다양한 유형의 로딩 애니메이션을 쉽게 구현할 수 있습니다. 이 문서에서는 NVActivityIndicatorView의 애니메이션 속도와 외관을 설정하는 방법을 알아보겠습니다.

## 애니메이션 속도 설정하기

NVActivityIndicatorView의 애니메이션 속도를 조절하려면 `animationDuration` 속성을 사용합니다. 이 속성의 기본값은 1.0입니다. 값을 낮추면 애니메이션이 더 빠르게 진행되고, 값을 높이면 더 느리게 진행됩니다.

아래는 애니메이션 속도를 0.5로 설정하는 예시입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
activityIndicatorView.animationDuration = 0.5
```

애니메이션 속도를 조절하여 적절한 속도를 찾아보세요.

## 외관 설정하기

NVActivityIndicatorView의 외관을 커스터마이즈하려면 다음 속성을 사용할 수 있습니다.

- `color`: 애니메이션과 인디케이터에 대한 색상을 설정합니다.
- `type`: 애니메이션의 유형을 설정합니다.
- `padding`: 인디케이터와 애니메이션 사이의 공간을 설정합니다.

아래는 외관 설정 예시입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
activityIndicatorView.color = UIColor.red
activityIndicatorView.type = NVActivityIndicatorType.ballScale
activityIndicatorView.padding = 10
```

`color` 속성을 사용하여 애니메이션 및 인디케이터의 색상을 변경할 수 있습니다. 또한, `type` 속성을 사용하여 애니메이션의 유형을 변경하고, `padding` 속성을 사용하여 인디케이터와 애니메이션 사이의 공간을 조절할 수 있습니다.

더 자세한 설정 방법은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.