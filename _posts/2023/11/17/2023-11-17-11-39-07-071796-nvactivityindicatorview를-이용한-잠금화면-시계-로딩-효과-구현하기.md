---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 잠금화면 시계 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 글에서는 NVActivityIndicatorView를 사용하여 잠금화면 시계의 로딩 효과를 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 로딩 인디케이터 라이브러리입니다. 다양한 스타일의 인디케이터를 제공하며, 간단한 코드 몇 줄로 로딩 효과를 쉽게 구현할 수 있습니다.

## NVActivityIndicatorView 설치하기

CocoaPods를 사용하여 NVActivityIndicatorView를 설치할 수 있습니다. `Podfile`에 다음과 같이 추가해주세요.

```
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 생성합니다. 로딩 인디케이터의 스타일과 크기, 색상 등을 설정할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .white, padding: nil)
```

3. 로딩 인디케이터를 원하는 위치에 추가합니다.

```swift
activityIndicatorView.center = view.center
view.addSubview(activityIndicatorView)
```

4. 로딩 인디케이터를 시작하고 멈출 때에는 다음과 같이 호출합니다.

```swift
activityIndicatorView.startAnimating()

activityIndicatorView.stopAnimating()
```

## 예제 코드

```swift
import UIKit
import NVActivityIndicatorView

class LockScreenViewController: UIViewController {
    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .white, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()
        setupActivityIndicatorView()
    }

    func setupActivityIndicatorView() {
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
    }

    func startLoading() {
        activityIndicatorView.startAnimating()
    }

    func stopLoading() {
        activityIndicatorView.stopAnimating()
    }
}
```

위 예제 코드는 잠금화면 뷰 컨트롤러에 NVActivityIndicatorView를 추가하고, 로딩을 시작하고 멈추는 기능을 구현한 것입니다. 사용하고자 하는 스타일에 따라 `type`의 값을 다르게 설정하여 다양한 인디케이터 스타일을 사용할 수 있습니다.

## 결론

NVActivityIndicatorView를 이용하면 iOS 앱에서 간편하게 로딩 인디케이터를 구현할 수 있습니다. 위 예제를 참고하여 잠금화면 시계의 로딩 효과를 구현해보세요!