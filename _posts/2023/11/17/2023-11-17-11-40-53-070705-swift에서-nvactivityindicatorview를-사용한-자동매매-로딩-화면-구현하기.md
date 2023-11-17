---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용한 자동매매 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번에는 Swift에서 NVActivityIndicatorView를 사용하여 자동매매 앱의 로딩 화면을 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 로딩 인디케이터 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하며, 다양한 크기와 색상으로 커스터마이징할 수 있습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 통해 라이브러리를 설치해야 합니다. 

Podfile에 다음과 같이 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 아래 명령어를 실행하여 Cocoapods를 설치합니다:

```
$ pod install
```

## NVActivityIndicatorView 사용하기

1. 먼저, 필요한 View Controller에 NVActivityIndicatorView를 추가합니다. 다음과 같은 코드를 viewDidLoad() 메소드에 추가합니다:

```swift
let activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: 0)
activityIndicator.center = self.view.center
activityIndicator.startAnimating()
self.view.addSubview(activityIndicator)
```

위 코드에서는 activityIndicator라는 변수를 생성하여 NVActivityIndicatorView를 초기화하고, view의 중앙에 위치시킵니다. 그리고 애니메이션을 시작하고, view에 추가합니다.

2. 로딩이 끝나면 NVActivityIndicatorView를 제거해야 합니다. 다음 코드를 사용하여 removeActivityIndicator() 메소드를 추가합니다:

```swift
func removeActivityIndicator() {
    if let activityIndicator = self.view.subviews.filter({ $0 is NVActivityIndicatorView }).first as? NVActivityIndicatorView {
        activityIndicator.stopAnimating()
        activityIndicator.removeFromSuperview()
    }
}
```

위 코드에서는 현재 view의 subviews에서 NVActivityIndicatorView를 찾아 애니메이션을 멈추고 제거합니다.

3. 로딩 화면을 사용할 때에는 다음과 같이 showActivityIndicator()와 hideActivityIndicator() 메소드를 호출하여 화면에 로딩 인디케이터를 추가 및 제거합니다:

```swift
func showActivityIndicator() {
    let activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: 0)
    activityIndicator.center = self.view.center
    activityIndicator.startAnimating()

    self.view.addSubview(activityIndicator)
}

func hideActivityIndicator() {
    if let activityIndicator = self.view.subviews.filter({ $0 is NVActivityIndicatorView }).first as? NVActivityIndicatorView {
        activityIndicator.stopAnimating()
        activityIndicator.removeFromSuperview()
    }
}
```

위 코드에서 showActivityIndicator() 메소드는 로딩 인디케이터를 추가하여 화면에 표시하고, hideActivityIndicator() 메소드는 로딩 인디케이터를 제거합니다.

## 마무리

이제 Swift에서 NVActivityIndicatorView를 사용하여 자동매매 앱의 로딩 화면을 구현할 수 있는 방법에 대해 알아보았습니다. 이 라이브러리를 활용하여 사용자에게 보다 나은 사용자 경험을 제공하는 앱을 개발할 수 있습니다.

더 많은 NVActivityIndicatorView의 사용법은 [공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고해주세요.