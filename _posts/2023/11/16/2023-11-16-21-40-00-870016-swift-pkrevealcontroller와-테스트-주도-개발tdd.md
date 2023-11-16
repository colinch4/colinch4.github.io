---
layout: post
title: "[swift] Swift PKRevealController와 테스트 주도 개발(TDD)"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 소개

이번 글에서는 Swift PKRevealController를 사용하여 iOS 애플리케이션을 개발하는 방법과 함께 테스트 주도 개발(Test-Driven Development, TDD)을 적용하는 방법에 대해 알아보겠습니다.

## PKRevealController 소개

PKRevealController는 iOS 애플리케이션의 네비게이션 기능을 구현하기 위한 라이브러리입니다. 이 라이브러리를 사용하면 사용자가 왼쪽으로 슬라이드하여 메뉴를 보여주는 기능을 쉽게 구현할 수 있습니다.

PKRevealController는 CocoaPods를 통해 설치할 수 있습니다. 설치하기 위해 `Podfile`에 다음과 같은 코드를 추가합니다.

```swift
pod 'PKRevealController'
```

## TDD 소개

테스트 주도 개발은 소프트웨어 개발 방법론 중 하나로, 테스트를 먼저 작성하고 그 테스트를 통과하기 위한 코드를 작성하는 방식입니다. 이를 통해 개발하는 동안 품질 유지 및 안정성을 높일 수 있습니다.

## PKRevealController 개발과 TDD

1. 기능 명세 작성: PKRevealController를 사용하여 특정 화면으로 이동하는 기능을 개발하기로 결정했다고 가정해보겠습니다. 이 기능을 위해 필요한 명세를 작성합니다. 예를 들어, "사용자가 메뉴에서 '상품 목록'을 선택하면 '상품 목록' 화면으로 이동한다"와 같은 명세를 작성할 수 있습니다.

2. 테스트 작성: 명세에 따라 테스트를 작성합니다. 이 경우, '상품 목록'을 선택했을 때 해당 화면으로 이동하는지 테스트하는 코드를 작성합니다.

```swift
func testMenuSelection() {
   // Given
   let revealController = PKRevealController() 
   let menuViewController = MenuViewController()
   let productListViewController = ProductListViewController()
   
   revealController.setMenuViewController(menuViewController)
   revealController.setContentViewController(productListViewController)

   // When
   menuViewController.selectItem("상품 목록")
   
   // Then
   XCTAssertEqual(revealController.contentViewController, productListViewController)
}
```

3. 테스트 실행: 작성한 테스트를 실행해보고 실패하는지 확인합니다. 이 경우, 명세에 따라 화면이 이동하지 않았으므로 테스트는 실패해야 합니다.

4. 테스트 통과를 위한 코드 작성: 테스트가 실패하는 이유를 분석하여 통과할 수 있는 코드를 작성합니다. 이 경우, '상품 목록'을 선택한 후 해당 화면으로 이동하는 코드를 `MenuViewController`에 추가합니다.

5. 테스트 재실행: 테스트 코드를 다시 실행하여 통과하는지 확인합니다. 이를 반복하여 테스트를 통과할 때까지 코드를 수정하는 작업을 진행합니다.

6. 추가 기능 개발과 테스트: 필요한 추가 기능이 있다면 해당 기능에 대한 명세를 작성하고 테스트를 작성하여 개발을 진행합니다. 이러한 과정을 반복하여 전체 기능을 완성합니다.

## 결론

Swift PKRevealController를 사용하여 iOS 애플리케이션을 개발하는 방법과 함께 테스트 주도 개발을 적용하는 방법을 살펴보았습니다. TDD를 활용하여 개발하면 코드의 품질을 개선하고 안정성을 높일 수 있습니다. PKRevealController를 사용하는 경우 테스트 주도 개발을 통해 좀 더 견고하고 안정적인 애플리케이션을 만들 수 있습니다.

## References

- [PKRevealController GitHub](https://github.com/pkluz/PKRevealController)
- [Test-Driven Development (Wikipedia)](https://en.wikipedia.org/wiki/Test-driven_development)