---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 외관 및 색상 커스터마이징하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

![NVActivityIndicatorView](https://raw.githubusercontent.com/ninjaprox/NVActivityIndicatorView/master/ReadmeResources/sample.gif)

NVActivityIndicatorView는 Swift로 작성된 로딩 애니메이션을 구현하기 위한 라이브러리입니다. 이 라이브러리를 사용하면 간단하고 멋진 로딩 애니메이션을 쉽게 추가할 수 있습니다. 이 포스트에서는 NVActivityIndicatorView를 사용하여 애니메이션의 외관과 색상을 커스터마이징하는 방법을 알아보겠습니다.

## NVActivityIndicatorView 가져오기
먼저, [CocoaPods](https://cocoapods.org/)를 통해 NVActivityIndicatorView를 프로젝트에 추가합니다. `Podfile`에 다음과 같은 라인을 추가한 후 `pod install` 명령어를 실행합니다.

```swift
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기
NVActivityIndicatorView를 사용하기 위해 다음과 같이 코드를 작성합니다.

```swift
import NVActivityIndicatorView
```

## 애니메이션 커스터마이징하기
NVActivityIndicatorView의 외관과 색상을 커스터마이징하기 위해 다음과 같은 속성을 사용할 수 있습니다.

- `type`: 애니메이션의 종류를 선택합니다. 가능한 값은 `ballPulse`, `ballGridPulse`, `ballClipRotate`, `squareSpin` 등이 있습니다.
- `color`: 애니메이션의 색상을 선택합니다.
- `padding`: 애니메이션의 간격을 설정합니다.
- `displayTimeThreshold`: 애니메이션을 표시하는 시간을 지정합니다.

아래는 간단한 예시입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballPulse, color: .blue, padding: 20)
```

## 정리
위의 방법을 사용하여 NVActivityIndicatorView를 사용하여 로딩 애니메이션의 외관과 색상을 커스터마이징할 수 있습니다. 더 많은 옵션과 기능을 사용하고 싶다면 [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.

> **참고:** NVActivityIndicatorView는 iOS 8.0 이상에서만 사용할 수 있습니다.