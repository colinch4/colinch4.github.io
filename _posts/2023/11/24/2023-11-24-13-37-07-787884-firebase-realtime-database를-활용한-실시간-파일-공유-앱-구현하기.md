---
layout: post
title: "[swift] Firebase Realtime Database를 활용한 실시간 파일 공유 앱 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Firebase는 실시간 데이터베이스를 제공하여 실시간 파일 공유 앱을 구현하기에 적합한 도구입니다. 이 튜토리얼에서는 Swift 언어를 사용하여 Firebase Realtime Database를 활용한 실시간 파일 공유 앱을 구현하는 방법에 대해 알아보겠습니다.

## 목차

- [Firebase 프로젝트 설정](#firebase-프로젝트-설정)
- [Firebase Realtime Database 설정](#firebase-realtime-database-설정)
- [Firebase SDK 설치](#firebase-sdk-설치)
- [파일 업로드 기능 구현](#파일-업로드-기능-구현)
- [파일 공유 기능 구현](#파일-공유-기능-구현)
- [파일 다운로드 기능 구현](#파일-다운로드-기능-구현)


## Firebase 프로젝트 설정

1. [Firebase 콘솔](https://console.firebase.google.com)에 접속하여 프로젝트를 생성합니다.
2. Firebase 프로젝트 설정 페이지에서 iOS 앱을 추가합니다.
3. 앱 번들 식별자를 입력하고, 앱 추가 단계에서 제공되는 GoogleService-Info.plist 파일을 다운로드합니다.


## Firebase Realtime Database 설정

1. Firebase 콘솔에서 '리얼타임 데이터베이스'를 선택합니다.
2. '규칙' 탭에서 규칙을 다음과 같이 변경합니다:
```json
{
  "rules": {
    ".read": true,
    ".write": true
  }
}
```
> :warning: 이 규칙은 개발 편의를 위해 모든 사용자에게 읽기 및 쓰기 권한을 부여하므로, 실제 앱에서 사용할 때에는 보안을 강화해야합니다. 


## Firebase SDK 설치

1. 프로젝트 폴더에서 Podfile을 생성합니다.
2. 다음과 같이 Podfile을 작성하고 저장합니다:
```
# Uncomment the next line to define a global platform for your project
# platform :ios, '9.0'

target 'YourApp' do
  # Comment the next line if you're not using Swift and don't want to use dynamic frameworks
  use_frameworks!

  # Pods for YourApp
  pod 'Firebase/Database'

end
```
3. 터미널에서 `pod install` 명령어를 실행하여 Firebase SDK를 설치합니다.


## 파일 업로드 기능 구현

1. Firebase 프로젝트에 파일 업로드를 위한 데이터베이스 구조를 생성합니다.
2. 앱에서 파일 선택 기능을 구현합니다. UIImagePickerController를 사용하여 사용자로부터 파일을 선택할 수 있습니다.
3. 선택한 파일을 Firebase Storage에 업로드합니다.
   - 저장된 파일의 다운로드 URL을 받아오기 위해 업로드가 완료되면, 해당 파일에 대한 메타데이터를 Firebase Realtime Database에 저장합니다.


## 파일 공유 기능 구현

1. 파일을 Firebase Realtime Database에서 가져와 사용자에게 보여주는 기능을 구현합니다.
2. 사용자 간의 파일 공유를 위해 적절한 권한 관리를 위한 코드를 작성합니다.
   - 기본적으로 Firebase Realtime Database에서는 모든 사용자에게 읽기 및 쓰기 권한이 부여됩니다. 이를 필요에 따라 수정하여 권한을 제어할 수 있습니다.
   - 사용자에게 파일 업로드 및 다운로드 권한을 부여하는 방법은 Firebase 인증 등 다른 기능과 연동하여 구현할 수 있습니다.


## 파일 다운로드 기능 구현

1. Firebase Realtime Database에서 파일의 다운로드 URL을 가져옵니다.
2. 다운로드 URL을 통해 해당 파일을 다운로드하여 사용자에게 제공하는 기능을 구현합니다.


이제 Firebase Realtime Database를 활용한 실시간 파일 공유 앱을 구현하기 위한 준비가 모두 완료되었습니다. 이 튜토리얼을 참고하여 앱 개발을 진행해 보세요. Firebase의 다양한 기능과 활용 방법에 대해서는 [Firebase 공식 문서](https://firebase.google.com/docs)를 참고하시기 바랍니다.