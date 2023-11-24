---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 UI 스타일링 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 소개
NVActivityIndicatorView는 iOS 앱에서 사용되는 다양한 로딩 인디케이터(UIActivityIndicator)를 구현할 수 있는 오픈 소스 라이브러리입니다. 이 라이브러리를 사용하면 로딩화면을 더욱 멋지고 다양한 스타일로 표현할 수 있습니다.

## 설치
NVActivityIndicatorView를 사용하기 위해선 CocoaPods를 통해 설치해야 합니다. Podfile에 다음과 같이 추가한 후, `pod install`을 실행합니다.

```
pod 'NVActivityIndicatorView'
```

## 사용법
1. 먼저, NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView 인스턴스를 생성하고 원하는 스타일 및 프로퍼티를 설정합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: nil)
activityIndicatorView.center = view.center
activityIndicatorView.startAnimating()
view.addSubview(activityIndicatorView)
```

3. 필요한 곳에서 `startAnimating()`을 호출하여 로딩 인디케이터를 시작하고, `stopAnimating()`을 호출하여 종료할 수 있습니다.

```swift
activityIndicatorView.startAnimating()
// 로딩 동작 중...

activityIndicatorView.stopAnimating()
// 로딩 종료
```

## 스타일 및 색상 변경
NVActivityIndicatorView는 다양한 스타일과 색상을 제공합니다. 다음과 같은 스타일과 색상을 사용할 수 있습니다.

### 스타일
- .ballPulse
- .ballGridPulse
- .ballClipRotate
- .squareSpin
- .ballClipRotatePulse
- .ballClipRotateMultiple
- .ballPulseRise
- .ballRotate
- .cubeTransition
- .ballZigZag
- .ballZigZagDeflect
- .ballTrianglePath
- .ballScale
- .lineScale
- .lineScaleParty
- .ballScaleMultiple
- .ballPulseSync
- .ballBeat
- .lineScalePulseOut
- .lineScalePulseOutRapid
- .ballScaleRipple
- .ballScaleRippleMultiple
- .ballSpinFadeLoader
- .lineSpinFadeLoader
- .triangleSkewSpin
- .pacman
- .ballGridBeat
- .semiCircleSpin

### 색상
- .white
- .gray
- .green
- .blue
- .red
- .orange
- .purple

원하는 스타일과 색상을 적용하려면 `type` 및 `color` 매개변수를 조정하면 됩니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: nil)
```

## 결론
NVActivityIndicatorView는 로딩 인디케이터를 쉽고 다양한 스타일로 표현할 수 있는 훌륭한 라이브러리입니다. iOS 앱에서 로딩 화면을 구현할 때 이 라이브러리를 사용하여 사용자에게 더 나은 사용자 경험을 제공할 수 있습니다.

## 참고
- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)