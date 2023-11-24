---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 정의 로딩 인디케이터 만들기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 개요

이번 글에서는 Swift 언어를 사용하여 NVActivityIndicatorView를 이용하여 사용자 정의 로딩 인디케이터를 만드는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 iOS 앱에서 로딩 상태를 시각적으로 보여주는 데 사용되는 오픈 소스 라이브러리입니다.

## Step 1: 프로젝트 설정

1. Cocoapods을 사용하여 NVActivityIndicatorView를 프로젝트에 추가합니다. `Podfile`에 다음과 같이 NVActivityIndicatorView를 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

2. 터미널을 열고 프로젝트의 루트 디렉터리로 이동한 다음 다음 명령어를 실행하여 Cocoapods을 설치합니다:

```shell
pod install
```

## Step 2: 인디케이터 뷰 생성

1. Xcode에서 `.xib` 또는 스토리보드에서 원하는 인디케이터 뷰를 추가합니다. 자신만의 사용자 정의 뷰를 정의하는 것도 가능합니다.
2. 추가한 인디케이터 뷰의 클래스를 `NVActivityIndicatorAnimationDelegate` 프로토콜을 구현한 클래스로 설정합니다. 예를들어 `CustomLoaderView` 클래스로 설정합니다.
3. `CustomLoaderView` 클래스에서 다음 코드를 삽입합니다:

```swift
import NVActivityIndicatorView

class CustomLoaderView: UIView, NVActivityIndicatorAnimationDelegate {

    private let activityIndicatorView: NVActivityIndicatorView

    override init(frame: CGRect) {
        super.init(frame: frame)

        activityIndicatorView = NVActivityIndicatorView(frame: frame)
        addSubview(activityIndicatorView)
    }

    required init?(coder aDecoder: NSCoder) {
        super.init(coder: aDecoder)

        activityIndicatorView = NVActivityIndicatorView(frame: frame)
        addSubview(activityIndicatorView)
    }

    override func layoutSubviews() {
        super.layoutSubviews()

        activityIndicatorView.frame = bounds
    }

    func startActivityAnimation() {
        activityIndicatorView.startAnimating()
    }

    func stopActivityAnimation() {
        activityIndicatorView.stopAnimating()
    }
}
```

## Step 3: 사용자 정의 로딩 인디케이터 사용

이제 `CustomLoaderView`를 사용하여 로딩 상태를 표시할 수 있습니다.

1. 사용자 정의 로딩 인디케이터를 추가하려는 뷰 컨트롤러에서 다음 코드를 삽입합니다:

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    private var customLoaderView: CustomLoaderView!

    override func viewDidLoad() {
        super.viewDidLoad()

        customLoaderView = CustomLoaderView(frame: view.bounds)
        view.addSubview(customLoaderView)
    }

    // 로딩 상태 표시
    func showLoadingIndicator() {
        customLoaderView.startActivityAnimation()
    }

    // 로딩 상태 숨김
    func hideLoadingIndicator() {
        customLoaderView.stopActivityAnimation()
    }
}
```

2. 로딩 상태를 표시하려는 시점에서 `showLoadingIndicator()`를 호출하고 로딩 상태를 숨기려는 시점에서 `hideLoadingIndicator()`를 호출하면 됩니다.

## 결론

이제 NVActivityIndicatorView를 사용하여 사용자 정의 로딩 인디케이터를 만드는 방법에 대해 알게되었습니다. 이를 활용하여 앱에 직접적으로 적용할 수 있으며, 사용자 정의 인디케이터 뷰를 만들어서 원하는 디자인을 적용할 수도 있습니다.

## 참고

- NVActivityIndicatorView GitHub repository: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)
- Cocoapods: [https://cocoapods.org/](https://cocoapods.org/)