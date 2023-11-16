---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 속도와 외관 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift에서 NVActivityIndicatorView를 사용하여 애니메이션을 추가할 수 있습니다. NVActivityIndicatorView는 다양한 스타일의 로딩 인디케이터를 제공하고, 애니메이션의 속도와 외관을 설정할 수 있습니다.

## NVActivityIndicatorView 속도 설정하기
NVActivityIndicatorView는 `startAnimating()` 메서드를 호출하여 애니메이션을 시작합니다. 이때, 애니메이션의 속도를 변경하려면 `animationDuration` 속성을 조정하면 됩니다. 기본적으로 `animationDuration`은 1초입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: frame)

activityIndicatorView.startAnimating()
activityIndicatorView.animationDuration = 0.5 // 애니메이션 속도를 0.5초로 설정

view.addSubview(activityIndicatorView)
```

## NVActivityIndicatorView 외관 설정하기
NVActivityIndicatorView는 다양한 외관 옵션을 제공하여 로딩 인디케이터의 모양과 색상을 변경할 수 있습니다. 외관 옵션은 다음과 같습니다:

- `type`: NVActivityIndicatorType 열거형으로, 로딩 인디케이터의 모양을 설정합니다. 예를 들어, `.circleStrokeSpin`은 원 형태의 인디케이터를 사용합니다.
- `color`: 로딩 인디케이터의 색상을 설정합니다. UIColor를 사용하여 색상을 지정할 수 있습니다.
- `padding`: 로딩 인디케이터의 padding 값을 설정합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: frame)

activityIndicatorView.type = .circleStrokeSpin // 인디케이터 모양 설정
activityIndicatorView.color = UIColor.red // 색상 설정
activityIndicatorView.padding = 20 // padding 설정

activityIndicatorView.startAnimating()

view.addSubview(activityIndicatorView)
```

NVActivityIndicatorView의 다양한 외관 옵션은 더욱 많습니다. 자세한 내용은 [NVActivityIndicatorView GitHub repository](https://github.com/ninjaprox/NVActivityIndicatorView)의 문서를 참조하시기 바랍니다.

위의 예제 코드를 사용하여 Swift에서 NVActivityIndicatorView 애니메이션의 속도와 외관을 설정해보세요.