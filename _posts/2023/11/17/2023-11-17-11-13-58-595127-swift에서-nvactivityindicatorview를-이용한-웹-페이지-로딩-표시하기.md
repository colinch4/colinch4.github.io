---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 이용한 웹 페이지 로딩 표시하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

[Swift](https://swift.org/)는 Apple이 개발한 iOS 및 macOS 앱을 위한 프로그래밍 언어입니다. NVActivityIndicatorView는 Swift에서 사용할 수 있는 로딩 표시 도구입니다. 이번 블로그 포스트에서는 Swift에서 NVActivityIndicatorView를 이용하여 웹 페이지 로딩을 표시하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 및 macOS 앱에서 사용할 수 있는 로딩 표시 도구입니다. 다양한 로딩 애니메이션 스타일을 제공하며, 간편하게 사용할 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 설치하기 위해, 먼저 [CocoaPods](https://cocoapods.org/)를 이용하여 프로젝트에 NVActivityIndicatorView를 추가해야 합니다. Podfile에 다음과 같이 추가합니다:

```swift
pod 'NVActivityIndicatorView'
```

그리고 다음 명령어를 실행하여 CocoaPods를 업데이트합니다:

```shell
$ pod install
```

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 먼저 NVActivityIndicatorView를 import해야 합니다:

```swift
import NVActivityIndicatorView
```

웹 페이지 로딩 표시를 위해 다음과 같이 NVActivityIndicatorView를 초기화합니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .white, padding: nil)
```

위 코드에서 `frame`은 로딩 표시 도구의 크기와 위치를 지정합니다. `type`은 로딩 애니메이션의 스타일을 선택합니다. 여러 가지 스타일 중 하나를 선택할 수 있습니다. `color`는 로딩 표시 도구의 색상을 지정하고, `padding`은 로딩 표시 도구의 여백을 지정합니다.

로딩 표시를 시작하려면 다음과 같이 로딩 표시 도구를 추가하고 애니메이션을 시작합니다:

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

로딩 표시를 중지하려면 다음과 같이 애니메이션을 멈춥니다:

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 결론

이번 포스트에서는 Swift에서 NVActivityIndicatorView를 이용하여 웹 페이지 로딩 표시하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하면 사용자에게 웹 페이지 로딩 중임을 시각적으로 알리는 효과적인 방법을 구현할 수 있습니다.