---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 스플래시 화면 구현 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

스플래시 화면은 앱이 로드되는 동안 사용자에게 보여지는 첫 번째 화면입니다. 이 화면은 앱 시작 로딩 과정을 표시하기 위해 일반적으로 사용됩니다. NVActivityIndicatorView는 Swift에서 스플래시 화면을 구현하는 데 도움이 되는 라이브러리입니다. 이 블로그 포스트에서는 NVActivityIndicatorView를 사용하여 스플래시 화면을 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 애니메이션 로딩 표시기를 생성하는 라이브러리입니다. 아래는 NVActivityIndicatorView의 핵심 기능입니다.

- 다양한 스타일과 색상의 로딩 표시기 제공
- 간단한 구현을 통해 로딩 표시기를 생성하고 제어
- Swift와 Objective-C에서 사용 가능

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 CocoaPods나 Carthage를 통해 라이브러리를 설치해야 합니다. 여기서는 CocoaPods를 사용하는 방법에 대해 설명하겠습니다.

1. `Podfile`을 열고 다음 라인을 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

2. 터미널에서 프로젝트 폴더로 이동한 후, 다음 명령어를 실행하여 CocoaPods를 업데이트합니다.

```bash
pod install
```

3. 이제 `.xcworkspace` 파일을 열어서 프로젝트를 진행할 수 있습니다.

## NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 사용할 ViewController 파일에 다음 코드를 추가합니다.

```swift
import NVActivityIndicatorView
```

2. 스플래시 화면을 구현할 뷰 컨트롤러의 `viewDidLoad()` 메서드에서 다음 코드를 추가합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballScaleRippleMultiple, color: .white)
activityIndicatorView.center = view.center
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

위 코드에서는 activityIndicatorView를 생성하고, 위치와 스타일, 색상을 설정한 후, 스플래시 화면의 중앙에 추가하고 애니메이션을 시작하도록 구현하였습니다.

3. 스플래시 화면이 일정 시간 동안 보여지도록 설정하려면 알맞은 시점에 `activityIndicatorView.stopAnimating()` 코드를 추가하여 애니메이션을 중지시키면 됩니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)

위에서 설명한 방법을 참고하여 NVActivityIndicatorView를 활용하여 스플래시 화면을 구현할 수 있습니다. NVActivityIndicatorView는 다양한 스타일과 색상의 로딩 표시기를 제공하며, 간단한 코드로 구현할 수 있습니다. 프로젝트에 적용해보고 사용자에게 더 나은 첫인상을 줄 수 있는 스플래시 화면을 구현해보세요.