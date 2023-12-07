---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UIImageView에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UIKit에서는 사용자가 화면을 터치했을 때 발생하는 터치 이벤트를 처리하기 위해 UIResponder를 사용합니다. UIImageView는 UIResponder를 상속받은 UIView의 하위 클래스이므로, UIImageView에서도 터치 이벤트를 처리할 수 있습니다.

## 터치 이벤트 처리를 위한 UIResponder 메소드

UIResponder에서는 다음과 같은 터치 이벤트 처리 관련 메소드를 제공합니다.

- `touchesBegan(_:with:)`: 사용자가 화면에 터치를 시작할 때 호출됩니다.
- `touchesMoved(_:with:)`: 사용자가 터치한 채로 손가락을 움직일 때 호출됩니다.
- `touchesEnded(_:with:)`: 사용자가 화면에서 손가락을 떼었을 때 호출됩니다.
- `touchesCancelled(_:with:)`: 특정 이벤트에 의해 터치가 취소되었을 때 호출됩니다.

이 메소드들을 오버라이드하여 터치 이벤트에 대한 처리 로직을 구현할 수 있습니다.

## UIImageView에서 터치 이벤트 처리 예제

다음은 UIImageView에서 터치 이벤트를 처리하는 예제 코드입니다.

```swift
import UIKit

class TouchImageView: UIImageView {
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치 시작 시 처리 로직 작성
        // 예: 이미지뷰를 빨간색으로 변환
        self.backgroundColor = .red
    }
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치 이동 시 처리 로직 작성
        // 예: 이미지뷰의 좌표를 이동하여 따라 움직이기
        if let touch = touches.first {
            let location = touch.location(in: self.superview)
            self.center = location
        }
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치 종료 시 처리 로직 작성
        // 예: 이미지뷰를 다시 원래 색으로 변환
        self.backgroundColor = .clear
    }
    
    override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치 취소 시 처리 로직 작성
    }
}
```

위의 예제 코드는 TouchImageView라는 UIImageView의 서브클래스를 정의하고, 터치 이벤트에 따른 처리 로직을 구현한 것입니다. touchesBegan에서는 이미지뷰의 배경색을 빨간색으로 변경하고, touchesMoved에서는 이미지뷰의 중심 좌표를 터치한 위치로 이동시킵니다. touchesEnded에서는 배경색을 다시 투명으로 되돌리는 로직을 작성하였습니다.

이제 위의 코드를 기반으로 UIImageView를 생성하고 화면에 추가하면, 해당 이미지뷰를 터치할 때마다 지정된 로직이 실행될 것입니다.

## 참고 자료

- [Apple Developer Documentation - UIResponder](https://developer.apple.com/documentation/uikit/uiresponder)
- [Apple Developer Documentation - UIView](https://developer.apple.com/documentation/uikit/uiview)
- [Hacking with Swift - How to handle touch events using UIResponder](https://www.hackingwithswift.com/example-code/uikit/how-to-handle-touch-events-using-uiresponder)