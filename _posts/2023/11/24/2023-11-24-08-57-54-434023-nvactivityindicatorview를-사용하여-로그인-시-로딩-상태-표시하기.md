---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 로그인 시 로딩 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번 포스트에서는 iOS 앱 개발에서 로그인 시 로딩 상태를 표시하는 방법에 대해 알아보겠습니다. 이를 위해 NVActivityIndicatorView를 사용할 것입니다. NVActivityIndicatorView는 사용자에게 로딩 중임을 시각적으로 알려주는 인디케이터입니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 Objective-C와 Swift를 지원하는 iOS용 로딩 인디케이터 라이브러리입니다. 다양한 모양과 스타일의 로딩 인디케이터를 제공하며, 쉽게 커스터마이징할 수 있습니다.

## 시작하기 전에
NVActivityIndicatorView를 사용하려면 먼저 CocoaPods를 사용하여 프로젝트에 라이브러리를 설치해야 합니다. Podfile에 다음과 같은 내용을 추가하세요.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치하세요.

## NVActivityIndicatorView 사용 방법
1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 인디케이터를 추가할 UIView를 생성합니다.

```swift
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .circleStrokeSpin, color: .white, padding: nil)
```

3. 인디케이터를 화면에 표시합니다.

```swift
loadingView.startAnimating()
```

4. 인디케이터를 화면에서 숨기거나 제거합니다.

```swift
loadingView.stopAnimating()
loadingView.removeFromSuperview()
```

## 예시 코드
다음은 NVActivityIndicatorView를 사용하여 로그인 시 로딩 상태를 표시하는 예시 코드입니다.

```swift
import NVActivityIndicatorView

class LoginViewController: UIViewController {
    let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .circleStrokeSpin, color: .white, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    func loginButtonTapped() {
        startLoading()
        
        // 로그인 작업 수행
        // ...
        
        stopLoading()
    }

    func startLoading() {
        loadingView.center = view.center
        view.addSubview(loadingView)
        loadingView.startAnimating()
    }

    func stopLoading() {
        loadingView.stopAnimating()
        loadingView.removeFromSuperview()
    }
}
```

## 마무리
NVActivityIndicatorView를 사용하여 로그인 시 로딩 상태를 표시하는 방법을 알아보았습니다. 이제 앱에 원하는 스타일의 인디케이터를 추가하여 사용자에게 로딩 중인 상태를 시각적으로 알려줄 수 있습니다.

더 많은 NVActivityIndicatorView 사용 방법과 설정 옵션은 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하세요.