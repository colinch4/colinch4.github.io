---
layout: post
title: "[swift] Swift PKRevealController와의 고급 사용법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

![PKRevealController](https://github.com/pkluz/PKRevealController/raw/master/Screenshots/iPhone5-full-left.png)

PKRevealController는 iOS 앱에서 사이드 메뉴 뷰를 쉽게 구현할 수 있도록 도와주는 라이브러리입니다. 이번 글에서는 Swift에서 PKRevealController를 고급으로 사용하는 방법을 알아보겠습니다.

## 1. PKRevealController 설치

PKRevealController를 사용하기 위해서는 먼저 CocoaPods를 설치해야 합니다. Terminal을 열고 다음 명령어를 실행하여 CocoaPods을 설치합니다.

```
$ gem install cocoapods
```

그리고 프로젝트의 Podfile에 다음 라인을 추가합니다.

```
pod 'PKRevealController', '~> 2.0'
```

Terminal에서 다음 명령어를 실행하여 PKRevealController를 설치합니다.

```
$ pod install
```

## 2. PKRevealController 초기화

PKRevealController를 사용하기 위해서는 우선 사이드 메뉴 뷰 컨트롤러와 메인 뷰 컨트롤러를 생성해야 합니다. 아래의 코드를 참고하여 PKRevealController를 초기화해봅시다. 

```swift
import PKRevealController

class MainViewController: PKRevealController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let leftViewController = LeftViewController() // 사이드 메뉴 뷰 컨트롤러
        let mainViewController = MainContentViewController() // 메인 콘텐츠 뷰 컨트롤러

        self.leftViewController = leftViewController
        self.mainViewController = mainViewController
    }
}
```

## 3. 사이드 메뉴 설정

PKRevealController는 왼쪽 사이드 메뉴와 오른쪽 사이드 메뉴를 모두 지원합니다. 아래의 코드를 참고하여 사이드 메뉴를 설정해봅시다.

```swift
import PKRevealController

class LeftViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let menuLabel = UILabel(frame: CGRect(x: 20, y: 20, width: 200, height: 30))
        menuLabel.text = "Left Menu"
        menuLabel.textColor = UIColor.white
        self.view.addSubview(menuLabel)
    }
}
```

## 4. 메인 콘텐츠 설정

메인 콘텐츠는 일반적인 뷰 컨트롤러처럼 구성하면 됩니다. 아래의 코드를 참고하여 메인 콘텐츠 뷰 컨트롤러를 설정해봅시다.

```swift
import PKRevealController

class MainContentViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let mainLabel = UILabel(frame: CGRect(x: 20, y: 20, width: 200, height: 30))
        mainLabel.text = "Main Content"
        mainLabel.textColor = UIColor.black
        self.view.addSubview(mainLabel)
    }
}
```

## 5. PKRevealController 사용

마지막으로, 앱의 AppDelegate에서 PKRevealController를 주요 뷰 컨트롤러로 설정해야 합니다. 아래의 코드를 참고하여 설정해봅시다.

```swift
import PKRevealController

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {

    var window: UIWindow?

    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

        let mainViewController = MainViewController()
        
        self.window = UIWindow(frame: UIScreen.main.bounds)
        self.window?.rootViewController = mainViewController
        self.window?.makeKeyAndVisible()

        return true
    }
}
```

## 결론

이제 PKRevealController를 사용하여 Swift iOS 앱에서 사이드 메뉴를 쉽게 구현할 수 있습니다. 많은 개발자들이 사용하는 PKRevealController를 활용하여 사용자 친화적인 앱을 만들어보세요.

## 참고 자료

- [PKRevealController GitHub 페이지](https://github.com/pkluz/PKRevealController)
- [PKRevealController 문서](https://cocoadocs.org/docsets/PKRevealController)