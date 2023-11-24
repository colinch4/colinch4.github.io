---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 인터페이스 개선 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 목차
- [NVActivityIndicatorView 소개](#NVActivityIndicatorView-소개)
- [사용자 인터페이스 개선을 위한 NVActivityIndicatorView 사용하기](#사용자-인터페이스-개선을-위한-NVActivityIndicatorView-사용하기)
- [코드 예시](#코드-예시)
- [참고 자료](#참고-자료)

## NVActivityIndicatorView 소개
NVActivityIndicatorView는 iOS 애플리케이션에서 로딩 인디케이터(로딩 스피너)를 구현하기 위한 라이브러리입니다. 이 라이브러리를 사용하면 간단하게 로딩 인디케이터를 추가하여 사용자에게 작업이 진행 중임을 시각적으로 알릴 수 있습니다. NVActivityIndicatorView는 다양한 스타일과 컬러를 제공하며, 커스터마이징할 수 있습니다.

## 사용자 인터페이스 개선을 위한 NVActivityIndicatorView 사용하기
1. 먼저, NVActivityIndicatorView 라이브러리를 프로젝트에 추가합니다. CocoaPods를 사용할 경우, Podfile에 다음과 같이 추가합니다:
```swift
pod 'NVActivityIndicatorView'
```

2. NVActivityIndicatorView를 사용할 뷰 컨트롤러에서 import문을 추가합니다:
```swift
import NVActivityIndicatorView
```

3. NVActivityIndicatorView를 초기화하고 뷰에 추가할 준비를 합니다:
```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
activityIndicatorView.color = .gray // 로딩 스피너의 컬러 설정
activityIndicatorView.type = .ballSpinFadeLoader // 로딩 스피너의 스타일 설정
self.view.addSubview(activityIndicatorView)
```

4. 로딩 인디케이터를 시작하거나 중지할 때, 해당 메소드를 호출합니다:
```swift
// 로딩 인디케이터 시작
activityIndicatorView.startAnimating()

// 로딩 인디케이터 중지
activityIndicatorView.stopAnimating()
```

## 코드 예시
```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {
    
    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))

    override func viewDidLoad() {
        super.viewDidLoad()
        
        activityIndicatorView.color = .gray
        activityIndicatorView.type = .ballSpinFadeLoader
        self.view.addSubview(activityIndicatorView)
    }
    
    func startLoading() {
        activityIndicatorView.startAnimating()
    }
    
    func stopLoading() {
        activityIndicatorView.stopAnimating()
    }
}
```

## 참고 자료
- [NVActivityIndicatorView GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView CocoaPods 페이지](https://cocoapods.org/pods/NVActivityIndicatorView)