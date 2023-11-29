---
layout: post
title: "[swift] PromiseKit와 함께 사용되는 디자인 패턴 소개 (ex. MVVM, VIPER 등)"
description: " "
date: 2023-11-29
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift 언어에서 PromiseKit 라이브러리를 사용하면서 유용하게 적용할 수 있는 디자인 패턴들에 대해 알아보겠습니다. PromiseKit는 비동기 작업을 처리하는데 도움이 되는 라이브러리로, 코드를 깔끔하게 구성하고 유지하기 위해 다양한 디자인 패턴들과 함께 사용될 수 있습니다.

## 1. MVVM (Model-View-ViewModel)

MVVM은 애플리케이션의 코드를 보다 재사용 가능하고 테스트하기 쉬운 구조로 만들기 위한 디자인 패턴입니다. PromiseKit와 함께 MVVM 패턴을 사용하면 비동기 작업의 결과를 ViewModel에서 처리하고, View는 ViewModel에 바인딩하여 UI를 업데이트할 수 있습니다.

PromiseKit의 `.then` 메서드를 사용하여 비동기 작업의 결과를 ViewModel에 전달하고, ViewModel은 해당 결과를 가공하여 View에 반영하는 역할을 수행합니다. 이 방식으로 코드를 구성하면 UI와 비즈니스 로직이 분리되어 개발과 유지보수가 훨씬 용이해집니다.

```swift
func fetchUser() -> Promise<User> {
    return Promise { resolver in
        APIClient.shared.getUser { result in
            switch result {
            case .success(let user):
                resolver.fulfill(user)
            case .failure(let error):
                resolver.reject(error)
            }
        }
    }
}

// ViewModel
class UserViewModel {
    private var user: User?
    
    func fetchUser() {
        fetchUser()
            .done { user in
                self.user = user
            }
            .catch { error in
                print(error.localizedDescription)
            }
    }
    
    // UI에 바인딩되는 속성들
    var userName: String? {
        return user?.name
    }
}
```

## 2. VIPER (View, Interactor, Presenter, Entity, Router)

VIPER는 애플리케이션을 각각의 역할에 따라 컴포넌트로 분리하여 개발하는 디자인 패턴입니다. PromiseKit와 함께 사용하면 비동기 작업을 각 컴포넌트에 분산시켜 코드를 간결하게 유지할 수 있습니다.

각각의 컴포넌트는 독립적인 역할과 책임을 가지며, 비동기 작업부터 UI 업데이트까지의 흐름이 한눈에 들어옵니다. PromiseKit에서 제공하는 `.map`이나 `.done` 메서드를 활용하면 각 컴포넌트에서 동작을 처리하고 다음 컴포넌트로 결과를 전달할 수 있습니다.

```swift
// Interactor
class UserInteractor {
    func fetchUser() -> Promise<User> {
        return Promise { resolver in
            APIClient.shared.getUser { result in
                switch result {
                case .success(let user):
                    resolver.fulfill(user)
                case .failure(let error):
                    resolver.reject(error)
                }
            }
        }
    }
}

// Presenter
class UserPresenter {
    private var user: User?
    
    func fetchUser() {
        interactor.fetchUser()
            .done { user in
                self.user = user
                self.view?.updateUI(with: user)
            }
            .catch { error in
                self.view?.showError(error)
            }
    }
}

// View
class UserViewController: UIViewController {
    private var presenter: UserPresenter!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        presenter.fetchUser()
    }
    
    func updateUI(with user: User) {
        // UI 업데이트 로직
    }
    
    func showError(_ error: Error) {
        // 에러 처리 로직
    }
}
```

## 참고 자료

- [PromiseKit 공식 문서](https://github.com/mxcl/PromiseKit)
- [Swift 애플리케이션 아키텍처 디자인 패턴 - MVVM](https://velog.io/@kesl6th/swift-mvvm-2)
- [iOS 모듈화의 최신 트렌드 - VIPER 구조](https://velog.io/@jwlee230/series/iOS-%EB%AA%A8%EB%93%88%ED%99%94%EC%9D%98-%EC%B5%9C%EC%97%B0-%ED%8A%B8%EB%A0%8C%EB%93%9C-VIPER-%EA%B5%AC%EC%A1%B0-%EC%84%A4%EB%AA%85)