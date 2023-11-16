---
layout: post
title: "[swift] Swift PKRevealController 사용 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

PKRevealController는 iOS 앱에서 사이드 메뉴를 만들기 위한 라이브러리입니다. 이번 포스트에서는 Swift를 사용하여 PKRevealController를 사용하는 방법을 알아보겠습니다.

## PKRevealController 라이브러리 추가하기

먼저, PKRevealController를 프로젝트에 추가해야 합니다. 가장 간단한 방법은 CocoaPods를 사용하는 것입니다. Podfile에 다음과 같이 추가합니다.

```ruby
pod 'PKRevealController'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## PKRevealController 설정하기

PKRevealController를 사용하기 위해서는 다음과 같은 단계를 따라야 합니다.

1. `PKRevealControllerDelegate` 프로토콜을 구현하는 클래스를 생성합니다.
2. `PKRevealController` 인스턴스를 생성합니다.
3. 왼쪽 메뉴와 오른쪽 메뉴의 뷰 컨트롤러를 생성합니다.
4. `PKRevealController` 인스턴스에 메뉴 뷰 컨트롤러를 설정합니다.

아래는 PKRevealController를 사용하는 예제 코드입니다.

```swift
import UIKit
import PKRevealController

class ViewController: UIViewController, PKRevealControllerDelegate {

    override func viewDidLoad() {
        super.viewDidLoad()

        // 좌측 메뉴 뷰 컨트롤러 생성
        let leftMenuViewController = LeftMenuViewController()
        
        // 우측 메뉴 뷰 컨트롤러 생성
        let rightMenuViewController = RightMenuViewController()

        // PKRevealController 인스턴스 생성
        let revealController = PKRevealController(frontViewController: self, leftViewController: leftMenuViewController, rightViewController: rightMenuViewController)

        // PKRevealController의 delegate 설정
        revealController.delegate = self

        // PKRevealController를 윈도우의 rootViewController로 설정
        UIApplication.shared.delegate?.window??.rootViewController = revealController
    }
}
```

위의 코드에서 `LeftMenuViewController`와 `RightMenuViewController`는 좌측과 우측 메뉴에 대한 커스텀 뷰 컨트롤러입니다. 이와 같이 생성한 뷰 컨트롤러를 `PKRevealController`의 인스턴스에 설정해주면 됩니다.

## Conclusion

이상으로 Swift를 사용하여 PKRevealController를 사용하는 방법에 대해 알아보았습니다. 이 라이브러리를 사용하면 iOS 앱에서 간편하게 사이드 메뉴를 구현할 수 있습니다.

더 자세한 내용은 [PKRevealController GitHub 페이지](https://github.com/pkluz/PKRevealController)를 참고하시기 바랍니다.