---
layout: post
title: "[swift] Firebase Authentication을 활용한 Swift 앱 로그인 기능 구현"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase Authentication은 사용자 인증을 위한 플랫폼으로, Swift 앱에서 사용자 로그인 기능을 구현할 수 있도록 도와줍니다. 이번 포스트에서는 Firebase Authentication을 활용하여 Swift 앱의 로그인 기능을 구현하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

먼저, Firebase 프로젝트를 생성하고 앱을 등록해야 합니다. Firebase 콘솔에서 프로젝트를 생성한 다음, iOS 앱을 추가합니다. 앱에 대한 패키지 이름을 입력하고, `GoogleService-Info.plist` 파일을 다운로드하여 프로젝트에 추가합니다.

## Firebase SDK 설치

Firebase Authentication을 사용하기 위해 `Firebase/Auth` 라이브러리를 설치해야 합니다. 프로젝트의 `Podfile`에 다음을 추가하고 터미널에서 `pod install` 명령을 실행합니다.

```
pod 'Firebase/Auth'
```

## 로그인 View 컨트롤러 생성

로그인 기능을 구현하기 위해, 새로운 View 컨트롤러를 생성합니다. 로그인 화면의 UI를 디자인하고, 이를 위한 IBOutlet들을 추가합니다.

## Firebase Authentication 초기화

Firebase Authentication을 초기화하기 위해, AppDelegate에서 `FirebaseApp.configure()`를 호출합니다.

## 이메일/비밀번호 로그인

이메일과 비밀번호를 사용한 로그인 기능을 구현해보겠습니다. 로그인 버튼의 액션 메소드에서 다음 코드를 추가합니다.

```swift
Auth.auth().signIn(withEmail: email, password: password) { (authResult, error) in
    if let error = error {
        // 로그인 실패 시 처리
        print("로그인 실패: \(error.localizedDescription)")
    } else {
        // 로그인 성공 시 처리
        print("로그인 성공!")
        
        // 로그인 후 화면 전환 등의 처리
    }
}
```

이메일과 비밀번호를 사용하여 `Auth.auth().signIn(withEmail:password:completion:)` 메소드를 호출하고, 로그인 결과에 따라 성공 또는 실패 처리를 합니다.

## 페이스북 로그인

페이스북을 사용한 로그인 기능을 구현하려면, Firebase 콘솔에서 페이스북 인증을 설정해야 합니다. 설정이 완료되면, 로그인 버튼의 액션 메소드에서 다음 코드를 추가합니다.

```swift
let loginManager = LoginManager()
loginManager.logIn(permissions: ["public_profile", "email"], from: self) { (result, error) in
    if let error = error {
        // 로그인 실패 시 처리
        print("페이스북 로그인 실패: \(error.localizedDescription)")
    } else if result?.isCancelled == true {
        // 로그인 취소 시 처리
        print("페이스북 로그인 취소")
    } else {
        // 로그인 성공 시 Firebase로 토큰 전달
        let credential = FacebookAuthProvider.credential(withAccessToken: AccessToken.current!.tokenString)
        Auth.auth().signIn(with: credential) { (authResult, error) in
            if let error = error {
                // Firebase 로그인 실패 시 처리
                print("Firebase 로그인 실패: \(error.localizedDescription)")
            } else {
                // 로그인 성공 시 처리
                print("페이스북 로그인 성공!")
                
                // 로그인 후 화면 전환 등의 처리
            }
        }
    }
}
```

페이스북 SDK의 `LoginManager`를 사용하여 사용자를 로그인하고, 로그인 결과에 따라 성공 또는 실패 처리를 합니다. 성공 시 Firebase로 토큰을 전달하여 Firebase Authentication으로 로그인합니다.

## 구글 로그인

구글을 사용한 로그인 기능을 구현하려면, Firebase 콘솔에서 구글 인증을 설정해야 합니다. 설정이 완료되면, 로그인 버튼의 액션 메소드에서 다음 코드를 추가합니다.

```swift
let googleSignIn = GIDSignIn.sharedInstance()
googleSignIn?.presentingViewController = self
googleSignIn?.signIn()
```

구글 SDK의 `GIDSignIn` 인스턴스를 사용하여 사용자를 로그인하고, 인증 플로우가 완료되면 Firebase로 토큰을 전달하여 Firebase Authentication으로 로그인합니다.

이처럼 Firebase Authentication을 활용하여 Swift 앱의 로그인 기능을 구현할 수 있습니다. Firebase는 이메일/비밀번호, 페이스북, 구글 외에도 다양한 인증 방법을 제공하므로, 필요한 경우 참고 자료를 찾아보시기 바랍니다.

## 참고 자료

- Firebase Authentication 문서: [https://firebase.google.com/docs/auth](https://firebase.google.com/docs/auth)
- Firebase iOS 샘플 코드: [https://github.com/firebase/quickstart-ios/tree/master/authentication](https://github.com/firebase/quickstart-ios/tree/master/authentication)
- 스위프트 개발자 포럼: [https://swiftdev.kr/](https://swiftdev.kr/)