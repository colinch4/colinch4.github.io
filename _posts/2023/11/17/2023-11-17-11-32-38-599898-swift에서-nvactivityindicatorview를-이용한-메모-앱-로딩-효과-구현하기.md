---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 이용한 메모 앱 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 소개

이 기사에서는 Swift를 사용하여 메모 앱에 로딩 효과를 구현하는 방법을 살펴보겠습니다. 우리는 NVActivityIndicatorView 라이브러리를 사용하여 로딩 인디케이터를 추가할 것입니다. NVActivityIndicatorView는 iOS 앱에 사용하기 쉬운 다양한 스타일의 로딩 인디케이터를 제공하는 오픈 소스 라이브러리입니다.

## 단계별 진행

### 1. NVActivityIndicatorView 설치하기

우선, Cocoapods를 사용하여 NVActivityIndicatorView를 설치해야 합니다. Podfile에 다음과 같은 코드를 추가하고, 터미널에서 `pod install` 명령어를 실행합니다.

```swift
pod 'NVActivityIndicatorView'
```

### 2. NVActivityIndicatorView 초기화하기

NVActivityIndicatorView를 사용하기 위해 View Controller에 import 문을 추가하고, `viewDidLoad` 메서드에서 NVActivityIndicatorView를 초기화합니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 초기화
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballBeat, color: .blue, padding: nil)
        activityIndicatorView.center = view.center
    }

    // ...
}
```

### 3. 로딩 효과 표시하기

로딩 효과를 표시하기 위해 NVActivityIndicatorView를 화면에 추가하고 시작하도록 코드를 추가합니다. 예를 들어, "로딩 시작" 버튼을 누르면 로딩 효과가 시작되고, "로딩 종료" 버튼을 누르면 로딩 효과가 종료되도록 구현할 수 있습니다.

```swift
class ViewController: UIViewController {

    // ...

    @IBAction func startLoadingButtonTapped(_ sender: UIButton) {
        // NVActivityIndicatorView를 화면에 추가
        view.addSubview(activityIndicatorView)
        activityIndicatorView.startAnimating()
    }

    @IBAction func stopLoadingButtonTapped(_ sender: UIButton) {
        // NVActivityIndicatorView를 화면에서 제거
        activityIndicatorView.stopAnimating()
        activityIndicatorView.removeFromSuperview()
    }

    // ...
}
```

### 4. 추가적인 커스터마이징

NVActivityIndicatorView는 다양한 스타일과 색상을 제공합니다. 위의 예제에서는 `ballBeat` 스타일과 파란색을 사용했습니다. 원하는 스타일과 색상으로 커스터마이징하려면 다음과 같이 코드를 수정하세요.

```swift
// 원하는 스타일과 색상으로 NVActivityIndicatorView 초기화
activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .yourStyle, color: .yourColor, padding: nil)
```

`type` 매개변수에는 `ballSpinFadeLoader`, `lineSpinFadeLoader`, `circleStrokeSpin`, `pacman` 등 다양한 스타일을 지정할 수 있습니다. 또한 `color` 매개변수에는 `UIColor` 객체를 전달하여 원하는 색상으로 설정할 수 있습니다.

## 결론

이제 Swift에서 NVActivityIndicatorView를 사용하여 메모 앱에 로딩 효과를 구현할 수 있습니다. NVActivityIndicatorView는 앱에 프로페셔널하고 멋진 로딩 인디케이터를 추가하는 데 도움이 됩니다. 자세한 내용은 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.

## 참고 자료

- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)