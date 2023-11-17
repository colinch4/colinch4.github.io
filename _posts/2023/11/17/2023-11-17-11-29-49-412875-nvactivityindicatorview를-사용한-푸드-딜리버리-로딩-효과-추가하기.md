---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 푸드 딜리버리 로딩 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

푸드 딜리버리 앱을 개발하고 있는데, 주문이 처리되는 동안 로딩 효과를 사용하여 사용자에게 진행 중임을 보여주고 싶다면, NVActivityIndicatorView를 사용해보는 것은 어떨까요? NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 많은 로딩 애니메이션을 제공하는 오픈 소스 라이브러리입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Lavanoid에 의해 개발된 iOS용 로딩 애니메이션 오픈 소스 라이브러리입니다. 다양한 스타일과 색상의 로딩 애니메이션을 제공하여 앱에 추가할 수 있습니다.

## 설치

NVActivityIndicatorView를 사용하기 위해 먼저 CocoaPods를 사용하여 프로젝트에 라이브러리를 추가해야 합니다. Podfile에 다음과 같이 추가하십시오.

```
pod 'NVActivityIndicatorView'
```

그런 다음 터미널에서 다음 명령을 실행하여 종속성을 설치합니다.

```
pod install
```

## 사용 방법

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView 인스턴스를 생성하고, 원하는 로딩 애니메이션 스타일과 색상을 선택합니다. 아래는 몇 가지 예시입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballRotateChase, color: .blue, padding: nil)
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .circleStrokeSpin, color: .red, padding: nil)
```

3. 로딩 효과를 보여주려는 뷰에 NVActivityIndicatorView를 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

4. 로딩이 완료되었을 때, NVActivityIndicatorView를 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 예제

다음은 푸드 딜리버리 앱에서 NVActivityIndicatorView를 사용하여 로딩 효과를 추가하는 예제입니다.

```swift
import UIKit
import NVActivityIndicatorView

class OrderViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballRotateChase, color: .blue, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 효과를 보여주려는 뷰에 NVActivityIndicatorView를 추가합니다.
        view.addSubview(activityIndicatorView)
        
        // 주문 처리 중 로딩 효과를 시작합니다.
        activityIndicatorView.startAnimating()
        
        // 주문이 완료되면 로딩 효과를 제거합니다.
        DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
            self.activityIndicatorView.stopAnimating()
            self.activityIndicatorView.removeFromSuperview()
        }
    }
}
```

위의 예제에서는 `ballRotateChase` 스타일의 로딩 애니메이션을 사용하고 있습니다. 필요에 따라 다른 스타일과 색상으로 변경할 수 있습니다.

## 결론

NVActivityIndicatorView를 사용하면 앱에 로딩 효과를 추가할 수 있습니다. 이를 통해 사용자에게 작업이 진행 중임을 시각적으로 보여줄 수 있습니다. NVActivityIndicatorView를 사용하여 푸드 딜리버리 앱과 같은 앱에 로딩 효과를 쉽게 적용할 수 있습니다.

참고: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)