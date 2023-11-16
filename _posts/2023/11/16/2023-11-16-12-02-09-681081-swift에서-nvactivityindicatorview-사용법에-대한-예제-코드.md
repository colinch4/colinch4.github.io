---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 사용법에 대한 예제 코드"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 로딩 인디케이터를 쉽게 구현할 수 있는 라이브러리입니다.

## NVActivityIndicatorView 설치

먼저, Swift 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. 

CocoaPods를 사용하는 경우, Podfile에 다음과 같이 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 의존성을 설치합니다:

```
pod install
```

CocoaPods를 사용하지 않고 수동으로 설치하는 경우, [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView) 페이지에서 최신 버전을 다운로드하고 프로젝트에 직접 추가합니다.

## NVActivityIndicatorView 사용해보기

NVActivityIndicatorView를 사용해 로딩 인디케이터를 구현해보겠습니다. 먼저, 프로젝트에서 NVActivityIndicatorView를 import하고, 인디케이터를 추가할 뷰를 생성합니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 인스턴스 생성
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .blue)

        // 뷰에 인디케이터 추가
        view.addSubview(activityIndicatorView)

        // 인디케이터를 화면 중앙에 위치시킴
        activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            activityIndicatorView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
            activityIndicatorView.centerYAnchor.constraint(equalTo: view.centerYAnchor)
        ])

        // 인디케이터를 시작
        activityIndicatorView.startAnimating()
    }
}
```

위 코드에서는 ViewController에 NVActivityIndicatorView를 추가합니다. 인스턴스를 생성한 후, 원하는 스타일과 색상을 설정한 다음, 뷰에 추가합니다. 인디케이터를 화면 중앙에 위치시키기 위해 오토레이아웃을 설정하고, startAnimating() 메소드를 호출하여 인디케이터를 시작합니다.

## 추가 옵션

NVActivityIndicatorView는 다양한 스타일과 색상을 제공하는데, 원하는 스타일과 색상을 선택할 수 있습니다. `NVActivityIndicatorView.Style`과 `UIColor`를 통해 스타일과 색상을 설정할 수 있습니다. 

```swift
// 다른 스타일로 인디케이터를 생성
activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballRotateChase, color: .red)

// 다른 색상으로 인디케이터를 생성
activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .green)
```

## 결론

이번 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하는 방법을 알아보았습니다. NVActivityIndicatorView를 사용하면 쉽고 간편하게 로딩 인디케이터를 구현할 수 있습니다. 자세한 내용은 [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView) 페이지에서 확인할 수 있습니다.

### 참고 자료

- [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)