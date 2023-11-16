---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 애니메이션 로딩 표시 지원하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱 개발에서 데이터를 로드하거나 오래 걸리는 작업을 수행할 때 사용자에게 로딩 상태를 알려주는 것은 중요합니다. 이를 위해 NVActivityIndicatorView를 사용하여 애니메이션 로딩 표시를 구현할 수 있습니다. 이 블로그에서는 Swift에서 NVActivityIndicatorView를 사용하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift에서 사용할 수 있는 로딩 애니메이션을 제공해주는 오픈소스 라이브러리입니다. 다양한 스타일과 크기의 로딩 인디케이터를 제공하며, 사용하기도 매우 간편합니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 CocoaPods를 통해 설치해야 합니다. Podfile에 다음과 같이 라이브러리를 추가해주세요:

```swift
pod 'NVActivityIndicatorView'
```

Terminal에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다. 이후, `.xcworkspace` 확장자를 가진 프로젝트 파일을 열어주세요.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView 라이브러리를 import 하세요.

```swift
import NVActivityIndicatorView
```

2. 로딩 인디케이터를 나타낼 UIView를 생성하세요.

```swift
var activityIndicatorView: NVActivityIndicatorView!
```

3. 적절한 위치에 로딩 인디케이터를 추가하세요.

```swift
activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
```

위 코드에서 `type`은 로딩 인디케이터의 스타일을 설정하고, `color`는 인디케이터 색상을 설정합니다. `padding`은 인디케이터 내부 여백을 설정할 수 있습니다.

4. 로딩 인디케이터를 표시하거나 숨기기 위한 함수를 작성하세요.

```swift
func showLoadingIndicator() {
    activityIndicatorView.startAnimating()
}

func hideLoadingIndicator() {
    activityIndicatorView.stopAnimating()
}
```

로딩 인디케이터를 사용하기 위해 필요한 메소드를 작성한 후, 적절한 시점에 호출하여 사용하면 됩니다.

## 예제

다음은 NVActivityIndicatorView를 사용하여 애니메이션 로딩 표시를 구현한 예제 코드입니다.

```swift
import NVActivityIndicatorView

class MyViewController: UIViewController {
    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)
        view.addSubview(activityIndicatorView)
        activityIndicatorView.center = view.center
    }

    func showLoadingIndicator() {
        activityIndicatorView.startAnimating()
    }

    func hideLoadingIndicator() {
        activityIndicatorView.stopAnimating()
    }

    // 예시: 데이터를 로드하는 함수
    func loadData() {
        showLoadingIndicator()

        // 데이터 로드 작업 수행
        // ...

        hideLoadingIndicator()
    }
}
```

위 코드에서는 `MyViewController` 클래스에 `showLoadingIndicator()`와 `hideLoadingIndicator()` 함수를 추가하여 로딩 인디케이터를 표시하고 숨기는 기능을 구현하였습니다.

## 결론

NVActivityIndicatorView를 사용하면 간단하게 애니메이션 로딩 표시를 구현할 수 있습니다. 로딩 상태를 사용자에게 알려주어 사용자 경험을 향상시킬 수 있습니다. 이러한 기능을 통해 앱 개발을 보다 효율적으로 진행할 수 있습니다.