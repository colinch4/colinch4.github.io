---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 터치 이벤트 중 로딩 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 개요
이번 블로그 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 터치 이벤트 중 로딩 상태를 표시하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 Swift에서 사용할 수 있는 로딩 인디케이터 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하며, 사용하기 간편하고 커스터마이징할 수 있는 특징을 가지고 있습니다.

## NVActivityIndicatorView 설치
NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다.
```
pod 'NVActivityIndicatorView'
```

## 로딩 상태 표시하기
1. NVActivityIndicatorView를 import 합니다.
```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 사용할 View를 생성합니다. 예를 들어, UIButton을 생성해보겠습니다.
```swift
let button = UIButton(frame: CGRect(x: 100, y: 100, width: 200, height: 50))
button.setTitle("로딩 시작", for: .normal)
button.addTarget(self, action: #selector(startLoading), for: .touchUpInside)

self.view.addSubview(button)
```

3. 로딩 시작을 위한 Selector 함수를 작성합니다. 이 함수에서 NVActivityIndicatorView를 생성하고 시작하도록 구현하겠습니다.
```swift
@objc func startLoading() {
    // NVActivityIndicatorView 생성
    let activityIndicatorView = NVActivityIndicatorView(frame: self.view.bounds,
                                                        type: .ballSpinFadeLoader,
                                                        color: .green,
                                                        padding: 50)
    
    // View에 추가
    self.view.addSubview(activityIndicatorView)
    
    // NVActivityIndicatorView 시작
    activityIndicatorView.startAnimating()
    
    // 터치 이벤트 중 로딩 상태를 표시하기 위해 터치 이벤트를 막아줍니다.
    button.isUserInteractionEnabled = false
}
```

4. 로딩이 끝났을 때, NVActivityIndicatorView를 제거하고 터치 이벤트를 다시 활성화해야 합니다. 이를 위해 로딩이 끝났을 때 호출되는 함수를 구현합니다.
```swift
func loadingFinished() {
    // NVActivityIndicatorView 제거
    activityIndicatorView.removeFromSuperview()
    
    // 터치 이벤트 다시 활성화
    button.isUserInteractionEnabled = true
}
```

위와 같이 NVActivityIndicatorView를 사용하여 터치 이벤트 중 로딩 상태를 표시할 수 있습니다.

## 결론
이번 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 터치 이벤트 중 로딩 상태를 표시하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하여 간편하게 로딩 인디케이터를 구현할 수 있고, 터치 이벤트 중 로딩 상태를 표시하는 경우 유용하게 사용할 수 있습니다.