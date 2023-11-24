---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 로딩 화면 디자인하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

애플리케이션에서 데이터를 가져오거나 작업을 수행하는 동안 로딩 화면을 보여주는 것은 사용자 경험 측면에서 중요합니다. 

이번에는 Swift에서 NVActivityIndicatorView를 사용하여 로딩 화면을 디자인하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 많은 다양한 로딩 애니메이션을 제공하는 오픈 소스 라이브러리입니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하려면 먼저 CocoaPods를 사용하여 프로젝트에 라이브러리를 설치해야 합니다. 

```swift
// Podfile
platform :ios, '12.0'

target 'YourApp' do
  use_frameworks!

  pod 'NVActivityIndicatorView'
end
```

위의 코드를 Podfile에 추가한 후 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView 라이브러리를 불러옵니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 화면을 보여주기 위해 UIView에 NVActivityIndicatorView 객체를 추가합니다. 

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
activityIndicatorView.center = self.view.center
self.view.addSubview(activityIndicatorView)
```

3. 로딩 화면을 시작하고 멈추는 메서드를 정의합니다.

```swift
func startLoading() {
    activityIndicatorView.startAnimating()
    self.view.isUserInteractionEnabled = false
}

func stopLoading() {
    activityIndicatorView.stopAnimating()
    self.view.isUserInteractionEnabled = true
}
```

로딩이 필요한 작업을 수행하기 전 `startLoading()` 메서드를 호출하여 로딩 화면을 보여주고, 작업이 완료되면 `stopLoading()` 메서드를 호출하여 로딩 화면을 숨깁니다.

## NVActivityIndicatorView 설정하기

NVActivityIndicatorView는 다양한 스타일의 로딩 애니메이션을 제공합니다. 

```swift
activityIndicatorView.type = .ballSpinFadeLoader
activityIndicatorView.color = .blue
activityIndicatorView.padding = 20
```

위의 코드에서는 로딩 애니메이션의 타입을 `ballSpinFadeLoader`로 설정하고, 색상을 파란색으로, 패딩을 20으로 설정하였습니다. 요구 사항에 맞게 스타일과 설정을 조정할 수 있습니다.

## 참고 자료

- NVActivityIndicatorView Github 저장소: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)

이제 Swift에서 NVActivityIndicatorView를 사용하여 로딩 화면을 디자인하는 방법을 알게 되었습니다. 이제 애플리케이션에 로딩 화면을 추가하여 사용자에게 즉각적인 피드백을 제공해보세요.