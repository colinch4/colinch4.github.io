---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 비동기 작업 진행 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift에서 NVActivityIndicatorView를 사용하여 비동기 작업의 진행 상태를 표시하는 방법에 대해 알아보겠습니다.

NVActivityIndicatorView는 iOS 앱에서 로딩 상태를 나타내는 라이브러리로, 다양한 유형의 로딩 인디케이터를 제공합니다. 이 라이브러리를 사용하면 앱에서 비동기 작업이 진행되는 동안 로딩 인디케이터를 표시하여 사용자에게 작업이 진행 중임을 알려줄 수 있습니다.

## NVActivityIndicatorView 설치

먼저, NVActivityIndicatorView를 설치해야 합니다. Cocoapods를 사용하는 경우, `Podfile`에 다음 줄을 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 설치합니다.

## NVActivityIndicatorView 사용 방법

다음은 NVActivityIndicatorView를 사용하여 비동기 작업 진행 상태를 표시하는 방법입니다.

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 생성합니다. 이때 스타일, 색상, 크기 등을 지정할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)
```

3. 비동기 작업을 시작하기 전에 `startAnimating()` 메서드를 호출하여 로딩 인디케이터를 표시합니다.

```swift
activityIndicatorView.startAnimating()
```

4. 비동기 작업이 완료되면 `stopAnimating()` 메서드를 호출하여 로딩 인디케이터를 숨깁니다.

```swift
activityIndicatorView.stopAnimating()
```

NVActivityIndicatorView는 다양한 스타일과 옵션을 제공하므로, 필요에 맞게 사용할 수 있습니다. 더 많은 정보는 NVActivityIndicatorView의 [공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하세요.

## 예시

다음은 NVActivityIndicatorView를 사용하여 비동기 작업 진행 상태를 표시하는 예시 코드입니다.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {
    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(activityIndicatorView)
    }

    func performAsyncTask() {
        activityIndicatorView.startAnimating()
        
        DispatchQueue.global().async {
            // 비동기 작업 수행
            // ...
            
            DispatchQueue.main.async {
                // 작업 완료 후 UI 업데이트
                // ...
                
                self.activityIndicatorView.stopAnimating()
            }
        }
    }
}
```

위 코드는 `performAsyncTask()` 메서드를 호출하면 비동기 작업이 시작되고, 작업이 완료된 후에 로딩 인디케이터가 숨겨지는 예시입니다.

이제 NVActivityIndicatorView를 사용하여 비동기 작업 진행 상태를 표시하는 방법을 알게 되었습니다. 이를 활용하여 앱의 사용자 경험을 개선할 수 있습니다.