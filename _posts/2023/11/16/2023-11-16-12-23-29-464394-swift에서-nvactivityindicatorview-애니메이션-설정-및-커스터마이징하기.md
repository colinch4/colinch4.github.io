---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 설정 및 커스터마이징하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 강력한 애니메이션 라이브러리입니다. 이 라이브러리는 다양한 종류의 로딩 인디케이터를 제공하며, 앱의 사용자 인터페이스에 효과적인 로딩 애니메이션을 구현할 수 있습니다.

이 가이드에서는 NVActivityIndicatorView를 설치하고 사용하는 방법에 대해 알아보고, 애니메이션의 스타일과 색상을 커스터마이징하는 방법에 대해 배워보겠습니다.

## 1. NVActivityIndicatorView 설치하기

첫째로, NVActivityIndicatorView를 프로젝트에 설치해야 합니다. Swift Package Manager 또는 CocoaPods를 사용하여 설치할 수 있습니다.

### 1.1 Swift Package Manager를 사용하는 경우

프로젝트의 `Package.swift` 파일에 아래와 같이 종속성을 추가합니다:

```swift
dependencies: [
    .package(url: "https://github.com/ninjaprox/NVActivityIndicatorView.git", from: "5.0.0")
]
```

### 1.2 CocoaPods를 사용하는 경우

프로젝트의 Podfile에 아래와 같이 NVActivityIndicatorView를 추가하고, 터미널에서 `pod install`을 실행합니다:

```ruby
pod 'NVActivityIndicatorView'
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 프로젝트에 추가했다면, 이제 애니메이션을 사용할 준비가 되었습니다.

```swift
import NVActivityIndicatorView
```

### 2.1 기본적인 NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하여 간단한 로딩 애니메이션을 만드는 방법은 아래와 같습니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: nil)
view.addSubview(activityIndicatorView)

activityIndicatorView.startAnimating()
```

위의 코드에서는 `NVActivityIndicatorView` 인스턴스를 생성하고, 원하는 스타일과 색상을 설정합니다. 그리고 해당 인스턴스를 화면에 추가하고 애니메이션을 시작합니다.

### 2.2 NVActivityIndicatorView 커스터마이징하기

NVActivityIndicatorView는 다양한 스타일과 색상을 제공합니다. 로딩 인디케이터의 스타일과 색상을 변경하여 원하는 디자인에 맞게 커스터마이징할 수 있습니다.

#### 스타일 변경하기

```swift
activityIndicatorView.type = .lineScale
```

위의 코드에서는 `type` 속성을 사용하여 로딩 인디케이터의 스타일을 변경합니다. 다양한 스타일 옵션은 `NVActivityIndicatorType` 열거형을 확인하여 선택할 수 있습니다.

#### 색상 변경하기

```swift
activityIndicatorView.color = .blue
```

위의 코드에서는 `color` 속성을 사용하여 로딩 인디케이터의 색상을 변경합니다. 원하는 색상을 선택하여 로딩 애니메이션을 보다 세련된 디자인으로 설정할 수 있습니다.

## 3. 마무리

이제 당신은 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션을 설정하고 커스터마이징할 수 있는 방법을 배웠습니다. 이 라이브러리는 로딩 인디케이터를 구현하는데 유용하며, 앱의 사용자 경험을 향상시킬 수 있는 강력한 도구입니다.

더 많은 옵션과 사용 방법은 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.