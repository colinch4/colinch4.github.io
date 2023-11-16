---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 로딩 화면 컴포넌트 디자인 및 사용자 인터렉션 개선하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱을 개발하다 보면 로딩 화면이나 네트워크 요청 시 인디케이터를 이용해서 사용자에게 진행 중임을 알리는 것이 중요합니다. 이때 NVActivityIndicatorView 라이브러리를 사용하면 쉽게 로딩 화면 컴포넌트를 디자인하고, 사용자 인터렉션을 개선할 수 있습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS용 로딩 인디케이터 라이브러리입니다. 다양한 스타일과 커스터마이징 옵션을 제공하여, 다양한 디자인의 로딩 화면을 구현할 수 있습니다.

## 설치 방법

NVActivityIndicatorView는 Cocoapods를 통해 설치할 수 있습니다. `Podfile`에 다음과 같이 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 의존성을 설치합니다.

```
$ pod install
```

## 사용 방법

1. 먼저, `NVActivityIndicatorView`를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 생성하고 원하는 위치에 추가합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballBeat, color: .gray, padding: nil)
view.addSubview(activityIndicatorView)
```

- `frame`: 로딩 화면의 크기와 위치를 지정합니다.
- `type`: 로딩 화면의 스타일을 선택합니다. 다양한 스타일이 제공되므로 원하는 스타일을 선택할 수 있습니다.
- `color`: 로딩 화면의 색상을 지정합니다.
- `padding`: 로딩 화면의 내부 여백을 지정합니다. (nil일 경우 기본값을 사용합니다.)

3. 로딩 화면을 시작하거나 중지합니다.

```swift
activityIndicatorView.startAnimating() // 로딩 화면 시작

activityIndicatorView.stopAnimating()  // 로딩 화면 중지
```

- `startAnimating()`: 로딩 화면을 시작합니다.
- `stopAnimating()`: 로딩 화면을 중지합니다.

## 사용자 인터렉션 개선하기

NVActivityIndicatorView는 로딩 화면을 표시하는 동안 사용자의 인터렉션을 막는 기능을 제공합니다. 사용자의 상호 작용을 제한하고 싶을 때, 다음 메서드를 호출하여 로딩 화면을 활성화시킵니다.

```swift
activityIndicatorView.startAnimating()
UIApplication.shared.beginIgnoringInteractionEvents()
```

로딩 화면을 중지하고 사용자의 인터렉션을 다시 활성화하려면 다음 메서드를 호출합니다.

```swift
activityIndicatorView.stopAnimating()
UIApplication.shared.endIgnoringInteractionEvents()
```

## 마무리

NVActivityIndicatorView를 사용하여 로딩 화면 컴포넌트를 디자인하고, 사용자 인터렉션을 개선하는 방법에 대해 알아보았습니다. 다양한 스타일과 커스터마이징 옵션을 활용하여 앱의 로딩 화면을 멋지게 구현해보세요. 더 자세한 내용은 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고해주세요.