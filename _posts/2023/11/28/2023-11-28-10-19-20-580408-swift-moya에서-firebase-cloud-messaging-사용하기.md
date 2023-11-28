---
layout: post
title: "[swift] Swift Moya에서 Firebase Cloud Messaging 사용하기"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

Firebase Cloud Messaging (FCM)은 앱 개발자가 앱 사용자들에게 푸시 알림을 보낼 수 있는 플랫폼입니다. Moya는 Swift로 작성된 네트워크 추상화 라이브러리로, FCM을 Swift Moya에서 사용하려면 몇 가지 설정이 필요합니다.

## 1. Firebase 설정

FCM을 사용하려면 먼저 Firebase 프로젝트를 만들고 FCM을 활성화해야 합니다. Firebase 콘솔에서 프로젝트를 생성하고, iOS 앱에 해당 프로젝트를 연결하세요. Firebase에서 제공하는 `GoogleService-Info.plist` 파일을 다운로드한 후, 프로젝트에 추가해야 합니다.

## 2. Moya에 FCM을 위한 Provider 추가

Moya를 사용하여 FCM을 사용하려면 Firebase의 `MessagingDelegate`를 구현해야 합니다. 이를 위해 `FirebaseMessagingProvider`라는 Moya에서 사용 가능한 커스텀 provider를 생성할 수 있습니다.

```swift
import FirebaseMessaging
import Moya

final class FirebaseMessagingProvider: MoyaProvider<MultiTarget> {
    
    init() {
        let configuration = URLSessionConfiguration.default
        configuration.requestCachePolicy = .reloadIgnoringLocalCacheData
        super.init(configuration: configuration)
    }
    
    func sendMessage(_ message: String, to token: String, completion: @escaping (_ success: Bool) -> Void) {
        let target = MultiTarget(FirebaseMessagingEndpoint.sendMessage(message: message, to: token))
        request(target) { result in
            switch result {
            case .success:
                completion(true)
            case .failure:
                completion(false)
            }
        }
    }
}

enum FirebaseMessagingEndpoint: TargetType {
    
    case sendMessage(message: String, to: String)
    
    var baseURL: URL {
        return URL(string: "https://fcm.googleapis.com/fcm/")!
    }
    
    var path: String {
        switch self {
        case .sendMessage:
            return "send"
        }
    }
    
    var method: Moya.Method {
        return .post
    }
    
    var sampleData: Data {
        return Data()
    }
    
    var task: Task {
        switch self {
        case .sendMessage(let message, let to):
            let parameters: [String: Any] = [
                "to": to,
                "notification": ["body": message],
                "priority": "high"
            ]
            return .requestParameters(parameters: parameters, encoding: JSONEncoding.default)
        }
    }
    
    var headers: [String: String]? {
        return [
            "Content-Type": "application/json",
            "Authorization": "key=YOUR_SERVER_KEY"
        ]
    }
}
```

위의 코드에서 `Authorization` 헤더에는 Firebase Console에서 받은 서버 키를 사용해야 합니다.

## 3. FCM 메시지 보내기

이제 FCM 메시지를 보낼 수 있는 `FirebaseMessagingProvider`를 사용하여 메시지를 보낼 수 있습니다. 다음은 예시 코드입니다.

```swift
let provider = FirebaseMessagingProvider()

provider.sendMessage("Hello, World!", to: "FIREBASE_DEVICE_TOKEN") { success in
    if success {
        print("Message sent successfully")
    } else {
        print("Failed to send message")
    }
}
```

`FIREBASE_DEVICE_TOKEN`은 푸시 알림을 받을 디바이스의 Firebase 토큰입니다.

이제 Swift Moya에서 Firebase Cloud Messaging을 사용하는 방법을 알았습니다. Firebase 프로젝트와 Swift Moya를 통해 앱에 푸시 알림을 구현할 수 있습니다.

## 참고 자료

- Firebase Cloud Messaging 문서: [https://firebase.google.com/docs/cloud-messaging](https://firebase.google.com/docs/cloud-messaging)
- Moya 문서: [https://github.com/Moya/Moya](https://github.com/Moya/Moya)