---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 포트폴리오 사이트 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 블로그 포스트에서는 Swift의 NVActivityIndicatorView 라이브러리를 사용하여 포트폴리오 사이트의 로딩 효과를 구현하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 효과를 구현하는 데 사용되는 오픈 소스 Swift 라이브러리입니다. 이 라이브러리는 많은 다양한 로딩 애니메이션을 제공하며 사용자가 쉽게 스타일을 변경할 수 있습니다.

## 2. NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 통해 라이브러리를 설치해야 합니다. 프로젝트의 Podfile에 다음 코드를 추가하고 `pod install` 명령을 실행합니다.

```swift
pod 'NVActivityIndicatorView'
```

## 3. NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 사용하기 위해 먼저 뷰 컨트롤러에 import 문을 추가합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 추가할 뷰를 생성합니다. 예를 들어, 로딩 효과를 추가할 UIView를 생성합니다.

```swift
let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

3. NVActivityIndicatorView를 생성하고 설정합니다. 이미지의 크기, 색상, 스타일 등을 변경할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(
    frame: CGRect(x: 0, y: 0, width: 50, height: 50),
    type: .ballSpinFadeLoader,
    color: .white,
    padding: nil
)
```

4. NVActivityIndicatorView를 생성한 뷰에 추가합니다.

```swift
loadingView.addSubview(activityIndicatorView)
```

5. NVActivityIndicatorView를 화면에 표시하거나 숨기는 메서드를 구현합니다.

```swift
func showLoadingView() {
    activityIndicatorView.startAnimating()
    self.view.addSubview(loadingView)
}

func hideLoadingView() {
    activityIndicatorView.stopAnimating()
    loadingView.removeFromSuperview()
}
```

## 4. NVActivityIndicatorView 스타일 변경하기

NVActivityIndicatorView는 다양한 스타일을 제공합니다. 예를 들어, 예제에서 사용한 ballSpinFadeLoader 스타일 외에도 다음과 같은 스타일을 사용할 수 있습니다.

- ballPulse
- lineScalePulseOut
- triangleSkewSpin
- ...

스타일을 변경하기 위해선 `type` 매개변수를 원하는 스타일로 설정하면 됩니다. 예를 들어, 다음은 ballPulse 스타일을 사용하는 코드입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(
    frame: CGRect(x: 0, y: 0, width: 50, height: 50),
    type: .ballPulse,
    color: .white,
    padding: nil
)
```

## 5. 마치며

이번 블로그 포스트에서는 NVActivityIndicatorView를 사용하여 포트폴리오 사이트의 로딩 효과를 구현하는 방법을 살펴보았습니다. NVActivityIndicatorView는 다양한 로딩 애니메이션을 제공하고 스타일을 쉽게 변경할 수 있는 강력한 라이브러리입니다. 이를 통해 사용자들에게 부드럽고 멋진 로딩 화면을 제공할 수 있습니다.

NVActivityIndicatorView에 대한 자세한 내용은 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하시기 바랍니다.