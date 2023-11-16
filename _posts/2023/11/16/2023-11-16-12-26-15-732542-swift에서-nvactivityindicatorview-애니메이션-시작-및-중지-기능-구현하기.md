---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 시작 및 중지 기능 구현하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱에 로딩 화면을 추가하거나 백그라운드 작업을 수행하는 동안 사용자에게 진행 상황을 알려주는 애니메이션을 사용하는 경우가 많습니다. NVActivityIndicatorView는 Swift에서 사용할 수 있는 강력한 오픈소스 라이브러리로, 다양한 스타일의 애니메이션을 제공합니다. 이번 블로그에서는 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션을 시작하고 중지하는 방법을 알아보겠습니다.

## NVActivityIndicatorView 설치하기

먼저, [CocoaPods](https://cocoapods.org/)를 사용하여 NVActivityIndicatorView를 프로젝트에 설치해야 합니다. Podfile에 다음 라인을 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 종속성을 설치합니다.

```bash
pod install
```

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 사용할 뷰에 추가합니다. 일반적으로 로딩이 필요한 뷰컨트롤러의 전체 뷰에 추가하는 것이 좋습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballScale, color: .gray, padding: nil)
view.addSubview(activityIndicatorView)
```

3. 애니메이션을 시작하고 중지하는 함수를 추가합니다.

```swift
func startAnimating() {
    activityIndicatorView.startAnimating()
}

func stopAnimating() {
    activityIndicatorView.stopAnimating()
}
```

4. 원하는 시점에서 애니메이션을 시작하거나 중지할 수 있습니다.

```swift
startAnimating() // 애니메이션 시작하기
stopAnimating() // 애니메이션 중지하기
```

NVActivityIndicatorView의 초기 설정값들(type, color, padding 등)은 사용자 정의 가능하며, 필요에 따라 조정할 수 있습니다. 자세한 내용은 [NVActivityIndicatorView 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.

이제, Swift에서 NVActivityIndicatorView를 사용하여 애니메이션을 시작하고 중지하는 기능을 구현하는 방법에 대해 알게 되었습니다. NVActivityIndicatorView를 사용하면 앱의 사용자 경험을 향상시키고 프로세스의 진행 상황을 시각적으로 나타낼 수 있습니다.