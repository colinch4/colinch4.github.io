---
layout: post
title: "[swift] Swift PKRevealController에서의 탭바와의 연동"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

PKRevealController는 iOS 애플리케이션에서 사이드 메뉴/페이지 네비게이션을 구현하는 데 사용되는 라이브러리입니다. 이 라이브러리를 사용하면 탭바와 사이드 메뉴를 함께 사용할 수 있어 사용자 친화적인 경험을 제공할 수 있습니다. 이 글에서는 Swift PKRevealController에서 탭바와의 연동 방법을 알아보겠습니다.

## 1. PKRevealController 설치

PKRevealController를 설치하기 위해 CocoaPods를 사용해보겠습니다. `Podfile`에 아래 코드를 추가합니다.

```ruby
pod 'PKRevealController'
```

그리고 터미널에서 `pod install` 명령을 실행하여 의존성을 설치합니다.

## 2. 프로젝트 설정

### 2.1 탭바 생성

먼저, 기본적인 탭바를 생성해야 합니다. 이를 위해 `UITabBarController`를 생성하고, 각 탭에 해당하는 뷰 컨트롤러들을 설정합니다.

```swift
// 뷰 컨트롤러들 생성
let homeViewController = HomeViewController()
let settingsViewController = SettingsViewController()

// 탭바 생성
let tabBarController = UITabBarController()
tabBarController.viewControllers = [homeViewController, settingsViewController]
```

### 2.2 PKRevealController 생성

다음으로, PKRevealController를 생성하여 탭바와 사이드 메뉴를 연동해야 합니다.

```swift
// PKRevealController 생성
let revealController = PKRevealController()

// 사이드 메뉴 설정
let sideViewController = SideMenuViewController()
revealController.leftViewController = sideViewController

// 사이드 메뉴가 표시될 탭 설정
revealController.frontViewController = tabBarController
```

### 2.3 메인 윈도우 설정

마지막으로, 앱의 메인 윈도우에 PKRevealController를 추가해야 합니다.

```swift
// 윈도우 생성
window = UIWindow(frame: UIScreen.main.bounds)

// 메인 윈도우에 PKRevealController 설정
window?.rootViewController = revealController

// 윈도우 보이기
window?.makeKeyAndVisible()
```

## 3. 탭바와 사이드 메뉴 연동하기

기본적으로 PKRevealController를 사용하면 사이드 메뉴가 표시된 상태에서도 탭바를 사용할 수 있습니다. 그러나 기본 동작은 사이드 메뉴가 감춰져 있는 상태에서 탭바의 선택 사항을 변경하면, 선택된 탭의 뷰 컨트롤러로 전환되는 것입니다.

만약, 표시된 사이드 메뉴와 탭바의 선택 항목을 동시에 변경하고자 한다면, 다음 코드를 사용하여 PKRevealControllerDelegate 메소드를 구현할 수 있습니다.

```swift
extension AppDelegate: PKRevealControllerDelegate {

    func revealController(_ revealController: PKRevealController!, willChangeTo nextState: PKRevealControllerState) {

        // 선택된 탭바 아이템 변경
        tabBarController.selectedIndex = 0        
        // nextState에 따라 탭바 아이템을 변경하면 됩니다.
    }
}
```

선택된 탭에 따라 nextState를 변경하여 탭바의 선택 항목과 사이드 메뉴를 함께 변경할 수 있습니다.

## 4. 마무리

이제 PKRevealController를 사용하여 탭바와 사이드 메뉴를 함께 사용하는 방법을 알아보았습니다. 이를 통해 사용자들은 앱을 보다 간편하게 탐색할 수 있게 될 것입니다. PKRevealController의 공식 문서와 예제 코드를 참조하여 더 많은 기능을 살펴보시기 바랍니다.

**참고 자료:**
- [PKRevealController 공식 문서](https://github.com/pkluz/PKRevealController)