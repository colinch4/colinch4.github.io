---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 인터페이스 디자인 강화하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

iOS 앱을 개발할 때, 사용자 인터페이스 디자인은 매우 중요한 요소입니다. 사용자들은 앱의 디자인에 큰 영향을 받으며, 시각적인 요소가 사용자 경험에 미치는 영향은 매우 큽니다. 이번 기사에서는 `NVActivityIndicatorView` 라이브러리를 이용하여 사용자 인터페이스를 더욱 향상시킬 수 있는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

`NVActivityIndicatorView`는 iOS 앱에서 사용할 수 있는 주로 로딩 인디케이터를 제공하는 오픈 소스 라이브러리입니다. 로딩 중인 상태를 사용자에게 시각적으로 알려주는 용도로 사용할 수 있으며, 다양한 스타일과 색상 옵션을 제공하여 개발자가 원하는 디자인에 맞추어 사용할 수 있습니다.

## 설치 방법

`NVActivityIndicatorView`를 사용하기 위해 먼저 CocoaPods을 이용하여 라이브러리를 설치해야 합니다. `Podfile`에 다음과 같은 내용을 추가한 뒤, 콘솔에서 `pod install` 명령을 실행하면 됩니다.

```swift
pod 'NVActivityIndicatorView'
```

## 사용 방법

1. 먼저, `NVActivityIndicatorView`를 사용할 Swift 파일에 import 구문을 추가합니다.

```swift
import NVActivityIndicatorView
```

2. `NVActivityIndicatorView`를 초기화하고 특정 위치에 추가합니다. 다음은 화면 중앙에 인디케이터를 추가하는 예시입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballBeat, color: .blue, padding: nil)
activityIndicatorView.center = self.view.center
self.view.addSubview(activityIndicatorView)
```

3. 원하는 시점에 인디케이터를 시작하고, 종료할 수 있습니다. 다음은 인디케이터를 시작하는 코드입니다.

```swift
activityIndicatorView.startAnimating()
```

4. 원하는 시점에 인디케이터를 종료하는 코드입니다.

```swift
activityIndicatorView.stopAnimating()
```

## 다양한 스타일과 색상 옵션

`NVActivityIndicatorView`는 다양한 스타일과 색상 옵션을 제공합니다. 로딩 인디케이터의 모양과 색상을 개발자가 직접 설정할 수 있으며, 아래는 몇 가지 예시입니다.

- 스타일: `NVActivityIndicatorType` 열거형을 사용하여 다양한 스타일 중 하나를 선택할 수 있습니다. 예를 들어 `.circleStrokeSpin`은 동그라미로 구성된 스타일이고, `.ballPulse`는 작은 구슬들이 펄스하는 스타일입니다.

- 색상: 인디케이터의 색상을 직접 지정할 수 있으며, `UIColor`를 사용하여 설정할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .circleStrokeSpin, color: .red, padding: nil)
```

## 마무리

`NVActivityIndicatorView`를 사용하여 앱의 사용자 인터페이스를 강화할 수 있습니다. 로딩 중임을 알려주는 인디케이터를 추가함으로써 사용자는 장기간 대기하는 동안에도 진행 중임을 알 수 있습니다. 다양한 스타일과 색상 옵션을 이용하여 앱의 디자인을 더욱 효과적으로 확장할 수 있습니다.

참고: [NVActivityIndicatorView GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)