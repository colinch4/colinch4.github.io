---
layout: post
title: "[swift] Swift PKRevealController와의 오토레이아웃 관리"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

PKRevealController은 iOS에서 사용하는 커스텀 컨테이너 뷰 컨트롤러로, 주로 사이드 메뉴를 구현할 때 사용됩니다. 이 글에서는 Swift로 PKRevealController와 함께 오토레이아웃을 관리하는 방법에 대해 알아보겠습니다.

## PKRevealController 설정하기

먼저 PKRevealController를 사용하기 위해 프로젝트에 추가해야 합니다. Cocoapods를 사용한다면, Podfile에 다음과 같이 추가한 뒤 `pod install` 명령어를 실행하세요.

```ruby
pod 'PKRevealController'
```

다음으로, `UIViewController`를 상속받는 클래스를 생성하고, PKRevealController를 초기화하고 설정해야 합니다. 

```swift
import PKRevealController

class MainViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let leftViewController = // 좌측 메뉴 뷰 컨트롤러 생성
        let mainViewController = // 메인 뷰 컨트롤러 생성
        
        let revealController = PKRevealController(frontViewController: mainViewController, leftViewController: leftViewController)
        revealController.delegate = self
        
        self.addChild(revealController)
        self.view.addSubview(revealController.view)
        
        revealController.view.frame = self.view.bounds
        revealController.view.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        
        revealController.didMove(toParent: self)
    }
}
```

위 예제에서 `leftViewController`는 좌측 메뉴 뷰 컨트롤러를 생성하고, `mainViewController`는 메인 뷰 컨트롤러를 생성하는 부분은 자신의 프로젝트에 맞게 구현해야 합니다.

그리고 PKRevealController를 생성할 때, `frontViewController`로는 메인 뷰 컨트롤러를, `leftViewController`로는 좌측 메뉴 뷰 컨트롤러를 전달해야 합니다. 그리고 `revealController.view`는 메인 뷰 컨트롤러의 뷰를 PKRevealController의 뷰 위에 추가하여 표시합니다.

## 오토레이아웃 설정하기

PKRevealController와 함께 오토레이아웃을 사용할 경우, 다음과 같이 오토레이아웃 제약 조건을 추가해야 합니다.

```swift
leftViewController.view.translatesAutoresizingMaskIntoConstraints = false
mainViewController.view.translatesAutoresizingMaskIntoConstraints = false

let views = ["leftView": leftViewController.view!, "mainView": mainViewController.view!]

self.view.addConstraints(NSLayoutConstraint.constraints(withVisualFormat: "H:|[leftView(200)][mainView]|", options: [], metrics: nil, views: views))
self.view.addConstraints(NSLayoutConstraint.constraints(withVisualFormat: "V:|[mainView]|", options: [], metrics: nil, views: views))
self.view.addConstraints(NSLayoutConstraint.constraints(withVisualFormat: "V:|[leftView]|", options: [], metrics: nil, views: views))
```

위 예제에서는 `leftViewController`와 `mainViewController`의 뷰를 오토레이아웃을 사용하여 관리하고 있습니다. `H:|[leftView(200)][mainView]|`는 좌측 메뉴 뷰 컨트롤러의 너비를 200으로 고정하고, 메인 뷰 컨트롤러는 좌측 메뉴 뷰 컨트롤러의 오른쪽에 위치하도록 하고 있습니다. `V:|[mainView]|`는 메인 뷰 컨트롤러의 세로정렬을 설정하고, `V:|[leftView]|`는 좌측 메뉴 뷰 컨트롤러의 세로정렬을 설정하는 것입니다.

## 참고 자료

- [PKRevealController Github 페이지](https://github.com/pkluz/PKRevealController)

위 글에서는 Swift로 PKRevealController와 함께 오토레이아웃을 관리하는 방법에 대해 소개했습니다. PKRevealController는 다양한 커스텀 사이드 메뉴를 구현할 때 유용하게 사용될 수 있습니다. 추가적인 정보는 PKRevealController의 공식 Github 페이지를 참고하시기 바랍니다.