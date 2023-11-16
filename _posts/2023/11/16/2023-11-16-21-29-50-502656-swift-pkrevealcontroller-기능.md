---
layout: post
title: "[swift] Swift PKRevealController 기능"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift PKRevealController는 iOS 애플리케이션에서 사이드 메뉴를 구현하는데 도움을 주는 라이브러리입니다. 이 라이브러리를 사용하면 간편하게 햄버거 메뉴나 드로어 형태의 사이드 메뉴를 만들 수 있습니다. 이번 포스트에서는 Swift PKRevealController의 기능에 대해 알아보겠습니다.

## 1. 설치 및 설정

Swift PKRevealController를 사용하기 위해서는 먼저 Cocoapods를 사용하여 프로젝트에 라이브러리를 추가해야 합니다. `Podfile`에 아래와 같은 코드를 추가하고 pod install을 실행합니다.

```swift
pod 'PKRevealController'
```

프로젝트에 라이브러리를 추가한 후, AppDelegate에서 PKRevealController를 초기화하고 설정해야 합니다. 아래와 같이 AppDelegate.swift 파일을 열고 아래의 코드를 추가합니다.

```swift
import PKRevealController

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
    // PKRevealController 설정
    let revealController = PKRevealingViewController()
    let viewController = ViewController()  // 메인 컨텐츠로 사용할 뷰 컨트롤러
    let menuViewController = MenuViewController()  // 사이드 메뉴로 사용할 뷰 컨트롤러
    
    revealController.contentViewController = viewController
    revealController.leftViewController = menuViewController
    
    self.window?.rootViewController = revealController
    
    return true
}
```

위의 코드에서 `ViewController`는 사이드 메뉴를 포함한 메인 컨텐츠를 담당하는 뷰 컨트롤러입니다. `MenuViewController`는 실제 사이드 메뉴를 보여줄 뷰 컨트롤러입니다. 

## 2. 사이드 메뉴 커스터마이징

PKRevealController를 사용하면 사이드 메뉴를 맞춤 설정할 수 있는 다양한 옵션을 제공합니다. 아래는 몇 가지 예시입니다.

- `animationDuration`: 사이드 메뉴가 열리거나 닫힐 때의 애니메이션의 지속 시간을 설정할 수 있습니다.
- `animationOptions`: 사이드 메뉴 애니메이션에 적용할 옵션을 설정할 수 있습니다.
- `gestureDriven`: 사용자 제스처로 사이드 메뉴를 열거나 닫을 수 있도록 설정할 수 있습니다.

이외에도 다양한 옵션을 사용하여 사이드 메뉴의 모양과 동작을 자유롭게 변경할 수 있습니다.

## 3. 컨텐츠 뷰와 사이드 메뉴 간의 상호작용

PKRevealController를 사용하면 컨텐츠 뷰와 사이드 메뉴 간의 상호작용을 쉽게 처리할 수 있습니다. 예를 들어, 사이드 메뉴에서 항목을 선택하면 해당 항목에 맞는 컨텐츠를 보여줄 수 있습니다.

이를 위해 PKRevealControllerDelegate를 구현하여 상호작용에 대한 이벤트를 처리하면 됩니다. 예를 들어, 아래의 코드는 사이드 메뉴에서 항목을 선택했을 때 컨텐츠 뷰를 변경하는 예시입니다.

```swift
class MainViewController: UIViewController, PKRevealControllerDelegate {
    func revealController(_ revealController: PKRevealController!, didChangeTo state: PKFrontViewPosition) {
        // 사이드 메뉴의 활성화 상태가 변경되었을 때 호출됩니다.
    }
    
    func revealController(_ revealController: PKRevealController!, didSwapTo newFrontViewController: UIViewController!) {
        // 컨텐츠 뷰가 변경되었을 때 호출됩니다.
    }
    
    ...
}
```

## 4. 결론

Swift PKRevealController를 사용하면 iOS 애플리케이션에서 사이드 메뉴를 쉽게 구현할 수 있습니다. 다양한 옵션을 사용하여 사이드 메뉴를 맞춤 설정하고 컨텐츠 뷰와의 상호작용을 쉽게 처리할 수 있습니다. 이를 통해 사용자들에게 더 나은 사용자 경험을 제공할 수 있습니다.

더 자세한 내용은 PKRevealController의 공식 문서를 참조하시기 바랍니다.

**참고 자료**
- [PKRevealController GitHub](https://github.com/pkluz/PKRevealController)