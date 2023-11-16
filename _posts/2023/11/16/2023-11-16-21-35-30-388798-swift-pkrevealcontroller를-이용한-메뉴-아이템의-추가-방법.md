---
layout: post
title: "[swift] Swift PKRevealController를 이용한 메뉴 아이템의 추가 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

PKRevealController는 iOS에서 사이드 메뉴를 구현하는 데 사용되는 강력한 라이브러리입니다. 이 라이브러리를 사용하여 메뉴 아이템을 추가하는 방법을 알아보겠습니다. 

## 1. PKRevealController 설치

먼저, PKRevealController를 프로젝트에 설치해야 합니다. 이를 위해서는 CocoaPods를 사용하는 것이 가장 간단하고 편리합니다. Podfile에 다음과 같이 PKRevealController를 추가합니다.

```ruby
pod 'PKRevealController'
```

그리고 터미널에서 다음 명령어를 실행하여 Pod를 설치합니다.

```bash
$ pod install
```

## 2. PKRevealController 설정

모든 설정이 완료되었으니 이제 PKRevealController 객체를 생성하고 메뉴 아이템을 추가해보겠습니다. 

```swift
import PKRevealController

class ViewController: PKRevealController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 왼쪽 메뉴를 설정합니다.
        let menuViewController = MenuViewController()
        menuViewController.view.backgroundColor = UIColor.red
        
        self.leftViewController = menuViewController
        
        // 오른쪽 컨텐츠를 설정합니다.
        let contentViewController = ContentViewController()
        contentViewController.view.backgroundColor = UIColor.white
        
        self.rightViewController = contentViewController
    }
    
}
```

위의 코드에서는 PKRevealController를 ViewController의 서브클래스로 정의하고, `viewDidLoad()` 메서드에서 왼쪽 메뉴와 오른쪽 컨텐츠를 설정합니다. `MenuViewController`와 `ContentViewController`는 각각 왼쪽 메뉴와 오른쪽 컨텐츠를 위한 커스텀 뷰 컨트롤러입니다.

## 3. 메뉴 아이템 추가

이제 왼쪽 메뉴에 실제 메뉴 아이템을 추가해보겠습니다. `MenuViewController` 클래스에서 다음과 같이 코드를 작성합니다.

```swift
class MenuViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {
    
    let menuItems = ["메뉴1", "메뉴2", "메뉴3"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let tableView = UITableView(frame: self.view.bounds, style: .plain)
        tableView.delegate = self
        tableView.dataSource = self
        
        self.view.addSubview(tableView)
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return menuItems.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = UITableViewCell(style: .default, reuseIdentifier: "cell")
        cell.textLabel?.text = menuItems[indexPath.row]
        return cell
    }
    
}
```

위의 코드에서는 `UITableViewDelegate`와 `UITableViewDataSource` 프로토콜을 채택하여 테이블뷰에 메뉴 아이템을 표시합니다. `menuItems` 배열에는 표시할 메뉴 아이템의 제목들이 저장되어 있습니다.

이렇게 설정하고 실행해보면 왼쪽 메뉴에 "메뉴1", "메뉴2", "메뉴3"이라는 아이템이 표시될 것입니다.

이제 PKRevealController를 사용하여 Swift에서 메뉴 아이템을 추가하는 방법에 대해 알아보았습니다. PKRevealController를 사용하면 iOS 앱에서 쉽고 간편하게 사이드 메뉴를 구현할 수 있습니다. 

더 많은 기능과 옵션에 대해서는 [PKRevealController GitHub 페이지](https://github.com/pkluz/PKRevealController)를 참조해주세요.