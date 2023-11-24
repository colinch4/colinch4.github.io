---
layout: post
title: "[swift] NVActivityIndicatorView의 사용 예시와 코드 샘플"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

[![NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView/raw/master/Demo.gif)](https://github.com/ninjaprox/NVActivityIndicatorView)

NVActivityIndicatorView는 Swift로 작성된 활동 표시기 라이브러리입니다. 이 라이브러리를 사용하면 로딩 중인 동안 사용자에게 시각적인 피드백을 제공할 수 있습니다.

## 설치

NVActivityIndicatorView는 CocoaPods를 사용하여 설치할 수 있습니다. 프로젝트의 Podfile에 다음 줄을 추가하고 `pod install` 명령을 실행하십시오.

```ruby
pod 'NVActivityIndicatorView'
```

## 사용법

1. 먼저, NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. 활동 표시기를 추가할 뷰를 생성합니다.

```swift
let view = UIView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))
```

3. NVActivityIndicatorView 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: nil)
```

4. 생성된 활동 표시기를 뷰에 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
```

5. 원하는 위치에서 활동 표시기를 시작하고 중지할 수 있습니다. 예를 들어, 화면 로딩 중에는 활동 표시기가 시작되고, 로딩이 끝난 후에는 중지될 수 있습니다.

```swift
// 활동 표시기 시작
activityIndicatorView.startAnimating()

// 활동 표시기 중지
activityIndicatorView.stopAnimating()
```

NVActivityIndicatorView는 여러 가지 유형의 활동 표시기를 제공하며, 콘텐츠의 적절한 색상과 패딩을 지정할 수 있습니다. 이러한 설정을 통해 원하는 디자인과 일관성을 유지할 수 있습니다.

더 많은 사용법과 설정 옵션에 대해서는 [NVActivityIndicatorView 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.

## 결론

NVActivityIndicatorView는 사용자에게 로딩 중임을 시각적으로 알려주는 데 아주 유용한 라이브러리입니다. 이번 포스트에서는 NVActivityIndicatorView의 간단한 사용 예시와 코드 샘플을 살펴보았습니다. 이제 여러분은 활동 표시기를 효과적으로 활용하여 사용자 경험을 개선할 수 있게 되었습니다.