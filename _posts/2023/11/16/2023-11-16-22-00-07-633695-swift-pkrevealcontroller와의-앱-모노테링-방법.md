---
layout: post
title: "[swift] Swift PKRevealController와의 앱 모노테링 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift에서 PKRevealController를 사용하여 앱의 모노테링 기능을 구현하는 방법에 대해 알아보겠습니다. PKRevealController는 iOS 개발에서 널리 사용되는 오픈 소스 라이브러리로, 사이드바와 메인 컨텐츠를 쉽게 관리하고 제어할 수 있습니다.

## 1. PKRevealController 설치

먼저, PKRevealController를 설치해야 합니다. Cocoapods를 사용한다면, Podfile에 아래의 코드를 추가하고 `pod install` 명령어를 실행하세요.

```swift
pod 'PKRevealController'
```

수동으로 설치하는 경우, [PKRevealController GitHub 페이지](https://github.com/pkluz/PKRevealController)에서 최신 버전의 소스 코드를 다운로드하여 프로젝트에 추가하세요.

## 2. PKRevealController 설정

```swift
import UIKit
import PKRevealController

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        // PKRevealController 초기화
        let revealController = PKRevealController()
        
        // 사이드바 뷰 설정
        let sidebarViewController = SidebarViewController()
        revealController.leftViewController = sidebarViewController
        
        // 메인 뷰 설정
        let mainViewController = MainViewController()
        revealController.centerViewController = mainViewController
        
        // PKRevealController를 루트 뷰로 설정
        UIApplication.shared.delegate?.window??.rootViewController = revealController
    }
}
```

위 코드에서 `SidebarViewController`와 `MainViewController`는 앱에 맞게 커스텀한 뷰 컨트롤러 클래스로 대체해야 합니다.

## 3. 모노테링 기능 구현

모노테링 기능을 구현하기 위해 사이드바에 있는 메뉴를 터치할 때마다 메인 컨텐츠가 변경되도록 할 수 있습니다. 예를 들어, `SidebarViewController`의 테이블 뷰에서 메뉴를 선택한 후, 해당 메뉴에 대한 콘텐츠를 표시하는 `ContentViewController`를 로드하도록 구현할 수 있습니다.

```swift
class SidebarViewController: UITableViewController {
    
    let menuItems = ["메뉴 1", "메뉴 2", "메뉴 3"]
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return menuItems.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: .default, reuseIdentifier: "Cell")
        cell.textLabel?.text = menuItems[indexPath.row]
        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        if let revealController = self.revealController() {
            
            let contentViewController = ContentViewController()
            contentViewController.menuItem = menuItems[indexPath.row]
            
            revealController.pushViewController(contentViewController, animated: true)
            revealController.showViewController(contentViewController)
        }
    }
}

class ContentViewController: UIViewController {
    
    var menuItem: String?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        if let menuItem = menuItem {
            // 메뉴에 따른 콘텐츠 설정
        }
    }
}
```

위의 코드에서는 `SidebarViewController`의 `didSelectRowAt` 메서드에서 선택한 메뉴에 따라 `ContentViewController`를 로드하고 메인 컨텐츠로 표시합니다.

## 결론

이제 PKRevealController를 사용하여 앱에 모노테링 기능을 구현하는 방법에 대해 알아보았습니다. PKRevealController는 강력한 라이브러리로 iOS 앱의 UI를 개선하고 사용자 경험을 향상시킬 수 있습니다.

더 많은 정보와 예제 코드는 [PKRevealController GitHub 페이지](https://github.com/pkluz/PKRevealController)를 참고하세요.