---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 표시하고 사용자 인터랙션 제어하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

지금은 모바일 애플리케이션에서 데이터를 로딩할 때 사용자에게 로딩 상태를 시각적으로 알려주는 것이 중요합니다. NVActivityIndicatorView는 Swift에서 사용할 수 있는 강력한 라이브러리로, 로딩 상태를 표시하기 위한 다양한 애니메이션을 제공합니다. 이 글에서는 NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 표시하고 사용자 인터랙션을 제어하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 로딩 상태를 보여줄 때 사용할 수 있는 iOS용 애니메이션 라이브러리입니다. 다양한 로딩 애니메이션 디자인을 제공하며, 쉽게 사용할 수 있습니다.

## 설치

NVActivityIndicatorView는 CocoaPods를 통해 간단하게 설치할 수 있습니다. 

```swift
pod 'NVActivityIndicatorView'
```

## 사용법

1. 먼저, NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 생성하고 표시할 위치를 정의합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballScaleRippleMultiple, color: .white, padding: nil)
activityIndicatorView.center = view.center
```

3. 데이터 로딩 전에 액티비티 인디케이터를 표시합니다.

```swift
activityIndicatorView.startAnimating()
view.addSubview(activityIndicatorView)
```

4. 데이터가 로딩되면 액티비티 인디케이터를 숨깁니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 사용자 인터랙션 제어

NVActivityIndicatorView를 사용하여 데이터 로딩 중에는 사용자 인터랙션을 제어할 수 있습니다. 데이터가 로딩 중일 때에는 버튼 클릭 등의 사용자 입력을 막아야 합니다. 이를 위해 UIView의 `isUserInteractionEnabled` 속성을 사용하여 사용자 인터랙션을 활성화 또는 비활성화할 수 있습니다.

```swift
// 데이터 로딩 시작
activityIndicatorView.startAnimating()
view.addSubview(activityIndicatorView)
view.isUserInteractionEnabled = false

// 데이터 로딩 완료 후
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
view.isUserInteractionEnabled = true
```

## NVActivityIndicatorView 사용 예제

아래는 NVActivityIndicatorView를 사용하여 로딩 중에는 사용자 인터랙션을 비활성화하는 예제입니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballScaleRippleMultiple, color: .white, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()
        // 액티비티 인디케이터 위치 설정
        activityIndicatorView.center = view.center
    }

    func fetchData() {
        // 데이터 로딩 시작
        activityIndicatorView.startAnimating()
        view.addSubview(activityIndicatorView)
        view.isUserInteractionEnabled = false
        
        // 데이터 로딩 완료 후
        activityIndicatorView.stopAnimating()
        activityIndicatorView.removeFromSuperview()
        view.isUserInteractionEnabled = true
    }
}
```

## 마무리

NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 시각적으로 표시하고 사용자 인터랙션을 제어하는 방법을 알아보았습니다. 이를 통해 애플리케이션의 사용자 경험을 향상시킬 수 있습니다. NVActivityIndicatorView의 다양한 옵션을 적용하여 애플리케이션에 적합한 로딩 애니메이션을 구현해보세요.

## 참고 자료

- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)