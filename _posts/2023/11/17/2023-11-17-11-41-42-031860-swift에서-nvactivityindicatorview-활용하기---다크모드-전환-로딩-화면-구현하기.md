---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 활용하기 - 다크모드 전환 로딩 화면 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱에서 사용자에게 로딩 중임을 알리는 화면을 구현하려면 많은 작업이 필요합니다. 이러한 로딩 화면을 구현하기 위해 NVActivityIndicatorView 라이브러리를 사용할 수 있습니다. 이 블로그 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 다크모드 전환 로딩 화면을 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 로딩 표시기 라이브러리입니다. 이 라이브러리는 다양한 로딩 표시기 스타일을 제공하며, 커스터마이징이 가능합니다. NVActivityIndicatorView는 iOS, watchOS, tvOS를 지원하며, Swift 3.0 이상 버전을 필요로 합니다. 

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. 

```swift
pod 'NVActivityIndicatorView'
```

터미널을 열고 프로젝트의 경로로 이동한 다음, `pod install` 명령을 실행하여 NVActivityIndicatorView를 설치합니다.

## NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 화면에 NVActivityIndicatorView를 추가합니다. 

```swift
// NVActivityIndicatorView 인스턴스 생성
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: 0)

// 화면 중앙에 표시하기 위해 위치 설정
activityIndicatorView.center = view.center

// NVActivityIndicatorView를 화면에 추가
view.addSubview(activityIndicatorView)
```

3. 로딩 화면 표시 및 숨기기

```swift
// 로딩 화면 표시
activityIndicatorView.startAnimating()

// 로딩 화면 숨기기
activityIndicatorView.stopAnimating()
```

4. 다크모드 전환에 대응하기

NVActivityIndicatorView는 다크모드에 대응하기 위해 `overrideUserInterfaceStyle` 속성을 사용합니다. 이를 통해 다크모드 전환이 발생할 때 로딩 표시기의 색상을 업데이트할 수 있습니다.

```swift
// 다크모드 전환에 대한 옵저버 등록
NotificationCenter.default.addObserver(self, selector: #selector(onUserInterfaceStyleDidChange), name: UIApplication.didChangeUserInterfaceStyleNotification, object: nil)

// 다크모드 전환 콜백 메서드
@objc private func onUserInterfaceStyleDidChange() {
    // 다크모드인 경우, 로딩 표시기 색상 변경
    if traitCollection.userInterfaceStyle == .dark {
        activityIndicatorView.color = .white
    } else {
        activityIndicatorView.color = .gray
    }
}
```

## 마무리

Swift에서 NVActivityIndicatorView를 사용하여 다크모드 전환 로딩 화면을 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 통해 로딩 화면을 간단하고 유연하게 구현할 수 있으며, 다크모드 전환에도 쉽게 대응할 수 있습니다. 

더 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하시기 바랍니다.