---
layout: post
title: "[swift] Firebase Cloud Messaging을 활용한 앱 내 광고 및 프로모션 푸시 알림 전달하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Firebase Cloud Messaging (FCM)은 개발자들이 안드로이드, iOS 및 웹 앱에 푸시 알림을 보낼 수 있는 강력한 도구입니다. 이를 통해 앱 내에서 광고 및 프로모션 푸시 알림을 전달할 수 있습니다. 이번 튜토리얼에서는 Swift를 사용하여 앱 내에 FCM을 통해 광고 및 프로모션 푸시 알림을 전달하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 설정

먼저, Firebase 콘솔에서 새로운 프로젝트를 생성하고 iOS 앱을 추가해야합니다. 앱을 추가할 때, 앱 번들 ID를 올바르게 입력해야합니다.

![](https://firebase.google.com/docs/cloud-messaging/images/fig-new-project.png)

Firebase 콘솔에서 "프로젝트 설정"으로 이동하고, "클라우드 메시징" 탭을 선택합니다. 여기서 FCM 서버 키와 Google 서비스 정보 파일을 받을 수 있습니다.

## 2. 앱에 Firebase 추가

Firebase를 앱에 추가하기 위해, 최신 버전의 Firebase SDK를 사용하여 앱에 Firebase 패키지를 설치해야합니다. 이를 위해 CocoaPods를 사용하려면 `Podfile`에 다음과 같이 작성합니다:

```swift
platform :ios, '9.0'

target 'YourApp' do
  use_frameworks!

  pod 'Firebase/Core'
  pod 'Firebase/Messaging'

end
```

그리고 터미널에서 다음 명령을 실행하여 CocoaPods를 설치합니다:

```bash
$ pod install
```

그런 다음, `AppDelegate.swift` 파일을 열고 다음과 같이 Firebase를 설정합니다:

```swift
import Firebase

...

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplicationLaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    ...
}
```

이제 Firebase가 앱에 추가되었으므로 FCM을 사용하여 푸시 알림을 보낼 수 있습니다.

## 3. FCM 푸시 알림 전송

FCM을 사용하여 앱 내에서 광고 및 프로모션 푸시 알림을 전송하려면 서버에 알림을 보내는 코드가 필요합니다. 서버에서 알림을 보내는 방법에 대해 자세히 알고 싶다면, FCM을 사용하여 푸시 알림을 전송하는 서버 측 코드에 대해 알아보세요.

알림을 보내기 위해 다음 코드를 사용하여 FCM 서버에 요청을 보낼 수 있습니다:

```swift
let url = URL(string: "https://fcm.googleapis.com/fcm/send")!
let authorizationKey = "YOUR_AUTHORIZATION_KEY"
let headers = [
    "Authorization": "key=\(authorizationKey)",
    "Content-Type": "application/json"
]
let body: [String: Any] = [
    "to": "<FCM_TOKEN>",
    "notification": [
        "title": "광고 및 프로모션 알림",
        "body": "새로운 광고 및 프로모션이 있습니다!"
    ]
]

var request = URLRequest(url: url)
request.httpMethod = "POST"
request.allHTTPHeaderFields = headers
request.httpBody = try? JSONSerialization.data(withJSONObject: body)

let task = URLSession.shared.dataTask(with: request) { (data, response, error) in
    if let error = error {
        print("Error: \(error.localizedDescription)")
    } else if let data = data {
        let responseJSON = try? JSONSerialization.jsonObject(with: data, options: [])
        if let responseJSON = responseJSON as? [String: Any] {
            print("Response: \(responseJSON)")
        }
    }
}
task.resume()
```

위의 코드에서 `authorizationKey`는 Firebase 프로젝트 설정에서 얻은 FCM 서버 키를 입력해야 합니다. 또한, `FCM_TOKEN`은 푸시 알림을 수신할 기기의 FCM 토큰으로 대체해야 합니다.

## 결론

이제 Firebase Cloud Messaging을 사용하여 앱 내에서 광고 및 프로모션 푸시 알림을 전송할 준비가 되었습니다. FCM을 통해 사용자에게 앱 내에서 중요한 정보를 전달할 수 있으며, 이는 사용자들이 앱과 상호작용하고 앱을 유지하는 데 도움이 될 것입니다.

Firebase 콘솔을 통해 알림을 보낼 수도 있습니다. 기본적인 알림 템플릿을 사용하거나 사용자 정의 페이로드를 지정하여 개인화된 알림을 제공할 수 있습니다. 자세한 내용은 Firebase 공식 문서를 참조하세요.

---
### 참고 자료
- [Firebase Cloud Messaging Documentation](https://firebase.google.com/docs/cloud-messaging)
- [Setting up Firebase Cloud Messaging for iOS](https://firebase.google.com/docs/cloud-messaging/ios/client)
- [FCM HTTP Protocol](https://firebase.google.com/docs/cloud-messaging/http-server-ref)
- [Firebase Console](https://console.firebase.google.com/)