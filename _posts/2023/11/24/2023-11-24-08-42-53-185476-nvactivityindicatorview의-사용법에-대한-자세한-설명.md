---
layout: post
title: "[swift] NVActivityIndicatorView의 사용법에 대한 자세한 설명"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 제공되는 애니메이션 라이브러리입니다. 이 라이브러리를 사용하면 간편하게 다양한 유형의 로딩 인디케이터를 구현할 수 있습니다. 

## 설치

NVActivityIndicatorView를 사용하려면 먼저 CocoaPods를 설치해야 합니다. `Podfile`에 다음과 같이 NVActivityIndicatorView를 추가합니다.

```
pod 'NVActivityIndicatorView'
```

그런 다음 터미널에서 `pod install` 명령을 실행하여 라이브러리를 프로젝트에 추가합니다.

## 사용법

1. 먼저, `import NVActivityIndicatorView`를 사용하여 라이브러리를 가져옵니다.

2. `NVActivityIndicatorView` 인스턴스를 만듭니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: nil)
```

- `frame`: 인디케이터의 위치와 크기를 설정합니다.
- `type`: 인디케이터의 스타일을 선택합니다. 다양한 스타일 옵션이 있습니다.
- `color`: 인디케이터의 색상을 설정합니다.
- `padding`: 내부 유형의 경우 인디케이터 내부에 패딩을 추가할 수 있습니다.

3. View에 인디케이터를 추가합니다.

```swift
view.addSubview(activityIndicatorView)
```

4. 인디케이터의 시작과 중지를 제어하려면 다음 함수를 사용합니다.

```swift
activityIndicatorView.startAnimating()
activityIndicatorView.stopAnimating()
```

## 예제

다음은 NVActivityIndicatorView를 사용하여 인디케이터를 구현하는 간단한 예제입니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {
    private var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: view.bounds.width/2 - 25, y: view.bounds.height/2 - 25, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: nil)
        view.addSubview(activityIndicatorView)
    }

    func startLoading() {
        activityIndicatorView.startAnimating()
    }

    func stopLoading() {
        activityIndicatorView.stopAnimating()
    }
}
```

위의 예제에서는 `ViewController`의 `viewDidLoad()` 함수에서 인디케이터를 생성하고, `startLoading()` 및 `stopLoading()` 함수를 호출하여 인디케이터의 시작과 중지를 제어합니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 문서](https://github.com/ninjaprox/NVActivityIndicatorView/blob/master/README.md)