---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 타이머 앱 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 NVActivityIndicatorView를 활용하여 타이머 앱의 로딩 효과를 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS에서 로딩 효과를 제공하는 오픈 소스 라이브러리입니다. 다양한 스타일과 크기의 로딩 인디케이터를 제공하여 앱의 로딩 상태를 시각적으로 표현할 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. Terminal을 실행하여 프로젝트의 Podfile이 위치한 폴더로 이동한 후, 다음 명령을 실행해주세요.

```swift
pod 'NVActivityIndicatorView'
```

그리고, Terminal에서 `pod install` 명령을 실행하여 라이브러리를 설치해주세요. 이제 프로젝트에서 NVActivityIndicatorView를 사용할 준비가 되었습니다.

## NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 import해주세요.

```swift
import NVActivityIndicatorView
```

2. 다음으로, NVActivityIndicatorView를 생성하고 화면에 표시하기 위한 코드를 작성해주세요.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballRotateChase, color: .blue, padding: nil)
activityIndicatorView.center = view.center
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위 코드에서는 NVActivityIndicatorView의 크기와 스타일을 설정하고, 앱 화면 중앙에 위치하도록 설정하였습니다. 그리고 `startAnimating()` 메서드를 호출하여 로딩 효과를 시작합니다.

3. 로딩 효과를 중지하고 제거하기 위한 코드를 작성해주세요.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

위 코드에서는 `stopAnimating()` 메서드를 호출하여 로딩 효과를 중지하고, `removeFromSuperview()` 메서드를 호출하여 NVActivityIndicatorView를 화면에서 제거합니다.

## 마무리

이제 NVActivityIndicatorView를 활용하여 타이머 앱의 로딩 효과를 구현하는 방법을 알아보았습니다. 라이브러리를 설치하고, 필요한 위치에서 로딩 효과를 생성하고 중지하는 코드를 작성하면 됩니다. 직접 다양한 스타일의 로딩 효과를 적용하여 앱의 사용성을 향상시켜보세요!

## 참고 자료

- NVActivityIndicatorView GitHub 저장소: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)