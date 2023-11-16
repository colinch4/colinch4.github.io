---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 UI 개선하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

일반적인 앱의 사용자 인터페이스(UI)에는 데이터를 로딩하는 동안 불편한 경험이 있을 수 있습니다. 사용자는 화면이 멈추었거나 반응이 없는 것처럼 느껴지며, 이로 인해 앱 사용에 불편함을 느끼게 됩니다. 이러한 사용자 경험을 개선하기 위해 오늘은 `NVActivityIndicatorView` 라이브러리를 사용하여 로딩 인디케이터를 구현해 보겠습니다.

## 1. NVActivityIndicatorView란?

NVActivityIndicatorView는 앱의 데이터 로딩 중에 활발한 동작을 시각적으로 보여주는 라이브러리입니다. 이 라이브러리는 다양한 모양과 색상의 로딩 인디케이터를 제공하며, 사용하기 쉽고 커스터마이징도 용이합니다.

## 2. NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 설치하기 위해서는 CocoaPods를 사용해야 합니다. 프로젝트의 `Podfile`에 다음과 같이 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령을 실행하여 라이브러리를 설치합니다:

```
$ pod install
```

## 3. NVActivityIndicatorView 사용하기

### 3.1. 인디케이터 추가하기

먼저, `NVActivityIndicatorView`를 원하는 화면에 추가해야 합니다. 인디케이터의 크기 및 위치를 지정하여 원하는 대로 배치할 수 있습니다. 예를 들어, `LoadingViewController`의 `viewDidLoad` 메서드에서 다음과 같이 인디케이터를 추가합니다:

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
        activityIndicatorView = NVActivityIndicatorView(frame: frame)
        activityIndicatorView.type = .circleStrokeSpin
        activityIndicatorView.color = .red
        activityIndicatorView.center = view.center
        view.addSubview(activityIndicatorView)
    }

    // ...
}
```

### 3.2. 인디케이터 시작 및 종료하기

이제 인디케이터를 시작하고 종료하는 방법을 알아보겠습니다. 예를 들어, 데이터를 로딩하는 동안 인디케이터를 표시하고, 로딩이 완료되면 인디케이터를 숨기는 동작을 수행하는 `startLoading` 및 `stopLoading` 메서드를 추가합니다:

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // ...

        startLoading() // 인디케이터 시작
        fetchData { result in
            // 데이터 로딩 완료
            self.stopLoading() // 인디케이터 종료
            if let data = result {
                // 데이터 사용
            } else {
                // 데이터 사용 실패
            }
        }
    }

    func startLoading() {
        activityIndicatorView.startAnimating()
    }

    func stopLoading() {
        activityIndicatorView.stopAnimating()
    }

    // ...
}
```

## 4. 마무리

NVActivityIndicatorView를 사용하여 앱의 UI를 개선할 수 있습니다. 이 라이브러리는 다양한 로딩 인디케이터를 제공하므로, 앱의 디자인에 맞게 커스텀할 수 있습니다. 사용자 경험을 향상시키기 위해 NVActivityIndicatorView를 사용해 보세요!

---

참고 문서:
- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)