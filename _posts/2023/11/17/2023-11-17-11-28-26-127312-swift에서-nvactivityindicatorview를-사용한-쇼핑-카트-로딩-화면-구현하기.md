---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용한 쇼핑 카트 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

쇼핑 앱에서 로딩 화면은 사용자에게 작업이 진행 중임을 알려주는 중요한 요소입니다. NVActivityIndicatorView는 Swift에서 사용할 수 있는 간단하고 유연한 로딩 인디케이터입니다. 이번 튜토리얼에서는 Swift에서 NVActivityIndicatorView를 사용하여 쇼핑 카트 로딩 화면을 구현하는 방법을 알아보겠습니다.

## Step 1: 프로젝트에 NVActivityIndicatorView 추가하기

먼저, 프로젝트에 NVActivityIndicatorView를 추가해야 합니다. 이를 위해 Cocoapods를 사용하겠습니다. 프로젝트 폴더에서 다음 명령어를 실행하여 Podfile을 생성합니다.

```bash
pod init
```

Podfile을 열고, 다음 줄을 추가하여 NVActivityIndicatorView를 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

터미널에서 다음 명령어를 실행하여 CocoaPods를 설치합니다.

```bash
pod install
```

## Step 2: NVActivityIndicatorView로 로딩 화면 구현하기

이제 NVActivityIndicatorView를 사용하여 로딩 화면을 구현할 수 있습니다. 먼저, 로딩 화면을 표시할 UIView를 생성합니다. 이를 위해 storyboard에서 UIView를 추가하거나 코드로 UIView를 생성할 수 있습니다.

```swift
import UIKit
import NVActivityIndicatorView

class LoadingViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // NVActivityIndicatorView 설정
        let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
        loadingView.center = view.center
        loadingView.type = .ballSpinFadeLoader
        loadingView.color = .gray

        // 로딩 화면 표시
        view.addSubview(loadingView)
        loadingView.startAnimating()
    }

}
```

NVActivityIndicatorView의 `frame` 속성을 사용하여 로딩 인디케이터의 크기와 위치를 설정합니다. `type` 속성으로 로딩 인디케이터의 스타일을 선택할 수 있으며, `color` 속성으로 로딩 인디케이터의 색상을 지정할 수 있습니다.

이제 쇼핑 카트 화면에서 로딩 화면을 표시하기 위해 다음 코드를 추가합니다.

```swift
let loadingVC = LoadingViewController()
addChild(loadingVC)
loadingVC.view.frame = view.frame
view.addSubview(loadingVC.view)
loadingVC.didMove(toParent: self)
```

로딩 화면을 표시할 때에는 `LoadingViewController`를 자식 뷰 컨트롤러로 추가하고, `view`를 적절한 위치에 추가합니다.

## 요약

NVActivityIndicatorView를 사용하면 Swift에서 간단하고 유연한 쇼핑 카트 로딩 화면을 구현할 수 있습니다. 이 튜토리얼에서는 Cocoapods를 사용하여 NVActivityIndicatorView를 프로젝트에 추가한 후, 앱에서 로딩 화면을 표시하는 방법을 알아보았습니다. 쇼핑 앱에서 사용자 경험을 향상시키기 위해 NVActivityIndicatorView를 활용해보세요.

## 참고 자료

- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)
- [CocoaPods](https://cocoapods.org/)