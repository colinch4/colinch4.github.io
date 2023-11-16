---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 시 인터렉션 제한하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

iOS 앱 개발 중 화면이 로딩 되는 동안 사용자의 인터랙션을 제한하고 싶을 때가 있습니다. 이러한 상황에서 NVActivityIndicatorView를 사용하면 로딩 인디케이터를 간편하게 구현할 수 있습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 쉽고 유연하게 커스터마이징 가능한 로딩 인디케이터를 제공하는 iOS 라이브러리입니다. 다양한 스타일과 애니메이션 효과를 제공하면서, 간편한 사용법으로 신속하게 로딩 인디케이터를 적용할 수 있습니다.

## 설치 방법

1. Cocoapods를 통해 NVActivityIndicatorView를 설치합니다. Podfile에 다음과 같이 추가합니다:
```ruby
pod 'NVActivityIndicatorView'
```

2. 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 다운로드합니다.

## 사용 방법

1. NVActivityIndicatorView를 import 합니다:
```swift
import NVActivityIndicatorView
```

2. UIView 인스턴스를 생성하여 로딩 인디케이터를 추가합니다:
```swift
let loaderView = NVActivityIndicatorView(
    frame: CGRect(x: 0, y: 0, width: 50, height: 50),
    type: .ballSpinFadeLoader,
    color: .blue,
    padding: nil
)
```

3. 인디케이터를 원하는 위치에 추가하고 시작합니다:
```swift
loaderView.center = view.center
view.addSubview(loaderView)
loaderView.startAnimating()
```

4. 로딩이 완료되면 인디케이터를 제거합니다:
```swift
loaderView.stopAnimating()
loaderView.removeFromSuperview()
```

## 예제

다음은 NVActivityIndicatorView를 사용하여 화면 로딩 시 인터랙션을 제한하는 간단한 예제입니다:

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {
    
    let loaderView = NVActivityIndicatorView(
        frame: CGRect(x: 0, y: 0, width: 50, height: 50),
        type: .ballSpinFadeLoader,
        color: .blue,
        padding: nil
    )
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 화면 로딩 시 인터랙션 제한
        startLoading()
        
        // 데이터 로딩 등의 작업 수행
        fetchData()
    }
    
    func startLoading() {
        loaderView.center = view.center
        view.addSubview(loaderView)
        loaderView.startAnimating()
    }
    
    func stopLoading() {
        loaderView.stopAnimating()
        loaderView.removeFromSuperview()
    }
    
    func fetchData() {
        // 데이터 로딩 작업 수행
        
        // 로딩이 완료되면 인디케이터 제거
        self.stopLoading()
    }
}
```

이 예제를 통해 NVActivityIndicatorView를 사용하여 화면 로딩 시 인터랙션을 제한할 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView Github](https://github.com/ninjaprox/NVActivityIndicatorView)

이 자료는 NVActivityIndicatorView를 사용하여 화면 로딩 시 인터랙션을 제한하는 방법에 대해 소개했습니다. 만약 더 자세한 내용이 필요하다면 NVActivityIndicatorView의 공식 Github 페이지를 참고해 보세요.