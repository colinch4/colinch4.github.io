---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UITextView에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

iOS 애플리케이션을 개발할 때, 사용자의 터치 이벤트를 처리해야 할 때가 있습니다. UITextView와 같은 텍스트 뷰에서 터치 이벤트를 다루는 방법에 대해 알아보겠습니다.

## UIResponder 클래스

UIKit 프레임워크에서 UIResponder는 사용자의 터치 이벤트를 처리하기 위한 기본 클래스입니다. UIResponder는 UIResponder 메서드를 오버라이드하여 터치 이벤트를 처리할 수 있습니다.

## UITextView에서의 UIResponder 사용법

다음은 UITextView에서 터치 이벤트를 처리하는 예제 코드입니다.

```swift
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let textView = UITextView(frame: CGRect(x: 50, y: 50, width: 200, height: 200))
        textView.backgroundColor = .white
        textView.text = "Tap Here"
        textView.textAlignment = .center
        textView.isUserInteractionEnabled = true
        
        self.view.addSubview(textView)
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        guard let touch = touches.first else { return }
        let touchLocation = touch.location(in: self.view)
        
        if let textView = self.view.hitTest(touchLocation, with: event) as? UITextView {
            print("Tapped on UITextView")
            // 터치한 UITextView에 대한 추가 작업을 수행할 수 있습니다.
        }
    }
}
```

위의 예제 코드에서 `touchesBegan(_:with:)` 메서드를 오버라이드하여 터치 이벤트를 처리합니다. 이 메서드는 터치가 시작된 시점에 호출되는 메서드입니다. 터치한 위치를 통해 뷰 계층 구조에서 터치한 뷰를 찾아내고, 해당 뷰가 UITextView인 경우 추가 작업을 수행할 수 있습니다.

## 정리

UITextView에서 터치 이벤트를 처리하기 위해 UIResponder의 메서드를 오버라이드하여 사용할 수 있습니다. 이를 통해 UITextView에 터치 이벤트에 대한 추가 작업을 쉽게 구현할 수 있습니다.

참고자료:
- [UIResponder - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiresponder)
- [UITextView - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitextview)