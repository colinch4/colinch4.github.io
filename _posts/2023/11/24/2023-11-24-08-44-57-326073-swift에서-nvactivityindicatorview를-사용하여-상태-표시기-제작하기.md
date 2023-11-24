---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 상태 표시기 제작하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱을 개발할 때 사용자에게 현재 작업 중임을 알리기 위해 상태 표시기를 사용하는 것은 매우 중요합니다. 이를 위해 Swift에서 많은 라이브러리가 제공되는데, 그 중에서도 NVActivityIndicatorView는 간편하게 상태 표시기를 구현할 수 있는 인기있는 오픈소스 라이브러리입니다.

이번 블로그 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 어떻게 상태 표시기를 제작하는지 알아보겠습니다.

## 1. NVActivityIndicatorView 설치하기

먼저 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. 이를 위해 CocoaPods를 사용할 수 있습니다. Podfile에 다음 내용을 추가하고 `pod install` 명령어를 실행하세요.

```swift
pod 'NVActivityIndicatorView'
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 다음과 같이 코드를 작성하세요.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 생성
        let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballSpinFadeLoader, color: .blue, padding: nil)

        // ViewController에 추가
        view.addSubview(activityIndicatorView)

        // 위치 설정
        activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            activityIndicatorView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            activityIndicatorView.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])

        // 상태 표시기 시작
        activityIndicatorView.startAnimating()

        // 네트워크 요청 또는 다른 작업 수행

        // 상태 표시기 중지
        activityIndicatorView.stopAnimating()
    }
}
```

위의 코드에서는 `LoadingViewController`에서 NVActivityIndicatorView를 생성하고, ViewController에 추가합니다. 화면 중앙에 위치하도록 제약 조건을 설정한 후, 작업이 수행되는 동안 상태 표시기를 시작하고, 작업이 완료되면 중지합니다.

## 3. 상태 표시기 스타일 변경하기

NVActivityIndicatorView는 다양한 스타일을 제공합니다. `type` 매개변수를 사용하여 스타일을 변경할 수 있습니다. 다음은 일부 스타일의 예입니다.

- .ballPulse
- .ballClipRotate
- .ballScaleRipple

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballPulse, color: .red, padding: nil)
```

## 마무리

이렇게 Swift에서 NVActivityIndicatorView를 사용하여 상태 표시기를 제작하는 방법을 알아보았습니다. NVActivityIndicatorView는 쉽게 사용할 수 있기 때문에, 앱에서 작업하는 동안 사용자에게 작업 중임을 시각적으로 알리는 것이 가능해집니다.

더 많은 스타일과 옵션을 사용하여 상태 표시기를 더욱 재미있고 다양하게 만들어보세요!

## 참고 자료

- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)