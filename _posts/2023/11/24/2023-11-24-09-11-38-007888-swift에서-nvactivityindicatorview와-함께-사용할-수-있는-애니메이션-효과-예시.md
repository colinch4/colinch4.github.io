---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 함께 사용할 수 있는 애니메이션 효과 예시"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Swift에서 NVActivityIndicatorView는 다양한 로딩 인디케이터를 사용할 수 있도록 제공하는 라이브러리입니다. 이를 사용하여 앱에 화려한 로딩 애니메이션을 추가할 수 있습니다. 이 포스트에서는 NVActivityIndicatorView를 사용하여 간단한 로딩 애니메이션을 만드는 예시를 알아보겠습니다.

## NVActivityIndicatorView 라이브러리 설치

먼저, NVActivityIndicatorView 라이브러리를 설치해야 합니다. 이를 위해 CocoaPods를 사용하는 경우, Podfile에 다음과 같이 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## 로딩 애니메이션 추가하기

1. NVActivityIndicatorView를 사용하기 위해 import문을 추가합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 애니메이션을 표시할 뷰를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
activityIndicatorView.center = view.center
```

로딩 애니메이션의 크기와 위치를 조정할 수 있습니다.

3. 로딩 애니메이션 스타일을 설정합니다.

```swift
activityIndicatorView.type = .ballPulse
activityIndicatorView.color = UIColor.red
```

NVActivityIndicatorView는 다양한 스타일을 제공합니다. 여기에서는 ballPulse 스타일을 사용하고, 테마 색상을 빨강으로 지정했습니다.

4. 뷰에 로딩 애니메이션을 추가합니다.

```swift
view.addSubview(activityIndicatorView)
```

5. 로딩 애니메이션을 시작하거나 중지합니다.

```swift
activityIndicatorView.startAnimating()

// 중지
activityIndicatorView.stopAnimating()
```

애니메이션을 시작하면 로딩 인디케이터가 표시되고, 중지하면 사라집니다.

## 예시 사용법

아래의 예시 코드를 사용하여 로딩 애니메이션을 만들어보세요.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {
    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))

    override func viewDidLoad() {
        super.viewDidLoad()
        
        activityIndicatorView.center = view.center
        activityIndicatorView.type = .ballPulse
        activityIndicatorView.color = UIColor.red
        view.addSubview(activityIndicatorView)
    }

    @IBAction func startButtonTapped(_ sender: UIButton) {
        activityIndicatorView.startAnimating()
    }

    @IBAction func stopButtonTapped(_ sender: UIButton) {
        activityIndicatorView.stopAnimating()
    }
}
```

위의 예시 코드에서는 UIButton을 사용하여 로딩 애니메이션을 시작 및 중지하는 기능을 추가했습니다. 이를 사용하여 사용자에게 로딩 상태를 시각적으로 알릴 수 있습니다.

NVActivityIndicatorView는 사용하기 쉽고 다양한 로딩 스타일을 제공하여 앱에 다양한 로딩 애니메이션을 추가할 수 있습니다. 더 자세한 정보는 [NVActivityIndicatorView 공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.