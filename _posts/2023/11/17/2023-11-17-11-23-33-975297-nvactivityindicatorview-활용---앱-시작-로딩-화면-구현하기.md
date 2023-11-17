---
layout: post
title: "[swift] NVActivityIndicatorView 활용 - 앱 시작 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱을 실행할 때 로딩 화면을 보여주는 것은 사용자들에게 앱이 제대로 동작하고 있음을 알려주는 좋은 방법입니다. 이번에는 Swift에서 NVActivityIndicatorView를 활용하여 앱 시작 로딩 화면을 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS 앱에서 로딩 화면을 보여주기 위한 라이브러리입니다. 다양한 스타일의 로딩 인디케이터를 제공하여 앱의 디자인에 맞춰 사용할 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 Swift Package Manager를 통해 라이브러리를 설치해야 합니다. 다음과 같이 Package.swift 파일에 의존성을 추가해주세요.

```swift
// Package.swift

// ...

dependencies: [
    .package(url: "https://github.com/ninjaprox/NVActivityIndicatorView.git", from: "5.1.1")
],
targets: [
    .target(name: "YourApp", dependencies: ["NVActivityIndicatorView"])
]
```

설치 후에는 import 구문을 통해 NVActivityIndicatorView를 불러올 수 있습니다.

```swift
import NVActivityIndicatorView
```

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하여 앱 시작 로딩 화면을 구현하는 방법은 간단합니다.

1. 먼저, 로딩 인디케이터를 담을 UIView를 생성합니다.

```swift
let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: 80, height: 80))
```

2. NVActivityIndicatorView를 생성하고 위에서 생성한 UIView에 추가합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 80, height: 80), type: .ballScaleRippleMultiple, color: .white, padding: nil)
loadingView.addSubview(activityIndicatorView)
```

3. 로딩 인디케이터를 화면에 보여주고 애니메이션을 시작합니다.

```swift
activityIndicatorView.startAnimating()
loadingView.center = view.center
view.addSubview(loadingView)
```

4. 로딩이 끝나면 로딩 화면을 숨기고 제거합니다.

```swift
activityIndicatorView.stopAnimating()
loadingView.removeFromSuperview()
```

## 마무리

이상으로 NVActivityIndicatorView를 활용하여 앱 시작 로딩 화면을 구현하는 방법에 대해 알아보았습니다. 다양한 스타일의 로딩 인디케이터를 제공하여 앱의 로딩 화면을 자유롭게 디자인할 수 있습니다. 

더 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하시기 바랍니다.