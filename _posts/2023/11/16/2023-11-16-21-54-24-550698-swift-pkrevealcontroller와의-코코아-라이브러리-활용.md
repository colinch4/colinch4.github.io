---
layout: post
title: "[swift] Swift PKRevealController와의 코코아 라이브러리 활용"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 목차
- [Swift PKRevealController란?](#swift-pkrevealcontroller란)
- [코코아 라이브러리를 활용한 PKRevealController 구현](#코코아-라이브러리를-활용한-pkrevealcontroller-구현)
- [결론](#결론)

## Swift PKRevealController란?
Swift PKRevealController는 iOS 앱에서 사이드 메뉴를 구현하기 위해 사용되는 라이브러리입니다. 이 라이브러리는 객체지향적인 방식으로 구현되어 있어 앱의 구조를 잘 유지하면서 편리하게 사이드 메뉴를 추가할 수 있습니다.

## 코코아 라이브러리를 활용한 PKRevealController 구현
아래는 코코아 라이브러리를 활용하여 PKRevealController를 구현하는 예시 코드입니다.

```swift
import UIKit
import PKRevealController

class MainViewController: PKRevealController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let menuViewController = MenuViewController()
        let contentViewController = ContentViewController()
        
        self.setFrontViewController(contentViewController, animated: false)
        self.setLeftViewController(menuViewController, animated: false)
        self.setFrontViewShadow(color: .black, offset: CGSize(width: 0, height: 2), opacity: 0.5, radius: 5)
        self.setMinimumWidth(200, maximumWidth: 300, for: .left)
        
        self.view.backgroundColor = .white
    }
}

class MenuViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.view.backgroundColor = .lightGray
    }
}

class ContentViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.view.backgroundColor = .white
        
        let openMenuButton = UIButton(type: .system)
        openMenuButton.setTitle("Open Menu", for: .normal)
        openMenuButton.addTarget(self, action: #selector(openMenu), for: .touchUpInside)
        openMenuButton.frame = CGRect(x: 100, y: 200, width: 200, height: 50)
        self.view.addSubview(openMenuButton)
    }
    
    @objc func openMenu() {
        if let revealController = self.revealController() {
            revealController.show(.left)
        }
    }
}
```

위 코드는 MainViewController 클래스에서 PKRevealController를 상속받아 사용하는 예시입니다. MainViewController에서는 ContentViewController와 MenuViewController를 각각 FrontViewController와 LeftViewController로 설정하고, 사이드 메뉴의 너비와 그림자 설정 등을 추가로 설정합니다.

ContentViewController에서는 "Open Menu"라는 버튼을 생성하고, 버튼을 누를 때 사이드 메뉴를 보여주도록 구현되어 있습니다. 이를 위해 `openMenu` 메서드에서 `self.revealController()?.show(.left)`를 호출하여 왼쪽 사이드 메뉴를 보여주고 있습니다.

## 결론
Swift PKRevealController는 iOS 앱에서 사이드 메뉴를 쉽게 구현하기 위해 사용할 수 있는 코코아 라이브러리입니다. 위 예시 코드를 참고하여 사용해보시기 바랍니다. 더 많은 기능과 설정은 PKRevealController의 공식 문서를 참고하시기 바랍니다.