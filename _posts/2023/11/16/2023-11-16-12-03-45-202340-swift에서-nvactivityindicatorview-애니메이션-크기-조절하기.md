---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 크기 조절하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 개발자들이 애니메이션을 쉽게 추가할 수 있는 오픈 소스 라이브러리입니다. 이 라이브러리를 사용하여 사용자에게 로딩 표시기를 제공하거나, 데이터를 로드하는 동안 애니메이션을 표시하는 등 다양한 사용처가 있습니다. 이번에는 Swift에서 NVActivityIndicatorView의 애니메이션 크기를 조절하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 애니메이션 크기 조절하기

NVActivityIndicatorView의 애니메이션 크기를 조절하려면 `type` 속성을 설정해야 합니다. NVActivityIndicatorView에는 30가지 이상의 다양한 애니메이션 유형이 제공되며, 그 중에서 알맞은 크기를 선택할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(
    frame: CGRect(x: 0, y: 0, width: 50, height: 50),
    type: .ballPulse,
    color: .blue,
    padding: 0
)
```
위의 예제에서는 `ballPulse` 유형의 애니메이션을 사용하고 있으며, 크기는 50x50으로 설정되어 있습니다. 만약 다른 크기를 원한다면 `frame` 속성의 값을 조절하면 됩니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)

이제 Swift에서 NVActivityIndicatorView의 애니메이션 크기를 조절하는 방법에 대해 알아보았습니다. 이를 통해 더 다양한 화면에서 적절한 크기의 애니메이션을 사용할 수 있게 되었습니다.