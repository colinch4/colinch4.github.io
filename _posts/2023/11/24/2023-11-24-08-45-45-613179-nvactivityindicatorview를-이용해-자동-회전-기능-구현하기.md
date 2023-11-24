---
layout: post
title: "[swift] NVActivityIndicatorView를 이용해 자동 회전 기능 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번에는 Swift에서 NVActivityIndicatorView를 이용하여 자동 회전 기능을 구현하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 애니메이션 인디케이터를 쉽게 구현할 수 있는 라이브러리입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 로딩 인디케이터를 구현하기 위한 Swift 라이브러리입니다. 다양한 스타일과 색상, 크기의 인디케이터를 제공하며, 커스텀화도 가능합니다.

자동 회전 기능은 인디케이터가 화면을 돌아다니면서 계속해서 회전하는 기능을 의미합니다. 이를 구현하기 위해서는 다음의 단계를 따라야 합니다.

## 단계 1: NVActivityIndicatorView 라이브러리 설치

먼저, NVActivityIndicatorView를 설치해야 합니다. CocoaPods를 사용하는 경우 Podfile에 다음과 같이 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## 단계 2: NVActivityIndicatorView 객체 생성

NVActivityIndicatorView 객체를 생성하여 해당 뷰에 추가합니다. 먼저 NVActivityIndicatorView를 import 하고, 뷰 컨트롤러의 viewDidLoad() 메소드에서 다음과 같이 추가합니다:

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 인디케이터 스타일과 프레임 설정
        let activityFrame = CGRect(x: 0, y: 0, width: 40, height: 40)
        activityIndicatorView = NVActivityIndicatorView(frame: activityFrame)

        // 인디케이터 색상 설정
        activityIndicatorView.color = UIColor.red

        // 인디케이터를 뷰에 추가
        view.addSubview(activityIndicatorView)
    }

    // ...
}
```

## 단계 3: 자동 회전 기능 추가

자동 회전 기능을 추가하기 위해서는 NVActivityIndicatorView.startAnimating() 메소드를 호출하고, NVActivityIndicatorView.stopAnimating() 메소드를 호출하여 멈추도록 해야 합니다. 일반적으로 네트워크 요청이 시작되거나 종료되는 시점에서 인디케이터를 동작시키는 것이 일반적입니다.

```swift
class ViewController: UIViewController {

    // ...

    func startLoading() {
        activityIndicatorView.startAnimating()
    }

    func stopLoading() {
        activityIndicatorView.stopAnimating()
    }

    // ...
}
```

이렇게 구현하면 네트워크 요청 중에 스크린을 회전시켜도 인디케이터가 동작하게 됩니다.

## 결론

NVActivityIndicatorView를 이용하면 간단하게 인디케이터를 구현할 수 있습니다. 자동 회전 기능을 추가해 네트워크 요청 중에도 인디케이터가 멈추지 않도록 할 수 있습니다. NVActivityIndicatorView를 사용하여 사용자 경험을 향상시키세요!

더 자세한 정보는 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하시기 바랍니다.