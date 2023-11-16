---
layout: post
title: "[swift] Firebase Realtime Database와 Swift의 연동"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase Realtime Database는 모바일 앱과 웹 앱에 실시간 데이터베이스 기능을 제공하는 클라우드 서비스입니다. 이 글에서는 Swift 언어로 Firebase Realtime Database와 어떻게 연동하는지 살펴보겠습니다.

## Firebase 프로젝트 설정

1. Firebase 콘솔에 접속하여 새로운 프로젝트를 생성합니다.
2. 프로젝트 설정 페이지에서 iOS 앱을 추가합니다. 앱에 고유한 번들 식별자를 입력하고, 프로젝트 구성 파일을 다운로드합니다.
3. 다운로드한 구성 파일을 프로젝트 폴더에 추가합니다.

## Firebase SDK 설치

Firebase SDK는 Swift 프로젝트와 Firebase 서비스 간의 통신을 용이하게 해주는 라이브러리입니다. Firebase SDK를 설치하려면 [CocoaPods](https://cocoapods.org/)을 사용하는 것이 좋습니다.

1. 프로젝트 폴더에서 터미널을 열고 아래 명령을 실행하여 CocoaPods을 초기화합니다.

```swift
pod init
```

2. 생성된 `Podfile`에 아래 내용을 추가합니다.

```swift
pod 'Firebase/Database'
```

3. 터미널에서 `pod install` 명령을 실행하여 Firebase SDK를 설치합니다.

## Firebase Realtime Database 연동

1. Xcode에서 프로젝트의 개발 환경을 엽니다.
2. Firebase 구성 파일을 프로젝트에 추가합니다. 이 파일의 이름이 `GoogleService-Info.plist`일 것입니다.
3. `AppDelegate.swift` 파일을 열고 `didFinishLaunchingWithOptions` 메서드 안에 다음 코드를 추가합니다.

```swift
import Firebase

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    return true
}
```

4. Firebase Realtime Database의 데이터를 가져오려는 Swift 파일을 열고 다음 코드를 추가합니다.

```swift
import Firebase

let ref = Database.database().reference()

ref.child("users").observeSingleEvent(of: .value) { (snapshot) in
    guard let users = snapshot.value as? [String: Any] else { return }
    for (key, value) in users {
        print("Key: \(key), Value: \(value)")
    }
}
```

위의 코드는 "users"라는 데이터베이스 경로의 데이터를 한 번만 가져오는 예시입니다. 데이터베이스에 변경사항이 발생하면 콜백 메서드가 자동으로 호출되며 새로운 값을 가져옵니다.

이제 Firebase Realtime Database와 Swift의 연동이 완료되었습니다. 필요에 따라서 Firebase SDK의 다른 기능들도 사용할 수 있습니다.

Firebase Realtime Database와 관련된 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/database)를 참고하세요.