---
layout: post
title: "[swift] Swift PKRevealController와의 앱 저장소 연동 및 배포 방법"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 목차
1. [소개](#introduction)
2. [PKRevealController 설정](#setup-pkrevealcontroller)
3. [앱을 저장소에 연동](#connect-to-app-store)
4. [앱 배포](#app-distribution)
5. [참고 자료](#references)

## 소개 <a name="introduction"></a>
앱을 개발하고 이를 사용자들에게 제공하기 위해서는 일련의 단계를 거쳐야 합니다. 이 중 앱의 네비게이션 화면을 쉽게 구현할 수 있는 `PKRevealController`를 사용하는 방법과, 앱 저장소에 연동하고 배포하는 방법에 대해 알아보겠습니다.

## PKRevealController 설정 <a name="setup-pkrevealcontroller"></a>
`PKRevealController`를 사용하기 위해서는 다음과 같은 단계를 거쳐 설정해야 합니다:

1. `Podfile`에 `PKRevealController`를 추가합니다.
```swift
pod 'PKRevealController'
```

2. Terminal에서 `pod install` 명령어를 실행하여 `PKRevealController`를 다운로드 합니다.

3. `PKRevealController`를 사용할 UIViewController를 생성하고, 해당 ViewController의 class를 `PKRevealController`로 지정합니다.

4. `PKRevealController`의 `setFront` 메소드를 사용하여 메인 컨텐츠를 설정합니다.
```swift
let mainContentVC = UIStoryboard(name: "Main", bundle: nil).instantiateViewController(withIdentifier: "MainContentViewController") as! MainContentViewController

let revealController = PKRevealController(frontViewController: mainContentVC, leftViewController: nil, rightViewController: nil)
revealController?.setFront(mainContentVC, animated: true)
```

5. 네비게이션 바 버튼을 추가하여 메뉴 열기/닫기 기능을 구현할 수 있습니다.
```swift
let menuBarButtonItem = UIBarButtonItem(title: "Menu", style: .plain, target: revealController!, action: #selector(PKRevealController.revealLeftViewController))
mainContentVC.navigationItem.leftBarButtonItem = menuBarButtonItem
```

이렇게 하면 `PKRevealController`를 사용하여 네비게이션 화면을 쉽게 구현할 수 있습니다.

## 앱을 저장소에 연동 <a name="connect-to-app-store"></a>
앱을 저장소에 연동하여 사용자들에게 제공하기 위해서는 Apple Developer 계정이 필요합니다. 계정을 만든 후 다음과 같은 단계를 통해 앱을 저장소에 연동할 수 있습니다.

1. Xcode에서 앱의 Bundle Identifier를 설정합니다. 이는 앱을 식별하는 고유한 값입니다.

2. Apple Developer 계정에서 App ID를 생성합니다. 이는 앱을 구별하는 고유한 값입니다.

3. Xcode에서 애플 개발자 계정을 설정하고, 앱을 생성합니다.

4. 앱을 저장소에 등록하기 위해 앱의 Provisioning Profile을 생성합니다.

5. iOS 개발 인증서 및 Provisioning Profile를 Xcode와 연동합니다.

이제 앱은 저장소에 연동되었습니다.

## 앱 배포 <a name="app-distribution"></a>
앱을 저장소에 등록하여 배포하기 위해 다음 단계를 따릅니다.

1. Xcode에서 앱을 빌드하고 일련의 테스트를 수행합니다.

2. 앱의 스토어에 등록하기 위해 iTunes Connect로 이동합니다.

3. iTunes Connect에서 앱의 정보를 작성하고, 앱의 아이콘, 스크린샷 등을 업로드합니다.

4. 앱을 저장소에 제출합니다. Apple은 앱의 승인 과정을 거친 후 앱을 배포합니다.

이제 앱은 사용자들이 다운로드하고 사용할 수 있습니다.

## 참고 자료 <a name="references"></a>
- [PKRevealController GitHub 페이지](https://github.com/pkluz/PKRevealController)
- [Apple Developer](https://developer.apple.com)
- [iTunes Connect](https://appstoreconnect.apple.com)