---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 크기와 외관 커스터마이징하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 간단하고 멋진 로딩 인디케이터입니다. 이 블로그 포스트에서는 Swift에서 NVActivityIndicatorView의 크기와 외관을 커스터마이징하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 앱의 작업이나 데이터를 로딩하는 동안 유저에게 시각적인 피드백을 제공하기 위해 사용됩니다. 즉, 로딩 중인 상태를 나타내는 애니메이션을 제공합니다. 

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView는 Cocoapods를 통해 쉽게 설치할 수 있습니다. 먼저 `Podfile`에 다음과 같이 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그런 다음 터미널에서 다음 명령어를 실행하여 Cocoapods를 설치합니다.

```
pod install
```

## NVActivityIndicatorView 사용하기

먼저, NVActivityIndicatorView를 import 하고 사용할 뷰 컨트롤러에서 `NVActivityIndicatorViewable` 프로토콜을 채택합니다.

```swift
import NVActivityIndicatorView
```

```swift
class MyViewController: UIViewController, NVActivityIndicatorViewable {
    // ...
}
```

### 기본 NVActivityIndicatorView 생성하기

```swift
let activityData = ActivityData()
NVActivityIndicatorView.startAnimating(activityData)
```

위 코드에서 `ActivityData()`는 NVActivityIndicatorView에 대한 기본 설정을 나타냅니다. 이 설정은 NVActivityIndicatorView의 크기, 스타일, 색상 등을 제어합니다. 아쉽게도, NVActivityIndicatorView에서 제공하는 크기 및 스타일 옵션은 제한적입니다.

### NVActivityIndicatorView 크기 및 외관 커스터마이징하기

NVActivityIndicatorView는 `.frame`, `.type`, `.color`, `.padding` 등의 속성을 통해 크기 및 외관을 커스터마이징할 수 있습니다.

#### 크기 조정하기

기본적으로 NVActivityIndicatorView의 크기는 제한적이며 크기를 조절하기 위해 `.frame` 속성을 사용할 수 있습니다. 아래 예제에서는 NVActivityIndicatorView의 프레임을 `(0, 0, 50, 50)`으로 설정합니다.

```swift
let activityData = ActivityData(size: CGSize(width: 50, height: 50))
NVActivityIndicatorView.startAnimating(activityData)
```

#### 스타일 변경하기

NVActivityIndicatorView는 다양한 스타일을 제공합니다. `.type` 속성을 사용하여 원하는 스타일을 선택할 수 있습니다. 예를 들어 아래 예제에서는 `.ballPulse` 스타일을 사용합니다.

```swift
let activityData = ActivityData(type: .ballPulse)
NVActivityIndicatorView.startAnimating(activityData)
```

#### 색상 변경하기

NVActivityIndicatorView의 색상은 `.color` 속성을 사용하여 변경할 수 있습니다. 아래 예제에서는 NVActivityIndicatorView의 색상을 빨간색으로 설정합니다.

```swift
let activityData = ActivityData(color: .red)
NVActivityIndicatorView.startAnimating(activityData)
```

#### 간격(padding) 조정하기

NVActivityIndicatorView의 외부와 실제 인디케이터 사이에 간격을 두려면 `.padding` 속성을 사용하면 됩니다. 아래 예제에서는 `20` 포인트의 간격을 두고 NVActivityIndicatorView를 시작합니다.

```swift
let activityData = ActivityData(padding: 20)
NVActivityIndicatorView.startAnimating(activityData)
```

## 결론

이제 Swift에서 NVActivityIndicatorView의 크기와 외관을 커스터마이징하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하여 로딩 인디케이터를 손쉽게 도입하고 앱의 사용자에게 시각적인 피드백을 제공할 수 있습니다. 감사합니다!

## 참고 문서

- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)