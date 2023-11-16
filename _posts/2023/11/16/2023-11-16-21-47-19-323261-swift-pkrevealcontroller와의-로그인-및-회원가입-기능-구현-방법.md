---
layout: post
title: "[swift] Swift PKRevealController와의 로그인 및 회원가입 기능 구현 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift를 사용하여 PKRevealController와 함께 로그인 및 회원가입 기능을 구현하는 방법에 대해 알아보겠습니다.

## 1. PKRevealController 설정

먼저, PKRevealController를 사용하기 위해 해당 라이브러리를 프로젝트에 추가해야 합니다. Cocoapods를 이용한다면 `Podfile`에 다음과 같이 추가하고 `pod install` 명령어를 사용하여 설치합니다.

```swift
pod 'PKRevealController'
```

다음으로, `PKRevealController` 객체를 생성하고 기본적인 설정을 해줍니다. 예를 들어, 로그인 및 회원가입 기능을 위한 메인 뷰 컨트롤러를 생성하고 네비게이션 컨트롤러에 Embed하여 사용할 수 있습니다.

```swift
import PKRevealController

class MainViewController: PKRevealController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let mainStoryboard = UIStoryboard(name: "MainStoryboard", bundle: nil)
        let loginViewController = mainStoryboard.instantiateViewController(withIdentifier: "LoginViewController")
        let navigationController = UINavigationController(rootViewController: loginViewController)

        self.setFront(navigationController, animated: false)
    }
}
```

## 2. 로그인 및 회원가입 기능 추가

로그인 및 회원가입 기능을 구현하기 위해 필요한 화면들을 스토리보드에 추가해줍니다. 예를 들어, `LoginViewController`와 `SignupViewController`를 생성합니다.

각 화면에서는 사용자가 입력한 정보와 서버와의 통신을 통해 로그인 및 회원가입 절차를 진행합니다. 이에 대한 자세한 내용은 생략하겠습니다. 각각의 화면에서 로그인 또는 회원가입이 성공했을 경우, `MainViewController`에서 컨텐츠를 업데이트하도록 설정해야 합니다.

```swift
import PKRevealController

class LoginViewController: UIViewController {

    func loginSuccess() {
        let mainViewController = self.revealController() as! MainViewController
        mainViewController.updateContent() // 로그인 성공 후 컨텐츠 업데이트
    }
}

class SignupViewController: UIViewController {

    func signupSuccess() {
        let mainViewController = self.revealController() as! MainViewController
        mainViewController.updateContent() // 회원가입 성공 후 컨텐츠 업데이트
    }
}

extension UIViewController {

    func revealController() -> PKRevealController? {
        var viewController: UIViewController? = self
        while viewController != nil {
            if let revealController = viewController as? PKRevealController {
                return revealController
            }
            viewController = viewController?.parent
        }
        return nil
    }
}

```

## 3. 컨텐츠 업데이트

마지막으로, `MainViewController`에서 컨텐츠를 업데이트하는 함수를 구현합니다. 로그인 또는 회원가입 성공 후에 호출되어야 합니다. 예를 들어, 로그인 후에는 사용자 정보를 가져와서 화면에 표시할 수 있습니다.

```swift
import PKRevealController

class MainViewController: PKRevealController {

    //...

    func updateContent() {
        // 사용자 정보 가져오기 및 컨텐츠 업데이트
    }
}
```

이제 PKRevealController와 함께 로그인 및 회원가입 기능을 구현하는 방법을 알아보았습니다. 이를 참고하여 프로젝트에 맞게 구현해보세요!

___
## 참고 자료

- [PKRevealController GitHub Repository](https://github.com/pkluz/PKRevealController)