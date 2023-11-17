---
layout: post
title: "[swift] - Swift에서 AlamofireNetworkActivityIndicator를 사용하여 네트워크 활동 로그에 타임스탬프 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

개발 중인 앱에서 네트워크 활동을 모니터링하고 타임스탬프를 로그에 추가하려면, AlamofireNetworkActivityIndicator를 사용할 수 있습니다. 이 라이브러리는 Alamofire를 확장하여 네트워크 활동을 추적하고 활성화된 네트워크 요청을 표시하는 데 도움을 줍니다.

## AlamofireNetworkActivityIndicator 라이브러리 설치하기

먼저, AlamofireNetworkActivityIndicator를 설치해야 합니다. CocoaPods를 사용하는 경우, Podfile에 다음과 같이 라이브러리를 추가합니다:

```ruby
pod 'Alamofire'
pod 'AlamofireNetworkActivityIndicator'
```

그런 다음, 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## AlamofireNetworkActivityIndicator 사용하기

이제 프로젝트에서 Alamofire를 사용하고 있으며, 네트워크 활동 로그에 타임스탬프를 추가하려는 경우, 다음과 같이 코드를 추가할 수 있습니다:

```swift
import Alamofire
import AlamofireNetworkActivityIndicator

class MyNetworkingManager {
    
    static let shared = MyNetworkingManager()
    
    private init() {
        // AlamofireNetworkActivityIndicator 설정
        NetworkActivityIndicatorManager.shared.isEnabled = true
        NetworkActivityIndicatorManager.shared.startDelay = 0.2
        NetworkActivityIndicatorManager.shared.completionDelay = 0.2
    }
    
    func makeNetworkRequest() {
        // 네트워크 요청 전에 타임스탬프 로그 작성
        let timestamp = DateFormatter.localizedString(from: Date(), dateStyle: .medium, timeStyle: .medium)
        print("Network request started at: \(timestamp)")
        
        // Alamofire를 사용하여 네트워크 요청 수행
        AF.request("https://api.example.com").responseJSON { (response) in
            // 네트워크 요청 완료 후 타임스탬프 로그 작성
            let timestamp = DateFormatter.localizedString(from: Date(), dateStyle: .medium, timeStyle: .medium)
            print("Network request completed at: \(timestamp)")
        }
    }
}
```

위의 코드에서는 AlamofireNetworkActivityIndicator를 사용하기 전에 `NetworkActivityIndicatorManager.shared.isEnabled`를 `true`로 설정하고, `startDelay`와 `completionDelay` 값을 조정하여 인디케이터의 시작 및 완료 지연 시간을 설정합니다. 그런 다음, `makeNetworkRequest()` 함수에서 네트워크 요청 전후에 타임스탬프를 로그로 작성합니다.

이제 `MyNetworkingManager.shared.makeNetworkRequest()`를 호출하여 네트워크 요청을 수행하면, 앱의 네트워크 활동 로그에 타임스탬프가 추가될 것입니다.

## 결론

이 가이드에서는 AlamofireNetworkActivityIndicator를 사용하여 Swift 앱에서 네트워크 활동 로그에 타임스탬프를 추가하는 방법을 살펴보았습니다. 이를 통해 앱의 네트워크 동작을 모니터링하고 디버깅하는 데 도움이 될 것입니다.

더 많은 정보와 옵션에 대해서는 [AlamofireNetworkActivityIndicator GitHub 페이지](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)를 참조하세요.