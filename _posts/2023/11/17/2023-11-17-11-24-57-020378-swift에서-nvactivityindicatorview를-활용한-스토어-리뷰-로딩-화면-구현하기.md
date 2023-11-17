---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 활용한 스토어 리뷰 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱의 사용자들에게 프로세스가 계속 진행 중인지 알려주기 위해 로딩화면은 중요합니다. 이번에는 Swift 언어를 사용하여 NVActivityIndicatorView를 활용하여 스토어 리뷰 로딩 화면을 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 앱에서 사용자에게 로딩상태를 알려주기 위해 사용되는 오픈 소스 라이브러리입니다. 다양한 스타일과 색상으로 구성된 로딩 화면을 생성할 수 있으며, 마음에 드는 스타일을 선택하여 앱에 적용할 수 있습니다.

## NVActivityIndicatorView 설치하기
NVActivityIndicatorView는 CocoaPods을 통해 간편하게 설치할 수 있습니다. 프로젝트의 Podfile에 다음의 코드를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고, 터미널에서 해당 프로젝트 경로로 이동하여 아래의 명령어를 실행합니다.

```
pod install
```

설치가 완료된 후, `.xcworkspace` 파일을 열어서 프로젝트를 진행합니다.

## NVActivityIndicatorView 사용하기
1. 먼저, NVActivityIndicatorView를 사용하기 위해 해당 뷰 컨트롤러에 아래의 import 구문을 추가합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 화면을 표시할 뷰를 생성합니다. 일반적으로 전체 화면을 덮는 뷰를 사용합니다.

```swift
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: view.bounds.width, height: view.bounds.height), type: .ballScaleRippleMultiple, color: .blue, padding: nil)
```

3. 생성한 뷰를 해당 뷰 컨트롤러의 view에 추가합니다.

```swift
view.addSubview(loadingView)
```

4. 로딩 화면을 시작하고 중지하는 액션에 따라 아래의 코드를 추가합니다.

```swift
// 로딩 화면 시작
loadingView.startAnimating()

// 로딩 화면 중지
loadingView.stopAnimating()
```

## NVActivityIndicatorView 스타일 및 옵션 변경하기
NVActivityIndicatorView는 다양한 스타일과 옵션을 제공하여 로딩 화면을 자신의 취향에 맞게 변경할 수 있습니다.

예를 들어, 로딩 화면의 스타일을 변경하고 싶다면 `type` 속성을 다른 값으로 설정하면 됩니다. 다음은 일부 가능한 스타일의 예시입니다.

- .ballPulse
- .lineScale
- .circleStrokeSpin
- .triangleSkewSpin
- .pacman

로딩 화면의 색상을 변경하고 싶다면 `color` 속성을 다른 값으로 설정하면 됩니다. 예를 들어 `.red`, `.green`, `.yellow` 등을 사용할 수 있습니다.

자세한 스타일과 옵션의 변경은 [NVActivityIndicatorView GitHub 리포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.

## 마무리
이제 Swift에서 NVActivityIndicatorView를 활용하여 스토어 리뷰 로딩 화면을 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하면 앱에 로딩 화면을 쉽게 추가할 수 있으며, 다양한 스타일과 옵션을 사용하여 자유롭게 커스터마이징할 수 있습니다. 이를 통해 사용자의 경험을 향상시킬 수 있습니다.

참고: [NVActivityIndicatorView GitHub 리포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)