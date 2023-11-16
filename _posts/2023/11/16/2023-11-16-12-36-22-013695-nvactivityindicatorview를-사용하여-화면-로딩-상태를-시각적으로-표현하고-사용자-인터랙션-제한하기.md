---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 상태를 시각적으로 표현하고 사용자 인터랙션 제한하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱에서 데이터를 로드하거나 오랜 시간 동안 작업을 처리해야 하는 경우에는 사용자가 앱이 작업을 수행 중임을 인식할 수 있는 시각적인 피드백을 제공하는 것이 중요합니다. 이러한 경우에 NVActivityIndicatorView 라이브러리를 사용하여 로딩 상태를 시각적으로 표현할 수 있습니다. 또한 사용자 인터랙션을 제한하여 앱이 작업을 완료하기 전까지 다른 작업을 수행하지 못하도록 할 수 있습니다.

## NVActivityIndicatorView 라이브러리 설치

먼저, NVActivityIndicatorView를 사용하기 위해 라이브러리를 설치해야 합니다. 이를 위해 Cocoapods를 사용하는 것이 가장 편리합니다. 프로젝트의 Podfile에 다음과 같은 코드를 추가한 후, `pod install` 명령을 사용하여 라이브러리를 설치합니다.

```ruby
pod 'NVActivityIndicatorView'
```

설치가 완료되면, 아래에서 설명할 작업을 수행할 준비가 완료됩니다.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 초기화합니다. 로딩 인디케이터의 모양, 색상, 크기 등을 설정할 수 있습니다. 예를 들어, 다음과 같이 초기화할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)
```

2. 로딩 상태를 표시할 뷰에 NVActivityIndicatorView를 추가합니다.

```swift
view.addSubview(activityIndicatorView)
```

3. NVActivityIndicatorView를 화면 중앙에 정렬하고, 로딩 상태를 표시하기 위해 시작 메소드를 호출합니다.

```swift
activityIndicatorView.center = view.center
activityIndicatorView.startAnimating()
```

4. 작업이 완료되었을 때, NVActivityIndicatorView를 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 사용자 인터랙션 제한하기

로딩 상태를 표시하고자 하는 작업 수행 중에는 사용자가 다른 작업을 수행하거나 인터랙션을 하지 못하도록 제한해야 합니다. 이를 위해 `UIApplication`의 `beginIgnoringInteractionEvents()`와 `endIgnoringInteractionEvents()` 메소드를 사용할 수 있습니다. 예를 들어, 로딩 상태를 표현하기 전에 다음과 같이 인터랙션을 제한합니다.

```swift
UIApplication.shared.beginIgnoringInteractionEvents()
```

작업이 완료된 후에는 다음과 같이 인터랙션을 다시 허용합니다.

```swift
UIApplication.shared.endIgnoringInteractionEvents()
```

## 요약

NVActivityIndicatorView를 사용하여 앱에서 화면 로딩 상태를 시각적으로 표현하고 사용자 인터랙션을 제한하는 방법을 알아보았습니다. 이를 통해 사용자에게 작업이 진행 중임을 알리고, 작업이 완료될 때까지 다른 작업을 수행하지 못하도록 할 수 있습니다. NVActivityIndicatorView의 다양한 설정 옵션을 활용하여 앱의 로딩 상태 표현을 개선할 수 있습니다.

참고: [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)