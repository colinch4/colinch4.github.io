---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator를 사용하여 네트워크 요청 중 Indicator의 위치를 원하는 곳으로 설정하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

네트워크 요청을 보낼 때 사용자에게 로딩 인디케이터를 표시하는 것은 사용성을 향상시킬 수 있는 좋은 방법입니다. Alamofire 라이브러리를 사용하면 간편하게 네트워크 인디케이터를 관리할 수 있습니다. AlamofireNetworkActivityIndicator를 사용하여 Indicator의 위치를 원하는 곳으로 설정하는 방법에 대해 알아보겠습니다.

먼저, Alamofire와 AlamofireNetworkActivityIndicator를 프로젝트에 추가합니다. CocoaPods를 사용한다면, Podfile에 다음과 같이 추가합니다.

```bash
pod 'Alamofire'
pod 'AlamofireNetworkActivityIndicator'
```

Podfile을 업데이트한 후, `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

그리고 나서, AppDelegate.swift 파일에서 다음 코드를 추가합니다.

```swift
import Alamofire
import AlamofireNetworkActivityIndicator

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // ...
    NetworkActivityIndicatorManager.shared.isEnabled = true
    NetworkActivityIndicatorManager.shared.startDelay = 0.2 // Indicator 표시 전 딜레이
    NetworkActivityIndicatorManager.shared.completionDelay = 0.2 // Indicator 숨김 전 딜레이
    // ...
    return true
}
```

위의 코드는 앱이 실행될 때 네트워크 인디케이터 관리자를 활성화시키고, 딜레이를 설정하는 부분입니다.

이제 Indicator를 표시하고 싶은 곳에 아래와 같이 코드를 추가하면 됩니다.

```swift
import Alamofire
import AlamofireNetworkActivityIndicator

func sendRequest() {
    NetworkActivityIndicatorManager.shared.incrementActivityCount()

    AF.request("https://api.example.com").response { response in
        // 네트워크 요청을 처리하는 코드 작성

        NetworkActivityIndicatorManager.shared.decrementActivityCount() // Indicator 감소
    }
}
```

위의 코드에서는 `NetworkActivityIndicatorManager.shared.incrementActivityCount()`로 Indicator를 증가시키고, 네트워크 요청을 보낸 후에 `NetworkActivityIndicatorManager.shared.decrementActivityCount()`로 Indicator를 감소시킵니다.

이렇게하면 네트워크 요청 중에 Indicator가 화면에 표시되고, 요청이 완료되면 Indicator가 자동으로 사라집니다.

이렇게 AlamofireNetworkActivityIndicator를 사용하면 네트워크 인디케이터의 위치를 원하는 곳으로 설정할 수 있습니다. 이는 사용자 경험을 향상시켜 앱의 성능을 개선하는데 도움이 됩니다.

자세한 내용은 [Alamofire](https://github.com/Alamofire/Alamofire)와 [AlamofireNetworkActivityIndicator](https://github.com/Alamofire/AlamofireNetworkActivityIndicator) 문서를 참고하시기 바랍니다.