---
layout: post
title: "[swift] Swift PKRevealController와의 디자인 가이드라인 준수"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

iOS 앱 개발을 하다보면 네비게이션 메뉴를 구현해야 할 때가 있습니다. 그럴 때 사용할 수 있는 라이브러리 중 하나가 Swift PKRevealController입니다. 

이 글에서는 PKRevealController를 사용하는 동안 디자인 가이드라인을 준수하는 방법에 대해 알아보겠습니다.

### 1. 네비게이션 메뉴 위치 결정하기

네비게이션 메뉴는 보통 왼쪽에 위치하는 것이 일반적입니다. 사용자는 왼쪽에서 오른쪽으로 읽기 때문에 이 위치에 익숙하고 사용하기 쉽습니다. 따라서 PKRevealController를 사용할 때에도 네비게이션 메뉴를 왼쪽에 위치시키는 것이 좋습니다.

```swift
let revealController = PKRevealController()
revealController.leftViewController = menuViewController
```

### 2. 네비게이션 메뉴 아이콘 디자인하기

네비게이션 메뉴 아이콘은 사용자가 메뉴를 열고 닫을 수 있는 버튼 역할을 합니다. iOS에서는 햄버거 아이콘을 대표적으로 사용하고 있으며, 앱 아이콘과 일관성을 유지하는 것이 중요합니다. 따라서 햄버거 아이콘을 사용하되, 앱 아이콘과 비슷한 스타일과 컬러를 적용하는 것이 좋습니다.

```swift
let menuButton = UIBarButtonItem(image: UIImage(named: "menuIcon"), style: .plain, target: self, action: #selector(openMenu))
navigationItem.leftBarButtonItem = menuButton
```

### 3. 컨텐츠 뷰 디자인하기

네비게이션 메뉴가 열리고 닫혀도 컨텐츠 뷰는 적절한 위치에 그대로 유지되어야 합니다. 화면 전체를 가리지 않고 일부만 가리도록 하여 사용자가 컨텐츠를 볼 수 있게 해야 합니다. 이는 PKRevealController의 기능을 활용하여 디자인할 수 있습니다.

```swift
revealController.frontViewPosition = .left
```

### 4. 애니메이션 효과 추가하기

네비게이션 메뉴 열림/닫힘 애니메이션은 사용자 경험을 향상시키는 데에 중요한 요소입니다. 네비게이션 메뉴가 부드럽게 슬라이드되는 효과를 주는 것이 좋습니다.

```swift
revealController.toggle(menuViewController)
```

### 5. 사용자 설정과 일치하는 디자인 적용하기

사용자 맞춤 설정에 따라 네비게이션 메뉴의 디자인을 변경할 수 있습니다. 예를 들어, 다크 모드를 사용하는 사용자에게는 밝은 컬러를, 또는 텍스트 크기를 조정하는 사용자에게는 네비게이션 메뉴 아이콘의 크기를 조정하는 등의 세부적인 디자인 변경을 적용할 수 있습니다.

```swift
if userSettings.darkModeEnabled {
    menuButton.tintColor = .white
} else {
    menuButton.tintColor = .black
}
```

위와 같이 Swift PKRevealController를 사용하는 동안 디자인 가이드라인을 준수하면 사용자들이 앱을 좀 더 편리하게 사용할 수 있게 될 것입니다.

> 코드 및 디자인 가이드라인은 PKRevealController 라이브러리의 특정 버전에 맞춰 작성되었습니다. 최신 버전에서는 일부 내용이 변경될 수 있으니 주의하시기 바랍니다.

**참고 자료**
- [PKRevealController 공식 문서](https://github.com/pkluz/PKRevealController)