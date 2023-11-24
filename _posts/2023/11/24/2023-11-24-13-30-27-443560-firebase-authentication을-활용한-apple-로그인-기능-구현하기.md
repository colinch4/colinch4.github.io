---
layout: post
title: "[swift] Firebase Authentication을 활용한 Apple 로그인 기능 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Firebase Authentication은 앱 사용자 인증을 간편하게 구현할 수 있는 도구입니다. 이번에는 Firebase Authentication을 이용하여 Apple 로그인 기능을 구현하는 방법에 대해 알아보겠습니다.

## Prerequisites

- Firebase 프로젝트 생성 및 설정
- Xcode 설치
- Swift 프로젝트 생성

## Firebase 프로젝트 설정

1. Firebase 콘솔(https://console.firebase.google.com/)에 접속하여 프로젝트를 생성합니다. 기존 프로젝트에도 추가할 수 있습니다.
2. 프로젝트 설정 페이지에서 "Authentication" 탭으로 이동합니다.
3. "로그인 방법" 섹션에서 Apple 로그인을 활성화합니다.
4. "Team ID" 및 "Bundle ID" 항목에는 Xcode 프로젝트의 정보를 입력합니다.

## Xcode에서 Firebase 설정

1. 터미널을 열고 Firebase CLI를 설치합니다.
   ```
   $ npm install -g firebase-tools
   ```

2. Firebase 프로젝트와 연결합니다.
   ```
   $ firebase login
   ```

3. Xcode 프로젝트 폴더로 이동합니다.
   ```
   $ cd /path/to/your/project
   ```

4. Firebase 초기화 파일을 생성합니다.
   ```
   $ firebase init
   ```
   초기화 단계에서 "Authentication"을 선택하고, Apple 로그인 기능을 활성화합니다.

5. Firebase SDK를 설치합니다.
   ```
   $ pod init
   ```
   Podfile에 다음 코드를 추가합니다.
   ```
   pod 'Firebase/Auth'
   pod 'FirebaseUI/Auth'
   pod 'FirebaseUI/Apple'
   ```

6. Firebase SDK를 설치합니다.
   ```
   $ pod install
   ```

## Apple 로그인 인증 흐름 구현

1. Xcode에서 `Info.plist` 파일을 열고, 다음 코드를 추가합니다.
   ```xml
   <key>NSAppleSignInButtonStyle</key>
   <string>black</string>
   ```

2. 로그인 화면을 구성하고, Apple 로그인 버튼을 추가합니다.
   ```swift
   import UIKit
   import FirebaseAuthUI
   import FirebaseUI

   class LoginViewController: UIViewController, FUIAuthDelegate {

       override func viewDidLoad() {
           super.viewDidLoad()

           let authUI = FUIAuth.defaultAuthUI()
           authUI?.delegate = self

           let providers: [FUIAuthProvider] = [
               FUIOAuth.appleAuthProvider()
           ]
           authUI?.providers = providers

           let authViewController = authUI!.authViewController()
           present(authViewController, animated: true, completion: nil)
       }

       func authUI(_ authUI: FUIAuth, didSignInWith authDataResult: AuthDataResult?, error: Error?) {
           if error != nil {
               // Handle error
           } else {
               // User signed in successfully
           }
       }
   }
   ```

3. Firebase 프로젝트에 Apple 인증 정보를 추가합니다.
   - Xcode에서 `Project Navigator`에서 프로젝트 파일을 선택합니다.
   - `Info` 탭으로 이동하고 `URL Types` 섹션을 찾습니다.
   - `+` 버튼을 클릭하여 새로운 URL Type을 추가합니다.
   - `URL Schemes` 필드에 `appleid.YOUR_TEAM_ID`를 입력합니다. `YOUR_TEAM_ID`는 Apple 개발자 계정에서 확인할 수 있습니다.

## 실행 및 테스트

1. Xcode에서 프로젝트를 빌드하고 실행합니다.
2. 로그인 화면이 나타나면 Apple 로그인 버튼을 클릭합니다.
3. Apple 계정으로 로그인하고 인증이 성공적으로 완료되는지 확인합니다.

이제 Firebase Authentication을 통해 Apple 로그인 기능을 성공적으로 구현한 것입니다. Firebase에서는 다양한 인증 방법을 지원하므로 필요에 따라 다른 로그인 기능도 추가할 수 있습니다.

## 참고 자료

- [Firebase Authentication](https://firebase.google.com/docs/auth)
- [FirebaseUI for iOS](https://github.com/firebase/FirebaseUI-iOS)
- [Apple Developer Documentation - Sign In with Apple](https://developer.apple.com/documentation/signinwithapple)