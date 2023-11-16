---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 외관 및 색상 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift로 작성된 활발한 애니메이션 인디케이터 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하며, 애플리케이션에서 작업이 진행 중임을 시각적으로 보여줄 수 있습니다.

이번 튜토리얼에서는 NVActivityIndicatorView를 사용하여 애니메이션 외관 및 색상을 설정하는 방법을 알아보겠습니다.

## NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 프로젝트에 추가해야 합니다. CocoaPods을 사용해 프로젝트에 NVActivityIndicatorView를 설치할 수 있습니다. Podfile에 다음 코드를 추가하고, 터미널에서 `pod install` 명령을 실행합니다.

```ruby
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하려면 먼저 뷰 컨트롤러에서 필요한 import 문을 추가해야 합니다.

```swift
import NVActivityIndicatorView
```

다음으로, NVActivityIndicatorView를 생성하고 뷰에 추가해야 합니다. 이때, NVActivityIndicatorView의 매개변수로 스타일과 색상을 지정할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: nil)
self.view.addSubview(activityIndicatorView)
```

위의 코드에서 `type` 매개변수를 통해 원하는 애니메이션 스타일을 선택할 수 있습니다. 또한, `color` 매개변수를 사용하여 원하는 색상을 선택할 수 있습니다.

애니메이션을 시작하려면 `startAnimating()` 메서드를 호출하고, 애니메이션을 정지하려면 `stopAnimating()` 메서드를 호출합니다.

```swift
activityIndicatorView.startAnimating()

// 애니메이션을 멈추려면
activityIndicatorView.stopAnimating()
```

## 외관 설정하기

NVActivityIndicatorView는 다양한 외관 설정 옵션을 제공합니다. 다음은 주로 사용되는 몇 가지 외관 설정 방법입니다.

### 애니메이션 크기 조정하기

`NVActivityIndicatorView`의 크기는 `frame` 속성을 통해 조정할 수 있습니다.

```swift
activityIndicatorView.frame = CGRect(x: 0, y: 0, width: 100, height: 100)
```

### 배경색 설정하기

NVActivityIndicatorView의 배경색은 `backgroundColor` 속성을 사용하여 지정할 수 있습니다.

```swift
activityIndicatorView.backgroundColor = .white
```

### 선 두께 설정하기

애니메이션에 사용되는 선의 두께는 `lineWidth` 속성을 통해 조정할 수 있습니다.

```swift
activityIndicatorView.lineWidth = 3
```

### 패딩 설정하기

NVActivityIndicatorView의 패딩은 `padding` 속성을 사용하여 조정할 수 있습니다. 패딩은 인디케이터와 뷰 경계 간의 공간입니다. 기본적으로 패딩은 인디케이터 크기의 절반입니다.

```swift
activityIndicatorView.padding = 10
```

## 결론

이번 튜토리얼에서는 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션 외관 및 색상을 설정하는 방법을 알아보았습니다. NVActivityIndicatorView의 다양한 설정 옵션을 사용하여 원하는 디자인의 로딩 인디케이터를 만들 수 있습니다. 더 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.