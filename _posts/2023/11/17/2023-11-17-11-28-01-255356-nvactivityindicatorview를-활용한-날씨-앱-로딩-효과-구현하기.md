---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 날씨 앱 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번에는 Swift에서 NVActivityIndicatorView를 사용하여 날씨 앱의 로딩 효과를 구현하는 방법을 알아보겠습니다.

NVActivityIndicatorView는 iOS 앱에서 로딩 효과를 제공하는 라이브러리로, 다양한 스타일과 크기의 로딩 효과를 제공합니다. 

## 1. NVActivityIndicatorView 설치하기

먼저, 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. CocoaPods를 사용한다면, Podfile에 다음과 같이 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해, 우선 NVActivityIndicatorView를 import 해야 합니다.

```swift
import NVActivityIndicatorView
```

그리고 로딩 효과를 넣을 UIView를 생성하고, 해당 UIView에 NVActivityIndicatorView를 추가합니다.

```swift
let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: 80, height: 80))
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 80, height: 80), type: .ballBeat, color: .white, padding: 0)
loadingView.addSubview(activityIndicatorView)
```

위 코드에서 `loadingView`는 로딩 효과를 넣을 UIView입니다. `activityIndicatorView`는 NVActivityIndicatorView입니다. 위 예시에서는 `ballBeat` 스타일을 사용하고, 흰색으로 설정하였습니다.

로딩 효과를 넣을 곳에서 `startAnimating()` 메서드를 호출하여 로딩 효과를 시작하고, `stopAnimating()` 메서드를 호출하여 로딩 효과를 멈출 수 있습니다.

```swift
activityIndicatorView.startAnimating()
```

## 3. 커스텀 로딩 효과 만들기

NVActivityIndicatorView에는 다양한 스타일의 로딩 효과가 제공되지만, 필요한 경우 직접 커스텀 로딩 효과를 만들 수도 있습니다.

```swift
let customIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 80, height: 80))
customIndicatorView.type = .custom(UIImage(named: "custom_indicator"))
```

위 코드에서 `custom_indicator`는 사용자가 직접 만든 커스텀 로딩 효과 이미지입니다. `type` 속성을 `.custom`으로 설정하고, 해당 이미지를 설정하는 것으로 커스텀 로딩 효과를 만들 수 있습니다.

## 결론

NVActivityIndicatorView를 활용하면 다양한 스타일의 날씨 앱 로딩 효과를 손쉽게 구현할 수 있습니다. 해당 라이브러리는 개발자가 로딩 효과를 직접 구현하는 수고를 덜어주고, 앱에 유용하고 멋진 로딩 효과를 추가하는 데 도움이 됩니다.

더 많은 NVActivityIndicatorView의 기능과 사용법은 [공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.