---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UIActionSheet에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 `UIActionSheet`에서 터치 이벤트를 처리하기 위해 `UIResponder`를 사용하는 방법에 대해 알아보겠습니다. 

## 1. `UIResponder`란?

`UIResponder`는 iOS 앱에서 이벤트를 처리하기 위한 추상 클래스입니다. 모든 사용자 이벤트는 `UIResponder`의 인스턴스로 전달되며, 이벤트 핸들링에 사용될 수 있는 메서드를 제공합니다. 

`UIResponder`는 다음과 같은 주요 메서드를 포함하고 있습니다.

- `touchesBegan(_:with:)`: 특정 뷰에서 터치 이벤트가 시작될 때 호출됩니다.
- `touchesMoved(_:with:)`: 특정 뷰에서 터치 이벤트가 이동될 때 호출됩니다.
- `touchesEnded(_:with:)`: 특정 뷰에서 터치 이벤트가 끝날 때 호출됩니다.
- `touchesCancelled(_:with:)`: 특정 뷰에서 터치 이벤트가 취소될 때 호출됩니다.

## 2. `UIActionSheet`에서 `UIResponder` 사용하기

`UIActionSheet`는 사용자가 선택할 수 있는 여러 개의 동작을 보여주는 화면입니다. 이러한 `UIActionSheet`에서 특정 버튼이나 영역을 터치했을 때 이벤트를 처리하려면 `UIResponder`를 구현해야 합니다. 아래는 `UIResponder`를 사용하여 터치 이벤트를 처리하는 예제 코드입니다.

```swift
class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let actionSheet = UIActionSheet(title: "액션 시트", delegate: self, cancelButtonTitle: "취소", destructiveButtonTitle: "삭제")
        actionSheet.showInView(self.view)
    }
    
    // 터치 이벤트가 시작될 때 호출되는 메서드
    override func touchesBegan(touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first
        let touchPoint = touch?.locationInView(self.view)
        
        // 터치한 지점의 좌표 값
        let x = touchPoint?.x
        let y = touchPoint?.y
        
        print("터치 시작 - x: \(x), y: \(y)")
    }
    
    // 터치 이벤트가 이동될 때 호출되는 메서드
    override func touchesMoved(touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first
        let touchPoint = touch?.locationInView(self.view)
        
        // 터치한 지점의 좌표 값
        let x = touchPoint?.x
        let y = touchPoint?.y
        
        print("터치 이동 - x: \(x), y: \(y)")
    }
    
    // 터치 이벤트가 끝날 때 호출되는 메서드
    override func touchesEnded(touches: Set<UITouch>, with event: UIEvent?) {
        let touch = touches.first
        let touchPoint = touch?.locationInView(self.view)
        
        // 터치한 지점의 좌표 값
        let x = touchPoint?.x
        let y = touchPoint?.y
        
        print("터치 종료 - x: \(x), y: \(y)")
    }
    
    // 터치 이벤트가 취소될 때 호출되는 메서드
    override func touchesCancelled(touches: Set<UITouch>, with event: UIEvent?) {
        print("터치 취소")
    }
}

extension ViewController: UIActionSheetDelegate {
    
    func actionSheet(actionSheet: UIActionSheet, clickedButtonAtIndex buttonIndex: Int) {
        // 버튼을 클릭했을 때 처리할 내용
        if buttonIndex == 0 {
            print("삭제 버튼 클릭")
        } else if buttonIndex == 1 {
            print("취소 버튼 클릭")
        }
    }
}
```

위의 코드에서 `touchesBegan(_:with:)`, `touchesMoved(_:with:)`, `touchesEnded(_:with:)`, `touchesCancelled(_:with:)` 메서드를 오버라이드하여 터치 이벤트를 처리하면 됩니다. `UIActionSheetDelegate` 프로토콜을 채택하여 `actionSheet(_:clickedButtonAtIndex:)` 메서드에서 버튼 클릭 이벤트를 처리할 수 있습니다.

이제 `UIActionSheet`에서 발생하는 터치 이벤트를 `UIResponder`를 사용하여 쉽게 처리할 수 있습니다. 각각의 이벤트 발생 시 호출되는 메서드를 사용하여 원하는 동작을 구현하면 됩니다.

## 참고 자료
- [Apple Developer Documentation - UIResponder](https://developer.apple.com/documentation/uikit/uiresponder)
- [Apple Developer Documentation - UIActionSheet](https://developer.apple.com/documentation/uikit/uiactionsheet)