---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 속도 조절하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 앱에서 쉽게 사용할 수 있는 로딩 애니메이션 라이브러리입니다. 이 라이브러리를 사용하면 다양한 스타일과 크기의 로딩 애니메이션을 간단하게 구현할 수 있습니다. 이번에는 NVActivityIndicatorView에서 애니메이션의 속도를 조절하는 방법에 대해 알아보도록 하겠습니다.

## NVActivityIndicatorView 속도 조절하기

NVActivityIndicatorView의 애니메이션 속도를 조절하는 방법은 매우 간단합니다. NVActivityIndicatorView 클래스의 `animationDuration` 속성을 사용하여 애니메이션의 지속 시간을 조정할 수 있습니다. 이 값을 조정하는 것으로 애니메이션의 속도를 조절할 수 있습니다.

``` swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
activityIndicatorView.type = .ballSpinFadeLoader
activityIndicatorView.color = .gray
activityIndicatorView.startAnimating()

// 애니메이션 속도 조절
activityIndicatorView.animationDuration = 0.5
```

위의 예시에서는 `activityIndicatorView`의 애니메이션 속도를 0.5로 설정했습니다. 이 값은 애니메이션이 1초당 반복되는 속도를 의미합니다. 따라서 값이 작을수록 애니메이션의 속도가 더 빨라집니다.

## 결론

이제 Swift에서 NVActivityIndicatorView의 애니메이션 속도를 조절하는 방법에 대해 알아보았습니다. `animationDuration` 속성을 사용하여 애니메이션의 지속 시간을 조정하여 애니메이션의 속도를 조절할 수 있습니다.

더 자세한 내용은 [NVActivityIndicatorView 공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.