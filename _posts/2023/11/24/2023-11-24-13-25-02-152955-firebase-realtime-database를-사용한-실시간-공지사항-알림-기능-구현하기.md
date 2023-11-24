---
layout: post
title: "[swift] Firebase Realtime Database를 사용한 실시간 공지사항 알림 기능 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Firebase Realtime Database는 실시간으로 데이터를 동기화하는 데 사용되는 클라우드 호스팅 데이터베이스입니다. 이 기능을 활용하여 실시간 공지사항 알림 기능을 구현해보겠습니다.

## 1. Firebase 프로젝트 설정

먼저, Firebase 콘솔에서 새로운 프로젝트를 만들고 Firebase Realtime Database를 활성화합니다. 필요한 설정을 마치고 Firebase SDK를 프로젝트에 추가합니다.

## 2. 데이터베이스 구조 설계

알림 기능을 구현하기 위해 데이터베이스에 공지사항 데이터를 저장할 구조를 설계해야 합니다. 예를 들어, "notices"라는 키를 가지는 노드를 생성하고 각 공지사항은 고유한 키를 가진 자식 노드로 저장할 수 있습니다. 각 공지사항 노드는 "title", "content", "timestamp" 등 필요한 속성을 가질 수 있습니다.

```swift
{
  "notices": {
    "notice1": {
      "title": "공지 제목 1",
      "content": "공지 내용 1",
      "timestamp": 1634620800
    },
    "notice2": {
      "title": "공지 제목 2",
      "content": "공지 내용 2",
      "timestamp": 1634707200
    },
    // ...
  }
}
```

## 3. 알림 수신 설정

iOS 앱에서 Firebase 알림을 수신하려면 Firebase Cloud Messaging (FCM)을 사용해야 합니다. Firebase 알림을 수신하려면 Firebase SDK를 사용하여 기기를 등록해야 합니다. 등록된 기기는 Firebase 토큰을 받고 이 토큰은 알림을 전송할 때 사용됩니다.

```swift
import FirebaseMessaging

func application(_ application: UIApplication, didRegisterForRemoteNotificationsWithDeviceToken deviceToken: Data) {
    // Firebase 토큰을 받아서 서버에 전송하거나 로컬에 저장합니다.
    Messaging.messaging().apnsToken = deviceToken
}
```

## 4. 공지사항 데이터 실시간 감시

Firebase Realtime Database에서 공지사항 데이터를 실시간으로 감시하려면 `observe` 메서드를 사용합니다. 예를 들어, 데이터베이스에서 "notices" 노드를 감시하고 새로운 공지사항이 추가될 때마다 알림을 보내는 코드는 다음과 같습니다.

```swift
import FirebaseDatabase
import UserNotifications

let databaseRef = Database.database().reference()

// "notices" 노드를 감시하여 새로운 데이터가 추가될 때마다 호출됩니다.
databaseRef.child("notices").observe(.childAdded) { snapshot in
    guard let notice = snapshot.value as? [String: Any] else {
        return
    }
    
    let title = notice["title"] as? String
    let content = notice["content"] as? String
    
    // 알림을 보내는 로직 구현
    sendNotification(title: title, content: content)
}

func sendNotification(title: String?, content: String?) {
    let content = UNMutableNotificationContent()
    content.title = title ?? ""
    content.body = content ?? ""
    
    // 알림 설정
    let trigger = UNTimeIntervalNotificationTrigger(timeInterval: 5, repeats: false)
    let request = UNNotificationRequest(identifier: "NoticeNotification", content: content, trigger: trigger)
    
    // 알림을 스케줄에 추가
    UNUserNotificationCenter.current().add(request) { error in
        if let error = error {
            print("알림을 추가하는 동안 에러 발생: \(error)")
        }
    }
}
```

위 코드는 Firebase Realtime Database에서 "notices" 노드를 감시하여 새로운 공지사항이 추가될 때마다 `sendNotification` 함수를 호출하여 iOS 알림을 보냅니다.

## 5. 결과 확인

Firebase Realtime Database에 새로운 공지사항을 추가하거나 수정하면 iOS 앱에서 실시간으로 알림이 도착하는지 확인할 수 있습니다.

---

이제 Firebase Realtime Database를 사용하여 실시간 공지사항 알림 기능을 구현하는 방법을 알아보았습니다. Firebase를 사용하여 데이터를 실시간으로 동기화하고 iOS 앱에 알림을 보내는 기능을 쉽게 구현할 수 있습니다. 자세한 내용은 Firebase 문서를 참조하시기 바랍니다.

**참고자료:**
- [Firebase Realtime Database 문서](https://firebase.google.com/docs/database)
- [Firebase Cloud Messaging 문서](https://firebase.google.com/docs/cloud-messaging)