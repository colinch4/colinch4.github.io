---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 활용하기 - 스포츠 피트니스 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

> 본 포스트에서는 Swift에서 NVActivityIndicatorView를 활용하여 스포츠 피트니스 앱의 로딩 화면을 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 화면을 구현할 때 사용되는 간단하고 세련된 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하며, 앱의 디자인과 일치하는 로딩 화면을 쉽게 구현할 수 있습니다. 

## 설치하기

NVActivityIndicatorView는 CocoaPods를 통해 쉽게 설치할 수 있습니다. 프로젝트의 Podfile에 다음과 같은 내용을 추가해주세요.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 라이브러리를 설치해주세요.

```bash
$ pod install
```

설치가 완료되면 `.xcworkspace` 파일을 열어주세요.

## 사용 방법

1. 먼저, 로딩 화면을 구현할 `UIViewController`에 NVActivityIndicatorView를 추가해주세요.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 인디케이터 설정
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballSpinFadeLoader, color: .white, padding: .none)
        activityIndicatorView.center = view.center

        // 로딩 인디케이터를 화면에 추가
        view.addSubview(activityIndicatorView)
    }

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)

        // 로딩 인디케이터를 시작
        activityIndicatorView.startAnimating()
    }

    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)

        // 로딩 인디케이터를 정지
        activityIndicatorView.stopAnimating()
    }
}
```

2. 로딩 화면을 보여줄 때 `LoadingViewController`를 present 해주세요.

```swift
let loadingViewController = LoadingViewController()
present(loadingViewController, animated: false)
```

3. 작업이 완료되면, 로딩 화면을 dismiss 해주세요.

```swift
loadingViewController.dismiss(animated: false)
```

## 추가적인 기능

NVActivityIndicatorView는 다양한 스타일의 로딩 인디케이터를 제공합니다. `type`을 변경하여 다른 스타일의 로딩 화면을 적용해볼 수 있습니다. 또한, `color`와 `padding` 등을 조정하여 로딩 화면의 디자인을 변경할 수도 있습니다.

자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고해주세요.

## 결론

이제 Swift에서 NVActivityIndicatorView를 활용하여 스포츠 피트니스 앱의 로딩 화면을 구현할 수 있게 되었습니다. NVActivityIndicatorView는 간단하고 사용하기 쉬운 라이브러리이므로, 다양한 iOS 앱에서 로딩 화면을 추가하고자 할 때 유용하게 활용할 수 있습니다.