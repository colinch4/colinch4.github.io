---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 소셜 미디어 공유 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

![NVActivityIndicatorView Logo](https://github.com/ninjaprox/NVActivityIndicatorView/raw/master/Resources/Images/logo.png)

이번 글에서는 NVActivityIndicatorView를 사용하여 소셜 미디어 공유 로딩 효과를 구현하는 방법을 알아보겠습니다. NVActivityIndicatorView는 iOS 앱에서 다양한 로딩 애니메이션을 쉽게 구현할 수 있도록 도와주는 오픈 소스 라이브러리입니다.

## 1. 라이브러리 설치

먼저, NVActivityIndicatorView를 설치해야 합니다. CocoaPods를 사용하여 라이브러리를 간편하게 설치할 수 있습니다. Podfile에 다음과 같이 추가합니다:

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## 2. NVActivityIndicatorView 추가

NVActivityIndicatorView를 사용하려는 ViewController에 import 구문을 추가합니다:

```swift
import NVActivityIndicatorView
```

NVActivityIndicatorView를 추가할 위치를 결정한 뒤, 다음 코드를 사용하여 로딩 애니메이션을 추가할 수 있습니다:

```swift
// 로딩 애니메이션 뷰 생성
let frame = CGRect(x: (view.bounds.width - 50) / 2, y: (view.bounds.height - 50) / 2, width: 50, height: 50)
let activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballSpinFadeLoader, color: .white, padding: nil)

// 로딩 애니메이션 뷰를 서브뷰로 추가
view.addSubview(activityIndicatorView)

// 애니메이션 시작
activityIndicatorView.startAnimating()

// 일정 시간 이후 애니메이션 종료
DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
    activityIndicatorView.stopAnimating()
    activityIndicatorView.removeFromSuperview()
}
```

위 코드에서는 로딩 애니메이션 뷰를 생성한 뒤, ViewController의 view에 서브뷰로 추가하고 애니메이션을 시작합니다. 일정 시간이 지난 뒤 애니메이션을 종료하고, 뷰에서 제거합니다.

## 3. 로딩 애니메이션 스타일 변경

NVActivityIndicatorView는 다양한 로딩 애니메이션 스타일을 제공합니다. 위 예제 코드에서 사용된 `.ballSpinFadeLoader` 대신 원하는 다른 스타일을 사용할 수 있습니다. 자세한 스타일 옵션은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하세요.

## 결론

이제 NVActivityIndicatorView를 사용하여 소셜 미디어 공유 로딩 효과를 구현하는 방법을 알아보았습니다. NVActivityIndicatorView는 간편한 설치와 사용법으로 다양한 로딩 애니메이션을 구현하는 데 도움이 됩니다. 참고 자료와 예제 코드를 통해 실제 앱에 적용해보세요.