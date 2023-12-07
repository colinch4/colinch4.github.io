---
layout: post
title: "[swift] 멀티 터치 감지를 위한 UIPinchGestureRecognizer 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

> 이번 블로그 포스트에서는 Swift에서 멀티 터치 감지를 위해 `UIPinchGestureRecognizer`를 사용하는 방법을 알아보겠습니다.

`UIPinchGestureRecognizer`는 사용자가 두 손가락으로 확대 또는 축소 동작을 했을 때 이를 감지하는 제스처 인식기입니다. 

---

## UIPinchGestureRecognizer 클래스 생성
먼저, `UIPinchGestureRecognizer` 클래스의 인스턴스를 생성해야 합니다. 일반적으로 이를 뷰 컨트롤러 내에서 생성하고 추가합니다.

```swift
let pinchGestureRecognizer = UIPinchGestureRecognizer(target: self, action: #selector(handlePinch))
view.addGestureRecognizer(pinchGestureRecognizer)
```

`target`은 제스처 이벤트 발생 시 호출할 메서드가 포함된 객체입니다. 이 예제에서는 현재 뷰 컨트롤러를 사용하고 있으므로 `self`를 전달합니다. `action`은 호출할 메서드를 선택합니다. 위의 예제에서는 `handlePinch()` 메서드를 호출합니다.

## 제스처 이벤트 처리

뷰 컨트롤러 내에 `handlePinch()` 메서드를 추가하여 제스처 이벤트를 처리합니다.

```swift
@objc func handlePinch(_ gestureRecognizer: UIPinchGestureRecognizer) {
    if gestureRecognizer.state == .began {
        // 줌 시작
        // 필요한 로직을 작성하세요
    }
    
    if gestureRecognizer.state == .changed {
        // 줌 변경
        let scale = gestureRecognizer.scale
        // 필요한 로직을 작성하세요
    }
    
    if gestureRecognizer.state == .ended {
        // 줌 종료
        // 필요한 로직을 작성하세요
    }
}
```

`gestureRecognizer.state`는 현재 제스처의 상태를 나타내는 속성입니다. `began`은 제스처가 시작되었음을 나타내며, `changed`는 실시간으로 제스처 변경사항을 감지하고, `ended`는 제스처가 종료되었음을 나타냅니다.

---

그럼 이제 멀티 터치 감지를 위해 `UIPinchGestureRecognizer`를 사용하는 방법에 대해 알아보았습니다. 이를 사용하여 사용자가 화면을 확대 또는 축소하는 동작을 쉽게 감지하고 관리할 수 있습니다.

> **참고 링크**
> - [Apple Developer Documentation - UIPinchGestureRecognizer](https://developer.apple.com/documentation/uikit/uipinchgesturerecognizer)