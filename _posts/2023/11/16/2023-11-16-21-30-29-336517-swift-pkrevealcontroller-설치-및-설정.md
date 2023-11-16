---
layout: post
title: "[swift] Swift PKRevealController 설치 및 설정"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift PKRevealController는 iOS 애플리케이션에서 드로어(Drawer) 메뉴를 구현하기 위한 라이브러리입니다. 이 라이브러리를 사용하면 매끄러운 드로어 메뉴를 손쉽게 구축할 수 있습니다.

## 설치방법

1. Cocoapods를 통해 PKRevealController를 설치합니다. `Podfile`에 다음 줄을 추가합니다.

```ruby
pod 'PKRevealController'
```

2. 터미널에서 다음 명령어를 실행하여 Cocoapods를 설치합니다.

```shell
pod install
```

## 사용법

1. 드로어 메뉴를 사용할 뷰 컨트롤러를 `PKRevealViewController`로 상속받습니다.

2. `PKRevealController`의 인스턴스를 생성하고, 메인 컨텐츠와 드로어 컨텐츠로 사용할 뷰 컨트롤러를 설정합니다.

```swift
let mainViewController = MainViewController()
let drawerViewController = DrawerViewController()

let revealController = PKRevealController()
revealController.mainViewController = mainViewController
revealController.leftViewController = drawerViewController
```

3. 드로어 메뉴를 열기 위한 액션을 설정합니다.

```swift
@IBAction func openDrawer(_ sender: UIButton) {
    revealController.showViewController(revealController.leftViewController)
}
```

4. `revealController`를 현재 화면에 표시합니다.

```swift
self.addChild(revealController)
self.view.addSubview(revealController.view)
revealController.view.frame = self.view.bounds
revealController.view.autoresizingMask = [.flexibleWidth, .flexibleHeight]
revealController.didMove(toParent: self)
```

## 커스터마이징

Swift PKRevealController는 다양한 옵션을 제공하여 드로어 메뉴의 동작 방식을 커스터마이징할 수 있습니다. 자세한 내용은 [PKRevealController GitHub 페이지](https://github.com/pkluz/PKRevealController)에서 확인할 수 있습니다.

이렇게 간단하게 Swift PKRevealController를 설치하고 설정하는 방법에 대해 알아보았습니다. 이제 드로어 메뉴를 쉽게 구현하여 사용자 친화적인 애플리케이션을 개발할 수 있습니다.