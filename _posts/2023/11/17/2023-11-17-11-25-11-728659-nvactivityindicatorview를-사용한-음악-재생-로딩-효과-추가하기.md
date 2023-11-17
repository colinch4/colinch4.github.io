---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 음악 재생 로딩 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번에는 Swift 언어를 사용하여 음악 재생 시 로딩 효과를 추가하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 iOS 애플리케이션에서 사용되는 로딩 인디케이터 라이브러리로, 다양한 모양과 스타일의 로딩 효과를 제공합니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. `Podfile`에 아래의 내용을 추가하고 터미널에서 `pod install` 명령어를 실행하세요.

```ruby
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. UIView 위에 로딩 효과를 추가할 준비를 합니다. 예를 들어, 뮤직 플레이어 화면의 별도의 뷰를 생성하여 사용할 수 있습니다.

```swift
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

3. 로딩 효과의 모양과 색상을 설정합니다.

```swift
loadingView.type = .ballSpinFadeLoader
loadingView.color = UIColor.red
```

4. 로딩 효과를 화면에 추가하고 애니메이션을 시작합니다.

```swift
loadingView.startAnimating()
```

5. 애니메이션을 멈추고 로딩 효과를 화면에서 제거할 때는 아래의 코드를 실행합니다.

```swift
loadingView.stopAnimating()
loadingView.removeFromSuperview()
```

이제 음악 재생 시 로딩 효과를 추가할 준비가 되었습니다. NVActivityIndicatorView의 다양한 모양과 스타일을 테스트해보며 원하는 로딩 효과를 선택할 수 있습니다.

자세한 내용은 [NVActivityIndicatorView 깃허브 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.