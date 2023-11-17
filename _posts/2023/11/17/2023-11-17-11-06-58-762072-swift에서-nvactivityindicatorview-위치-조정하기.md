---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 위치 조정하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 NVActivityIndicatorView를 사용하여 로딩 인디케이터를 표시할 때, 종종 인디케이터의 위치를 조정해야 할 때가 있습니다. 이 글에서는 Swift에서 NVActivityIndicatorView의 위치를 조정하는 방법을 소개합니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 로딩 인디케이터를 표시하는데 사용되는 Swift 라이브러리입니다. 다양한 디자인과 스타일의 인디케이터를 제공하며, 애플리케이션의 로딩 상태를 시각적으로 표현하는데 사용됩니다.

## NVActivityIndicatorView 위치 조정하기

NVActivityIndicatorView의 위치를 조정하려면 다음 단계를 따르세요.

1. `NVActivityIndicatorView` 클래스의 인스턴스를 생성합니다.
```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

2. `NVActivityIndicatorView` 객체의 `center` 속성을 조정하여 원하는 위치로 인디케이터를 이동합니다.
```swift
activityIndicatorView.center = CGPoint(x: view.bounds.width/2, y: view.bounds.height/2)
```

위 예제에서는 인디케이터를 화면의 가운데로 이동시킵니다.

3. `NVActivityIndicatorView` 객체를 애플리케이션의 뷰에 추가합니다.
```swift
view.addSubview(activityIndicatorView)
```

4. 필요에 따라 인디케이터를 시작하거나 정지합니다.
```swift
activityIndicatorView.startAnimating()
activityIndicatorView.stopAnimating()
```
`startAnimating()` 메서드를 호출하면 인디케이터 애니메이션이 시작되고, `stopAnimating()` 메서드를 호출하면 애니메이션이 정지됩니다.

## 결론

Swift에서 NVActivityIndicatorView의 위치를 조정하기 위해서는 `NVActivityIndicatorView` 객체의 `center` 속성을 이용하여 위치를 조정하면 됩니다. 이를 위해 적절한 좌표값을 설정하고, 애플리케이션의 뷰에 인디케이터를 추가합니다.

더 많은 NVActivityIndicatorView 사용 예제와 옵션에 대한 정보는 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.