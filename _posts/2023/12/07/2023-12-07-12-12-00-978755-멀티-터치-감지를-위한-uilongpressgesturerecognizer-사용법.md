---
layout: post
title: "[swift] 멀티 터치 감지를 위한 UILongPressGestureRecognizer 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UIKit에서 제공하는 UILongPressGestureRecognizer는 사용자가 뷰를 오랫동안 누르고 있는 동안의 터치를 감지하는 기능을 제공합니다. 이 기능을 이용하여 멀티 터치를 감지하는 방법에 대해 알아보겠습니다.

## UILongPressGestureRecognizer 초기화

UILongPressGestureRecognizer를 사용하려면 먼저 인스턴스를 초기화해야 합니다. 이때 초기화 함수에 타겟 객체와 액션 메서드를 지정합니다. 아래는 초기화 예시입니다.

```swift
let longPressGestureRecognizer = UILongPressGestureRecognizer(target: self, action: #selector(handleLongPress(_:)))
```

위 코드에서 `target`은 이벤트를 처리할 객체(보통 뷰 컨트롤러)를 의미하며, `action`은 이벤트가 발생했을 때 호출될 메서드를 지정합니다.

## 멀티 터치 감지 설정

UILongPressGestureRecognizer를 멀티 터치를 감지하기 위해 설정해야 합니다. 이를 위해 `numberOfTouchesRequired` 프로퍼티에 값을 할당합니다. 아래는 멀티 터치를 감지하기 위한 설정 예시입니다.

```swift
longPressGestureRecognizer.numberOfTouchesRequired = 2
```

위 코드에서 `numberOfTouchesRequired`에 할당된 값은 멀티 터치를 감지하기 위해 필요한 터치 개수를 의미합니다. 위 예시는 2개의 터치를 감지하도록 설정한 것입니다.

## 액션 메서드 구현

UILongPressGestureRecognizer가 설정된 뷰에서 터치가 발생하면, 설정한 액션 메서드가 호출됩니다. 액션 메서드는 UILongPressGestureRecognizer 인스턴스를 인자로 받아 필요한 작업을 수행합니다. 아래는 액션 메서드의 예시입니다.

```swift
@objc func handleLongPress(_ gestureRecognizer: UILongPressGestureRecognizer) {
    if gestureRecognizer.state == .began {
        // 멀티 터치가 감지되었을 때 실행할 코드
        print("멀티 터치 감지됨")
    }
}
```

위 예시에서는 `gestureRecognizer`의 `state` 프로퍼티를 확인하여 멀티 터치가 감지되었을 때 실행할 코드를 구현하였습니다.

이제 위의 코드를 참고하여 UILongPressGestureRecognizer를 사용하여 멀티 터치를 감지하는 기능을 구현해보세요!

## 참고 자료

- [UILongPressGestureRecognizer - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer)
- [TouchEvent Programming Guide - Apple Developer Documentation](https://developer.apple.com/library/archive/documentation/EventHandling/Conceptual/EventHandlingiPhoneOS/event_delivery_responder_chain/event_delivery_responder_chain.html)