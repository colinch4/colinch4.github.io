---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 커스텀 탭바 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱 개발 중에는 데이터를 가져오거나 처리하는 동안 로딩 효과를 보여주는 것이 사용자 경험을 향상시키는 좋은 방법입니다. 이번에는 NVActivityIndicatorView를 사용하여 커스텀 탭바에 로딩 효과를 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS에서 로딩 인디케이터를 구현하기 위한 오픈 소스 라이브러리입니다. 깔끔하고 다양한 스타일의 로딩 인디케이터를 제공하여 앱에 애니메이션 효과를 추가할 수 있습니다. 

## 설치

NVActivityIndicatorView는 CocoaPods를 통해 설치할 수 있습니다. `Podfile`에 다음과 같이 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install`을 실행하여 라이브러리를 설치합니다.

## 구현

### 1. NVActivityIndicatorView 추가하기

탭바에 로딩 효과를 추가하기 위해, 우선 NVActivityIndicatorView를 가져옵니다.

```swift
import NVActivityIndicatorView
```

### 2. 커스텀 탭바 만들기

커스텀 탭바를 만들기 위해 `UITabBarController`를 상속받는 클래스를 생성합니다.

```swift
class CustomTabBarController: UITabBarController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 탭바 아이템을 설정하고 추가하는 코드 작성
    }
}
```

### 3. 로딩 효과 추가하기

로딩 효과를 추가할 탭바 아이템을 선택하고, 선택한 탭바 아이템에 NVActivityIndicatorView를 추가합니다. NVActivityIndicatorView의 위치는 탭바 아이템의 가운데로 설정합니다.

```swift
class CustomTabBarController: UITabBarController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
        loadingView.color = .gray
        loadingView.type = .ballScaleRipple
        
        // 탭바 아이템 설정
        
        // 로딩 효과 추가
        let tabBar = self.tabBar
        let selectedTabBarItem = tabBar.selectedItem!
        selectedTabBarItem.title = ""

        let centerX = selectedTabBarItem.image!.size.width / 2
        let centerY = selectedTabBarItem.image!.size.height / 2
        loadingView.center = CGPoint(x: centerX, y: centerY)
        selectedTabBarItem.image?.withRenderingMode(.alwaysOriginal)
        selectedTabBarItem.image = selectedTabBarItem.image?.withAlignmentRectInsets(UIEdgeInsets(top: 0, left: 0, bottom: -12, right: 0))
        
        selectedTabBarItem.addSubview(loadingView)
    }
}
```

### 4. 로딩 효과 제어하기

로딩 효과를 제어하기 위해, `startAnimating()` 및 `stopAnimating()` 메소드를 호출합니다. 데이터를 로딩할 때 로딩 효과를 시작하고, 로딩이 완료되면 효과를 중지합니다.

```swift
class CustomTabBarController: UITabBarController {
    let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        loadingView.color = .gray
        loadingView.type = .ballScaleRipple
        
        // 탭바 아이템 설정
        
        // 로딩 효과 추가
        
        // 데이터 로딩 시작
        self.startLoading()
    }
    
    func startLoading() {
        loadingView.startAnimating()
        
        // 데이터 로딩 및 처리 코드 작성
        
        // 로딩 완료 후 로딩 효과 중지
        self.stopLoading()
    }
    
    func stopLoading() {
        loadingView.stopAnimating()
    }
}
```

## 결론

이제 NVActivityIndicatorView를 사용하여 커스텀 탭바에 로딩 효과를 구현할 수 있습니다. 이를 통해 사용자 경험을 개선하고 앱의 완성도를 높일 수 있습니다. 더 다양한 로딩 인디케이터 스타일을 적용해보고 앱에 적합한 디자인을 찾아보세요.

## 참고 자료

- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView Documentation](https://github.com/ninjaprox/NVActivityIndicatorView/blob/master/README.md)