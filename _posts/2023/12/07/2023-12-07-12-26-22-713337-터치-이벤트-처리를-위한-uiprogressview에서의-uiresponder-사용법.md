---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UIProgressView에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UIProgressView는 iOS 앱에서 진행 상태를 표시하는데 사용되는 UI 요소입니다. UIProgressView에는 기본적으로 터치 이벤트 처리를 위한 기능이 내장되어 있지 않습니다. 하지만 UIResponder를 사용하여 터치 이벤트를 처리할 수 있습니다. 

## UIResponder를 상속하여 UIProgressView에 터치 이벤트 추가하기

터치 이벤트를 처리하기 위해 UIProgressView를 상속한 자체적인 클래스를 만들어야 합니다. 이 클래스는 UIResponder를 상속하고, touchesBegan(_:_:), touchesMoved(_:_:), touchesEnded(_:_:), touchesCancelled(_:_:)와 같은 UIResponder의 메서드를 구현해야 합니다.

```swift
class TouchableProgressView: UIProgressView {

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치가 시작될 때 실행되는 코드
        super.touchesBegan(touches, with: event)
        
        // 터치 이벤트를 처리하는 코드 작성
        // 예: 진행 상태를 변경하거나 특정 동작을 수행합니다.
    }
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치가 이동될 때 실행되는 코드
        super.touchesMoved(touches, with: event)
        
        // 터치 이벤트를 처리하는 코드 작성
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치가 끝났을 때 실행되는 코드
        super.touchesEnded(touches, with: event)
        
        // 터치 이벤트를 처리하는 코드 작성
    }
    
    override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치가 취소될 때 실행되는 코드
        super.touchesCancelled(touches, with: event)
        
        // 터치 이벤트를 처리하는 코드 작성
    }
}
```

## 사용 예제

위에서 정의한 TouchableProgressView를 사용하려면 다음과 같이 인스턴스화하고 뷰 계층에 추가해야 합니다.

```swift
let touchableProgressView = TouchableProgressView(frame: CGRect(x: 50, y: 100, width: 200, height: 20))
self.view.addSubview(touchableProgressView)
```

TouchableView로부터 상속한 클래스를 사용하면 해당 UIProgressView에 터치 이벤트를 처리할 수 있습니다. touchesBegan(_:_:), touchesMoved(_:_:), touchesEnded(_:_:), touchesCancelled(_:_:) 메서드를 사용하여 터치 이벤트를 적절히 처리하세요.

## 결론

UIProgressView에서 UIResponder를 사용하여 터치 이벤트를 처리하는 것은 매우 유용합니다. 이를 통해 사용자의 터치 동작에 따라 진행 상태를 변경하거나 추가적인 동작을 수행할 수 있습니다. 이를 통해 앱의 사용자 경험을 개선할 수 있습니다.