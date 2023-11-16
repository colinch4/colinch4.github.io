---
layout: post
title: "[swift] Swift PKRevealController의 사용자 인터페이스(UI) 측면 분석"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 소개
Swift PKRevealController는 iOS 애플리케이션에서 햄버거 메뉴를 제공하는 커스텀 뷰 컨트롤러입니다. 이 라이브러리를 사용하면 좌측 또는 우측에서 슬라이드하여 메뉴를 열거나 닫을 수 있습니다. 

이 튜토리얼에서는 Swift PKRevealController의 사용자 인터페이스(UI)를 분석해보겠습니다.

## PKRevealController 클래스
PKRevealController는 UIViewController를 상속받은 클래스입니다. 따라서 다른 뷰 컨트롤러들과 마찬가지로 viewDidLoad(), viewWillAppear(), viewDidAppear() 등의 뷰 라이프사이클 메서드를 사용할 수 있습니다.

PKRevealController는 mainViewController와 leftViewController 또는 rightViewController를 가지고 있습니다. mainViewController는 메인 컨텐츠 뷰를 보여주고, leftViewController는 좌측 메뉴를 보여줄 때 사용됩니다. rightViewController는 우측 메뉴를 보여줄 때 사용됩니다.

## UI 측면
PKRevealController는 메인 컨텐츠 뷰와 메뉴 뷰(좌측 메뉴 뷰 혹은 우측 메뉴 뷰)를 제공합니다. 사용자는 화면에서 스와이프 또는 버튼을 통해 메뉴를 열거나 닫을 수 있습니다.

### 메인 컨텐츠 뷰
메인 컨텐츠 뷰는 PKRevealController의 mainViewController에 의해 제어됩니다. 이 뷰는 주 앱 컨텐츠를 보여주는 역할을 합니다. 사용자는 이 뷰를 스와이프하여 메뉴를 열거나 닫을 수 있습니다.

### 메뉴 뷰
메뉴 뷰는 PKRevealController의 leftViewController 또는 rightViewController에 의해 제어됩니다. 이 뷰는 좌측 또는 우측 메뉴를 보여주는 역할을 합니다. 기본적으로는 메뉴 뷰가 화면에서 숨겨져 있으며, 사용자는 화면을 스와이프하여 열거나 버튼을 탭하여 열 수 있습니다.

## 사용자 지정 예제
다음은 PKRevealController를 사용하여 사용자 인터페이스를 확장하는 방법의 예시입니다.

```swift
let mainViewController = MainViewController() // 메인 컨텐츠 뷰 컨트롤러

let leftViewController = LeftMenuViewController() // 좌측 메뉴 뷰 컨트롤러

let revealController = PKRevealController(mainViewController: mainViewController, leftViewController: leftViewController)

self.window?.rootViewController = revealController
self.window?.makeKeyAndVisible()
```

위의 코드에서는 메인 컨텐츠 뷰 컨트롤러와 좌측 메뉴 뷰 컨트롤러를 생성하고, 이를 사용하여 PKRevealController를 초기화한 후, 앱의 rootViewController로 설정하고 있습니다.

## 결론
Swift PKRevealController는 iOS 애플리케이션에 햄버거 메뉴를 쉽게 구현할 수 있는 라이브러리입니다. 이 튜토리얼에서는 PKRevealController의 사용자 인터페이스(UI) 측면을 분석하고, 기본적인 사용자 정의 예시를 제공했습니다.

더 자세한 정보는 [공식 문서](https://github.com/pkluz/PKRevealController)를 참조하세요.