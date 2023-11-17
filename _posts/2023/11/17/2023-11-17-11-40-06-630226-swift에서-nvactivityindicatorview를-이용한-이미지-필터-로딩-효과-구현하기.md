---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 이용한 이미지 필터 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이미지 처리 및 필터링은 iOS 애플리케이션에서 자주 사용되는 기능입니다. 사용자가 이미지를 선택하고, 필터를 적용하고, 결과를 보기를 기다리는 동안 로딩 효과를 제공하는 것은 좋은 사용자 경험을 위해 중요합니다.

이번 튜토리얼에서는 Swift에서 NVActivityIndicatorView 라이브러리를 사용하여 이미지 필터 로딩 효과를 구현하는 방법을 알아보겠습니다. NVActivityIndicatorView는 로딩 인디케이터를 간단하게 구현할 수 있는 좋은 오픈 소스 라이브러리입니다.

## 1. NVActivityIndicatorView 설치하기

우선, NVActivityIndicatorView를 프로젝트에 설치해야 합니다. 가장 간단한 방법은 CocoaPods를 사용하는 것입니다. Podfile에 다음과 같이 작성하세요.

```ruby
pod 'NVActivityIndicatorView'
```

그런 다음, 터미널에서 프로젝트 루트 디렉토리로 이동하여 다음 명령어를 실행하세요.

```sh
pod install
```

## 2. NVActivityIndicatorView 사용하기

2-1. 필요한 클래스와 라이브러리를 import합니다.

```swift
import UIKit
import NVActivityIndicatorView
```

2-2. 사용할 인디케이터 스타일과 크기를 선택합니다. NVActivityIndicatorView에는 다양한 스타일이 제공되며, 상황에 맞게 선택할 수 있습니다. 예를 들어, .ballPulse 스타일과 .medium 크기를 사용할 수 있습니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .gray, padding: nil)
```

2-3. 이미지 필터가 적용되는 동안 로딩 효과를 보여주기 위해 필터링 메소드를 호출하기 전에 인디케이터를 추가하고 시작합니다.

```swift
func applyFilter(to image: UIImage) {
    // 이미지 필터 로딩 효과를 보여주기 위해 인디케이터를 추가합니다.
    view.addSubview(indicatorView)
    indicatorView.center = view.center
    indicatorView.startAnimating()
    
    // 이미지 필터링 작업을 수행합니다.
    // 필터링 작업이 완료되면 로딩 효과를 중지하고 결과를 표시합니다.
    // ...
}
```

2-4. 이미지 필터링 작업이 완료되면 인디케이터를 중지하고 화면에서 제거합니다.

```swift
func applyFilter(to image: UIImage) {
    // ...
    
    // 이미지 필터링 작업이 완료되면 로딩 효과를 중지하고 결과를 표시합니다.
    // ...
    
    // 인디케이터를 중지하고 화면에서 제거합니다.
    indicatorView.stopAnimating()
    indicatorView.removeFromSuperview()
}
```

## 3. 결과 확인하기

이제 이미지 필터링 로직을 적용한 후, NVActivityIndicatorView를 사용하여 로딩 효과를 구현할 준비가 되었습니다. 애플리케이션을 실행하여 이미지를 선택하고 로딩 효과를 확인하세요.

### 참고 자료

* [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)