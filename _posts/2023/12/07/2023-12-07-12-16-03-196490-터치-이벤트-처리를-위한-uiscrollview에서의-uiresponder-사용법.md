---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UIScrollView에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UIScrollView는 iOS 앱에서 많이 사용되는 스크롤 가능한 뷰입니다. UIScrollView에서 터치 이벤트를 처리하기 위해 UIResponder를 사용할 수 있습니다. UIResponder 클래스는 iOS에서 이벤트에 응답하는 데 사용되는 추상 기본 클래스입니다.

## UIResponder 이해하기

UIResponder를 이해하기 위해 먼저 UIResponder의 역할과 특징을 살펴보겠습니다. UIResponder는 오직 한 번에 하나의 이벤트에만 응답할 수 있으며, 먼저 이벤트를 받을 수 있는 응답자가 이벤트를 처리하게 됩니다. UIResponder를 상속받은 클래스는 이벤트를 처리하기 위해 다음과 같은 메서드를 오버라이드할 수 있습니다:

- `touchesBegan(_:with:)`: 터치가 시작될 때 호출되는 메서드입니다.
- `touchesMoved(_:with:)`: 터치가 움직일 때 호출되는 메서드입니다.
- `touchesEnded(_:with:)`: 터치가 끝날 때 호출되는 메서드입니다.
- `touchesCancelled(_:with:)`: 터치가 취소될 때 호출되는 메서드입니다.

### UIScrollView에서의 UIResponder 사용하기

UIScrollView는 UIResponder를 상속받은 클래스이므로, 위의 메서드들을 오버라이드하여 터치 이벤트를 처리할 수 있습니다. 다음과 같은 단계를 따라 UIScrollView에서 터치 이벤트를 처리해보세요:

1. UIScrollView를 서브클래싱합니다. 예를 들어, 아래의 코드와 같이 CustomScrollView 클래스를 작성합니다.

```swift
class CustomScrollView: UIScrollView {
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치 시작 시 호출되는 메서드
        // 여기에 터치 시작 이벤트 처리 로직을 작성하세요
    }
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치 이동 시 호출되는 메서드
        // 여기에 터치 이동 이벤트 처리 로직을 작성하세요
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치 종료 시 호출되는 메서드
        // 여기에 터치 종료 이벤트 처리 로직을 작성하세요
    }
    
    override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치 취소 시 호출되는 메서드
        // 여기에 터치 취소 이벤트 처리 로직을 작성하세요
    }
}
```

2. UIScrollView를 CustomScrollView로 바꾸어 사용합니다.

```swift
let customScrollView = CustomScrollView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
// UIScrollView 대신 CustomScrollView를 사용합니다.
```

3. 이제 CustomScrollView에서 원하는 터치 이벤트를 처리할 수 있습니다. 오버라이드한 메서드에서 원하는 로직을 작성하세요.

## 결론

UIScrollView는 UIResponder를 상속받은 클래스이기 때문에 터치 이벤트를 처리할 수 있습니다. 이를 활용하여 UIScrollView에서 사용자의 터치 동작을 캡처하고 원하는 동작을 수행할 수 있습니다. UIResponder의 다른 메서드 및 속성도 사용하여 더 복잡한 동작을 구현할 수 있습니다.

더 자세한 내용은 [Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiresponder)을 참조하세요.