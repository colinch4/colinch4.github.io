---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 크기와 외관 조절 방법 소개"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

![](https://raw.githubusercontent.com/ninjaprox/NVActivityIndicatorView/master/Screenshots/sample.gif)

이번에는 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션의 크기와 외관을 조절하는 방법을 알아보겠습니다. NVActivityIndicatorView는 다양한 종류의 로딩 애니메이션을 제공하는 오픈 소스 라이브러리로, 시간이 지연되는 작업 또는 작업이 진행 중임을 사용자에게 알리는데 사용할 수 있습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView는 CocoaPods를 사용하여 쉽게 설치할 수 있습니다. Podfile에 다음과 같은 코드를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 애니메이션 크기 조절

NVActivityIndicatorView는 다양한 크기의 애니메이션을 제공합니다. 디폴트로 설정된 크기는 `default`로, 총 7가지의 크기를 선택할 수 있습니다.

다음은 `default` 크기로 애니메이션을 설정하는 코드입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .default)
```

이외에도 `.small`, `.medium`, `.large`, `.xLarge`, `.xxLarge`, `.custom` 등의 크기를 선택할 수 있습니다. `.custom`을 선택한 경우에는 `size` 파라미터를 사용하여 원하는 크기로 설정할 수 있습니다.

## 애니메이션 외관 조절

NVActivityIndicatorView는 다양한 외관을 조절하는 옵션을 제공합니다.

1. `color`: 애니메이션의 색상을 변경할 수 있습니다. UIColor 객체를 사용하여 변경할 수 있습니다.

```swift
activityIndicatorView.color = .red
```

2. `padding`: 애니메이션의 내부 여백을 설정할 수 있습니다. 기본값은 0입니다.

```swift
activityIndicatorView.padding = 20
```

3. `type`: 애니메이션의 모양을 변경할 수 있습니다. 다양한 종류의 모양을 사용할 수 있습니다.

```swift
activityIndicatorView.type = .ballClipRotatePulse
```

4. `backgroundColor`: 애니메이션의 배경색을 변경할 수 있습니다.

```swift
activityIndicatorView.backgroundColor = .lightGray
```

NVActivityIndicatorView의 다양한 옵션을 조합하여 애니메이션의 크기와 외관을 원하는대로 설정할 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView Documentation](https://github.com/ninjaprox/NVActivityIndicatorView#usage)

위의 참고 자료를 통해 더 자세한 정보를 얻을 수 있습니다.