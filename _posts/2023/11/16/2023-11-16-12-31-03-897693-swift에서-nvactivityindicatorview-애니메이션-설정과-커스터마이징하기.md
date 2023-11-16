---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 설정과 커스터마이징하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 라이브러리로, 로딩 스피너와 애니메이션 효과를 구현할 때 유용하게 사용됩니다. 이 블로그 포스트에서는 NVActivityIndicatorView를 사용하여 애니메이션을 설정하고 커스터마이징하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 설치해야 합니다. Cocoapods를 사용하는 경우, Podfile에 다음 줄을 추가하고 `pod install` 명령어를 실행하세요.

```swift
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해, `import NVActivityIndicatorView` 구문을 추가하세요.

```swift
import NVActivityIndicatorView
```

다음으로, NVActivityIndicatorView를 생성하고 애니메이션을 추가하려는 뷰에 추가해야 합니다. 일반적인 사용 사례는 다음과 같습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballSpinFadeLoader, color: .black)
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위의 예제에서는 `ballSpinFadeLoader` 유형의 애니메이션 효과를 가지는 로딩 스피너를 생성하고, 해당 뷰에 추가한 뒤 애니메이션을 시작합니다.

## NVActivityIndicatorView 커스터마이징하기

NVActivityIndicatorView를 사용하여 애니메이션을 커스터마이징하는 방법에 대해 알아보겠습니다.

### 애니메이션 유형 변경하기

`type` 매개변수를 사용하여 애니메이션 유형을 변경할 수 있습니다. NVActivityIndicatorType 열거형을 사용하여 다양한 유형의 애니메이션을 선택할 수 있습니다. 예를 들어, `.circleStrokeSpin`이나 `.lineScalePulseOut`와 같은 다른 유형을 선택할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .circleStrokeSpin, color: .black)
```

### 색상 변경하기

`color` 매개변수를 사용하여 로딩 스피너의 색상을 변경할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballClipRotateMultiple, color: .red)
```

### 크기 변경하기

`frame` 매개변수를 사용하여 로딩 스피너의 크기를 변경할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 80, height: 80), type: .lineScalePulseOut, color: .black)
```

## 결론

이번 블로그 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션을 설정하고 커스터마이징하는 방법을 알아보았습니다. NVActivityIndicatorView를 사용하면 로딩 스피너와 애니메이션 효과를 쉽게 구현할 수 있습니다. 추가적인 기능과 옵션에 대해서는 [NVActivityIndicatorView의 공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.