---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 원형로딩 인디케이터 만들기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱에서 데이터를 로딩하는 동안 사용자에게 로딩 중임을 시각적으로 표시하는 인디케이터는 매우 유용합니다. 이번 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 간단한 원형 로딩 인디케이터를 만드는 방법을 알아보겠습니다.

## NVActivityIndicatorView 소개

NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 다양한 스타일의 로딩 인디케이터를 제공하는 라이브러리입니다. 많은 스타일과 커스터마이징 옵션을 제공하여 앱의 디자인에 적합한 로딩 인디케이터를 만들 수 있습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 프로젝트에 설치해야 합니다. Podfile에 다음과 같은 라인을 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령을 실행하여 Pod을 설치합니다.

```shell
pod install
```

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해, 먼저 해당 클래스를 import 해줘야 합니다.

```swift
import NVActivityIndicatorView
```

인디케이터를 추가할 뷰에 NVActivityIndicatorView 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

인디케이터 스타일, 색상, 크기를 설정할 수 있습니다.

```swift
activityIndicatorView.type = .ballRotateChase
activityIndicatorView.color = .blue
activityIndicatorView.padding = 20
```

뷰에 인디케이터를 추가합니다.

```swift
view.addSubview(activityIndicatorView)
```

인디케이터를 중앙에 위치시키고, 애니메이션을 시작합니다.

```swift
activityIndicatorView.center = view.center
activityIndicatorView.startAnimating()
```

애니메이션을 중지하고, 인디케이터를 제거하려면 다음 코드를 사용합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

이상으로 NVActivityIndicatorView를 사용하여 원형 로딩 인디케이터를 만들고 제어하는 방법을 알아보았습니다. 더 많은 스타일과 옵션을 알아보려면 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조해주세요.