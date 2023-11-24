---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 비동기 작업 처리 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

비동기 작업을 수행할 때 사용자에게 작업이 진행 중임을 알리는 것은 중요합니다. NVActivityIndicatorView는 Swift에서 비동기 작업 처리 상태를 표시하는 데 유용한 라이브러리입니다. 이 블로그 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 비동기 작업 처리 상태를 표시하는 방법을 소개하겠습니다.

## NVActivityIndicatorView란 무엇인가?

NVActivityIndicatorView는 로딩 애니메이션을 표시하는 데 사용되는 오픈 소스 라이브러리입니다. 이 라이브러리는 다양한 로딩 스타일과 색상을 제공하며, 사용하기 쉬운 인터페이스를 제공합니다. NVActivityIndicatorView는 Cocoapods를 통해 설치할 수 있습니다. 설치 방법은 아래와 같습니다.

```swift
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용법

1. NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView 인스턴스를 생성합니다. 인스턴스는 UIView의 서브클래스로 생성할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

3. 필요에 따라 로딩 스타일과 색상을 설정할 수 있습니다.

```swift
activityIndicatorView.type = .circleStrokeSpin
activityIndicatorView.color = .red
```

4. NVActivityIndicatorView를 화면에 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
```

5. 비동기 작업을 시작하기 전에 NVActivityIndicatorView를 시작합니다.

```swift
activityIndicatorView.startAnimating()
```

6. 비동기 작업이 완료되면 NVActivityIndicatorView를 중지합니다.

```swift
activityIndicatorView.stopAnimating()
```

## 예제 코드

다음은 NVActivityIndicatorView를 사용하여 비동기 작업 처리 상태를 표시하는 예제 코드입니다.

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 스타일과 색상 설정
        activityIndicatorView.type = .circleStrokeSpin
        activityIndicatorView.color = .red

        // NVActivityIndicatorView를 화면에 추가
        view.addSubview(activityIndicatorView)
        activityIndicatorView.center = view.center
    }

    func startAsyncTask() {
        // 비동기 작업 시작 시 NVActivityIndicatorView 시작
        activityIndicatorView.startAnimating()

        // 비동기 작업 수행

        // 비동기 작업 완료 시 NVActivityIndicatorView 중지
        activityIndicatorView.stopAnimating()
    }

}
```

위의 코드에서 `startAsyncTask` 함수는 비동기 작업을 시작하고 완료된 후 NVActivityIndicatorView를 중지합니다.

## 결론

이렇게 Swift에서 NVActivityIndicatorView를 사용하여 비동기 작업 처리 상태를 표시할 수 있습니다. 해당 플러그인을 사용하면 사용자에게 작업이 진행 중임을 시각적으로 알리는 데 도움이 됩니다. NVActivityIndicatorView를 사용하여 앱의 사용자 경험을 향상시킬 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)