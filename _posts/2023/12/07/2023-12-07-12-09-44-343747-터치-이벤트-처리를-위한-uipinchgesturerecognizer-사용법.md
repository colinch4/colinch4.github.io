---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UIPinchGestureRecognizer 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

`UIPinchGestureRecognizer`는 화면에서 손가락으로 핀치 동작을 감지할 수 있는 제스처 인식기입니다. 이를 사용하여 iOS 애플리케이션에서 핀치 동작에 대한 이벤트를 처리할 수 있습니다. 이번 글에서는 `UIPinchGestureRecognizer`를 사용하는 방법에 대해 알아보겠습니다.

## `UIPinchGestureRecognizer` 추가하기

먼저, 핀치 동작을 처리할 뷰에 `UIPinchGestureRecognizer`를 추가해야 합니다. 이를 위해 다음과 같이 코드를 작성합니다.

```swift
let pinchGesture = UIPinchGestureRecognizer(target: self, action: #selector(handlePinch(_:)))
view.addGestureRecognizer(pinchGesture)
```

`UIPinchGestureRecognizer`를 생성하고, `target`에는 핀치 동작을 처리할 메서드가 구현된 객체를 지정합니다. `action`에는 해당 메서드를 지정합니다. 위 예제에서는 `handlePinch(_:)` 메서드를 사용하고 있습니다.

## 핀치 동작 처리하기

핀치 동작을 처리하기 위해 `handlePinch(_:)` 메서드를 구현해야 합니다. 이 메서드는 다음과 같이 작성할 수 있습니다.

```swift
@objc func handlePinch(_ gesture: UIPinchGestureRecognizer) {
    if gesture.state == .began {
        // 핀치 동작이 시작될 때 처리할 작업
    }
    else if gesture.state == .changed {
        // 핀치 동작 중에 변경되는 부분에 대한 처리
        let scale = gesture.scale
        // 작업에 따른 뷰의 변화 적용
    }
    else if gesture.state == .ended {
        // 핀치 동작이 종료될 때 처리할 작업
    }
}
```

위 코드에서 `gesture.state`는 현재 핀치 제스처의 상태를 나타냅니다. `.began`은 핀치 동작이 시작될 때 감지되는 상태이고, `.changed`는 핀치 동작 중에 변경되는 상태를 나타냅니다. `.ended`는 핀치 동작이 종료될 때의 상태를 나타냅니다.

핀치 제스처의 세부 정보는 `gesture.scale`을 통해 접근할 수 있습니다. 이 값을 활용하여 필요한 작업을 수행하고, 뷰의 변화를 반영할 수 있습니다.

## 예제

다음은 핀치 동작으로 이미지 크기를 조절하는 예제 코드입니다.

```swift
@IBOutlet weak var imageView: UIImageView!

override func viewDidLoad() {
    super.viewDidLoad()

    let pinchGesture = UIPinchGestureRecognizer(target: self, action: #selector(handlePinch(_:)))
    imageView.addGestureRecognizer(pinchGesture)
}

@objc func handlePinch(_ gesture: UIPinchGestureRecognizer) {
    if gesture.state == .began || gesture.state == .changed {
        let scale = gesture.scale
        imageView.transform = CGAffineTransform(scaleX: scale, y: scale)
    }
}
```

이 예제에서는 이미지 뷰에 `UIPinchGestureRecognizer`를 추가하고, 핀치 동작이 일어날 때마다 이미지 뷰의 크기를 조절하여 확대/축소하는 동작을 구현하고 있습니다.

## 결론

`UIPinchGestureRecognizer`를 사용하면 핀치 동작을 감지하고, 해당 동작에 대한 이벤트를 처리할 수 있습니다. 이를 이용하여 iOS 애플리케이션에서 다양한 핀치 동작을 구현할 수 있습니다.

참고
- [Apple Developer Documentation - UIPinchGestureRecognizer](https://developer.apple.com/documentation/uikit/uipinchgesturerecognizer)