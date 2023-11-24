---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 경험 향상 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift 언어를 사용하여 사용자 경험(UX)을 향상시킬 수 있는 NVActivityIndicatorView에 대해 알아보겠습니다. 

NVActivityIndicatorView는 iOS 개발에서 로딩 인디케이터를 구현하는 데 유용한 오픈 소스 라이브러리입니다. 이를 통해 사용자에게 작업이 진행 중임을 시각적으로 알려주고, 원형, 선형, 도트 등 다양한 스타일의 인디케이터를 제공할 수 있습니다. 

## 1. NVActivityIndicatorView 설치하기

CocoaPods를 사용하여 NVActivityIndicatorView를 프로젝트에 추가할 수 있습니다. `Podfile`에 다음과 같이 추가하고, 터미널에서 `pod install` 명령어를 실행하세요.

```
pod 'NVActivityIndicatorView'
```

## 2. NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 import 해야 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

3. 원하는 스타일과 색상을 설정합니다.

```swift
activityIndicatorView.type = .ballSpinFadeLoader
activityIndicatorView.color = .red
```

4. 화면에 보이도록 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

5. 작업이 끝나면 인디케이터를 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 3. 활용 예시

NVActivityIndicatorView를 활용하여 로딩 중인 상태를 시각적으로 표시할 수 있습니다. 예를 들어, 비동기 작업을 수행하는 동안 인디케이터를 보이게하고 작업이 완료되면 숨기는 방식입니다.

```swift
func fetchData() {
    showLoader()
    
    // 비동기 작업 수행
    
    hideLoader()
}

func showLoader() {
    activityIndicatorView.center = view.center
    view.addSubview(activityIndicatorView)
    activityIndicatorView.startAnimating()
}

func hideLoader() {
    activityIndicatorView.stopAnimating()
    activityIndicatorView.removeFromSuperview()
}
```

이렇게 하면 사용자가 데이터를 기다리는 동안 로딩 인디케이터가 화면에 표시되어 UX를 향상시킬 수 있습니다.

## 4. 마무리

NVActivityIndicatorView는 간단하게 사용할 수 있는 로딩 인디케이터 라이브러리로, 사용자 경험을 향상시키는 데 큰 도움이 됩니다. 이번 글에서는 NVActivityIndicatorView의 설치와 사용 방법에 대해 알아보았습니다. 프로젝트에 적용하여 원하는 스타일의 로딩 인디케이터를 구현해보세요!