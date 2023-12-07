---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UIPanGestureRecognizer 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UIPanGestureRecognizer는 사용자의 터치 동작을 감지하여 이벤트를 처리하는데 사용됩니다. 이 제스처는 사용자가 화면에서 손가락을 누르고 드래그하면 발생하며, 해당 위치의 변화를 추적하여 처리할 수 있습니다.

## 1. UIPanGestureRecognizer 객체 생성

터치 이벤트를 처리하기 위해 먼저 UIPanGestureRecognizer 객체를 생성해야 합니다. 다음과 같은 코드를 사용하여 객체를 생성할 수 있습니다.

```swift
let panGestureRecognizer = UIPanGestureRecognizer(target: self, action: #selector(handlePan(_:)))
```

위 코드에서 `target` 파라미터는 이벤트 처리를 담당할 객체를 지정하고, `action` 파라미터는 이벤트가 발생했을 때 호출될 메서드를 지정합니다.

## 2. 이벤트 처리 메서드 구현

이어서, 터치 이벤트가 발생했을 때 호출될 메서드를 구현해야 합니다. `@objc` 어노테이션을 사용하여 Objective-C에서 호환되는 메서드로 선언해야 합니다. 메서드는 `UIPanGestureRecognizer` 객체를 파라미터로 전달받을 수 있도록 해야합니다. 다음은 간단한 예시입니다.

```swift
@objc func handlePan(_ gestureRecognizer: UIPanGestureRecognizer) {
    // 이벤트 처리 로직 작성
}
```

위 예시에서는 `handlePan:` 메서드가 UIPanGestureRecognizer를 파라미터로 받아서 이벤트 처리를 할 수 있는 로직을 작성하면 됩니다.

## 3. 제스처 등록

마지막으로, 생성한 UIPanGestureRecognizer 객체를 해당 뷰에 등록해야 합니다. 등록된 제스처는 뷰에서 터치 이벤트를 받을 수 있게 됩니다. 예시 코드는 다음과 같습니다.

```swift
view.addGestureRecognizer(panGestureRecognizer)
```

위 코드에서 `view`는 이벤트를 처리할 뷰 객체입니다. 위 코드로 제스처가 등록되면 사용자의 터치 동작을 감지할 수 있게 됩니다.

## 예시

이제 실제로 UIPanGestureRecognizer를 사용하여 터치 이벤트를 처리하는 예시를 살펴보겠습니다.

```swift
class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let panGestureRecognizer = UIPanGestureRecognizer(target: self, action: #selector(handlePan(_:)))
        view.addGestureRecognizer(panGestureRecognizer)
    }
    
    @objc func handlePan(_ gestureRecognizer: UIPanGestureRecognizer) {
        let translation = gestureRecognizer.translation(in: view)
        if let view = gestureRecognizer.view {
            view.center = CGPoint(x: view.center.x + translation.x, y: view.center.y + translation.y)
        }
        gestureRecognizer.setTranslation(CGPoint.zero, in: view)
    }
}
```

위 예제 코드는 뷰 컨트롤러에 UIPanGestureRecognizer를 추가하고, 사용자가 뷰를 드래그하여 이동시키는 기능을 구현합니다. 사용자가 드래그하는 방향에 따라 뷰가 이동하게 되며, 사용자가 손가락을 뗄 때마다 뷰의 위치를 초기화합니다.

## 참고 자료

- [Apple Developer Documentation - UIPanGestureRecognizer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer)
- [Swift Docs - #selector](https://docs.swift.org/swift-book/ReferenceManual/Expressions.html#grammar_selector)
- [raywenderlich.com - Gesture Recognizers Tutorial: Getting Started](https://www.raywenderlich.com/10326409-gesture-recognizers-tutorial-getting-started)