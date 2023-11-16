---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 표시하고 사용자 인터렉션 제어하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift에서 NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 표시하고 사용자 인터렉션을 제어하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift용으로 개발된 스피너 라이브러리입니다. 이 라이브러리를 사용하면 데이터가 로딩 중일 때 사용자에게 로딩 상태를 시각적으로 전달할 수 있습니다. 다양한 스피너 스타일과 커스텀화가 가능하여 사용자 인터페이스에 맞게 디자인할 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView는 CocoaPods를 통해 쉽게 설치할 수 있습니다. `Podfile`에 다음 내용을 추가한 후, `pod install` 명령을 실행하면 됩니다.

```swift
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기

먼저, 스피너를 표시할 뷰 컨트롤러에서 NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

다음으로, NVActivityIndicatorView를 초기화하고 위치를 지정합니다. 로딩 상태의 뷰에 스피너를 추가합니다. 예를 들어, UIViewController의 viewDidLoad() 메서드에서 다음 코드를 작성할 수 있습니다.

```swift
class ViewController: UIViewController {
    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .red, padding: nil)
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
    }
}
```

위의 코드에서는 스피너의 크기, 스타일, 색상 등을 설정하고, 뷰의 중앙에 위치하도록 지정하였습니다.

로딩 상태를 시작하려면 아래와 같이 `startAnimating()` 메서드를 호출합니다.

```swift
activityIndicatorView.startAnimating()
```

로딩 상태를 종료하려면 아래와 같이 `stopAnimating()` 메서드를 호출합니다.

```swift
activityIndicatorView.stopAnimating()
```

로딩 상태 중에 스피너를 감추고자 할 경우에는 `hidesWhenStopped` 속성을 `true`로 설정합니다.

```swift
activityIndicatorView.hidesWhenStopped = true
```

## 사용자 인터렉션 제어하기

로딩 상태 중에 사용자 인터렉션을 제어하는 방법은 간단합니다. `startAnimating()` 메서드를 호출하여 스피너를 표시하면, 스피너가 화면을 가리므로 사용자는 인터렉션을 수행할 수 없습니다. 반대로, `stopAnimating()` 메서드를 호출하여 스피너를 감추면, 사용자는 다시 인터렉션을 수행할 수 있습니다.

예를 들어, 서버에서 데이터를 가져오는 동안 사용자가 다른 작업을 수행하지 못하도록 하려면, 데이터 로딩을 시작할 때 스피너를 표시하고 로딩이 완료된 후에 스피너를 감추면 됩니다.

```swift
activityIndicatorView.startAnimating()
// 데이터 로딩 작업 수행

// 데이터 로딩 작업이 완료된 후에 스피너를 감추는 코드
activityIndicatorView.stopAnimating()
```

## 마무리

이번에는 NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 시각적으로 표시하고 사용자 인터렉션을 제어하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 간편하게 설치하고 다양한 스피너 스타일을 제공하여 사용자 경험 향상에 도움이 됩니다. 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.