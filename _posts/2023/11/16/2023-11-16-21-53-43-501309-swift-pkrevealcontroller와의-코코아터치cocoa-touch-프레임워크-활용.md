---
layout: post
title: "[swift] Swift PKRevealController와의 코코아터치(Cocoa Touch) 프레임워크 활용"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

PKRevealController는 iOS 애플리케이션에서 사이드바 네비게이션을 구현하기 위한 강력한 프레임워크입니다. 이 프레임워크는 사용자가 메인 컨텐츠를 보기 전에 사이드바를 열고 닫을 수 있는 기능을 제공합니다. 이번 포스팅에서는 PKRevealController를 Swift 언어와 코코아터치(Cocoa Touch) 프레임워크와 함께 사용하는 방법에 대해 알아보겠습니다.

## 1. PKRevealController 설치하기

PKRevealController는 CocoaPods를 통해 설치할 수 있습니다. `Podfile` 파일에 다음과 같이 추가하세요:

```
pod 'PKRevealController'
```

그리고 터미널에서 다음 명령을 실행하여 의존성을 설치해주세요:

```bash
$ pod install
```

## 2. PKRevealController 구성하기

PKRevealController를 사용하려면 크게 세 가지 요소가 필요합니다:

- `PKRevealController` 인스턴스
- 메인 컨텐츠 뷰 컨트롤러
- 사이드바 뷰 컨트롤러

다음은 간단한 예제입니다. `ViewController.swift` 파일을 만들고 다음 코드를 추가하세요:

```swift
import UIKit
import PKRevealController

class ViewController: PKRevealController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 메인 컨텐츠 뷰 설정
        let mainViewController = MainViewController()
        self.setMainViewController(mainViewController)
        
        // 사이드바 뷰 설정
        let sidebarViewController = SidebarViewController()
        self.setLeftViewController(sidebarViewController)
    }
    
}
```

위 코드에서 `MainViewController`와 `SidebarViewController`는 각각 메인 컨텐츠와 사이드바 뷰 컨트롤러입니다.

## 3. PKRevealController 설정하기

`ViewController.swift` 파일에 다음 코드를 추가하여 PKRevealController를 설정하세요.

```swift
import UIKit
import PKRevealController

class ViewController: PKRevealController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // ...

        // 화면 크기에 맞게 컨텐츠 뷰와 사이드바 뷰 크기 설정
        let sidebarWidth: CGFloat = 250.0
        self.setMinimumWidth(sidebarWidth, maximumWidth: sidebarWidth, forViewController: sidebarViewController)
        self.setRecognizesPanningOnFrontView(true)
        
        // 전환 애니메이션 설정
        self.setAnimationDuration(0.25)
        self.setAnimationType(PKRevealControllerAnimationType.none)
    }
    
}
```

위 코드에서는 사이드바의 폭을 250.0으로 고정하고, 전환 애니메이션을 설정하고 있습니다.

## 4. PKRevealController 사용하기

마지막으로, `AppDelegate.swift` 파일에서 `ViewController`를 루트 뷰 컨트롤러로 설정하세요.

```swift
import UIKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        
        let viewController = ViewController()
        self.window = UIWindow(frame: UIScreen.main.bounds)
        self.window?.rootViewController = viewController
        self.window?.makeKeyAndVisible()

        return true
    }
}
```

위 코드에서 `ViewController()`로 `ViewController`를 생성하고, `rootViewController`로 설정하고 있습니다.

## 결론

이제 PKRevealController를 Swift와 코코아터치(Cocoa Touch) 프레임워크와 함께 활용하는 방법을 알아보았습니다. 이 프레임워크는 iOS 애플리케이션에서 사이드바 네비게이션을 구현하기 위한 강력한 도구로 사용할 수 있습니다. 자세한 내용은 [PKRevealController](https://github.com/pkluz/PKRevealController) GitHub 저장소를 참고하세요.