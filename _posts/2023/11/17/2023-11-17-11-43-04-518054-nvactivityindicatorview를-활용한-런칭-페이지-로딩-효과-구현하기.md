---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 런칭 페이지 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱을 개발할 때, 사용자들이 앱을 처음 실행했을 때 로딩 화면을 보여주는 것이 중요합니다. 이를 통해 사용자들에게 앱이 로딩 중임을 알리고, 앱이 준비되어 있는 것처럼 느끼게 할 수 있습니다.

이번 글에서는 NVActivityIndicatorView를 사용하여 iOS 앱의 런칭 페이지에 로딩 효과를 구현하는 방법을 살펴보겠습니다.

### NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift에서 사용할 수 있는 로딩 인디케이터 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하며, 앱의 런칭 페이지나 데이터 로딩 중에 사용자에게 로딩 중임을 시각적으로 보여줄 수 있습니다.

### NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해, 먼저 CocoaPods를 통해 라이브러리를 설치해야 합니다. Podfile에 다음과 같이 추가해주세요:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 라이브러리를 설치합니다:

```
$ pod install
```

### NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 import하세요:

```swift
import NVActivityIndicatorView
```

2. 로딩 효과를 보여줄 뷰를 생성합니다. 일반적으로는 런칭 페이지의 배경 뷰에 추가하는 것이 좋습니다.:

```swift
let backgroundView = UIView(frame: CGRect(x: 0, y: 0, width: view.bounds.width, height: view.bounds.height))
backgroundView.backgroundColor = UIColor.white // 배경 색상은 원하는 색상으로 설정해주세요
view.addSubview(backgroundView)
```

3. NVActivityIndicatorView를 생성하고 설정합니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .circleStrokeSpin, color: UIColor.red)
activityIndicatorView.center = view.center
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

`type`은 로딩 효과의 스타일을 선택할 수 있는 옵션입니다. 다양한 스타일 중 원하는 스타일로 설정해주세요.

4. 앱이 로딩 준비가 완료되면 로딩 효과를 제거해야 합니다. 다음 코드를 알맞은 위치에 추가해주세요:

```swift
activityIndicatorView.stopAnimating()
backgroundView.removeFromSuperview()
```

### 예시 전체 코드

```swift
import UIKit
import NVActivityIndicatorView

class LaunchViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let backgroundView = UIView(frame: CGRect(x: 0, y: 0, width: view.bounds.width, height: view.bounds.height))
        backgroundView.backgroundColor = UIColor.white
        view.addSubview(backgroundView)

        let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .circleStrokeSpin, color: UIColor.red)
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
        activityIndicatorView.startAnimating()

        // 앱 로딩 준비 완료 후 로딩 효과 제거
        DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
            activityIndicatorView.stopAnimating()
            backgroundView.removeFromSuperview()
        }
    }
}
```

### 결론

NVActivityIndicatorView를 사용하면 iOS 앱의 런칭 페이지에 다양한 스타일의 로딩 효과를 쉽게 구현할 수 있습니다. 사용자들에게 로딩 중임을 시각적으로 전달함으로써, 앱의 전체적인 사용자 경험을 향상시킬 수 있습니다.

더 자세한 NVActivityIndicatorView 사용 방법은 [공식 GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하세요.

[swift]: https://swift.org/