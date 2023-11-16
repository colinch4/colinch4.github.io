---
layout: post
title: "[swift] Swift PKRevealController를 이용한 데이터 시각화"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이 블로그 포스트에서는 Swift PKRevealController를 사용하여 데이터 시각화를 구현하는 방법을 알려드리겠습니다. PKRevealController는 화면 왼쪽에 있는 사이드 바를 통해 다른 화면으로 전환할 수 있는 컨트롤러입니다. 이를 활용하여 데이터 시각화를 구현할 수 있습니다.

## 1. PKRevealController 설치하기

PKRevealController는 CocoaPods를 통해 설치할 수 있습니다. `Podfile`에 다음과 같이 추가해주세요.

```
pod 'PKRevealController', '~> 2.0.0'
```

그리고 터미널에서 다음 명령어를 실행하여 CocoaPods를 설치하세요.

```
pod install
```

## 2. 데이터 시각화 화면 구성하기

먼저, `PKRevealController`를 초기화한 후에 데이터 시각화에 사용할 뷰 컨트롤러를 추가해야합니다. 다음은 예시 코드입니다.

```swift
import UIKit
import PKRevealController

class DataVisualizationViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 좌측 사이드 바 설정
        if let revealController = revealViewController() {
            let sideMenuViewController = SideMenuViewController()
            let navigationController = UINavigationController(rootViewController: sideMenuViewController)
            revealController.setFront(navigationController, animated: true)
            
            // 좌측 사이드 바를 열기 위한 버튼 설정
            let menuButton = UIBarButtonItem(title: "Menu", style: .plain, target: revealController, action: #selector(PKRevealController.revealLeftView))
            navigationItem.leftBarButtonItem = menuButton
        }
        
        // 데이터 시각화 화면 설정
        let dataVisualizationView = DataVisualizationView()
        view.addSubview(dataVisualizationView)
        // 데이터 시각화 화면의 레이아웃 설정
        dataVisualizationView.translatesAutoresizingMaskIntoConstraints = false
        NSLayoutConstraint.activate([
            dataVisualizationView.topAnchor.constraint(equalTo: view.topAnchor),
            dataVisualizationView.bottomAnchor.constraint(equalTo: view.bottomAnchor),
            dataVisualizationView.leadingAnchor.constraint(equalTo: view.leadingAnchor),
            dataVisualizationView.trailingAnchor.constraint(equalTo: view.trailingAnchor)
        ])
    }
    
}
```

## 3. 사이드 메뉴 화면 구성하기

데이터 시각화 화면을 전환하기 위해 좌측에 사이드 메뉴를 구성해야합니다. 다음은 예시 코드입니다.

```swift
import UIKit

class SideMenuViewController: UITableViewController {
    
    let menuItems = ["Chart 1", "Chart 2", "Chart 3"]
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        tableView.register(UITableViewCell.self, forCellReuseIdentifier: "Cell")
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return menuItems.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.textLabel?.text = menuItems[indexPath.row]
        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        if let revealController = revealViewController() {
            revealController.setFront(DataVisualizationViewController(), animated: true)
        }
    }
    
}
```

## 4. 실행하기

앱을 실행하면 좌측 상단에 "Menu"라는 버튼이 나타납니다. 이 버튼을 클릭하면 사이드 메뉴가 나타나고, 메뉴 아이템을 선택하면 해당 데이터 시각화 화면으로 전환됩니다.

이제 Swift PKRevealController를 사용하여 데이터 시각화를 구현할 수 있게 되었습니다. 더욱 상세한 내용은 [공식 문서](https://github.com/pkluz/PKRevealController)를 참고하시기 바랍니다.