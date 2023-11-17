---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용한 가계부 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱의 사용자 경험을 향상시키기 위해 로딩 화면은 매우 중요합니다. NVActivityIndicatorView는 동적인 로딩 인디케이터를 구현하는 데 도움을 주는 강력한 라이브러리입니다. 이번 튜토리얼에서는 Swift에서 NVActivityIndicatorView를 사용하여 가계부 앱의 로딩 화면을 구현하는 방법에 대해 알아보겠습니다.

## 1. NVActivityIndicatorView 설치

NVActivityIndicatorView는 Cocoapods를 통해 설치할 수 있습니다. `Podfile`에 다음 라인을 추가하고 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

```swift
pod 'NVActivityIndicatorView'
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 우선 `NVActivityIndicatorView` 뷰를 생성해야 합니다. 로딩 화면이 표시되어야 하는 뷰 컨트롤러에 다음 코드를 추가합니다.

```swift
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 로딩 인디케이터 설정
        let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
        activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .circleStrokeSpin, color: .white, padding: 0)

        // 로딩 인디케이터 위치 설정
        activityIndicatorView.center = view.center

        // 로딩 인디케이터를 뷰에 추가
        view.addSubview(activityIndicatorView)
    }

    // 로딩 화면 표시
    func showLoadingScreen() {
        activityIndicatorView.startAnimating()
    }

    // 로딩 화면 숨기기
    func hideLoadingScreen() {
        activityIndicatorView.stopAnimating()
    }
}
```

## 3. 로딩 화면 사용 예제

이제 가계부 앱에서 로딩 화면을 사용하는 예제를 살펴보겠습니다.

```swift
import UIKit
import NVActivityIndicatorView

class HomeViewController: UIViewController {

    let loadingViewController = LoadingViewController()

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 화면을 뷰에 추가
        addChild(loadingViewController)
        loadingViewController.view.frame = view.bounds
        view.addSubview(loadingViewController.view)
        loadingViewController.didMove(toParent: self)
    }

    func fetchAccountData() {
        // 로딩 화면 표시
        loadingViewController.showLoadingScreen()
        
        // 가계부 데이터 가져오기
        // ...
        
        // 데이터 가져오기 완료 후 로딩 화면 숨기기
        loadingViewController.hideLoadingScreen()
    }
}
```

위 예제에서는 `HomeViewController`에 `LoadingViewController`를 추가하여 로딩 화면을 표시합니다. `fetchAccountData()` 메서드가 호출될 때, 로딩 화면을 표시하고 가계부 데이터를 가져온 후 로딩 화면을 숨깁니다.

## 마무리

이제 Swift에서 NVActivityIndicatorView를 사용하여 가계부 앱의 로딩 화면을 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 간편한 구현과 다양한 디자인 옵션을 제공하여 앱의 로딩 화면을 개선하기에 좋은 선택입니다. 자유롭게 라이브러리의 문서를 참조하여 다양한 설정과 사용법을 익히세요.

참고 링크:
- [NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)