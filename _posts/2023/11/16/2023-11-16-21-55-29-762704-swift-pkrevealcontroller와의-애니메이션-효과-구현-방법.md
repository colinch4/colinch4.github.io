---
layout: post
title: "[swift] Swift PKRevealController와의 애니메이션 효과 구현 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

PKRevealController는 iOS에서 슬라이딩 메뉴를 구현하는 데 사용할 수 있는 오픈 소스 프레임워크입니다. 이 프레임워크를 사용하면 사용자 정의 가능한 애니메이션 효과를 사용하여 메뉴를 열거나 닫을 수 있습니다.

이 문서에서는 Swift를 사용하여 PKRevealController와 함께 애니메이션 효과를 구현하는 방법을 설명합니다.

## 1. PKRevealController 설치

먼저 Cocoapods를 이용하여 PKRevealController를 프로젝트에 설치해야 합니다. Podfile 파일에 다음의 내용을 추가하세요:

```ruby
pod 'PKRevealController'
```

그런 다음 터미널에서 `pod install` 명령을 실행하여 PKRevealController를 프로젝트에 추가하세요.

## 2. PKRevealController 초기화

PKRevealController를 초기화하기 위해 다음과 같이 코드를 작성할 수 있습니다:

```swift
import PKRevealController

class ViewController: PKRevealController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let mainStoryboard = UIStoryboard(name: "Main", bundle: nil)
        let mainViewController = mainStoryboard.instantiateViewController(withIdentifier: "MainViewController")
        let menuViewController = mainStoryboard.instantiateViewController(withIdentifier: "MenuViewController")
        
        self.frontViewController = mainViewController
        self.leftViewController = menuViewController
        
        self.animateChildViewController(mainViewController, completion: nil)
        self.animateChildViewController(menuViewController, completion: nil)
    }
}
```

위의 코드에서 `MainViewController`는 메인 화면을 나타내고, `MenuViewController`는 슬라이딩 메뉴를 나타냅니다. 적절한 식별자로 Storyboard에서 이 두 개의 뷰 컨트롤러를 초기화해야 합니다.

## 3. 애니메이션 효과 추가

PKRevealController는 다양한 애니메이션 효과를 제공합니다. 다음은 애니메이션 효과를 추가하는 예시 코드입니다:

```swift
import PKRevealController

class MenuViewController: UIViewController, UITableViewDelegate, UITableViewDataSource {

    // ...

    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        tableView.deselectRow(at: indexPath, animated: true)
        
        let mainStoryboard = UIStoryboard(name: "Main", bundle: nil)
        let selectedViewController = mainStoryboard.instantiateViewController(withIdentifier: "SelectedViewController")
        
        if let revealController = self.revealController {
            revealController.pushFrontViewController(selectedViewController, animated: true)
        }
    }

}
```

위의 코드에서 `didSelectRowAt` 메서드는 테이블 뷰에서 특정 항목을 선택할 때 호출됩니다. 선택된 뷰 컨트롤러를 초기화하고, `pushFrontViewController` 메서드를 사용하여 선택된 뷰 컨트롤러를 표시합니다.

## 4. 기타 설정 옵션

PKRevealController에는 많은 사용자 정의 설정 옵션이 제공됩니다. 예를 들어, 메뉴가 왼쪽에서 오른쪽으로 슬라이딩되는 대신 오른쪽에서 왼쪽으로 슬라이딩되도록 설정할 수 있습니다. 

```swift
self.options = [
    .animationDuration: 0.3,
    .animationCurve: .easeInOut,
    .recognizesPanningOnFrontView: true,
    .pushesFrontViewControllerVertically: true,
    .frontViewShadowRadius: 10,
    .frontViewShadowOffset: CGSize(width: 0, height: 4),
    .frontViewShadowOpacity: 0.5,
    .frontViewShadowColor: UIColor.black
]
```

위의 설정을 사용하여 PKRevealController의 동작 및 추가적인 애니메이션 효과를 변경할 수 있습니다.

## 결론

이렇게 하면 Swift에서 PKRevealController와 함께 애니메이션 효과를 구현할 수 있습니다. PKRevealController를 사용하여 사용자 정의 가능한 슬라이딩 메뉴를 만들어 앱에 세련된 UI를 추가할 수 있습니다. 자세한 내용은 PKRevealController의 공식 문서를 참조하시기 바랍니다.

참고 자료:
- PKRevealController GitHub 페이지: [https://github.com/pkluz/PKRevealController](https://github.com/pkluz/PKRevealController)
- Cocoapods: [https://cocoapods.org/](https://cocoapods.org/)