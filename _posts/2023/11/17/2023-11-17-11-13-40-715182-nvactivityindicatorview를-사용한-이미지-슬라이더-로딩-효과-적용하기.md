---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 이미지 슬라이더 로딩 효과 적용하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번에는 Swift로 개발 중인 앱에서 이미지 슬라이더에 로딩 효과를 적용하는 방법을 알아보겠습니다. 우리는 NVActivityIndicatorView라는 라이브러리를 사용하여 간단하고 멋진 로딩 효과를 구현할 것입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 효과를 구현하기 위한 오픈소스 라이브러리입니다. 다양한 모양과 색상의 로딩 인디케이터를 제공하여 앱에 사용자 친화적인 로딩 화면을 만들 수 있습니다. 

## 시작하기

1. 먼저 [CocoaPods](https://cocoapods.org/)를 사용하여 프로젝트에 NVActivityIndicatorView를 설치합니다. 

```swift
pod 'NVActivityIndicatorView'
```

2. Podfile에서 설치한 후 터미널에서 `pod install`을 실행하여 종속성을 설치합니다. 

3. Xcode를 열고 앱 프로젝트의 `ViewController.swift` 파일을 엽니다.

4. `ViewController` 클래스 상단에 다음과 같이 NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

5. `ViewController` 클래스에 NVActivityIndicatorView의 인스턴스 변수를 추가합니다.

```swift
var activityIndicatorView: NVActivityIndicatorView!
```

6. `viewDidLoad` 함수에서 NVActivityIndicatorView를 초기화하고 설정합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    // NVActivityIndicatorView 초기화
    let frame = CGRect(x: view.frame.width / 2 - 25, y: view.frame.height / 2 - 25, width: 50, height: 50)
    activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballBeat, color: .systemBlue, padding: nil)
    view.addSubview(activityIndicatorView)
}
```

7. 이미지 슬라이더가 로딩되는 동안 로딩 효과를 표시하기 위해 `viewDidAppear` 함수에서 NVActivityIndicatorView를 시작합니다.

```swift
override func viewDidAppear(_ animated: Bool) {
    super.viewDidAppear(animated)
    
    // 로딩 효과 시작
    activityIndicatorView.startAnimating()
    
    // 이미지 슬라이더 로딩
    loadImageSliderData()
}
```

8. 이미지 슬라이더 데이터를 로딩하는 `loadImageSliderData` 함수에서 이미지 슬라이더 데이터를 가져온 후에는 NVActivityIndicatorView를 중지시킵니다.

```swift
func loadImageSliderData() {
    // 이미지 슬라이더 데이터 로딩 후 작업
    
    // 로딩 효과 중지
    activityIndicatorView.stopAnimating()
}
```

## 결론

이제 NVActivityIndicatorView를 사용하여 이미지 슬라이더에 멋진 로딩 효과를 적용하는 방법을 알아보았습니다. NVActivityIndicatorView를 사용하면 사용자들에게 로딩 중임을 시각적으로 알려주어 더 좋은 사용자 경험을 제공할 수 있습니다.