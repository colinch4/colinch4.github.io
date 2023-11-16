---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 경험 향상"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift에서 NVActivityIndicatorView를 이용하여 사용자의 경험(UX)을 향상시키는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS에서 로딩 인디케이터(Loading Indicator)를 간편하게 구현할 수 있는 라이브러리입니다. 이 라이브러리를 사용하면 앱이 어떤 작업을 수행하는 동안 로딩 인디케이터를 보여줄 수 있어 사용자가 작업이 진행 중인지 알기 쉽습니다.

## NVActivityIndicatorView 설치

먼저, NVActivityIndicatorView를 설치해야 합니다. CocoaPods를 사용하실 경우 `Podfile`에 다음과 같이 추가해주세요.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널을 열어 프로젝트 폴더로 이동한 뒤 `pod install` 명령어를 실행하면 NVActivityIndicatorView가 설치됩니다.

## NVActivityIndicatorView 사용 방법

NVActivityIndicatorView를 사용하기 위해서는 다음과 같은 단계를 따라야 합니다.

### 1. NVActivityIndicatorView 초기화

```swift
import NVActivityIndicatorView
```

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballBeat, color: .gray, padding: nil)
```

위의 코드에서 `type`은 로딩 인디케이터의 모양을 정하는데, 여러 가지 모양 중 하나를 선택할 수 있습니다. `color`는 인디케이터의 색상을 정하는데 사용되며, `padding`은 인디케이터의 크기를 조절하는 옵션입니다.

### 2. 인디케이터 보여주기

인디케이터를 보여주려면 다음과 같은 코드를 사용합니다.

```swift
activityIndicatorView.startAnimating()
```

### 3. 인디케이터 숨기기

인디케이터를 숨기려면 다음과 같은 코드를 사용합니다.

```swift
activityIndicatorView.stopAnimating()
```

## NVActivityIndicatorView 커스터마이징

NVActivityIndicatorView는 다양한 커스터마이징 옵션을 제공합니다. 예를 들어, 색상, 크기, 애니메이션 속도 등을 조정할 수 있습니다. 자세한 내용은 도큐멘테이션을 참고하시기 바랍니다.

## 마무리

이번 포스트에서는 Swift에서 NVActivityIndicatorView를 이용하여 사용자 경험을 향상시킬 수 있다는 것을 알아보았습니다. 로딩 인디케이터는 사용자가 어떤 작업을 수행하는 동안에도 편안한 사용자 경험을 제공할 수 있는 중요한 요소입니다.