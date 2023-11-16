---
layout: post
title: "[swift] Swift PKRevealController를 사용한 실제 앱 사례"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 개요

이번 포스트에서는 Swift를 사용하여 PKRevealController를 구현한 실제 앱 사례를 알아보겠습니다. PKRevealController는 iOS에서 네비게이션 컨트롤러를 쉽게 구현할 수 있도록 도와주는 라이브러리입니다.

## PKRevealController란?

PKRevealController는 iOS에서 슬라이딩 메뉴를 구현하기 위한 컨트롤러입니다. 이 라이브러리를 사용하면 메인 뷰 컨트롤러와 사이드 메뉴 뷰 컨트롤러를 쉽게 연결하고 사용자가 화면을 스와이프하여 메뉴를 열고 닫을 수 있습니다.

## 실제 앱 사례

저희 팀에서 개발한 앱인 'Travel Diary'는 PKRevealController를 사용하여 메인 화면과 메뉴 화면을 연결하였습니다. 이 앱은 사용자의 여행 일지를 기록하고 공유할 수 있는 앱으로, 사용자는 메인 화면에서 일지를 작성하고 메뉴 화면에서 다른 사용자의 일지를 둘러볼 수 있습니다.

### 구현 방법

1. 'Travel Diary' 앱 프로젝트를 열고 Swift 패키지 매니저를 사용하여 PKRevealController를 추가합니다:

```swift
import PKRevealController
```

2. `PKRevealController` 클래스를 상속받은 `MainViewController`를 생성합니다. 이 클래스는 메인 화면 역할을 맡게 됩니다:

```swift
class MainViewController: PKRevealController {
    // MainViewController의 구현 내용
}
```

3. `MenuViewController`를 생성하여 사이드 메뉴를 구현합니다:

```swift
class MenuViewController: UIViewController {
    // MenuViewController의 구현 내용
}
```

4. `AppDelegate.swift` 파일에서 `didFinishLaunchingWithOptions` 메서드를 수정하여 `PKRevealController`의 인스턴스를 생성하고 메인 화면과 메뉴 화면을 연결합니다:

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // PKRevealController 인스턴스 생성
    let revealController = PKRevealController()
    
    // 메인 화면 설정
    let mainViewController = MainViewController()
    revealController.setMainViewController(mainViewController)
    
    // 메뉴 화면 설정
    let menuViewController = MenuViewController()
    revealController.setLeftViewController(menuViewController)
    
    // rootViewController로 설정
    window?.rootViewController = revealController
    
    return true
}
```

5. 나머지 기능과 UI를 구현하고 필요한 경우 PKRevealController의 다양한 메서드와 속성을 사용하여 화면 전환 등을 처리합니다.

## 결론

이번 포스트에서는 Swift를 사용하여 PKRevealController를 구현한 실제 앱 사례를 살펴보았습니다. PKRevealController는 iOS 앱에서 슬라이딩 메뉴를 구현하는 데 유용한 라이브러리입니다. 'Travel Diary' 앱의 예시를 통해 구체적인 구현 방법을 알아보았습니다. 개발자는 PKRevealController를 활용하여 다양한 앱에서 사용자 인터페이스를 개선할 수 있습니다.

## 참고 자료
- [PKRevealController 공식 GitHub 저장소](https://github.com/pkluz/PKRevealController)
- [Travel Diary 앱 다운로드 링크](https://example.com)