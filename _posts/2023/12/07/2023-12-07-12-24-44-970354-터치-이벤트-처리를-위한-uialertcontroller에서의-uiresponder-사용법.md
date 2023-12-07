---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UIAlertController에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UIAlertController는 iOS 애플리케이션에서 간단한 팝업 알림을 표시할 때 자주 사용되는 UI 컴포넌트입니다. UIAlertController에는 기본적으로 "OK"나 "Cancel"과 같은 단순한 액션 버튼을 추가할 수 있습니다. 그러나 때로는 UIAlertController에 사용자 정의 동작을 추가하고 싶을 때가 있습니다. 이런 경우 UIResponder를 사용하여 터치 이벤트를 처리할 수 있습니다.

아래는 터치 이벤트 처리를 위해 UIAlertController에서 UIResponder를 사용하는 간단한 예제입니다.

```swift
import UIKit

class CustomAlertController: UIAlertController {
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        // 터치 이벤트 처리 로직을 작성합니다.
        super.touchesBegan(touches, with: event)
    }
}

class ViewController: UIViewController {
    
    @IBAction func showAlert(_ sender: UIButton) {
        let alertController = CustomAlertController(title: "알림", message: "버튼을 터치했습니다!", preferredStyle: .alert)
        
        let okAction = UIAlertAction(title: "확인", style: .default, handler: nil)
        alertController.addAction(okAction)
        
        present(alertController, animated: true, completion: nil)
    }

    //...
}
```

위의 예제에서는 CustomAlertController라는 서브클래스를 만들어 UIResponder를 상속받습니다. 그리고 touchesBegan 메서드를 오버라이드하여 터치 이벤트를 처리할 수 있는 커스텀 로직을 추가합니다. 이 커스텀 알림 컨트롤러는 기본 UIAlertController와 동일하게 작동하지만, touchesBegan 메서드가 호출되는 것을 확인할 수 있습니다.

이제 ViewController에서 showAlert 메서드를 호출하면 커스텀 알림이 화면에 표시되고, 터치 이벤트가 발생하면 touchesBegan 메서드가 호출됩니다.

기존의 UIAlertController에 추가적인 기능을 더해야할 때에는 UIResponder를 상속받아 해당 기능을 구현하는 방식을 사용할 수 있습니다.

이외에도 UIResponder는 다른 UI 컴포넌트에서도 터치 이벤트를 처리하는데 사용될 수 있으며, 각 컴포넌트마다 다양한 메서드들을 오버라이드하여 터치 이벤트를 커스텀으로 처리할 수 있습니다.

참고: 
- [Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiresponder)
- [Swift Documentation](https://docs.swift.org/swift-book/LanguageGuide/Inheritance.html)
- [iOS Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/overview/themes)