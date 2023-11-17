---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 스케줄 관리 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 개요

이 글에서는 NVActivityIndicatorView라는 라이브러리를 사용하여 스케줄 관리 애플리케이션에서 로딩 효과를 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 애플리케이션에서 간편하게 사용할 수 있는 로딩 효과를 제공하는 오픈 소스 라이브러리입니다. 다양한 스타일, 색상 및 크기의 로딩 효과를 제공하여 사용자에게 재미있는 로딩 화면을 구현할 수 있습니다.

## 필요한 준비물

1. Xcode 프로젝트
2. CocoaPods (라이브러리 관리 도구)
3. NVActivityIndicatorView 라이브러리

## 설치

1. `pod init` 명령어를 사용하여 Podfile을 생성합니다.
2. Podfile에 다음 코드를 추가하고 저장합니다.

```ruby
pod 'NVActivityIndicatorView'
```

3. `pod install` 명령어를 사용하여 라이브러리를 설치합니다.

## 구현 방법

1. Xcode 프로젝트를 열고 적절한 위치에 .xib 또는 .storyboard 파일을 추가합니다.
2. 추가한 파일을 선택한 후, Identity Inspector에서 Custom Class를 `NVActivityIndicatorView`로 설정합니다.
3. 스타일, 색상 및 크기를 원하는 대로 설정합니다.

### 예시 코드

```swift
import NVActivityIndicatorView

class ViewController: UIViewController {

    var activityIndicatorView: NVActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 로딩 효과를 표시할 위치와 크기를 정의합니다.
        let frame = CGRect(x: 0, y: 0, width: 100, height: 100)
        
        // 로딩 효과의 스타일 및 색상을 설정합니다.
        let activityIndicatorStyle = NVActivityIndicatorType.circleStrokeSpin
        let activityIndicatorColor = UIColor.red
        
        // NVActivityIndicatorView 인스턴스를 생성합니다.
        activityIndicatorView = NVActivityIndicatorView(frame: frame, type: activityIndicatorStyle, color: activityIndicatorColor)
        
        // 로딩 효과를 표시할 위치를 지정합니다.
        activityIndicatorView.center = view.center
        
        // 뷰에 로딩 효과를 추가합니다.
        view.addSubview(activityIndicatorView)
    }

    // 로딩 효과를 표시하거나 숨기는 함수를 구현합니다.
    func showActivityIndicator() {
        activityIndicatorView.startAnimating()
    }

    func hideActivityIndicator() {
        activityIndicatorView.stopAnimating()
    }

    // 예시로 버튼 액션에 로딩 효과를 추가하는 코드를 작성합니다.
    @IBAction func startButtonTapped(_ sender: UIButton) {
        showActivityIndicator()
        
        // 여기에 로딩이 필요한 작업을 수행합니다.
        
        hideActivityIndicator()
    }
}
```

## 마무리

이제 NVActivityIndicatorView를 사용하여 스케줄 관리 애플리케이션에서 로딩 효과를 구현할 수 있게 되었습니다. 위의 예시 코드를 참고하여 애플리케이션에 로딩 효과를 추가해 보세요.

## 참고 자료

- NVActivityIndicatorView GitHub 레포지토리: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)
- CocoaPods 웹사이트: [https://cocoapods.org/](https://cocoapods.org/)