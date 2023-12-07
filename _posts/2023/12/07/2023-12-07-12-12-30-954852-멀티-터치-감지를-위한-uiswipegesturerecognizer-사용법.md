---
layout: post
title: "[swift] 멀티 터치 감지를 위한 UISwipeGestureRecognizer 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

iOS 애플리케이션을 개발하다보면 사용자의 멀티 터치 입력을 감지해야 할 때가 있습니다. 이때 `UISwipeGestureRecognizer`를 사용하면 간편하게 멀티 터치 제스처를 처리할 수 있습니다. 이번 블로그 포스트에서는 `UISwipeGestureRecognizer`를 사용하여 멀티 터치를 감지하는 방법에 대해 알아보겠습니다.

## Step 1: Gesture Recognizer 생성 및 설정

```swift
let swipeGestureRecognizer = UISwipeGestureRecognizer(target: self, action: #selector(handleSwipeGesture(_:)))
swipeGestureRecognizer.numberOfTouchesRequired = 2
swipeGestureRecognizer.direction = .up
```

먼저, `UISwipeGestureRecognizer` 인스턴스를 생성하고 관련 설정을 해줍니다. 이 예제에서는 `numberOfTouchesRequired` 프로퍼티를 2로 설정하여 2개의 손가락을 필요로 하는 멀티 터치를 감지하도록 합니다. 그리고 `direction` 프로퍼티를 `.up`으로 설정하여 위로 스와이프 동작을 감지하도록 합니다.

## Step 2: Gesture Recognizer 추가하기

```swift
view.addGestureRecognizer(swipeGestureRecognizer)
```

생성한 `UISwipeGestureRecognizer` 인스턴스를 뷰에 추가합니다. 이렇게 하면 해당 뷰에서 멀티 터치 스와이프 제스처를 감지할 수 있습니다.

## Step 3: 제스처 처리하기

```swift
@objc func handleSwipeGesture(_ gestureRecognizer: UISwipeGestureRecognizer) {
    if gestureRecognizer.state == .ended {
        // 멀티 터치 스와이프 제스처가 발생했을 때 처리할 작업
        // ...
    }
}
```

마지막으로, 해당 멀티 터치 스와이프 제스처가 발생했을 때 실행될 메소드를 구현합니다. 위의 예제에서는 `handleSwipeGesture(_:)` 메소드를 구현했습니다. 이 메소드는 제스처가 종료(`state == .ended`)되었을 때 호출됩니다. 이곳에서 멀티 터치 스와이프 제스처가 발생했을 때 원하는 작업을 수행할 수 있습니다.

이제 위의 세 가지 단계를 따라 멀티 터치 스와이프 제스처를 감지하고 원하는 작업을 처리할 수 있는 애플리케이션을 만들 수 있습니다. `UISwipeGestureRecognizer`를 사용하여 사용자의 멀티 터치 입력을 감지하는 방법에 대해 알고 계시면 다양한 상황에서 유용하게 활용할 수 있을 것입니다.

## 참고 자료

- [Apple Developer Documentation - UISwipeGestureRecognizer](https://developer.apple.com/documentation/uikit/uiswipegesturerecognizer)