---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 이용한 테스트 앱 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱의 사용자 경험을 향상시키기 위해 로딩 효과를 구현하는 것은 중요합니다. 이번 글에서는 Swift에서 NVActivityIndicatorView를 이용하여 테스트 앱에 로딩 효과를 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 로딩 인디케이터 라이브러리로, 다양한 스타일의 로딩 효과를 제공합니다. 특히 앱의 로딩 화면이나 비동기 작업 중에 로딩 효과를 보여주는 데 유용합니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. Podfile에 다음 내용을 추가하고, `pod install` 명령을 실행해주세요.

```ruby
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용법

### 1. NVActivityIndicatorView 추가하기

먼저, 로딩 효과를 보여줄 뷰 컨트롤러에 NVActivityIndicatorView를 추가해줍니다. 이를 위해, NVActivityIndicatorView를 import하고, 로딩 효과를 보여줄 뷰에 NVActivityIndicatorView를 추가하는 코드를 작성해야 합니다.

```swift
import NVActivityIndicatorView

class MainViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 생성
        activityIndicatorView = NVActivityIndicatorView(
            frame: CGRect(x: 0, y: 0, width: 40, height: 40),
            type: .ballSpinFadeLoader,
            color: .gray,
            padding: nil
        )
        activityIndicatorView.center = view.center

        // 뷰에 NVActivityIndicatorView 추가
        view.addSubview(activityIndicatorView)
    }

    // 로딩 효과 시작
    func startLoading() {
        activityIndicatorView.startAnimating()
    }

    // 로딩 효과 중지
    func stopLoading() {
        activityIndicatorView.stopAnimating()
    }
}
```

### 2. 로딩 효과 시작 및 중지

위 코드에서 `startLoading()` 메서드는 로딩 효과를 시작하고, `stopLoading()` 메서드는 로딩 효과를 중지하는 역할을 합니다. 이는 로딩이 필요한 부분에서 해당 메서드를 호출하여 사용할 수 있습니다.

예를 들어, 네트워크 요청이 필요한 작업을 수행할 때 `startLoading()`을 호출하여 로딩 효과를 보여주고, 작업이 완료된 후에 `stopLoading()`을 호출하여 로딩 효과를 중지할 수 있습니다.

```swift
func fetchData() {
    startLoading()

    // 네트워크 요청 수행

    stopLoading()
}
```

## 마무리

이렇게 Swift에서 NVActivityIndicatorView를 이용하여 테스트 앱에 로딩 효과를 구현하는 방법을 알아보았습니다. NVActivityIndicatorView는 다양한 스타일의 로딩 효과를 제공하기 때문에, 앱의 디자인에 맞게 선택하여 사용할 수 있습니다. 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고해주세요.