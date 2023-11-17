---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용한 여행 일정 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

여행 앱을 개발할 때, 일정을 불러오는 동안 로딩 화면을 보여주는 것은 사용자 경험을 향상시키는 중요한 요소입니다. 이번 블로그 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 로딩 화면을 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란

NVActivityIndicatorView는 iOS 앱에서 사용자에게 로딩 상태를 시각적으로 보여주는 라이브러리입니다. 다양한 스타일의 로딩 애니메이션을 제공하며, 사용이 간편하고 커스터마이징이 가능합니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView는 Cocoapods를 통해 설치할 수 있습니다. 프로젝트의 Podfile에 다음과 같이 추가해주세요:

```
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치해주세요.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import 합니다:

```swift
import NVActivityIndicatorView
```

2. 로딩 인디케이터를 추가할 UIView를 생성합니다:

```swift
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballSpinFadeLoader, color: .white, padding: nil)
```

위 코드에서 `type`은 로딩 애니메이션의 스타일을 지정하고, `color`는 로딩 애니메이션의 색상을 지정합니다. `padding`은 로딩 애니메이션과 UIView의 간격을 의미합니다. 필요에 따라 값을 조정해주세요.

3. 로딩 인디케이터를 UIView에 추가합니다:

```swift
view.addSubview(loadingView)
```

4. 로딩 인디케이터의 위치를 설정합니다:

```swift
loadingView.center = view.center
```

5. 로딩 인디케이터를 시작하고 멈추는 함수를 정의합니다:

```swift
func startLoading() {
    loadingView.startAnimating()
}

func stopLoading() {
    loadingView.stopAnimating()
}
```

6. 로딩 인디케이터를 사용하여 여행 일정을 불러오는 동안 로딩 화면을 보여줍니다:

```swift
startLoading()

// 로딩 작업 수행

stopLoading()
```

위 코드에서 `startLoading` 함수를 호출하여 로딩 인디케이터를 시작하고, 원하는 로딩 작업을 수행한 뒤 `stopLoading` 함수를 호출하여 로딩 인디케이터를 멈춥니다.

## 마무리

이번 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 여행 일정 로딩 화면을 구현하는 방법을 살펴보았습니다. NVActivityIndicatorView는 사용이 간편하고 다양한 스타일의 로딩 애니메이션을 제공하여 앱의 사용자 경험을 향상시킬 수 있습니다.