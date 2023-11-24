---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 정의 로딩 화면 구현하는 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

로딩 화면은 사용자 경험을 향상시키는 데에 매우 유용합니다. 이번에는 Swift에서 NVActivityIndicatorView를 사용하여 사용자 정의 로딩 화면을 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 빠르고 쉽게 구현할 수 있는 iOS 및 tvOS에서 사용 가능한 로딩 인디케이터 라이브러리입니다. 다양한 스타일과 색상의 인디케이터를 제공하며, 화면에 로딩 인디케이터를 표시하는 데 사용할 수 있습니다.

## NVActivityIndicatorView 설치

CocoaPods를 이용하여 NVActivityIndicatorView를 설치하는 방법은 다음과 같습니다. 

1. `Podfile`을 열고 `pod 'NVActivityIndicatorView'`를 추가합니다.
2. 터미널에서 `pod install`을 실행합니다.
3. 생성된 `.xcworkspace` 파일을 열어서 작업을 진행합니다.

## 사용자 정의 로딩 화면 구현하기

### 1. NVActivityIndicatorView 추가하기

첫 번째로, 사용자 정의 로딩 화면을 표시할 뷰에 NVActivityIndicatorView를 추가해야 합니다. Interface Builder를 사용하거나 코드로 직접 추가할 수 있습니다. 

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50),
                                                    type: .ballScaleRippleMultiple,
                                                    color: .white,
                                                    padding: 0)
        indicatorView.center = view.center
        view.addSubview(indicatorView)
        indicatorView.startAnimating()
    }
}
```

### 2. 로딩 화면 표시하기

로딩 화면을 표시해야 할 때는 다음과 같이 `present(_:animated:completion:)` 메서드를 사용하여 LoadingViewController를 모달로 표시합니다.

```swift
let loadingViewController = LoadingViewController()
present(loadingViewController, animated: true, completion: nil)
```

### 3. 로딩 화면 숨기기

로딩이 완료되면 로딩 화면을 숨기고 원래 화면으로 돌아가야 합니다. 다음과 같이 `dismiss(animated:completion:)` 메서드를 사용하여 로딩 화면을 숨깁니다.

```swift
dismiss(animated: true, completion: nil)
```

위의 코드를 사용하여 NVActivityIndicatorView를 이용한 사용자 정의 로딩 화면을 구현할 수 있습니다. 화면에 로딩 인디케이터를 표시함으로써 사용자는 앱이 작업을 수행하고 있음을 인지할 수 있습니다. 사용자 경험을 개선하기 위해 로딩 화면을 추가해보세요!

## 참고자료

- [NVActivityIndicatorView GitHub Repo](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView Documentation](http://cocoadocs.org/docsets/NVActivityIndicatorView)