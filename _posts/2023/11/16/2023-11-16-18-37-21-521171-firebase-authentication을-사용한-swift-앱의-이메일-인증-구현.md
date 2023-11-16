---
layout: post
title: "[swift] Firebase Authentication을 사용한 Swift 앱의 이메일 인증 구현"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Firebase는 Google에서 제공하는 개발 플랫폼으로, 실시간 데이터베이스, 스토리지, 인증 등 다양한 기능을 제공합니다. 이 중에서 Firebase Authentication을 사용하면 앱에 이메일 인증 기능을 간편하게 구현할 수 있습니다.

## Firebase 프로젝트 설정

먼저, Firebase 콘솔에서 프로젝트를 생성하고, iOS 앱을 등록해야합니다. 
1. Firebase 콘솔에 로그인하고, 새 프로젝트를 생성합니다.
2. 프로젝트 이름을 설정하고, 필요한 설정을 완료합니다.
3. iOS 앱 등록을 선택하고, 앱 번들 식별자를 입력합니다.
4. GoogleService-Info.plist 파일을 다운로드하고, 프로젝트에 추가합니다.

## Firebase Authentication 설정

Firebase Authentication을 활성화하고, 이메일/비밀번호 인증을 사용하도록 설정해야합니다.
1. Firebase 콘솔에서 "Authentication" 섹션으로 이동합니다.
2. "로그인 방법" 탭에서 "이메일/비밀번호" 옵션을 활성화합니다.

## Swift 프로젝트 설정

Firebase SDK를 Swift 프로젝트에 추가해야합니다.
1. Cocoapods가 설치되어 있지 않은 경우, 터미널에서 `sudo gem install cocoapods` 명령어를 실행하여 Cocoapods를 설치합니다.
2. 프로젝트 디렉토리에서 `pod init` 명령어를 실행하여 Podfile을 생성합니다.
3. Podfile을 열고, 다음과 같이 Firebase/Core와 Firebase/Auth를 추가합니다.

```swift
target 'YourProjectTarget' do
  use_frameworks!
  
  pod 'Firebase/Core'
  pod 'Firebase/Auth'
  
  # Add other pods if needed
  
end
```

4. 터미널에서 `pod install` 명령어를 실행하여 Firebase SDK를 다운로드합니다.
5. `.xcworkspace` 확장자가 포함된 프로젝트 파일을 열어서 작업합니다.

## 이메일 인증 구현하기

### 이메일/비밀번호 회원가입

이메일로 새로운 계정을 만들고 비밀번호로 회원가입을 구현합니다.
```swift
import Firebase

// ... Firebase 초기화 코드 생략 ...

Auth.auth().createUser(withEmail: email, password: password) { (authResult, error) in
  if let error = error {
    print("Error creating user: \(error.localizedDescription)")
  } else {
    // 회원가입 성공 처리
  }
}
```

### 이메일/비밀번호 로그인

이미 등록된 이메일과 비밀번호로 로그인을 구현합니다.
```swift
import Firebase

// ... Firebase 초기화 코드 생략 ...

Auth.auth().signIn(withEmail: email, password: password) { (authResult, error) in
  if let error = error {
    print("Error signing in: \(error.localizedDescription)")
  } else {
    // 로그인 성공 처리
  }
}
```

### 이메일 확인 메일 전송

회원가입 후, 사용자에게 이메일 확인 메일을 전송하고, 확인 작업을 구현합니다.
```swift
import Firebase

// ... Firebase 초기화 코드 생략 ...

if let user = Auth.auth().currentUser {
  user.sendEmailVerification { (error) in
    if let error = error {
      print("Error sending verification email: \(error.localizedDescription)")
    } else {
      // 이메일 전송 성공 처리
    }
  }
}
```

### 이메일 확인 상태 확인

사용자의 이메일 확인 상태를 확인하고 처리합니다.
```swift
import Firebase

// ... Firebase 초기화 코드 생략 ...

if let user = Auth.auth().currentUser {
  if user.isEmailVerified {
    // 이메일 확인 완료 처리
  } else {
    // 이메일 확인 필요 처리
  }
}
```

## 결론

Firebase Authentication을 사용하여 Swift 앱에서 이메일 인증 기능을 구현할 수 있습니다. Firebase 콘솔과 Swift 프로젝트의 설정을 완료하고, 간단한 코드로 회원가입, 로그인, 이메일 확인 메일 전송, 이메일 확인 상태 확인 등의 기능을 구현할 수 있습니다.

더 자세한 내용은 [Firebase 공식 문서](https://firebase.google.com/docs/auth/ios/start?hl=ko)를 참고하세요.