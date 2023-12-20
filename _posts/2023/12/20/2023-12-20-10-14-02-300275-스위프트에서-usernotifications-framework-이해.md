---
layout: post
title: "[swift] 스위프트에서 UserNotifications framework 이해"
description: " "
date: 2023-12-20
tags: [swift]
comments: true
share: true
---

앱 개발 과정에서 사용자에게 알림을 전달해야 하는 경우가 많습니다. 스위프트에서는 UserNotifications framework을 사용하여 다양한 종류의 알림을 구현할 수 있습니다. 이 블로그에서는 UserNotifications framework을 사용하여 iOS 앱에서 알림을 만드는 방법에 대해 알아보겠습니다.

## UserNotifications framework 소개

UserNotifications framework은 iOS 10 이상에서 사용자에게 푸시 알림, 로컬 알림 및 앱 아이콘 뱃지 설정을 관리하는 데 사용됩니다. 이 framework을 사용하여 사용자에게 시간 및 장소 기반의 알림을 전송할 수 있습니다.

## UserNotifications framework를 사용하여 알림 만들기

### 1. 알림 권한 요청

앱에서 알림을 보내기 전에 사용자에게 알림 권한을 요청해야 합니다. 다음 코드는 사용자에게 알림 권한을 요청하는 방법을 보여줍니다.

```swift
import UserNotifications

UNUserNotificationCenter.current().requestAuthorization(options: [.alert, .sound, .badge]) { granted, error in
    if granted {
        print("알림 권한이 허용됨")
    } else {
        print("알림 권한이 거부됨")
    }
}
```

### 2. 로컬 알림 생성

로컬 알림을 생성하려면 `UNMutableNotificationContent` 및 `UNNotificationRequest` 객체를 사용해야 합니다. 다음은 간단한 텍스트 알림을 생성하는 예제입니다.

```swift
let content = UNMutableNotificationContent()
content.title = "새로운 메시지"
content.body = "안 읽은 메시지가 있습니다."
content.sound = UNNotificationSound.default

let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 5, repeats: false)

let request = UNNotificationRequest(identifier: "newMessage", content: content, trigger: trigger)

UNUserNotificationCenter.current().add(request) { error in
    if let error = error {
        print("알림 추가 실패: \(error.localizedDescription)")
    }
}
```

이렇게하면 5초 후에 "새로운 메시지"라는 제목과 "안 읽은 메시지가 있습니다."라는 내용을 가진 알림이 표시됩니다.

## 결론

UserNotifications framework을 사용하면 iOS 앱에서 다양한 종류의 알림을 생성하고 관리할 수 있습니다. 꼼꼼한 권한 요청 및 적절한 알림 내용 및 타이밍 설정을 통해 사용자에게 유용한 알림 서비스를 제공할 수 있습니다.

더 많은 자세한 내용은 [Apple 개발자 문서](https://developer.apple.com/documentation/usernotifications)를 확인하십시오.