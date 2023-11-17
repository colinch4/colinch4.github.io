---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 활용하기 - 할일 목록 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

로딩 화면은 사용자의 경험을 향상시키는 데 일반적으로 사용되는 기능입니다. Swift 언어에서 NVActivityIndicatorView 라이브러리를 사용하여 할일 목록 로딩 화면을 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift에서 로딩 인디케이터를 쉽게 구현할 수 있는 라이브러리입니다. 이 라이브러리는 다양한 모양의 로딩 인디케이터를 제공하며, 간편한 사용 방법으로 다른 UI 요소들과 쉽게 통합할 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 이용하여 설치해야 합니다. `Podfile`을 열고 다음과 같이 NVActivityIndicatorView를 추가해주세요:

```swift
pod 'NVActivityIndicatorView'
```

설치가 완료되면 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 다운로드하고 프로젝트에 적용해주세요.

## 사용 방법

1. NVActivityIndicatorView를 import 해주세요.

```swift
import NVActivityIndicatorView
```

2. 인디케이터를 추가할 UIView를 생성합니다.

```swift
let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))
loadingView.center = self.view.center
view.addSubview(loadingView)
```

3. NVActivityIndicatorView를 초기화하고 인디케이터 모양과 색상을 설정합니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .gray, padding: nil)
loadingView.addSubview(indicatorView)
```

4. 인디케이터를 시작하고 멈추는 메서드를 이용하여 로딩 화면을 표시 및 숨김 처리합니다.

```swift
indicatorView.startAnimating() // 로딩 화면 표시

indicatorView.stopAnimating() // 로딩 화면 숨김 처리
```

## 할일 목록 로딩 화면 구현하기

이제 NVActivityIndicatorView를 사용하여 할일 목록 로딩 화면을 구현할 수 있습니다. 예를 들어, 할일 목록을 불러오는 동안 로딩 화면을 표시하고, 데이터가 로드되면 화면을 업데이트하는 방법은 다음과 같습니다.

```swift
import NVActivityIndicatorView

class TodoViewController: UIViewController {
    let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))
    let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRippleMultiple, color: .gray, padding: nil)

    override func viewDidLoad() {
        super.viewDidLoad()

        loadingView.center = self.view.center
        view.addSubview(loadingView)

        indicatorView.center = CGPoint(x: loadingView.bounds.midX, y: loadingView.bounds.midY)
        loadingView.addSubview(indicatorView)

        startLoading()

        // 할일 목록을 불러와서 데이터 업데이트

        stopLoading()
    }

    func startLoading() {
        indicatorView.startAnimating()
        loadingView.isHidden = false
    }

    func stopLoading() {
        indicatorView.stopAnimating()
        loadingView.isHidden = true
    }
}
```

위의 코드는 `loadingView`와 `indicatorView`를 생성하고, `startLoading()`과 `stopLoading()` 메서드를 이용하여 로딩 화면을 표시 및 숨김 처리하는 방법을 보여줍니다. 실제로 할일 목록을 데이터베이스 등에서 불러올 때 로딩 화면을 활용하여 사용자에게 대기 상태임을 알리고 UX를 개선할 수 있습니다.

## 결론

Swift에서 NVActivityIndicatorView를 활용하여 할일 목록 로딩 화면을 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 다양한 로딩 인디케이터를 제공하며, 간편한 사용 방법으로 로딩 화면을 구현할 수 있습니다. 이를 통해 사용자 경험을 향상시킬 수 있습니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)