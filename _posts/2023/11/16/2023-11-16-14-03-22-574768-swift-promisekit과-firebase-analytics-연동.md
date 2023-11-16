---
layout: post
title: "[swift] Swift PromiseKit과 Firebase Analytics 연동"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase Analytics는 앱의 사용자 동작 및 사용량을 추적하는 강력한 도구입니다. PromiseKit은 비동기 작업을 보다 간편하게 처리할 수 있도록 도와주는 라이브러리입니다. 이번 튜토리얼에서는 Swift에서 PromiseKit과 Firebase Analytics을 연동하는 방법을 살펴보겠습니다.

## 1. Firebase 프로젝트 설정

먼저, Firebase 콘솔에서 새로운 프로젝트를 생성하고 iOS 앱을 추가합니다. Firebase SDK를 다운로드하고 해당 프로젝트의 GoogleService-Info.plist 파일을 Xcode 프로젝트에 추가합니다.

## 2. PromiseKit 설치

PromiseKit을 사용하기 위해 먼저 Cocoapods를 설치해야 합니다. 따라서 Podfile을 만들고 아래의 내용을 추가합니다:

```ruby
platform :ios, '9.0'
use_frameworks!

target 'YourAppName' do
    pod 'PromiseKit', '~> 6.13'
end
```

그리고 터미널에서 `pod install` 명령어를 실행하여 PromiseKit을 설치합니다.

## 3. Firebase Analytics 및 PromiseKit 연동

Firebase와 PromiseKit을 연동하기 위해, 우선 Firebase Analytics 관련 모듈을 import 해야 합니다:

```swift
import FirebaseAnalytics
import PromiseKit
```

그리고 PromiseKit을 사용하여 Firebase Analytics 이벤트를 전송하는 함수를 작성합니다:

```swift
func sendAnalyticsEvent(eventName: String) -> Promise<Void> {
    return Promise { seal in
        Analytics.logEvent(eventName, parameters: nil) { error in
            if let error = error {
                seal.reject(error)
            } else {
                seal.fulfill(())
            }
        }
    }
}
```

위의 함수는 Promise를 반환하고, 전송한 이벤트가 성공적이면 fulfill하고 오류가 발생하면 reject 합니다.

이제 해당 함수를 사용하여 Firebase Analytics 이벤트를 전송해 볼 수 있습니다. 예를 들어, 버튼을 클릭하는 동작에 대한 이벤트를 추적하려면 다음과 같이 코드를 작성할 수 있습니다:

```swift
@IBAction func buttonTapped(_ sender: UIButton) {
    sendAnalyticsEvent(eventName: "button_clicked")
        .done {
            print("Event sent successfully")
        }
        .catch { error in
            print(error.localizedDescription)
        }
}
```

위의 코드에서는 `sendAnalyticsEvent` 함수를 호출하고, 이벤트 전송이 성공하면 `.done` 블록이 실행되고, 오류가 발생하면 `.catch` 블록이 실행됩니다.

## 마무리

이렇게 Swift PromiseKit과 Firebase Analytics을 연동하는 방법을 알아보았습니다. PromiseKit을 사용하여 비동기 작업을 처리하고 Firebase Analytics을 활용하여 앱의 사용자 동작을 추적하는 것은 개발자들에게 큰 도움이 될 것입니다. 추가적인 사용법이나 설정에 대해서는 PromiseKit와 Firebase Analytics의 공식 문서를 참고하시기 바랍니다.

## 참고 자료
- [Firebase 콘솔](https://console.firebase.google.com/)
- [PromiseKit GitHub](https://github.com/mxcl/PromiseKit)
- [Firebase Analytics 문서](https://firebase.google.com/docs/analytics)