---
layout: post
title: "[ios] EventKit 프레임워크와 iCloud Calendar의 연동 방법"
description: " "
date: 2023-12-15
tags: [ios]
comments: true
share: true
---

이 글에서는 **EventKit** 프레임워크를 사용하여 iOS 앱에서 **iCloud Calendar**와의 연동 방법에 대해 알아보겠습니다.

## EventKit 프레임워크란?

**EventKit** 은 iOS 앱에서 캘린더 데이터를 읽고, 쓰고, 수정할 수 있는 프레임워크입니다. 이를 사용하여 사용자의 iCloud Calendar와 같은 캘린더 데이터에 액세스하여 이를 편리하게 관리할 수 있습니다.

## iCloud Calendar와의 연동

### 1. 권한 요청

우선, 앱에서 캘린더 데이터에 접근하기 위해 권한을 요청해야 합니다. Info.plist 파일에 `NSCalendarsUsageDescription`를 추가하여 사용자에게 권한 요청 사유를 설명합니다.

```xml
<key>NSCalendarsUsageDescription</key>
<string>캘린더에 접근하기 위해 권한이 필요합니다.</string>
```

### 2. EventStore 인스턴스 생성

캘린더 데이터를 읽고 쓰기 위해 **EventStore** 인스턴스를 생성합니다.

```swift
import EventKit

let eventStore = EKEventStore()
```

### 3. 권한 확인

사용자의 권한을 확인하고, 권한이 없는 경우 권한 요청을 합니다.

```swift
eventStore.requestAccess(to: .event) { (granted, error) in
    if granted {
        // 권한이 허용된 경우
    } else {
        // 권한이 거부된 경우
    }
}
```

### 4. 캘린더 데이터 읽기

사용자의 iCloud Calendar에서 이벤트를 읽어올 수 있습니다.

```swift
let calendars = eventStore.calendars(for: .event)
for calendar in calendars {
    // 캘린더 데이터 처리
}
```

### 5. 캘린더 데이터 쓰기

새로운 이벤트를 생성하여 iCloud Calendar에 추가할 수 있습니다.

```swift
let event = EKEvent(eventStore: eventStore)
event.title = "새 이벤트"
event.startDate = Date()
event.endDate = Date()
event.calendar = eventStore.defaultCalendarForNewEvents

do {
    try eventStore.save(event, span: .thisEvent)
} catch {
    // 오류 처리
}
```

위와 같이 **EventKit** 프레임워크를 사용하여 iCloud Calendar와 연동할 수 있습니다. 앱에서 사용자의 캘린더 데이터를 관리하고 활용할 수 있는 다양한 기능을 구현할 수 있습니다.