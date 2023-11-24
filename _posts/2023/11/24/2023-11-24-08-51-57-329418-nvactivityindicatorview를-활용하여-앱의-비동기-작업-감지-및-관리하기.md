---
layout: post
title: "[swift] NVActivityIndicatorView를 활용하여 앱의 비동기 작업 감지 및 관리하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱 개발에서 비동기 작업은 자주 사용되는 요소입니다. 사용자 경험을 향상시키기 위해 작업이 진행 중임을 표시하는 것은 중요합니다. 이 때 NVActivityIndicatorView를 활용하면 사용자에게 진행 중임을 시각적으로 알려줄 수 있습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 오픈 소스 라이브러리로, iOS 앱에서 활용할 수 있습니다. 이 라이브러리를 사용하면 로딩 인디케이터를 쉽게 구현할 수 있습니다. 다양한 스타일과 색상을 제공하며, 사용자 지정도 가능합니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView는 CocoaPods를 사용하여 설치할 수 있습니다. Podfile에 다음과 같이 추가한 후 `pod install` 명령을 실행합니다.

```swift
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. 인디케이터를 생성하고, 표시할 super view를 지정합니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .systemBlue, padding: nil)
let superView = self.view // 표시할 super view
```

3. 생성한 인디케이터를 super view에 추가합니다.

```swift
superView.addSubview(indicatorView)
```

4. 인디케이터를 표시하고 숨깁니다.

```swift
indicatorView.startAnimating()
indicatorView.stopAnimating()
```

## NVActivityIndicatorView 사용 예시

비동기 작업 중에 인디케이터를 표시하는 예시를 살펴보겠습니다.

```swift
func fetchData() {
    showLoader() // 인디케이터 표시
    
    DispatchQueue.global().async {
        // 비동기 작업 수행
        
        DispatchQueue.main.async {
            hideLoader() // 인디케이터 숨김
        }
    }
}

func showLoader() {
    indicatorView.startAnimating()
}

func hideLoader() {
    indicatorView.stopAnimating()
}
```

이렇게 NVActivityIndicatorView를 활용하여 앱의 비동기 작업을 감지하고 관리할 수 있습니다.

더 자세한 정보는 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.