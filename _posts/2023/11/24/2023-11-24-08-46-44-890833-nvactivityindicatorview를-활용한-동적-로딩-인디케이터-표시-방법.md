---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 동적 로딩 인디케이터 표시 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번에는 Swift 언어의 NVActivityIndicatorView라는 라이브러리를 사용하여 동적 로딩 인디케이터를 표시하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 상태를 표시하기 위한 간단하고 유연한 라이브러리입니다. 다양한 스타일의 인디케이터를 제공하며, 화면에 로딩 중임을 알려주는 용도로 사용됩니다.

## NVActivityIndicatorView 설치

CocoaPods를 사용하여 NVActivityIndicatorView를 설치할 수 있습니다. 

1. Podfile에 다음과 같이 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

2. 터미널을 열고 프로젝트가 있는 디렉토리로 이동한 후, 다음 명령어를 실행합니다.

```bash
$ pod install
```

3. 설치가 완료되면 Xcode에서 `.xcworkspace` 파일을 열어서 사용할 준비를 합니다.

## NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 인디케이터를 표시할 뷰를 생성합니다. 

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))
```

3. 인디케이터의 스타일을 설정합니다. 다양한 스타일 중 하나를 선택할 수 있습니다.

```swift
activityIndicatorView.type = .ballSpinFadeLoader
```

4. 화면에 로딩 인디케이터를 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
activityIndicatorView.startAnimating()
```

5. 로딩이 완료된 후에는 인디케이터를 숨기고 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 예제

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))

    override func viewDidLoad() {
        super.viewDidLoad()
        
        activityIndicatorView.type = .ballSpinFadeLoader
        
        view.addSubview(activityIndicatorView)
        activityIndicatorView.center = view.center
        activityIndicatorView.startAnimating()
        
        // 로딩 시뮬레이션을 위해 3초 후에 인디케이터를 숨기고 제거
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
            self.activityIndicatorView.stopAnimating()
            self.activityIndicatorView.removeFromSuperview()
        }
    }
}
```

위 예제에서는 `ViewController`에 NVActivityIndicatorView를 추가하고, 인디케이터를 3초 동안 표시한 후에 숨기고 제거하는 방법을 보여줍니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)