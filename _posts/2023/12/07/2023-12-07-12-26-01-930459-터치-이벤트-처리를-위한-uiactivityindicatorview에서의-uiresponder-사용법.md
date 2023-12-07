---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UIActivityIndicatorView에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 UIActivityIndicatorView에서의 터치 이벤트 처리에 대해 알아보겠습니다. 

UIActivityIndicatorView는 작업이 진행 중임을 나타내는 인디케이터로, 기본적으로 사용자의 상호작용을 받지 않습니다. 그러나 필요에 따라 사용자와의 인터랙션을 허용하고 터치 이벤트를 처리할 수도 있습니다. 이를 위해 UIResponder를 사용하여 커스텀한 터치 이벤트를 처리해보겠습니다.

## UIResponder를 상속한 커스텀 클래스 생성하기

먼저, 사용자 인터랙션을 허용하고자 하는 UIActivityIndicatorView에 대해 UIResponder를 상속한 커스텀 클래스를 생성합니다. 아래와 같이 코드를 작성해주세요.

```swift
import UIKit

class TouchableActivityIndicatorView: UIActivityIndicatorView {

    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesBegan(touches, with: event)
        // 터치 이벤트 처리 로직 추가
        // 예시: 인디케이터를 일시정지하는 로직
        self.stopAnimating()
    }
}
```

위의 코드에서는 touchesBegan 메서드를 오버라이드하여 터치 이벤트를 처리합니다. 여기서는 간단한 예시로, UIActivityIndicatorView를 일시정지하는 로직을 추가하였습니다.

## 사용자 인터랙션을 허용하는 UIActivityIndicatorView 사용하기

자 이제, 커스텀한 TouchableActivityIndicatorView를 사용해봅시다. 다음과 같이 코드를 작성해주세요.

```swift
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let touchableActivityIndicatorView = TouchableActivityIndicatorView(style: .large)
        touchableActivityIndicatorView.frame = CGRect(x: 0, y: 0, width: 100, height: 100)
        touchableActivityIndicatorView.center = self.view.center
        touchableActivityIndicatorView.isUserInteractionEnabled = true
        self.view.addSubview(touchableActivityIndicatorView)
        
        touchableActivityIndicatorView.startAnimating()
    }
}
```

위의 코드에서는 TouchableActivityIndicatorView를 생성하고, 화면 중앙에 배치한 뒤, `isUserInteractionEnabled` 속성을 true로 설정하여 사용자 인터랙션을 허용하였습니다. 마지막으로, `startAnimating()` 메서드를 호출하여 인디케이터를 시작합니다.

## 마무리

이제 UIActivityIndicatorView에서의 터치 이벤트 처리를 위해 UIResponder를 사용하는 방법에 대해 알아보았습니다. 필요에 따라 코드를 수정하여 다양한 터치 이벤트를 처리할 수 있습니다. 추가로, 다른 UIResponder 메서드를 오버라이드하여 원하는 동작을 추가할 수도 있습니다.