---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 크기와 외관 변경하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

애플리케이션 개발 시에는 종종 로딩 인디케이터를 사용하여 사용자에게 어떤 작업이 진행 중임을 알리는 경우가 있습니다. NVActivityIndicatorView는 iOS 애플리케이션에서 사용할 수 있는 인디케이터 라이브러리입니다. 이 라이브러리는 다양한 애니메이션 스타일과 크기를 제공하며, Swift에서 쉽게 사용할 수 있습니다.

이번 글에서는 NVActivityIndicatorView를 사용하여 애니메이션의 크기와 외관을 변경하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 사용하기 위해 프로젝트에 라이브러리를 설치해야 합니다. CocoaPods를 사용하여 설치할 수 있습니다. `Podfile`에 다음과 같이 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 아래 명령어를 실행하여 라이브러리를 설치합니다.

```bash
$ pod install
```

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하여 애니메이션을 생성하려면 다음과 같이 코드를 작성합니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: 0)
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
    }

    func startAnimating() {
        activityIndicatorView.startAnimating()
    }

    func stopAnimating() {
        activityIndicatorView.stopAnimating()
    }
}
```

위의 코드에서 `NVActivityIndicatorView`의 인스턴스를 만들고 원하는 크기와 스타일을 설정합니다. `startAnimating()` 메서드를 호출하여 애니메이션을 시작하고, `stopAnimating()` 메서드를 호출하여 애니메이션을 중지할 수 있습니다.

## 애니메이션 크기 변경하기

NVActivityIndicatorView의 크기를 조정하기 위해서는 `frame` 속성을 변경하면 됩니다. 위의 예시에서는 가로와 세로 크기를 각각 50으로 설정했습니다. 이 값을 원하는 크기로 변경하여 애니메이션의 크기를 조정할 수 있습니다.

## 애니메이션 외관 변경하기

NVActivityIndicatorView는 다양한 스타일을 제공하며, 스타일을 변경하기 위해서는 `type` 속성을 설정하면 됩니다. 위의 예시에서는 `.ballSpinFadeLoader` 스타일을 사용했습니다. 이 값을 다른 스타일로 변경하여 원하는 애니메이션 외관을 얻을 수 있습니다.

또한, `color` 속성을 사용하여 애니메이션의 색상을 변경할 수 있습니다. 예시에서는 `.blue` 색상을 사용했지만, 원하는 색상으로 변경할 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)