---
layout: post
title: "[swift] Swift PKRevealController의 소스 코드 분석"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이번에는 Swift로 작성된 PKRevealController의 소스 코드를 분석해 보겠습니다. PKRevealController는 iOS 앱에서 슬라이딩 형태의 메뉴를 구현하는 데 도움이 되는 라이브러리입니다.

## PKRevealController 클래스

PKRevealController는 UIViewController를 상속받은 클래스입니다. 아래는 PKRevealController 클래스의 선언부입니다.

```swift
class PKRevealController: UIViewController { 
    // 클래스 속성 및 메서드 정의
}
```

PKRevealController 클래스는 메인 컨텐츠와 사이드 메뉴를 관리하고 제어하는 역할을 담당합니다. 

## 초기화 메서드

PKRevealController 클래스에는 다양한 초기화 메서드가 구현되어 있습니다. 아래는 그 중 하나인 `init(rearViewController: UIViewController, frontViewController: UIViewController)` 메서드입니다.

```swift
init(rearViewController: UIViewController, frontViewController: UIViewController)
```

이 메서드는 사이드 메뉴와 메인 컨텐츠를 각각 `rearViewController`와 `frontViewController`로 전달받아 초기화하는 역할을 합니다.

## 메뉴 표시 기능

PKRevealController 클래스는 사이드 메뉴를 표시하는 기능도 제공합니다. 이를 위해 `show(_:animated:completion:)` 메서드를 사용합니다.

```swift
func show(_ controller: UIViewController, animated: Bool, completion: ((Bool) -> Void)? = nil)
```

이 메서드는 `controller`를 표시하여 사이드 메뉴를 보여줍니다. `animated` 매개 변수를 사용하여 애니메이션 효과를 설정할 수 있습니다. 또한 `completion` 매개 변수를 사용하여 메뉴 표시가 완료된 후에 실행될 클로저를 지정할 수 있습니다.

## 참고 자료

PKRevealController의 소스 코드와 관련된 자세한 정보는 [PKRevealController GitHub 페이지](https://github.com/pkluz/PKRevealController)에서 확인할 수 있습니다.