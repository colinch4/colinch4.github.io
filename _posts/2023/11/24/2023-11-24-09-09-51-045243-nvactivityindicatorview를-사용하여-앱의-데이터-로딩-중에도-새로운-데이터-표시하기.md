---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 앱의 데이터 로딩 중에도 새로운 데이터 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱을 개발할 때 데이터를 로딩하는 동안 사용자에게 로딩 중임을 알려주는 인디케이터가 필요할 수 있습니다. NVActivityIndicatorView는 Swift로 작성된 iOS 앱에서 동작하는 인디케이터 뷰입니다. 이 라이브러리를 사용하여 앱의 데이터 로딩 중에도 새로운 데이터를 표시할 수 있습니다.

## NVActivityIndicatorView 설치

먼저, NVActivityIndicatorView를 프로젝트에 설치해야 합니다. CocoaPods를 사용하고 있다면 Podfile에 아래의 코드를 추가합니다.

```
pod 'NVActivityIndicatorView'
```

그런 다음 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

CocoaPods를 사용하지 않고 수동으로 설치하려는 경우, [GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)에서 라이브러리를 다운로드하고 프로젝트에 직접 추가하면 됩니다.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import합니다.
```swift
import NVActivityIndicatorView
```

2. 뷰 컨트롤러에 인디케이터를 추가하고 시작하는 코드를 작성합니다.

```swift
class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 인디케이터 뷰 초기화
        activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRipple, color: .red, padding: nil)

        // 인디케이터 위치 설정
        activityIndicatorView.center = view.center

        // 인디케이터 뷰를 서브뷰로 추가
        view.addSubview(activityIndicatorView)
    }

    // 데이터 로딩 시작 시 호출하는 함수
    func startLoading() {
        activityIndicatorView.startAnimating()
    }

    // 데이터 로딩 완료 시 호출하는 함수
    func stopLoading() {
        activityIndicatorView.stopAnimating()
    }
}
```

3. 데이터를 로딩하는 동안 `startLoading()` 함수를 호출하여 인디케이터를 시작하고, 데이터 로딩이 완료된 후 `stopLoading()` 함수를 호출하여 인디케이터를 중지합니다.

```swift
startLoading()

// 데이터 로딩 코드 작성

stopLoading()
```

NVActivityIndicatorView를 사용하면 앱의 데이터 로딩 중에도 사용자에게 로딩 중임을 알려줄 수 있습니다. 이를 통해 사용자는 데이터 로딩이 진행 중임을 이해하고, 동시에 새로운 데이터를 제공할 수 있는 앱을 만들 수 있습니다.

---
참고문헌:
- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)