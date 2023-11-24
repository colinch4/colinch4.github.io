---
layout: post
title: "[swift] Firebase In-App Messaging을 통한 앱 내 메시지 전송 기능 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Firebase는 Google의 모바일 개발 플랫폼으로, 다양한 기능을 제공합니다. 그 중 Firebase In-App Messaging은 앱 내에서 사용자에게 메시지를 보낼 수 있는 강력한 기능입니다. 이 기능을 사용하여 앱 내 메시지 전송 기능을 구현할 수 있습니다.

## Firebase 프로젝트 설정

Firebase In-App Messaging을 사용하기 위해서는 Firebase 프로젝트에 앱을 추가해야 합니다. Firebase 콘솔에서 "프로젝트 추가"를 선택하고, 앱의 패키지 이름을 입력한 후, 구성 파일을 다운로드 받습니다. 이 파일은 나중에 앱에서 Firebase에 연결할 때 사용합니다.

## Firebase SDK 설정

Firebase SDK를 추가하기 위해, 프로젝트의 `Podfile` 파일에 다음과 같은 내용을 추가합니다.

```swift
pod 'Firebase/InAppMessaging'
```

파일을 저장한 후, 터미널에서 `pod install` 명령어를 실행하여 Firebase SDK를 설치합니다.

## 메시지 템플릿 만들기

Firebase In-App Messaging을 사용하여 앱 내 메시지를 전송하려면, 먼저 메시지 템플릿을 만들어야 합니다. 콘솔에서 "In-App Messaging"을 선택하고, "새로운 템플릿 만들기"를 선택합니다.

템플릿을 만들 때는 다음과 같은 정보를 입력해야합니다:

- 템플릿 이름
- 메시지 유형 (배너, 모달, 이미지 등)
- 메시지 내용 (텍스트, 이미지 등)
- 화면 타겟팅 (어떤 화면에서 메시지를 보여줄 것인지)

## 앱에서 Firebase 초기화 및 메시지 전송

Firebase SDK를 사용하여 앱에서 Firebase를 초기화하고, 메시지를 전송할 준비를 해야합니다. 앱의 `AppDelegate` 파일에서 다음과 같이 Firebase를 초기화합니다.

```swift
import Firebase

...

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    return true
}
```

메시지를 전송하려면, 다음의 코드를 사용하면 됩니다:

```swift
import FirebaseInAppMessaging

...

let inAppMessaging = InAppMessaging.inAppMessaging()

// 템플릿 이름을 사용하여 메시지를 보냅니다.
inAppMessaging.triggerEvent("your_template_name")
```

## 결론

Firebase In-App Messaging을 사용하면, 앱 내에서 사용자에게 메시지를 전송하는 기능을 쉽게 구현할 수 있습니다. Firebase 프로젝트 설정, SDK 설정, 메시지 템플릿 만들기, 앱에서 Firebase 초기화와 메시지 전송 단계를 따라하면 됩니다.

더 자세한 내용은 [Firebase In-App Messaging 문서](https://firebase.google.com/docs/in-app-messaging)를 참고하시기 바랍니다.