---
layout: post
title: "[swift] Swift PKRevealController에서의 화면 전환 기능"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

PKRevealController는 iOS 앱에서 사이드 메뉴를 구현하기 위해 사용되는 라이브러리입니다. 이 라이브러리를 사용하여 사이드 메뉴를 추가하고 화면 전환 기능을 구현하는 방법에 대해 알아보겠습니다.

## 1. PKRevealController 설치

먼저, PKRevealController를 프로젝트에 설치해야 합니다. 아래 명령을 터미널에서 실행하여 CocoaPods를 이용하여 PKRevealController를 설치합니다.

```
$ pod install
```

Podfile에 아래 내용을 추가한 후 `pod install`을 실행합니다.

```ruby
pod 'PKRevealController', '~> 2.1'
```

## 2. PKRevealController 설정

PKRevealController를 사용하기 위해 아래 코드를 AppDelegate.swift 파일에 추가합니다.

```swift
import PKRevealController

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {

    // PKRevealController 인스턴스 생성
    let mainStoryboard = UIStoryboard(name: "Main", bundle: nil)
    let mainVC = mainStoryboard.instantiateViewController(withIdentifier: "MainViewController")
    let menuVC = mainStoryboard.instantiateViewController(withIdentifier: "MenuViewController")

    let revealController = PKRevealController(frontViewController: mainVC, leftViewController: menuVC)
    revealController?.delegate = self

    self.window = UIWindow(frame: UIScreen.main.bounds)
    self.window?.rootViewController = revealController
    self.window?.makeKeyAndVisible()

    return true
}
```

## 3. 화면 전환 기능 구현

PKRevealController를 사용하여 화면 전환 기능을 구현하려면 다음 단계를 따릅니다.

### 3.1. 메인 화면에서 사이드 메뉴 열기

메인 화면에서 버튼을 추가하고, 버튼이 눌렸을 때 사이드 메뉴를 열 수 있도록 합니다.

```swift
@IBAction func openSideMenuButtonTapped(_ sender: UIButton) {
    if let revealController = self.revealController {
        revealController.show(.left, animated: true)
    }
}
```

### 3.2. 사이드 메뉴에서 화면 전환

사이드 메뉴에서 다른 화면으로 전환하기 위해 `MenuViewController`에 전환할 화면을 띄우는 코드를 작성합니다.

```swift
@IBAction func transitionButtonTapped(_ sender: UIButton) {
    if let revealController = self.revealController,
       let mainViewController = revealController.frontViewController as? MainViewController {

        let detailStoryboard = UIStoryboard(name: "Detail", bundle: nil)
        let detailVC = detailStoryboard.instantiateViewController(withIdentifier: "DetailViewController")

        mainViewController.navigationController?.pushViewController(detailVC, animated: true)
    }
}
```

위의 코드에서 `DetailViewController`는 전환할 화면의 뷰 컨트롤러입니다. 실제 프로젝트에서는 해당 뷰 컨트롤러에 맞게 수정해야 합니다.

## 참고 자료

- [PKRevealController 공식 문서](https://github.com/pkluz/PKRevealController)
- [CocoaPods 설치 가이드](https://cocoapods.org)