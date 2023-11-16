---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 색상 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS에서 사용되는 활동 중 표시기를 만들기 위한 오픈 소스 라이브러리입니다. 이 라이브러리를 사용하면 쉽게 다양한 형태의 로딩 인디케이터를 만들 수 있습니다. 이번에는 Swift에서 NVActivityIndicatorView 애니메이션의 색상을 설정하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 위해 먼저 CocoaPods를 이용하여 프로젝트에 라이브러리를 추가해야 합니다. Podfile에 다음과 같이 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```
그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 2. NVActivityIndicatorView 생성 및 색상 설정

다음은 NVActivityIndicatorView를 생성하고 색상을 설정하는 예제 코드입니다:

```swift
import NVActivityIndicatorView

let frame = CGRect(x: 0, y: 0, width: 100, height: 100)
let activityIndicatorView = NVActivityIndicatorView(frame: frame)

// 애니메이션 색상 설정
activityIndicatorView.color = .red

// 애니메이션 시작
activityIndicatorView.startAnimating()
```

위 코드에서는 적절한 크기의 NVActivityIndicatorView를 생성하고, 원하는 색상을 설정한 후 애니메이션을 시작합니다. `.color` 속성을 사용하여 색상을 설정할 수 있으며, UIColor나 NSColor 값을 할당하면 됩니다.

## 3. 색상 옵션과 스타일

NVActivityIndicatorView는 다양한 스타일과 색상 옵션을 제공합니다. 예를 들어 원하는 스타일로 NVActivityIndicatorView를 생성하고 색상을 설정할 수 있습니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(
    frame: frame,
    type: .ballTrianglePath,
    color: .blue,
    padding: 20.0
)
```

`type` 매개 변수를 사용하여 원하는 스타일을 선택하고, `color` 매개 변수를 사용하여 색상을 설정할 수 있습니다.

## 마치며

이번 글에서는 Swift에서 NVActivityIndicatorView 애니메이션의 색상을 설정하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 활동 중 표시기를 쉽게 만들 수 있는 강력한 라이브러리이므로, 앱 개발에 유용하게 활용할 수 있습니다.

[참고 링크](https://github.com/ninjaprox/NVActivityIndicatorView)