---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 이용한 웹 스크랩 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

많은 앱에서 웹 스크랩을 사용하는 경우, 사용자가 기다리는 동안 로딩 효과를 보여주는 것은 좋은 사용자 경험이됩니다. 이를 위해 Swift에서 NVActivityIndicatorView 라이브러리를 사용하여 웹 스크랩 로딩 효과를 구현할 수 있습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS에서 로딩 인디케이터를 만들기위한 라이브러리입니다. 다양한 로딩 스타일과 색상을 제공하여 필요한 대로 로딩 효과를 사용자 정의할 수 있습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 위해 우선 CocoaPods를 사용하여 프로젝트에 라이브러리를 설치해야합니다. Podfile에 다음 줄을 추가하고 `pod install` 명령을 실행하세요.

```ruby
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 추가하기

먼저 해당 프로젝트의 ViewController에 NVActivityIndicatorView를 추가해야합니다. 

```swift
import NVActivityIndicatorView
```

이제 ViewController 클래스 내에 다음 코드를 추가하여 NVActivityIndicatorView를 초기화하고 화면에 추가합니다.

```swift
class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 초기화
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: self.view.frame.size.width/2 - 25, y: self.view.frame.size.height/2 - 25, width: 50, height: 50), type: .ballScaleRipple, color: UIColor.blue, padding: nil)
        view.addSubview(activityIndicatorView)
    }

}
```

## 웹 스크랩 로딩 효과 구현하기

이제 웹 스크랩을 시작하기 전에 `startAnimating()` 메서드를 호출하여 로딩 효과를 표시 할 수 있습니다. 스크랩이 완료되면 `stopAnimating()` 메서드를 호출하여 로딩 효과를 중지 할 수 있습니다.

```swift
class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 초기화
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: self.view.frame.size.width/2 - 25, y: self.view.frame.size.height/2 - 25, width: 50, height: 50), type: .ballScaleRipple, color: UIColor.blue, padding: nil)
        view.addSubview(activityIndicatorView)

        // 웹 스크랩 시작
        startWebScraping()
    }

    func startWebScraping() {
        // 로딩 효과 표시
        activityIndicatorView.startAnimating()

        // 웹 스크랩 로직

        // 웹 스크랩 완료 후 로딩 효과 중지
        activityIndicatorView.stopAnimating()
    }
}
```

## 결과 확인하기

이제 앱을 실행하고 웹 스크랩이 시작되면 로딩 효과가 표시됩니다. 스크랩이 완료되면 로딩 효과가 중지됩니다. 이와 같은 방식으로 NVActivityIndicatorView를 사용하여 웹 스크랩 로딩 효과를 구현할 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView Documentation](https://github.com/ninjaprox/NVActivityIndicatorView/blob/master/README.md)