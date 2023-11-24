---
layout: post
title: "[swift] NVActivityIndicatorView의 기능과 특징"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

### 소개
NVActivityIndicatorView는 iOS 애플리케이션에서 사용되는 로딩 인디케이터를 구현하기 위해 제공되는 오픈 소스 라이브러리입니다. 이 라이브러리는 다양한 로딩 애니메이션을 제공하며, 사용하기 쉬운 인터페이스를 가지고 있습니다.

### 기능
- 다양한 로딩 애니메이션: NVActivityIndicatorView는 다양한 로딩 애니메이션을 제공합니다. 사용자는 원하는 애니메이션을 선택하여 로딩 인디케이터를 구현할 수 있습니다.
- 사용자 정의 가능: NVActivityIndicatorView는 사용자가 로딩 애니메이션을 자유롭게 커스터마이즈할 수 있는 기능을 제공합니다. 색상, 크기 등을 조정하여 애플리케이션에 맞게 로딩 인디케이터를 디자인할 수 있습니다.
- 간편한 통합: NVActivityIndicatorView는 Cocoapods를 통해 쉽게 프로젝트에 통합할 수 있습니다. Cocoapods를 사용하여 NVActivityIndicatorView를 설치한 후, 몇 줄의 코드만으로 로딩 인디케이터를 사용할 수 있습니다.

### 사용법
1. Cocoapods를 사용하여 NVActivityIndicatorView를 프로젝트에 추가합니다.
   ```swift
   pod 'NVActivityIndicatorView'
   ```
2. NVActivityIndicatorView를 import 합니다.
   ```swift
   import NVActivityIndicatorView
   ```
3. NVActivityIndicatorView를 생성하고 원하는 로딩 애니메이션을 설정합니다.
   ```swift
   let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballRotateChase, color: .purple, padding: nil)
   ```
4. 원하는 시점에 로딩 애니메이션을 시작합니다.
   ```swift
   activityIndicatorView.startAnimating()
   ```
5. 로딩 애니메이션을 중지합니다.
   ```swift
   activityIndicatorView.stopAnimating()
   ```

### 예제 코드
```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballRotateChase, color: .purple, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()
        // 로딩 애니메이터를 화면에 추가합니다.
        view.addSubview(activityIndicatorView)
        
        // 로딩 애니메이션을 시작합니다.
        activityIndicatorView.startAnimating()
        
        // 5초 후에 로딩 애니메이션을 중지합니다.
        DispatchQueue.main.asyncAfter(deadline: .now() + 5) {
            self.activityIndicatorView.stopAnimating()
        }
    }
}
```

### 참고 자료
- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 문서](https://cocoapods.org/pods/NVActivityIndicatorView)