---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 설정과 커스터마이징 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 강력한 애니메이션 라이브러리 중 하나입니다. 이 라이브러리는 다양한 종류의 로딩 애니메이션을 제공하며, 설정과 커스터마이징을 통해 원하는 모양과 동작을 만들 수 있습니다.

## NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 프로젝트에 추가해야합니다. 이를 위해 Cocoapods를 사용하려면 Podfile에 다음과 같은 의존성을 추가하세요.

```
pod 'NVActivityIndicatorView'
```

그런 다음 터미널에서 `pod install` 명령을 실행하여 의존성을 설치하세요.

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하려면 먼저 해당 라이브러리를 import 해야합니다.

```swift
import NVActivityIndicatorView
```

다음으로, 원하는 위치에 NVActivityIndicatorView를 추가하고 시작하는 방법을 알아보겠습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: nil)
self.view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위 예시에서는 새로운 NVActivityIndicatorView 인스턴스를 생성하고, 해당 뷰에 추가한 다음, `startAnimating()` 메서드를 호출하여 애니메이션을 시작합니다.

## NVActivityIndicatorView 커스터마이징

NVActivityIndicatorView는 다양한 커스터마이징 옵션을 제공합니다. 몇 가지 예를 살펴보겠습니다.

### 색상 변경하기

```swift
activityIndicatorView.color = .red
```

위 예시에서는 NVActivityIndicatorView의 색상을 빨간색으로 변경합니다.

### 크기 조정하기

```swift
activityIndicatorView.frame = CGRect(x: 0, y: 0, width: 100, height: 100)
```

위 예시에서는 NVActivityIndicatorView의 크기를 변경합니다.

### 애니메이션 타입 변경하기

```swift
activityIndicatorView.type = .circleStrokeSpin
```

위 예시에서는 NVActivityIndicatorView의 애니메이션 타입을 원형으로 변경합니다.

## 결론

이제 Swift에서 NVActivityIndicatorView의 설정과 커스터마이징 방법에 대해 알아보았습니다. 이 라이브러리는 애니메이션을 사용하여 로딩 화면을 구현할 때 유용한 도구입니다. 원하는 스타일과 동작을 만들기 위해 다양한 옵션을 활용해보세요.

## 참고 자료

- [NVActivityIndicatorView GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)