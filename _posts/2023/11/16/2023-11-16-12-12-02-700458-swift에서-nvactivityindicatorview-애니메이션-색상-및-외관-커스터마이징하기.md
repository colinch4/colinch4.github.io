---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 색상 및 외관 커스터마이징하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

[Swift](https://swift.org/)는 iOS 및 macOS 애플리케이션 개발을 위한 강력한 프로그래밍 언어입니다. 우리는 종종 앱에서 로딩 인디케이터를 사용하여 작업이 진행 중임을 사용자에게 알리는 데 사용합니다. NVActivityIndicatorView는 Swift에서 쉽게 사용할 수 있는 많은 애니메이션 효과를 제공하는 뛰어난 라이브러리입니다. 하지만 기본 테마 이외에도 로딩 인디케이터의 색상이나 외관을 사용자 정의해야하는 경우가 있습니다.

이 글에서는 Swift에서 NVActivityIndicatorView 애니메이션의 색상과 외관을 사용자 정의하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 소개

NVActivityIndicatorView는 iOS 및 macOS에서 사용할 수 있는 로딩 인디케이터를 구현하기 위한 쉬운 방법을 제공하는 Swift 라이브러리입니다. 다양한 애니메이션 스타일과 색상 테마를 제공하여 애플리케이션에 맞는 로딩 인디케이터를 만들 수 있습니다.

## NVActivityIndicatorView 적용

첫 번째로, NVActivityIndicatorView 라이브러리를 프로젝트에 추가해야합니다. [CocoaPods](https://cocoapods.org/)를 사용하는 경우 `Podfile`에 다음과 같이 추가할 수 있습니다:

```ruby
pod 'NVActivityIndicatorView', '~> 5.0'
```

프로젝트를 업데이트하기 위해 터미널에서 `pod install` 명령을 실행하세요.

이제 `ViewController` 파일로 이동하여 NVActivityIndicatorView를 적용해보겠습니다. 먼저, import 문을 추가하여 NVActivityIndicatorView를 불러옵니다:

```swift
import NVActivityIndicatorView
```

이제 인스턴스를 생성하고 원하는 위치에 적용해보겠습니다. `viewDidLoad` 메서드에 다음 코드를 추가하세요:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballPulse, color: .red, padding: nil)
activityIndicatorView.center = view.center
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위의 코드에서 `NVActivityIndicatorView` 인스턴스를 생성한 후, 프레임 크기, 애니메이션 유형, 색상, 패딩 등을 설정합니다. 그런 다음, 인스턴스를 뷰의 중앙에 배치하고 뷰에 추가한 후, `startAnimating()`으로 애니메이션을 시작합니다.

## 커스터마이징 옵션

NVActivityIndicatorView는 많은 커스터마이징 옵션을 제공하여 로딩 인디케이터의 색상과 외관을 변경할 수 있습니다. 몇 가지 중요한 옵션에 대해 알아보겠습니다:

### 색상 변경

NVActivityIndicatorView의 색상은 `.color` 속성을 통해 변경할 수 있습니다. 다음과 같이 코드를 수정하여 로딩 인디케이터의 색상을 변경할 수 있습니다:

```swift
activityIndicatorView.color = .blue
```

### 애니메이션 타입 변경

NVActivityIndicatorView의 애니메이션 타입은 `.type` 속성을 통해 변경할 수 있습니다. 로딩 인디케이터 유형을 변경하는 예시 코드는 다음과 같습니다:

```swift
activityIndicatorView.type = .lineScalePulseOut
```

### 크기 변경

NVActivityIndicatorView의 크기는 프레임 크기를 조정하여 변경할 수 있습니다. 다음 코드는 로딩 인디케이터의 너비와 높이를 50으로 변경하는 예시입니다:

```swift
activityIndicatorView.frame.size = CGSize(width: 50, height: 50)
```

### 패딩 설정

NVActivityIndicatorView의 패딩은 `.padding` 속성을 통해 변경할 수 있습니다. 로딩 인디케이터 주위의 여백을 조정하는 예시 코드는 다음과 같습니다:

```swift
activityIndicatorView.padding = 20
```

## 결론

이제 Swift에서 NVActivityIndicatorView 애니메이션의 색상과 외관을 사용자 정의하는 방법을 알게되었습니다. NVActivityIndicatorView는 다양한 옵션을 제공하여 로딩 인디케이터를 개인화하고 다른 애니메이션 스타일을 적용할 수 있습니다. 고유한 애플리케이션에 맞는 로딩 인디케이터를 만들어보세요!