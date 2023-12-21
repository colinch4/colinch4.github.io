---
layout: post
title: "[swift] CallKit과 VoIP(Internet Protocol)-(IP-)기반 통화"
description: " "
date: 2023-12-22
tags: [swift]
comments: true
share: true
---

iOS에서 VoIP 통화를 개발하고 싶다면 Apple의 CallKit 프레임워크를 활용하여 구현할 수 있다. CallKit은 앱을 기본 통화 앱처럼 작동하게 하며, iOS의 UI와 기능을 이용하여 전화 기능을 제공하는 프레임워크이다.

## CallKit의 기능

CallKit을 이용하면 다음과 같은 기능을 구현할 수 있다:

- 앱 UI에 전화 알림을 표시
- 통화 기록 저장 및 편집
- 통화를 받거나 거절하는 등의 사용자 조작에 대한 UI

## CallKit의 구현 방법

### 1. CallKit을 통한 Caller ID 통화 표시

CallKit은 VoIP 통화 시에도 통화 화면을 표시할 수 있는 Caller ID 기능을 제공한다. VoIP 통화 시에는 CallKit 프레임워크를 이용하여 incoming call을 표시할 수 있으며, 사용자는 이를 통해 전화를 받거나 거절할 수 있다.

```swift
import CallKit

let provider = CXProvider(configuration: CXProviderConfiguration(localizedName: "내 앱 이름"))
provider.setDelegate(self, queue: nil)

let update = CXCallUpdate()
update.remoteHandle = CXHandle(type: .generic, value: "전화번호")
provider.reportIncomingCall(with: UUID(), update: update, completion: { error in })
```

### 2. CallKit을 통한 통화 UI 표시

CallKit을 이용하면 앱의 사용자 인터페이스에 통화 알림을 표시할 수 있다. 이를 통해 사용자는 통화를 받거나 거절할 수 있으며, 통화 상태에 따른 UI 업데이트도 가능하다.

```swift
func provider(_ provider: CXProvider, perform action: CXAnswerCallAction) {
    // 통화 받기 동작 수행
    action.fulfill()
}

func provider(_ provider: CXProvider, perform action: CXEndCallAction) {
    // 통화 종료 동작 수행
    action.fulfill()
}
```

### 3. CallKit을 통한 통화 기록 저장

CallKit은 통화 기록을 저장하고 편집하는 기능도 제공한다. 이를 통해 사용자는 앱 내에서 통화 기록을 확인하고 관리할 수 있다.

```swift
let controller = CXCallObserver()

controller.setDelegate(self, queue: nil)

func callObserver(_ callObserver: CXCallObserver, callChanged call: CXCall) {
    if call.hasEnded {
        // 통화 종료 시 동작 수행
    } else if call.isOutgoing {
        // 아웃고잉 콜 시 동작 수행
    } else if call.isOnHold {
        // 홀드된 콜 시 동작 수행
    }
}
```

## CallKit의 장점

- **유연한 UI**: CallKit을 이용하면 iOS 플랫폼에서 제공하는 통화 UI를 쉽게 구현할 수 있다.
- **통화 기록 관리**: 통화 기록 저장 및 편집 기능을 활용하여 사용자가 편리하게 통화 기록을 관리할 수 있다.

이러한 기능을 활용하여 VoIP 통화를 개발할 때, CallKit을 이용하여 iOS에서 제공하는 기본 통화 기능을 사용자에게 제공할 수 있다.

참고문헌:
- [Apple Developer Documentation](https://developer.apple.com/documentation/callkit)