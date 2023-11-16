---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 표시하고 사용자 인터렉션 제어하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

데이터를 로딩하는 동안 사용자에게 로딩 상태를 시각적으로 표시하고, 사용자의 인터렉션을 제어하는 것은 앱의 사용성을 향상시키는 중요한 요소입니다. NVActivityIndicatorView는 Swift에서 데이터 로딩 상태를 시각적으로 나타내기 위한 강력한 도구입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 데이터 로딩 상태를 나타내기 위한 활동 표시기입니다. 다양한 형태의 애니메이션을 제공하며, 크기와 색상도 다양하게 설정할 수 있습니다. 또한, 사용자의 인터렉션을 감지하여 로딩 중에는 사용자의 입력을 차단할 수도 있습니다.

## 설치

먼저, Cocoapods를 사용하여 NVActivityIndicatorView를 설치합니다. Podfile에 다음과 같은 의존성을 추가한 후, 터미널에서 `pod install` 명령을 실행합니다.

```ruby
pod 'NVActivityIndicatorView'
```

## 사용 방법

NVActivityIndicatorView를 사용하기 위해 다음 단계를 따라주세요.

1. NVActivityIndicatorView import하기

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView 인스턴스 생성하기

```swift
let activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballSpinFadeLoader, color: .gray, padding: nil)
```

3. 화면에 표시할 위치 설정하기

```swift
activityIndicator.center = view.center
```

4. 화면에 추가하기

```swift
view.addSubview(activityIndicator)
```

5. 로딩 시작하기

```swift
activityIndicator.startAnimating()
```

6. 로딩 종료하기

```swift
activityIndicator.stopAnimating()
```

7. 사용자 인터렉션 제어하기

로딩 중에 사용자의 입력을 차단하고 싶다면, 다음과 같이 인터렉션 제어 메서드를 사용할 수 있습니다.

```swift
// 인터렉션 제어 시작
activityIndicator.startAnimating()
UIApplication.shared.beginIgnoringInteractionEvents()

// 인터렉션 제어 종료
activityIndicator.stopAnimating()
UIApplication.shared.endIgnoringInteractionEvents()
```

## 추가 설정

NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 표시하는 동안 다양한 설정을 추가할 수 있습니다. 예를 들어, 애니메이션의 크기와 색상을 변경하거나 패딩을 설정할 수 있습니다.

```swift
activityIndicator.color = .red
activityIndicator.padding = 20
```

## 마무리

NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 시각적으로 표시하고 사용자의 인터렉션을 제어하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 앱의 사용성을 향상시키는데 유용한 도구이며, 다양한 설정으로 로딩 상태를 자유롭게 커스터마이징할 수 있습니다.

더 자세한 정보는 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하세요.