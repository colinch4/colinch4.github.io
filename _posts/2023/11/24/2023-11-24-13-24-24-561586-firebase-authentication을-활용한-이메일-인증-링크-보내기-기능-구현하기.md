---
layout: post
title: "[swift] Firebase Authentication을 활용한 이메일 인증 링크 보내기 기능 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Firebase는 다양한 기능을 제공하는 백엔드 서비스입니다. Firebase Authentication을 활용하면 사용자 인증 기능을 손쉽게 구현할 수 있습니다. 이 중에서 이메일을 이용한 인증 링크 보내기 기능을 구현하는 방법에 대해 알아보겠습니다.

## 1. Firebase 프로젝트 생성 및 설정

먼저 Firebase 콘솔에 접속하여 새로운 프로젝트를 생성합니다. 그리고 "Authentication" 메뉴로 이동하여 "이메일/비밀번호"를 선택한 후, "이메일 링크 보내기" 옵션을 활성화합니다.

## 2. Firebase SDK 설치 및 초기 설정

Firebase SDK를 프로젝트에 추가하고, AppDelegate.swift 파일에서 Firebase를 초기화해야합니다. 이를 위해 다음과 같은 코드를 추가합니다:

```swift
import Firebase

// ...

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    return true
}
```

## 3. 이메일 인증 링크 발송하기

Firebase 에서 제공하는 인증 메일 전송 메서드를 이용하여, 이메일 인증 링크를 보내는 기능을 구현할 수 있습니다. 다음은 이를 수행하는 코드입니다:

```swift
import FirebaseAuth

// ...

func sendEmailVerification() {
    if let user = Auth.auth().currentUser {
        user.sendEmailVerification { (error) in
            if let error = error {
                print("Error sending email verification: \(error)")
                return
            }
            print("Email verification sent.")
        }
    }
}
```

위의 코드에서 `Auth.auth().currentUser` 를 통해 현재 로그인된 사용자를 가져오고, `sendEmailVerification` 메서드를 호출하여 이메일 인증 메일을 전송합니다. 이메일 전송에 실패한 경우 `error` 객체가 반환됩니다.

## 4. 이메일 인증 확인하기

이메일을 통해 인증 링크를 클릭한 사용자가 인증되었는지 확인하기 위해서는 다음과 같이 코드를 작성할 수 있습니다:

```swift
import FirebaseAuth

// ...

func checkEmailVerification() {
    if let user = Auth.auth().currentUser {
        user.reload { (error) in
            if let error = error {
                print("Error reloading user: \(error)")
                return
            }
            
            if user.isEmailVerified {
                print("Email verification successful.")
            } else {
                print("Email verification not completed.")
            }
        }
    }
}
```

위의 코드에서 `user.reload` 메서드를 호출하여 사용자 정보를 새로고침하고, `user.isEmailVerified` 속성을 통해 이메일 인증 상태를 확인할 수 있습니다.

## 마무리

위의 단계를 따라하면 Firebase Authentication을 활용한 이메일 인증 링크 보내기 기능을 구현할 수 있습니다. Firebase의 다양한 기능들을 적절히 활용하여 사용자 인증 기능을 간편하게 구현해보세요.

참고문서: [Firebase Authentication Documentation](https://firebase.google.com/docs/auth)