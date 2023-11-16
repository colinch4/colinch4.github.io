---
layout: post
title: "[swift] SwiftUI에서 Firebase Authentication 구현하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase는 구글에서 제공하는 모바일 및 웹 애플리케이션 개발 플랫폼입니다. Firebase Authentication은 Firebase의 인증 서비스로 사용자 인증 및 관리를 쉽게 구현할 수 있게 해줍니다. 

이 글에서는 SwiftUI를 사용하여 iOS 앱에서 Firebase Authentication을 구현하는 방법을 알아보겠습니다.

## 1. Firebase 프로젝트 생성 및 설정

Firebase 콘솔에 접속하여 새 프로젝트를 생성한 후, iOS 앱을 추가합니다. Bundle Identifier를 입력해야 합니다. 이 Bundle Identifier는 앱의 고유 식별자로 사용됩니다.

Firebase SDK를 다운로드하고, 프로젝트에서 생성한 Firebase 구성 파일(`GoogleService-Info.plist`)을 추가해줍니다.

## 2. Firebase SDK 및 인증 패키지 추가

iOS 프로젝트의 `Podfile`에 Firebase SDK와 인증 패키지를 추가합니다.

```swift
platform :ios, '13.0'

target 'YourApp' do
  use_frameworks!

  # Add Firebase pods
  pod 'Firebase/Analytics'
  pod 'Firebase/Auth'
end
```

터미널에서 `pod install` 명령어를 실행하여 패키지를 설치합니다.

## 3. Firebase 인증 구현

Firebase 인증을 사용하기 위해 당신의 SwiftUI 앱에 Firebase 구성을 추가해야 합니다. 

Firebase 초기화를 위해 `AppDelegate`에서 `FirebaseApp.configure()`를 호출합니다.

```swift
import Firebase

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
  func application(_ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions:
      [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    return true
  }
}
```

SwiftUI 앱의 `SceneDelegate`에서 `FirebaseApp.configure()`를 호출합니다.

```swift
import SwiftUI
import Firebase

class SceneDelegate: UIResponder, UIWindowSceneDelegate {
  var window: UIWindow?
  func scene(_ scene: UIScene,
    willConnectTo session: UISceneSession,
    options connectionOptions: UIScene.ConnectionOptions) {
    FirebaseApp.configure()
    // ...
  }
}
```

Firebase 인증을 사용하여 사용자를 생성하거나 로그인하는 등의 작업을 수행할 때, `FirebaseAuth`를 사용합니다. 

```swift
import Firebase

class AuthManager {
  let auth = Auth.auth()
  
  func createUser(email: String, password: String,
    completion: @escaping (Bool, Error?) -> Void) {
    auth.createUser(withEmail: email, password: password) { (result, error) in
      if let error = error {
        completion(false, error)
        return
      }
      completion(true, nil)
    }
  }
  
  func signIn(email: String, password: String,
    completion: @escaping (Bool, Error?) -> Void) {
    auth.signIn(withEmail: email, password: password) { (result, error) in
      if let error = error {
        completion(false, error)
        return
      }
      completion(true, nil)
    }
  }
  
  // ... (기타 인증 관련 메서드 구현)
}
```

위와 같이 `AuthManager` 클래스를 만들어 인증 관련 작업을 처리할 수 있습니다.

## 4. 사용자 인증화면 구현

SwiftUI에서 사용자 인터페이스를 구성하기 위해 `View` 프로토콜을 채택하는 구조체나 클래스를 사용합니다. 아래는 사용자 로그인을 위한 화면을 구현한 예시입니다.

```swift
import SwiftUI

struct LoginView: View {
  @State private var email = ""
  @State private var password = ""
  
  private let authManager = AuthManager()
  
  var body: some View {
    VStack {
      Text("로그인")
        .font(.largeTitle)
        .bold()
        .padding()
      
      TextField("이메일", text: $email)
        .padding()
      
      SecureField("패스워드", text: $password)
        .padding()
      
      Button(action: {
        authManager.signIn(email: email, password: password) { success, error in
          // 로그인 결과 처리
        }
      }) {
        Text("로그인")
          .bold()
          .font(.title)
          .frame(minWidth: 0, maxWidth: .infinity)
          .padding()
          .foregroundColor(.white)
          .background(Color.blue)
          .cornerRadius(40)
      }
      // ... (다른 UI 요소 구현)
    }
    .padding()
  }
}
```

위의 예시에서는 `@State` 속성을 사용하여 사용자가 입력한 이메일과 패스워드 값을 저장하고, `AuthManager`의 `signIn` 메서드를 호출하여 로그인을 수행합니다.

위 예시처럼 `TextField`와 `SecureField`를 사용하여 사용자의 입력을 받을 수 있습니다. `Button`을 통해 사용자의 로그인 버튼 클릭을 처리할 수 있습니다.

Firebase Authentication을 사용하여 회원 가입이나 로그인 기능을 간단하게 구현할 수 있습니다. 참고로, Firebase Authentication은 이메일/패스워드 인증뿐만 아니라 다른 소셜 로그인 인증 방식도 지원합니다.

자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/auth)를 참조하십시오.