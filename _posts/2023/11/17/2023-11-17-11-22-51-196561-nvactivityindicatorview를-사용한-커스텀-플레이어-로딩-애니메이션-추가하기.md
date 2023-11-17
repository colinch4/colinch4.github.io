---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 커스텀 플레이어 로딩 애니메이션 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift에서 NVActivityIndicatorView를 사용하여 커스텀 플레이어 로딩 애니메이션을 추가하는 방법에 대해 알아보겠습니다.

NVActivityIndicatorView는 iOS에서 사용할 수 있는 강력한 로딩 애니메이션 라이브러리입니다. 이 라이브러리는 여러 가지 스타일의 로딩 애니메이션을 제공하며, 커스텀 로딩 애니메이션을 만들 수도 있습니다.

## NVActivityIndicatorView 설치하기

먼저, NVActivityIndicatorView를 프로젝트에 추가해야 합니다. Cocoapods를 사용하신다면, Podfile에 다음과 같이 추가해주세요:

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install`을 실행하여 라이브러리를 설치하세요.

만약 Cocoapods를 사용하지 않는다면, 해당 라이브러리의 GitHub 저장소에서 수동으로 다운로드하여 프로젝트에 추가할 수도 있습니다.

## 커스텀 플레이어 로딩 애니메이션 추가하기

1. 먼저, NVActivityIndicatorView를 import합니다:

```swift
import NVActivityIndicatorView
```

2. 다음으로, 로딩 애니메이션을 추가할 뷰를 생성합니다. 예를 들어, UIView의 서브뷰로 추가할 수 있습니다:

```swift
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
loadingView.color = .white
loadingView.type = .ballRotateChase
```

위의 코드에서 `frame`은 로딩 애니메이션의 크기 및 위치를 지정하고, `color`는 애니메이션 색상을 설정합니다. `type`은 로딩 애니메이션 스타일을 설정하는데, 위의 예시에서는 `ballRotateChase` 스타일을 사용하였습니다.

3. 로딩 애니메이션을 시작하고 멈추는 메소드를 추가합니다:

```swift
func startLoading() {
    loadingView.startAnimating()
    // 로딩 애니메이션을 추가한 뷰를 보여주는 코드를 작성하세요
}

func stopLoading() {
    loadingView.stopAnimating()
    // 로딩 애니메이션을 추가한 뷰를 숨기는 코드를 작성하세요
}
```

위의 메소드들은 로딩 애니메이션을 시작하고 멈추는 기능을 구현합니다. `startLoading` 메소드는 로딩 애니메이션을 시작하고, `stopLoading` 메소드는 로딩 애니메이션을 멈춥니다. 이 코드들을 알맞은 장소에 추가하여 사용할 수 있습니다.

4. 마지막으로, 플레이어나 웹뷰 등 사용자에게 로딩 상태를 보여줄 때 로딩 애니메이션을 추가합니다. 예를 들어, 플레이어 컨트롤러의 `viewDidLoad` 메소드에서 로딩 애니메이션을 추가할 수 있습니다:

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    // 플레이어 뷰를 초기화하는 코드를 작성하세요

    // 로딩 애니메이션을 추가한 뷰를 생성하여 플레이어 뷰에 추가합니다
    let loadingView = createLoadingView()
    playerView.addSubview(loadingView)
    loadingView.center = playerView.center

    // 로딩 애니메이션을 시작합니다
    startLoading()
}
```

위의 예시에서는 `createLoadingView()` 메소드로 로딩 애니메이션을 포함한 뷰를 생성하고, 플레이어 뷰에 해당 뷰를 추가한 후 로딩 애니메이션을 시작하고 있습니다.

## 마무리

위에서 설명한 방법을 따라 NVActivityIndicatorView를 사용하여 커스텀 플레이어 로딩 애니메이션을 손쉽게 추가할 수 있습니다. 다양한 스타일과 옵션을 활용하여 원하는 로딩 애니메이션을 만들어보세요!

더 자세한 내용은 [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView) 저장소를 참고해주세요.