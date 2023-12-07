---
layout: post
title: "[swift] 멀티 터치 감지를 위한 UIRotationGestureRecognizer 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

iOS 애플리케이션을 개발할 때, 사용자의 제스처를 인식하여 기능을 추가하는 것은 매우 중요합니다. 이 중 멀티 터치 감지는 사용자가 동시에 여러 개의 손가락으로 화면을 터치하거나 제스처를 수행할 때 필요한 기능입니다. 이번 글에서는 멀티 터치 감지를 위해 UIRotationGestureRecognizer를 사용하는 방법을 알아보겠습니다.

UIRotationGestureRecognizer는 회전 제스처를 감지하는 제스처 리코그나이저입니다. 사용자가 두 손가락으로 화면을 터치한 상태에서 손가락을 돌리면 회전 제스처를 감지하여 알맞은 동작을 수행할 수 있습니다.

## UIRotationGestureRecognizer 추가하기

먼저, UIRotationGestureRecognizer를 사용하기 위해 다음과 같이 제스처 리코그나이저를 추가해야 합니다.

```swift
let rotationGestureRecognizer = UIRotationGestureRecognizer(target: self, action: #selector(handleRotation(_:)))
view.addGestureRecognizer(rotationGestureRecognizer)
```

위 코드에서는 `rotationGestureRecognizer`라는 이름의 UIRotationGestureRecognizer를 생성하고, `target`과 `action`을 설정하여 해당 제스처가 감지되었을 때 어떤 메서드를 호출할 지 지정합니다. 이 예제에서는 `handleRotation(_:)` 메서드를 호출하도록 설정하였습니다. 그리고 `view`에 제스처 리코그나이저를 추가하여 화면에서 회전 제스처를 감지할 수 있도록 합니다.

## 회전 제스처 처리하기

이제 회전 제스처가 감지되었을 때 어떤 동작을 할 지 정의해야 합니다. 이를 위해 `handleRotation(_:)` 메서드를 구현합니다.

```swift
@objc func handleRotation(_ gestureRecognizer: UIRotationGestureRecognizer) {
    // 회전 각도 가져오기
    let rotationAngle = gestureRecognizer.rotation
    
    // 회전 제스처에 따른 동작 수행
    // 예를 들어, 뷰를 회전시키는 등의 작업을 수행할 수 있습니다.
    
    // 회전 제스처 종료 시 초기화
    if gestureRecognizer.state == .ended {
        gestureRecognizer.rotation = 0
    }
}
```

위의 예제 코드에서는 `rotationAngle` 변수를 사용하여 회전 각도를 가져올 수 있습니다. 이 각도를 활용하여 회전 제스처에 따른 동작을 수행할 수 있습니다. 예를 들어, 뷰를 회전시키거나 회전 각도에 따라 특정한 작업을 수행할 수 있습니다.

또한, 제스처의 상태를 체크하여 회전 제스처 종료 시에는 `rotation` 값을 초기화합니다. 이는 제스처를 연속적으로 감지하기 위해 필요한 작업입니다.

## 참고 자료

- [Apple Developer Documentation - UIRotationGestureRecognizer](https://developer.apple.com/documentation/uikit/uirotationgesturerecognizer)

위에서 설명한 내용은 UIRotationGestureRecognizer의 기본적인 사용법을 알려드렸습니다. 더 자세한 내용은 Apple Developer Documentation을 참고하시면 됩니다.