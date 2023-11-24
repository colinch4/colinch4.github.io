---
layout: post
title: "[swift] Firebase Authentication을 사용한 구글 및 페이스북 로그인 기능 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

모바일 앱을 개발하다보면 사용자 인증과 관련된 기능이 필요할 때가 많습니다. Firebase는 이를 간편하게 구현할 수 있는 기능을 제공하고 있습니다. 이번 글에서는 Firebase Authentication을 이용하여 구글 및 페이스북 로그인 기능을 구현하는 방법에 대해 알아보겠습니다.

## Firebase 프로젝트 설정

먼저, Firebase 콘솔에서 Firebase 프로젝트를 생성하고 앱을 추가합니다. 그런 다음, 앱 설정에서 각각의 서비스(구글, 페이스북)에 대한 인증 정보를 등록해야 합니다. 구글의 경우에는 Google Sign-In API를, 페이스북의 경우에는 Facebook Login API를 활성화한 후, 인증 정보를 등록해야 합니다.

## Firebase SDK 및 플러그인 추가

Firebase Authentication을 사용하기 위해 해당 플랫폼에 맞는 Firebase SDK와 플러그인을 추가해야 합니다. Swift에서는 Firebase iOS SDK를 사용하고, Firebase Authentication을 사용하기 위해 FirebaseAuth 라이브러리를 추가해야 합니다. 

먼저, `Podfile`에 다음과 같이 Firebase 관련 라이브러리를 추가합니다.

```swift
pod 'Firebase/Analytics'
pod 'Firebase/Auth'
```

그런 다음, 터미널을 열고 다음 명령어를 실행하여 라이브러리를 설치합니다.

```bash
$ pod install
```

## 사용자 인증 흐름 구성

Firebase Authentication을 사용한 사용자 인증 흐름은 다음과 같습니다.

1. 사용자가 구글 또는 페이스북 로그인 버튼을 클릭합니다.
2. Firebase Authentication을 사용하여 사용자 인증 플로우를 시작합니다.
3. 사용자가 로그인을 완료하면 Firebase에서 제공하는 사용자 인증 정보를 반환합니다.
4. 앱은 이 정보를 사용하여 사용자를 인증하고, 필요한 작업을 수행합니다.

## 구글 로그인 구현

구글 로그인을 구현하기 위해서는 Google SignIn SDK를 사용해야 합니다. 먼저, Firebase 콘솔에서 구글 로그인에 대한 인증 정보를 등록해야 합니다.

다음으로, Xcode에서 `Info.plist` 파일을 열고 다음 내용을 추가합니다.

```xml
<key>CFBundleURLTypes</key>
<array>
	<dict>
		<key>CFBundleTypeRole</key>
		<string>Editor</string>
		<key>CFBundleURLName</key>
		<string>[Firebase 앱 ID]</string>
		<key>CFBundleURLSchemes</key>
		<array>
			<string>com.googleusercontent.apps.[Firebase 앱 ID]</string>
		</array>
	</dict>
</array>
```

`[Firebase 앱 ID]`를 Firebase 콘솔에서 확인해야 합니다.

그리고, `AppDelegate.swift` 파일을 열고 다음 코드를 추가합니다.

```swift
import UIKit
import Firebase
import GoogleSignIn

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate, GIDSignInDelegate {
  func application(_ application: UIApplication,
                   didFinishLaunchingWithOptions launchOptions:
                       [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    GIDSignIn.sharedInstance().clientID = FirebaseApp.app()?.options.clientID
    GIDSignIn.sharedInstance().delegate = self

    return true
  }

  func application(_ app: UIApplication, open url: URL,
                     options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    return GIDSignIn.sharedInstance().handle(url,
        sourceApplication: options[UIApplication.OpenURLOptionsKey.sourceApplication] as? String,
        annotation: options[UIApplication.OpenURLOptionsKey.annotation])
  }

  func sign(_ signIn: GIDSignIn!, didSignInFor user: GIDGoogleUser!, withError error: Error?) {
    if let error = error {
      print(error.localizedDescription)
      return
    }
    guard let authentication = user.authentication else { return }
    let credential = GoogleAuthProvider.credential(withIDToken: authentication.idToken,
                                                    accessToken: authentication.accessToken)
    Auth.auth().signIn(with: credential) { (authResult, error) in
      if let error = error {
        print(error.localizedDescription)
        return
      }
      // 인증이 완료되었으므로 추가 작업 수행
    }
  }
}
```

마지막으로, 로그인 버튼을 추가하고 눌렀을 때 구글 인증 흐름을 시작하는 코드를 작성합니다.

```swift
import UIKit
import GoogleSignIn

class LoginViewController: UIViewController, GIDSignInUIDelegate {
  override func viewDidLoad() {
    super.viewDidLoad()

    GIDSignIn.sharedInstance().uiDelegate = self
  }

  @IBAction func signInWithGoogle(_ sender: Any) {
    GIDSignIn.sharedInstance().signIn()
  }
}
```

## 페이스북 로그인 구현

페이스북 로그인을 구현하기 위해서는 Facebook SDK를 사용해야 합니다. 먼저, Firebase 콘솔에서 페이스북 로그인에 대한 인증 정보를 등록해야 합니다.

다음으로, Xcode에서 `Info.plist` 파일을 열고 다음 내용을 추가합니다.

```xml
<key>CFBundleURLTypes</key>
<array>
  <dict>
	<key>CFBundleURLName</key>
    <string>[연동한 Facebook 앱 ID]</string>
	<key>CFBundleURLSchemes</key>
    <array>
	  <string>fb[연동한 Facebook 앱 ID]</string>
	</array>
  </dict>
</array>
<key>FacebookAppID</key>
<string>[연동한 Facebook 앱 ID]</string>
<key>FacebookDisplayName</key>
<string>[연동한 Facebook 앱 이름]</string>
```

`[연동한 Facebook 앱 ID]`와 `[연동한 Facebook 앱 이름]`은 Facebook 개발자 사이트에서 확인할 수 있습니다.

그리고, `AppDelegate.swift` 파일을 열고 다음 코드를 추가합니다.

```swift
import UIKit
import Firebase
import FBSDKCoreKit

@UIApplicationMain
class AppDelegate: UIResponder, UIApplicationDelegate {
...

  func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    FirebaseApp.configure()
    ApplicationDelegate.shared.application(application, didFinishLaunchingWithOptions: launchOptions)
    return true
  }

  func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    return ApplicationDelegate.shared.application(app, open: url, options: options)
  }
...
}
```

마지막으로, 로그인 버튼을 추가하고 눌렀을 때 페이스북 인증 흐름을 시작하는 코드를 작성합니다.

```swift
import UIKit
import FBSDKLoginKit
import Firebase

class LoginViewController: UIViewController, LoginButtonDelegate {
  override func viewDidLoad() {
    super.viewDidLoad()

    let loginButton = FBLoginButton()
    loginButton.center = view.center
    loginButton.delegate = self
    view.addSubview(loginButton)
  }

  func loginButton(_ loginButton: FBLoginButton, didCompleteWith result: LoginManagerLoginResult?, error: Error?) {
    if let error = error {
      print(error.localizedDescription)
      return
    }
    guard let result = result, !result.isCancelled else { return }
    let credential = FacebookAuthProvider.credential(withAccessToken: AccessToken.current!.tokenString)
    Auth.auth().signIn(with: credential) { (authResult, error) in
      if let error = error {
        print(error.localizedDescription)
        return
      }
      // 인증이 완료되었으므로 추가 작업 수행
    }
  }

  func loginButtonDidLogOut(_ loginButton: FBLoginButton) {
    // 로그아웃 처리
  }
}
```

## 결론

Firebase Authentication을 사용하여 구글 및 페이스북 로그인 기능을 구현하는 방법을 알아보았습니다. 이를 통해 사용자 인증에 대한 복잡한 작업을 간편하게 처리할 수 있습니다. Firebase의 다양한 인증 기능을 활용하여 앱의 사용자 경험을 향상시킬 수 있습니다. 

더 자세한 내용은 [Firebase Authentication 문서](https://firebase.google.com/docs/auth)를 참고하시기 바랍니다.