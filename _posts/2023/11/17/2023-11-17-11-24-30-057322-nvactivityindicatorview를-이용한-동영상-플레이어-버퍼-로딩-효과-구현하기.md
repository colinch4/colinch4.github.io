---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 동영상 플레이어 버퍼 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 소개
동영상 플레이어 앱을 개발할 때, 사용자가 동영상을 로딩하는 동안 버퍼링 중임을 시각적으로 알려주는 효과는 매우 중요합니다. 이번 글에서는 NVActivityIndicatorView를 이용하여 동영상 플레이어의 버퍼 로딩 효과를 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 앱에서 다양한 로딩 효과를 구현할 수 있는 Swift 라이브러리입니다. 이 라이브러리는 다양한 스타일과 색상을 지원하며, 간단한 코드로 로딩 효과를 구현할 수 있습니다.

## NVActivityIndicatorView 설치
NVActivityIndicatorView를 사용하기 위해서는 먼저 CocoaPods를 이용하여 프로젝트에 라이브러리를 추가해야 합니다. 

1. 프로젝트 디렉터리에서 터미널을 열고 `pod init` 명령어를 실행하여 Podfile을 생성합니다.
2. Podfile을 열고 다음과 같이 작성합니다.

```
platform :ios, '9.0'
target 'YourTargetName' do
  use_frameworks!
  pod 'NVActivityIndicatorView'
end
```

3. 터미널에 `pod install` 명령어를 실행하여 라이브러리를 설치합니다. 

## NVActivityIndicatorView 사용법
NVActivityIndicatorView를 사용하기 위해 다음과 같은 단계를 따릅니다.

1. NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 효과를 추가할 뷰를 생성합니다. 예를 들어, 버퍼링 중임을 나타내는 로딩 효과를 추가하기 위해 UIView를 생성합니다.

```swift
let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

3. NVActivityIndicatorView를 초기화하고 로딩 효과를 설정합니다. 스타일과 색상을 선택할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .white, padding: nil)
```

4. 로딩 효과를 뷰에 추가합니다.

```swift
loadingView.addSubview(activityIndicatorView)
```

5. 로딩 효과를 시작하거나 중지합니다.

```swift
// 로딩 효과 시작
activityIndicatorView.startAnimating()

// 로딩 효과 중지
activityIndicatorView.stopAnimating()
```

## 예시 코드

```swift
import UIKit
import NVActivityIndicatorView

class VideoPlayerViewController: UIViewController {
    
    let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
    let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .white, padding: nil)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        loadingView.addSubview(activityIndicatorView)
        // 로딩 효과를 중앙에 위치시킴
        activityIndicatorView.center = loadingView.center
        
        // 로딩 효과를 시작
        activityIndicatorView.startAnimating()
    }
    
    func startBuffering() {
        view.addSubview(loadingView)
    }
    
    func stopBuffering() {
        loadingView.removeFromSuperview()
    }
}
```

위의 예시 코드에서는 `VideoPlayerViewController` 클래스에서 NVActivityIndicatorView를 사용하여 버퍼링 중임을 나타내는 로딩 효과를 구현하였습니다. `startBuffering` 함수를 호출하여 로딩 효과를 시작하고, `stopBuffering` 함수를 호출하여 로딩 효과를 중지할 수 있습니다.

## 결론
NVActivityIndicatorView를 사용하여 동영상 플레이어 앱에서 버퍼링 로딩 효과를 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 통해 앱에 멋진 로딩 효과를 추가하여 사용자에게 좋은 사용자 경험을 제공할 수 있습니다.

## 참고 자료
- [NVActivityIndicatorView GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView Documentation](https://cocoapods.org/pods/NVActivityIndicatorView)