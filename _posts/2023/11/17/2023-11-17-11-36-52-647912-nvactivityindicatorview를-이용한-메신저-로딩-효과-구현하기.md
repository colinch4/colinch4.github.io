---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 메신저 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번에는 Swift 언어에서 NVActivityIndicatorView를 사용하여 메신저 로딩 효과를 구현하는 방법에 대해 알아보겠습니다. 

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 효과를 구현하기 위한 오픈 소스 라이브러리입니다. 다양한 종류의 로딩 애니메이션을 제공하며, 스피너의 크기, 색상 및 스타일을 설정할 수 있습니다.

## 설치

NVActivityIndicatorView를 사용하기 위해선 먼저 CocoaPods를 이용하여 라이브러리를 프로젝트에 추가해야 합니다. 

```swift
pod 'NVActivityIndicatorView'
```

프로젝트 경로에 Podfile을 생성한 후, 위의 코드를 추가하고 터미널에서 `pod install` 명령어를 실행합니다. 

## 사용 방법

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .white, padding: nil)
```

- frame: NVActivityIndicatorView의 위치 및 크기를 설정합니다.
- type: 로딩 애니메이션의 스타일을 설정합니다.
- color: 로딩 애니메이션의 색상을 설정합니다.
- padding: 로딩 애니메이션의 여백을 설정합니다. (nil일 경우 기본값 사용)

3. NVActivityIndicatorView를 화면에 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
```

4. NVActivityIndicatorView의 애니메이션을 시작하거나 중지합니다.

```swift
activityIndicatorView.startAnimating()  // 애니메이션 시작
activityIndicatorView.stopAnimating()   // 애니메이션 중지
```

## 예제

다음은 메신저 앱에서 메시지를 전송하는 동안 로딩 효과를 보여주는 예제입니다.

```swift
import UIKit
import NVActivityIndicatorView

class ViewController: UIViewController {

    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .white, padding: nil)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.addSubview(activityIndicatorView)
        activityIndicatorView.center = view.center
    }

    @IBAction func sendMessageButtonTapped(_ sender: UIButton) {
        // 메시지 전송 버튼을 탭했을 때
        startLoadingAnimation()
        
        // 메시지 전송 로직
        
        DispatchQueue.main.asyncAfter(deadline: .now() + 3) {
            self.stopLoadingAnimation()
            // 메시지 전송 완료 후 로직
        }
    }
    
    private func startLoadingAnimation() {
        activityIndicatorView.startAnimating()
    }
    
    private func stopLoadingAnimation() {
        activityIndicatorView.stopAnimating()
    }
}
```

## 마치며

이번에는 NVActivityIndicatorView를 이용하여 메신저 로딩 효과를 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하면 앱에 다양하고 멋진 로딩 애니메이션을 손쉽게 추가할 수 있습니다. 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하세요.