---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UISwipeGestureRecognizer 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

이 포스트에서는 iOS 앱에서 터치 이벤트를 처리하기 위해 UISwipeGestureRecognizer를 사용하는 방법에 대해 알아보겠습니다.

## UISwipeGestureRecognizer란?
UISwipeGestureRecognizer는 사용자의 터치 스와이프 동작을 인식하는 제스처 인식기입니다. 이 제스처 인식기를 사용하면 사용자가 화면을 터치하고 스와이프 동작을 수행할 때, 해당 이벤트를 캡처하고 처리할 수 있습니다.

## UISwipeGestureRecognizer 추가하기
먼저, UISwipeGestureRecognizer를 추가하기 위해 다음과 같이 코드를 작성합니다:

```swift
let swipeGestureRecognizer = UISwipeGestureRecognizer(target: self, action: #selector(handleSwipeGesture(_:)))
self.view.addGestureRecognizer(swipeGestureRecognizer)
```

위의 코드에서는 `UISwipeGestureRecognizer(target:action:)` 생성자를 사용하여 새로운 UISwipeGestureRecognizer를 만듭니다. `target` 매개변수에는 이벤트를 처리할 메서드의 대상을 지정하고, `action` 매개변수에는 이벤트가 발생했을 때 호출될 메서드의 이름을 지정합니다.

또한 `self.view.addGestureRecognizer(swipeGestureRecognizer)`를 사용하여 생성된 제스처 인식기를 ViewController의 뷰에 추가합니다.

## 이벤트 처리하기
이제 이벤트를 처리하기 위해 `handleSwipeGesture(_:)` 메서드를 작성해보겠습니다:

```swift
@objc func handleSwipeGesture(_ gestureRecognizer: UISwipeGestureRecognizer) {
    if gestureRecognizer.direction == .left {
        // 왼쪽 스와이프 처리
        print("왼쪽으로 스와이프 되었습니다.")
    } else if gestureRecognizer.direction == .right {
        // 오른쪽 스와이프 처리
        print("오른쪽으로 스와이프 되었습니다.")
    } else if gestureRecognizer.direction == .up {
        // 위로 스와이프 처리
        print("위로 스와이프 되었습니다.")
    } else if gestureRecognizer.direction == .down {
        // 아래로 스와이프 처리
        print("아래로 스와이프 되었습니다.")
    }
}
```

위의 코드에서는 `handleSwipeGesture(_:)` 메서드를 작성하고, `UISwipeGestureRecognizer`의 `direction` 속성을 확인하여 해당하는 스와이프 방향에 따라 처리할 로직을 작성합니다.

## 참고 자료
- [UISwipeGestureRecognizer - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiswipegesturerecognizer)

이제 UISwipeGestureRecognizer를 사용하여 터치 이벤트를 처리하는 방법에 대해 알아보았습니다. 이를 활용하여 사용자의 터치 동작에 반응하는 기능을 구현할 수 있습니다.