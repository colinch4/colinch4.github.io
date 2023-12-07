---
layout: post
title: "[swift] 멀티 터치 감지를 위한 UIPanGestureRecognizer 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

Swift 언어를 사용하여 멀티 터치를 감지하고 처리하기 위해 UIPanGestureRecognizer를 사용하는 방법을 알아보겠습니다.

## 1. UIPanGestureRecognizer란?

UIPanGestureRecognizer는 사용자의 터치 입력을 감지하여 드래그 동작을 처리하는 제스처 인식기입니다. 다중 터치를 감지할 수 있으며, 터치의 상대적인 이동을 추적하여 드래그 제스처를 인식합니다.

## 2. UIPanGestureRecognizer 사용하기

### 2.1 Gesture Recognizer 생성

UIPanGestureRecognizer를 사용하기 위해 먼저 해당 제스처 인식기를 생성해야 합니다. 아래의 코드를 사용하여 UIPanGestureRecognizer 인스턴스를 생성하세요.

```swift
let panGestureRecognizer = UIPanGestureRecognizer(target: self, action: #selector(handlePan(_:)))
```

### 2.2 Gesture Recognizer 설정

생성한 UIPanGestureRecognizer 인스턴스를 원하는 뷰에 설정해야 합니다. 대상 뷰에서 해당 제스처를 감지하려면 아래의 코드를 사용하여 설정하세요.

```swift
view.addGestureRecognizer(panGestureRecognizer)
```

### 2.3 Gesture Recognizer 동작 처리

UIPanGestureRecognizer의 동작을 처리하기 위해서는 해당 동작을 처리하는 함수를 구현해야 합니다. 아래와 같은 코드를 작성하세요.

```swift
@objc func handlePan(_ gestureRecognizer: UIPanGestureRecognizer) {
    // UIPanGestureRecognizer로부터 이벤트를 처리하는 코드 작성
}
```

이제 UIPanGestureRecognizer에서 발생한 동작을 위의 `handlePan(_:)` 함수에서 처리할 수 있습니다.

## 3. Gesture Recognizer 데이터 활용

UIPanGestureRecognizer는 사용자의 터치 이동 정보를 제공하므로, 이를 활용하여 드래그 동작에 따른 추가적인 처리를 할 수 있습니다. 아래는 gestureRecognizer를 통해 얻을 수 있는 주요 정보입니다.

- `translation(in: view: CGPoint)`: 사용자의 이동한 거리를 반환합니다.
- `velocity(in: view: CGPoint)`: 사용자의 이동 속도(velocity)를 반환합니다.

이러한 정보를 활용하여 원하는 동작을 수행하거나 애니메이션 등을 구현할 수 있습니다.

## 4. 예제 코드

```swift
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()

        let panGestureRecognizer = UIPanGestureRecognizer(target: self, action: #selector(handlePan(_:)))
        view.addGestureRecognizer(panGestureRecognizer)
    }

    @objc func handlePan(_ gestureRecognizer: UIPanGestureRecognizer) {
        let translation = gestureRecognizer.translation(in: view)
        let velocity = gestureRecognizer.velocity(in: view)

        if gestureRecognizer.state == .began {
            // 드래그 시작 시 동작
        } else if gestureRecognizer.state == .changed {
            // 드래그 중일 때 동작
        } else if gestureRecognizer.state == .ended {
            // 드래그 종료 시 동작
        }
    }
}
```

위의 예제 코드를 사용하여 UIPanGestureRecognizer를 사용해 멀티 터치를 감지하고 처리하는 방법을 실습해보세요.

## 참고 문서

- [Apple Developer - UIPanGestureRecognizer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer)
- [Hacking with Swift - How to detect pan gestures](https://www.hackingwithswift.com/example-code/uikit/how-to-detect-pan-gestures)

감사합니다!