---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 활용하기 - 커플 다이어리 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

커플 다이어리 앱을 개발하고 있는데, 로딩 화면에 좀 더 멋진 효과를 주고 싶다면 [NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)를 사용해보세요. 이 라이브러리는 로딩 인디케이터를 구현하는데 도움이 되는 오픈소스 라이브러리입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 중임을 나타내는 인디케이터를 구현하는 데 사용되는 라이브러리입니다. 다양한 스타일과 커스터마이징 옵션을 제공하여 앱의 디자인에 적합한 로딩 화면을 만들 수 있습니다.

## 설치하기

CocoaPods를 사용한다면, Podfile에 다음과 같이 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

그런 다음 터미널에서 `pod install`을 실행합니다.

## 사용하기

1. 뷰 컨트롤러에서 NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 뷰 컨트롤러에 추가합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballRotateChase, color: .white, padding: 0)
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
```

3. 로딩 화면 표시하기

```swift
activityIndicatorView.startAnimating()
```

4. 로딩 화면 종료하기

```swift
activityIndicatorView.stopAnimating()
```

## 커스터마이징하기

NVActivityIndicatorView는 다양한 스타일과 커스터마이징 옵션을 제공합니다. 자세한 내용은 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.

## 결론

NVActivityIndicatorView를 사용하면 커플 다이어리 앱에 멋진 로딩 화면을 구현할 수 있습니다. 이 라이브러리는 다양한 스타일과 커스터마이징 옵션을 제공하여 앱의 디자인에 완벽하게 맞출 수 있습니다.