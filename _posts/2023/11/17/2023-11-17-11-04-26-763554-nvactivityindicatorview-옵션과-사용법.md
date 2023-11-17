---
layout: post
title: "[swift] NVActivityIndicatorView 옵션과 사용법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

![](https://github.com/ninjaprox/NVActivityIndicatorView/raw/master/Demo.gif)

NVActivityIndicatorView는 Swift에서 사용할 수 있는 매우 유용한 로딩 인디케이터 라이브러리입니다. 이 라이브러리는 로딩 중임을 시각적으로 표시해주는 다양한 스타일의 인디케이터를 제공합니다. 이번 글에서는 NVActivityIndicatorView의 옵션과 사용법에 대해 알아보도록 하겠습니다.

### 설치

NVActivityIndicatorView를 사용하기 위해 먼저 CocoaPods를 통해 라이브러리를 설치해야 합니다. `Podfile`에 다음과 같이 라이브러리를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 라이브러리를 설치합니다.

```shell
pod install
```

### 사용법

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 생성하고, 원하는 스타일을 선택하고, 원하는 위치에 추가합니다. 예를 들어, 인디케이터를 가운데에 추가하고 원의 스타일을 사용하려면 다음과 같이 코드를 작성합니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .circleStrokeSpin, color: .gray, padding: nil)
indicatorView.center = view.center
view.addSubview(indicatorView)
```

3. 인디케이터를 시작하거나 정지할 수 있습니다. 시작하는 경우에는 `startAnimating()` 메서드를 호출하고, 정지하는 경우에는 `stopAnimating()` 메서드를 호출합니다.

```swift
indicatorView.startAnimating()
```

```swift
indicatorView.stopAnimating()
```

### 옵션

NVActivityIndicatorView는 다양한 옵션을 제공하여 사용자의 필요에 맞게 커스터마이징할 수 있습니다. 다음은 일부 주요 옵션에 대한 설명입니다.

- `type`: 인디케이터의 스타일을 지정합니다. `NVActivityIndicatorType` 열거형에서 원하는 스타일을 선택할 수 있습니다. 예를 들어, `.circleStrokeSpin`, `.ballSpinFade`, `.cubeTransition`, 등 다양한 스타일이 제공됩니다.

- `color`: 인디케이터의 색상을 지정합니다. `.gray`, `.red`, `.green`, 등 원하는 색상을 사용할 수 있습니다.

- `padding`: 인디케이터의 내부 여백을 지정합니다. 원하는 만큼의 여백을 설정할 수 있습니다.

### 참고 자료

- NVActivityIndicatorView GitHub 레포지토리: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)

이를 통해 NVActivityIndicatorView의 옵션과 사용법에 대해 알아보았습니다. 이제 적절한 스타일과 옵션을 선택하여 앱의 로딩 인디케이터를 쉽게 구현할 수 있습니다.