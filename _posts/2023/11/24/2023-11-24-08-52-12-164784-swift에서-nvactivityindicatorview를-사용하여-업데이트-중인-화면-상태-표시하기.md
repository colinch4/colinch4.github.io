---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 업데이트 중인 화면 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번 블로그 포스트에서는 Swift 언어를 사용하여 화면 업데이트 중에 로딩 상태를 표시하는 방법을 알려드리겠습니다. 이를 위해 NVActivityIndicatorView라는 라이브러리를 사용할 것입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 상태를 표시하는 데 사용할 수 있는 간단한 애니메이션 뷰입니다. 기본 설정이 가능하며 다양한 타입과 스타일을 제공합니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 Cocoapods를 통해 해당 라이브러리를 프로젝트에 추가해야 합니다. Podfile에 아래 내용을 추가하고, `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

```swift
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용 방법

1. NVActivityIndicatorView를 사용할 뷰 컨트롤러에 import 문을 추가합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 추가하고 싶은 뷰에 대한 IBOutlet을 만들어 줍니다.

```swift
@IBOutlet weak var loadingIndicatorView: NVActivityIndicatorView!
```

3. viewDidLoad() 메서드에서 로딩 인디케이터를 초기화하고 뷰에 추가합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    // 로딩 인디케이터 초기화
    let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
    let activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballSpinFadeLoader, color: .blue, padding: nil)
    
    // 뷰에 추가
    view.addSubview(activityIndicatorView)
    
    // 로딩 인디케이터를 가운데 위치시킴
    activityIndicatorView.center = view.center
}
```

4. 원하는 곳에서 로딩 상태를 시작하거나 중지할 수 있습니다.

```swift
// 로딩 시작
loadingIndicatorView.startAnimating()

// 로딩 중지
loadingIndicatorView.stopAnimating()
```

## 추가 설정 및 사용자 정의

NVActivityIndicatorView는 기본 설정 이외에도 다양한 설정을 제공합니다. 아래는 몇 가지 예시입니다.

- 현재의 로딩 상태 등급을 설정합니다.

```swift
loadingIndicatorView.startAnimating(message: "로딩 중...")
```

- 로딩 인디케이터의 크기를 조절합니다.

```swift
loadingIndicatorView.sizeToFit()
```

위에서 소개한 방법 외에도 더 자세한 내용과 추가 기능을 확인하려면 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.

이렇게 NVActivityIndicatorView를 사용하여 Swift에서 화면 업데이트 중에 로딩 상태를 표시할 수 있습니다. 라이브러리의 다양한 타입과 스타일을 활용하여 앱의 사용자 경험을 향상시키는 것을 고려해보세요.