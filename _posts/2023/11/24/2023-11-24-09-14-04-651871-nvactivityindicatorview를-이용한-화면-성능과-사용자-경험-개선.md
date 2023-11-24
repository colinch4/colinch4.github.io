---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 화면 성능과 사용자 경험 개선"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 소개
앱 개발의 핵심 목표 중 하나는 원활한 화면 전환과 사용자 경험을 제공하는 것입니다. 특히, 네트워크 요청이나 데이터 처리와 같은 작업이 오래 걸릴 수 있는 경우에는 화면을 멋지게 로딩하는 것이 중요합니다. 이를 위해 NVActivityIndicatorView라는 라이브러리를 소개하고자 합니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 Swift로 구현된 오픈소스 라이브러리로, 다양한 유형의 로딩 인디케이터를 제공합니다. 이 라이브러리는 화면 로딩 중에 사용자에게 진행 중임을 시각적으로 알려주는 역할을 합니다. 또한, 맞춤 설정 가능한 디자인과 애니메이션 기능을 제공하여 원하는 스타일의 로딩 인디케이터를 만들 수 있습니다.

## 설치
NVActivityIndicatorView를 사용하기 위해서는 CocoaPods를 통해 프로젝트에 라이브러리를 추가해야 합니다. Podfile에 다음을 추가한 후, `pod install` 명령어를 실행합니다.

```swift
pod 'NVActivityIndicatorView'
```

## 사용법
1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 인디케이터를 추가할 View를 생성합니다.

```swift
let loaderView = UIView(frame: CGRect(x: 0, y: 0, width: 80, height: 80))
view.addSubview(loaderView)
loaderView.center = view.center
```

3. NVActivityIndicatorView 인스턴스를 생성하고 초기 설정을 합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 60, height: 60), type: .circleStrokeSpin, color: .gray, padding: 0)
loaderView.addSubview(activityIndicatorView)
```

4. 인디케이터를 화면에 보여주거나 숨기는 동작을 처리합니다.

```swift
// 인디케이터 표시
activityIndicatorView.startAnimating()

// 인디케이터 숨김
activityIndicatorView.stopAnimating()
```

## 예제
다음은 NVActivityIndicatorView를 사용하여 로딩 인디케이터를 추가하는 예제 코드입니다.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {
    
    let loaderView = UIView(frame: CGRect(x: 0, y: 0, width: 80, height: 80))
    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 60, height: 60), type: .circleStrokeSpin, color: .gray, padding: 0)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 인디케이터 설정
        activityIndicatorView.center = loaderView.center
        loaderView.addSubview(activityIndicatorView)
        
        // 뷰에 로딩 인디케이터를 추가
        view.addSubview(loaderView)
        
        // 화면 중앙에 위치
        loaderView.center = view.center
    }
    
    func showLoader() {
        activityIndicatorView.startAnimating()
    }
    
    func hideLoader() {
        activityIndicatorView.stopAnimating()
    }
}
```

## 결론
NVActivityIndicatorView를 통해 로딩 인디케이터를 화면에 추가하고, 사용자에게 작업이 진행 중임을 시각적으로 알려줄 수 있습니다. 이를 통해 앱의 화면 성능과 사용자 경험을 개선할 수 있습니다.

## 참고 자료
- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)