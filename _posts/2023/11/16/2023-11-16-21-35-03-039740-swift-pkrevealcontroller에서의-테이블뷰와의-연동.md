---
layout: post
title: "[swift] Swift PKRevealController에서의 테이블뷰와의 연동"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

PKRevealController는 iOS 애플리케이션에서 사이드 메뉴를 구현하기 위해 사용되는 라이브러리입니다. 이 라이브러리는 테이블뷰와의 연동을 통해 사용자가 사이드 메뉴를 열고 닫을 수 있도록 합니다. 

### 테이블뷰와의 연동 설정

1. PKRevealController를 프로젝트에 추가하고, 뷰 컨트롤러에 import 문을 추가합니다.

   ```swift
   import PKRevealController
   ```

2. 메인 뷰 컨트롤러 클래스에 PKRevealControllerDelegate를 구현합니다.

   ```swift
   class MainViewController: UIViewController, PKRevealControllerDelegate {
       // ...
   }
   ```

3. viewDidLoad() 함수에서 PKRevealController 객체를 만들고 루트 뷰 컨트롤러로 설정합니다.

   ```swift
   override func viewDidLoad() {
       super.viewDidLoad()

       let revealController = PKRevealController()
       revealController.delegate = self
       revealController.setFrontViewController(frontViewController, animated: true)
       revealController.setLeftViewController(leftViewController, animated: true)

       self.addChildViewController(revealController)
       self.view.addSubview(revealController.view)
       revealController.didMove(toParentViewController: self)
   }
   ```

   위 코드에서 `frontViewController`는 메인 뷰 컨트롤러의 메인 콘텐츠 뷰이고, `leftViewController`는 사이드 메뉴 뷰입니다.

4. PKRevealControllerDelegate의 메서드를 구현하여 사용자 인터랙션에 따라 사이드 메뉴를 열고 닫을 수 있도록 합니다.

   ```swift
   func revealController(_ revealController: PKRevealController, didChangeTo state: PKRevealControllerState) {
       if state == .leftVisible {
           // 사이드 메뉴가 열린 경우
           // 테이블뷰 설정 등 필요한 작업을 수행합니다.
       } else {
           // 사이드 메뉴가 닫힌 경우
           // 테이블뷰 설정 등 필요한 작업을 수행합니다.
       }
   }
   ```

   위 코드에서 `state`의 값이 `leftVisible`일 때는 사이드 메뉴가 열린 상태를 의미하며, `leftVisible`가 아닐 때는 사이드 메뉴가 닫힌 상태를 의미합니다.

### 마무리

위의 단계를 따라하면 Swift PKRevealController에서 테이블뷰와의 연동을 구현할 수 있습니다. PKRevealController를 사용하여 사이드 메뉴를 간편하게 구현하고 테이블뷰와의 연동을 통해 더 편리한 사용자 경험을 제공할 수 있습니다.

### 참고 자료

- [PKRevealController GitHub 페이지](https://github.com/pkluz/PKRevealController)