---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator를 이용한 네트워크 활동 표시기에 원형 Progress 애니메이션 적용하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

네트워크 요청을 처리할 때, 사용자에게 현재 네트워크 활동을 시각적으로 알려주는 것은 매우 중요합니다. AlamofireNetworkActivityIndicator라는 라이브러리는 Alamofire와 함께 사용되어 네트워크 활동을 감지하고 시스템의 네트워크 활동 표시기를 제어할 수 있도록 해줍니다. 

이번 글에서는 AlamofireNetworkActivityIndicator를 이용하여 네트워크 활동 표시기에 원형 Progress 애니메이션을 적용하는 방법에 대해 알아보겠습니다.

## 1. Alamofire 및 AlamofireNetworkActivityIndicator 설치하기

먼저, Alamofire와 AlamofireNetworkActivityIndicator를 프로젝트에 설치해야 합니다. `Podfile`에 다음과 같이 의존성을 추가하고, `pod install` 명령을 통해 설치합니다.

```ruby
pod 'Alamofire'
pod 'AlamofireNetworkActivityIndicator'
```

## 2. AlamofireNetworkActivityIndicator 설정하기

앱을 로드할 때, `AppDelegate.swift` 파일에서 `application(_:didFinishLaunchingWithOptions:)` 메서드 내부에 다음 코드를 추가합니다.

```swift
import AlamofireNetworkActivityIndicator

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // AlamofireNetworkActivityIndicator 설정
    NetworkActivityIndicatorManager.shared.isEnabled = true
    NetworkActivityIndicatorManager.shared.startDelay = 0.1
    NetworkActivityIndicatorManager.shared.completionDelay = 0.2

    return true
}
```

위 코드에서는 `NetworkActivityIndicatorManager`의 `isEnabled` 속성을 `true`로 설정하여 활성화 시킵니다. `startDelay`와 `completionDelay` 속성은 네트워크 활동 표시기가 보여지기 전과 사라지기 전에 딜레이를 설정하는데 사용됩니다.

## 3. 원형 Progress 애니메이션 추가하기

이제 Alamofire를 사용하여 네트워크 요청을 할 때마다, 원형 Progress 애니메이션을 보여줄 수 있도록 설정해보겠습니다.

```swift
import Alamofire
import AlamofireNetworkActivityIndicator

func makeNetworkRequest() {
    let spinner = UIActivityIndicatorView(style: .whiteLarge)
    spinner.color = .gray
    spinner.startAnimating()

    AF.request("https://api.example.com/data", method: .get)
        .responseJSON { response in
            spinner.stopAnimating()
            spinner.removeFromSuperview()

            // 네트워크 요청 결과 처리
            if response.error == nil {
                // 성공적으로 데이터를 받아온 경우
            } else {
                // 요청 실패 시
            }
        }
}
```

위 코드에서는 `UIActivityIndicatorView`를 생성하여 로딩 스피너를 만들고, `startAnimating()` 메서드를 호출하여 애니메이션을 시작합니다. 네트워크 요청을 보내기 전에는 화면에 로딩 스피너가 표시됩니다.

네트워크 요청이 완료되면, `responseJSON` 클로저 내에서 로딩 스피너의 애니메이션을 멈추고 화면에서 제거합니다. 이후 요청 결과를 처리하는 코드를 작성할 수 있습니다.

## 결론

AlamofireNetworkActivityIndicator를 이용하여 네트워크 활동 표시기에 원형 Progress 애니메이션을 적용하는 방법에 대해 알아보았습니다. 이를 통해 사용자에게 네트워크 활동을 시각적으로 알리고, 더 나은 사용자 경험을 제공할 수 있습니다.

참고자료:
- [Alamofire GitHub Repository](https://github.com/Alamofire/Alamofire)
- [AlamofireNetworkActivityIndicator GitHub Repository](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)