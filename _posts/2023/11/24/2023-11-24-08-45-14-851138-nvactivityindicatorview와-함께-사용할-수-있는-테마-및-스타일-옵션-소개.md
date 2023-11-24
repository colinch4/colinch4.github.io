---
layout: post
title: "[swift] NVActivityIndicatorView와 함께 사용할 수 있는 테마 및 스타일 옵션 소개"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 활동 표시기 라이브러리입니다. 이 라이브러리는 사용자가 작업 진행 상태를 시각적으로 나타낼 때 유용하게 사용될 수 있습니다.

NVActivityIndicatorView 라이브러리에는 다양한 테마와 스타일 옵션이 제공되며, 이를 사용하여 활동 표시기의 외관을 원하는 대로 변경할 수 있습니다. 이번 글에서는 몇 가지 주요한 테마와 스타일 옵션을 알아보겠습니다.

## 테마 (Themes)

NVActivityIndicatorView는 다양한 테마를 제공합니다. 각 테마는 활동 표시기의 색상과 디자인을 나타냅니다. 다음은 몇 가지 테마의 예입니다:

### 1. .ballPulse

![ballPulse](https://raw.githubusercontent.com/ninjaprox/NVActivityIndicatorView/master/Images/ballPulse.gif)

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .red, padding: 0)
```

### 2. .lineScale

![lineScale](https://raw.githubusercontent.com/ninjaprox/NVActivityIndicatorView/master/Images/lineScale.gif)

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .lineScale, color: .blue, padding: 0)
```

### 3. .pacman

![pacman](https://raw.githubusercontent.com/ninjaprox/NVActivityIndicatorView/master/Images/pacman.gif)

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .pacman, color: .green, padding: 0)
```

## 스타일 (Styles)

NVActivityIndicatorView는 활동 표시기의 스타일도 변경할 수 있습니다. 다음은 몇 가지 스타일 옵션의 예입니다:

### 1. .default

![default](https://raw.githubusercontent.com/ninjaprox/NVActivityIndicatorView/master/Images/default.gif)

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .red, padding: 0)
activityIndicatorView.padding = 20
activityIndicatorView.backgroundColor = .black
activityIndicatorView.layer.cornerRadius = 5
activityIndicatorView.layer.masksToBounds = true
```

### 2. .circleStrokeSpin

![circleStrokeSpin](https://raw.githubusercontent.com/ninjaprox/NVActivityIndicatorView/master/Images/circleStrokeSpin.gif)

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .blue, padding: 0)
activityIndicatorView.padding = 10
activityIndicatorView.backgroundColor = .clear
activityIndicatorView.layer.borderWidth = 1
activityIndicatorView.layer.borderColor = UIColor.black.cgColor
```

### 3. .ballGridBeat

![ballGridBeat](https://raw.githubusercontent.com/ninjaprox/NVActivityIndicatorView/master/Images/ballGridBeat.gif)

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .green, padding: 0)
activityIndicatorView.padding = 5
activityIndicatorView.backgroundColor = .clear
activityIndicatorView.layer.borderWidth = 2
activityIndicatorView.layer.borderColor = UIColor.red.cgColor
activityIndicatorView.layer.cornerRadius = 25
activityIndicatorView.layer.masksToBounds = true
```

위의 예시 코드에서는 함께 제공되는 테마와 스타일 옵션들을 사용하여 NVActivityIndicatorView의 외관을 변경하는 방법을 보여줍니다. 이 밖에도 다양한 옵션들을 조합하여 원하는 디자인을 구현할 수 있습니다.

더 자세한 정보를 원한다면 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하세요.