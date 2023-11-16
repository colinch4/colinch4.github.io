---
layout: post
title: "[swift] Swift PKRevealController와의 push 알림 연동"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱 개발 중에는 사용자에게 중요한 정보나 업데이트를 알리기 위해 푸시 알림을 사용하는 경우가 많습니다. iOS 앱의 경우, PKRevealController를 사용하여 사이드 메뉴를 구현하는 경우가 있는데, 이때 푸시 알림을 사이드 메뉴에 표시하는 방법에 대해 알아보겠습니다.

## PKRevealController

PKRevealController는 iOS 앱에서 사이드 메뉴를 구현하기 위해 사용되는 오픈 소스 라이브러리입니다. 이 라이브러리는 UINavigationController와 비슷한 동작을 수행하면서, 앱의 여러 뷰 컨트롤러를 사이드 메뉴로 슬라이드하는 것을 가능하게 합니다.

## 푸시 알림과의 연동

사이드 메뉴에 푸시 알림을 표시하기 위해서는 다음과 같은 단계를 수행해야 합니다.

1. 푸시 알림을 수신하는 코드 작성: 알림을 수신하고 필요한 데이터를 추출하는 코드를 작성합니다.
2. 사이드 메뉴에 푸시 알림을 표시하는 코드 작성: 추출한 데이터를 가지고 사이드 메뉴에 알림을 표시하는 코드를 작성합니다.

다음은 예시 코드입니다.

```swift
// 푸시 알림을 수신하는 코드
func didReceivePushNotification(userInfo: [AnyHashable : Any]) {
    // 필요한 데이터 추출
    let message = userInfo["message"] as? String
    
    // 사이드 메뉴에 알림 표시
    let sideMenuViewController = PKRevealController.shared().leftViewController as? SideMenuViewController
    sideMenuViewController?.showPushNotification(message: message)
}
```

위 예시 코드에서는 `didReceivePushNotification` 메서드에서 푸시 알림을 수신하고 필요한 데이터를 추출합니다. 추출한 데이터를 가지고 `PKRevealController`에서 저장된 `leftViewController`의 인스턴스를 가져온 다음, 해당 뷰 컨트롤러의 `showPushNotification` 메서드를 호출하여 알림을 표시합니다.

이렇게 연동하면 푸시 알림을 사이드 메뉴에 표시할 수 있습니다.

## 참고 자료

- [PKRevealController GitHub 레포지토리](https://github.com/pkluz/PKRevealController)