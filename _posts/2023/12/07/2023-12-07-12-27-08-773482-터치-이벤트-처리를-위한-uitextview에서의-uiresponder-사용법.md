---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UITextView에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

앱에서 UITextView를 사용하여 텍스트를 입력하고 편집할 때, 때로는 특정 터치 이벤트를 처리해야 할 수 있습니다. UIResponder를 사용하여 UITextView에서의 터치 이벤트를 처리하는 방법에 대해 알아보겠습니다.

### UIResponder란?

UIResponder는 iOS 앱에서 이벤트를 처리하기 위한 추상 클래스입니다. 모든 UIView, UIViewController, UIApplication은 UIResponder를 상속받습니다. UIResponder 클래스는 UIResponderChain으로 불리는 이벤트 전달 체인을 통해 이벤트를 처리합니다.

### 터치 이벤트 처리하기

일반적으로 UITextView에서의 터치 이벤트 처리는 UIResponder의 메소드를 override하여 구현합니다. 다음은 UITextView에서의 터치 이벤트 처리를 위해 UIResponder를 사용하는 예제입니다.

```swift
import UIKit

class CustomTextView: UITextView {
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesBegan(touches, with: event)
        
        guard let touch = touches.first else {
            return
        }
        
        let location = touch.location(in: self)
        
        // 터치한 위치에 따라 특정 동작 수행
        if location.x < bounds.width / 2 {
            // 왼쪽 절반 부분 터치 시 동작
            // ...
        } else {
            // 오른쪽 절반 부분 터치 시 동작
            // ...
        }
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesEnded(touches, with: event)
        
        // 터치 종료 시 동작
        // ...
    }
    
    override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesCancelled(touches, with: event)
        
        // 터치 취소 시 동작
        // ...
    }
}
```

위의 예제에서는 UITextView를 상속받은 CustomTextView를 만들고, 터치 이벤트가 발생할 때 호출되는 UIResponder 메소드들을 override하여 원하는 동작을 구현하였습니다. 터치 시작, 터치 종료, 터치 취소 시 각각 특정 동작을 수행할 수 있습니다.

### 참고 자료

- [Apple Developer Documentation - UIResponder](https://developer.apple.com/documentation/uikit/uiresponder)
- [Apple Developer Documentation - UIResponder Chain](https://developer.apple.com/documentation/uikit/event_delivery_responder_chain)