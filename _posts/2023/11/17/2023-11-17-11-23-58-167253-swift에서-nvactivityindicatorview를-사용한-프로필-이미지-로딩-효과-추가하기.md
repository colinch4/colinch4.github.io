---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용한 프로필 이미지 로딩 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

프로필 이미지 로딩 시 사용자에게 시각적인 피드백을 제공하는 것은 앱의 사용자 경험을 향상시키는 중요한 요소입니다. 이를 위해 NVActivityIndicatorView라는 오픈 소스 라이브러리를 사용하여 Swift에서 프로필 이미지 로딩 효과를 추가해 보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 커스텀 로딩 인디케이터를 제공하는 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하며, 간단한 API를 통해 쉽게 사용할 수 있습니다.

## 프로젝트 설정

먼저, 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. 이를 위해 CocoaPods를 사용하겠습니다. Podfile에 아래와 같이 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 아래 명령어를 실행하여 의존성을 설치합니다.

```
pod install
```

## 사용 방법

### 1. NVActivityIndicatorView 추가하기

프로필 이미지 로딩 효과를 추가할 뷰 컨트롤러에서 `NVActivityIndicatorView`를 import 해줍니다.

```swift
import NVActivityIndicatorView
```

### 2. 인디케이터 생성하기

로딩 효과를 추가할 뷰 컨트롤러에서 `NVActivityIndicatorView` 인스턴스를 생성합니다. 타입이 `NVActivityIndicatorView`이므로 원하는 위치와 크기를 지정하여 뷰에 추가합니다.

```swift
let activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
view.addSubview(activityIndicator)
```

### 3. 인디케이터 스타일 설정하기

`NVActivityIndicatorView`의 `type` 프로퍼티를 설정하여 로딩 효과의 스타일을 선택할 수 있습니다. 다양한 스타일 중에서 원하는 스타일을 선택하세요.

```swift
activityIndicator.type = .ballSpinFadeLoader
```

### 4. 인디케이터 색상 설정하기

`NVActivityIndicatorView`의 `color` 프로퍼티를 설정하여 로딩 효과의 색상을 변경할 수 있습니다. 원하는 색상으로 설정하세요.

```swift
activityIndicator.color = .red
```

### 5. 인디케이터 애니메이션 시작하기

로딩 효과를 시작하기 위해 `startAnimating()` 메서드를 호출합니다.

```swift
activityIndicator.startAnimating()
```

### 6. 인디케이터 애니메이션 정지하기

로딩 효과를 정지하기 위해 `stopAnimating()` 메서드를 호출합니다.

```swift
activityIndicator.stopAnimating()
```

## 결론

NVActivityIndicatorView를 사용하여 Swift에서 프로필 이미지 로딩 효과를 추가하는 방법에 대해 알아보았습니다. 이러한 로딩 효과는 사용자들에게 로딩 중임을 시각적으로 알려주어 좋은 사용자 경험을 제공할 수 있습니다. 이러한 기능은 앱의 성능 향상을 위해 매우 유용하므로, 앱 개발에 활용해보세요.

## 참고 자료

1. [NVActivityIndicatorView Github 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)
2. [CocoaPods 공식 웹사이트](https://cocoapods.org/)