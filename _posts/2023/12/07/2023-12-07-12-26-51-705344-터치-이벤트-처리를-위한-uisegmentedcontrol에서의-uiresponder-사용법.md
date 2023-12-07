---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UISegmentedControl에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

iOS 앱을 개발할 때, 사용자의 터치 이벤트를 처리해야 할 때가 많습니다. 이 중에서 UISegmentedControl는 여러 개의 선택지 중에서 하나를 선택할 수 있는 컨트롤입니다. 이번 글에서는 UISegmentedControl에서 발생하는 터치 이벤트를 처리하는 방법에 대해 알아보겠습니다.

## 1. UIResponder를 상속받는 커스텀 뷰 만들기

먼저, UISegmentedControl에서 발생하는 터치 이벤트를 처리하기 위해 UIResponder를 상속받는 커스텀 뷰를 만들어야 합니다. 다음과 같이 코드를 작성해보세요.

```swift
import UIKit

class CustomSegmentedControl: UISegmentedControl {
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesBegan(touches, with: event)
        
        // 터치 이벤트가 시작되었을 때 실행할 코드 작성
        print("Touches began")
        
        // 선택된 세그먼트의 인덱스 가져오기
        if let touch = touches.first {
            let location = touch.location(in: self)
            let selectedSegmentIndex = self.segmentIndex(at: location)
            print("Selected segment index: \(selectedSegmentIndex)")
        }
    }
    
    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesMoved(touches, with: event)
        
        // 터치 이벤트가 이동중일 때 실행할 코드 작성
        print("Touches moved")
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        super.touchesEnded(touches, with: event)
        
        // 터치 이벤트가 종료되었을 때 실행할 코드 작성
        print("Touches ended")
    }
}
```

위 코드는 `CustomSegmentedControl`이라는 이름의 커스텀 뷰를 만들어줍니다. `touchesBegan`, `touchesMoved`, `touchesEnded` 메소드를 오버라이드하여 각각 터치 이벤트가 발생했을 때 실행될 코드를 작성합니다. 예시로 각각 "Touches began", "Touches moved", "Touches ended"라는 메시지를 출력하고, 선택된 세그먼트의 인덱스도 출력하게 하였습니다.

## 2. 커스텀 뷰 사용하기

이제 위에서 만든 커스텀 뷰를 실제로 사용해보겠습니다. UIViewController에서 커스텀 뷰를 추가하고, 터치 이벤트를 처리하는 코드를 작성해보세요.

```swift
import UIKit

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 커스텀 뷰 생성
        let segmentedControl = CustomSegmentedControl(items: ["First", "Second", "Third"])
        segmentedControl.frame = CGRect(x: 50, y: 100, width: 300, height: 50)
        
        // 세그먼트 선택 시 발생할 액션 설정
        segmentedControl.addTarget(self, action: #selector(segmentedControlValueChanged), for: .valueChanged)
        
        // 뷰에 추가
        view.addSubview(segmentedControl)
    }
    
    @objc func segmentedControlValueChanged(_ sender: UISegmentedControl) {
        // 세그먼트 선택 시 실행될 코드 작성
        let selectedSegmentIndex = sender.selectedSegmentIndex
        print("Selected segment index: \(selectedSegmentIndex)")
    }
}
```

위 코드에서는 `ViewController` 클래스에서 `CustomSegmentedControl`을 생성하여 뷰에 추가하고, 세그먼트가 선택되었을 때 실행될 액션 메소드를 설정합니다. 예시로 선택된 세그먼트의 인덱스를 출력하는 코드를 작성했습니다.

이제 앱을 실행하고 세그먼트를 선택해보면, 터치 이벤트 처리와 관련된 메시지와 선택된 세그먼트의 인덱스가 콘솔에 출력될 것입니다.

이처럼 UISegmentedControl에서 발생하는 터치 이벤트를 처리하는 방법에 대해 알아보았습니다. 커스텀 뷰를 만들어서 사용하는 방법을 알고 있다면 다양한 터치 이벤트를 자유롭게 처리할 수 있습니다.

## 참고 자료

- [Apple Developer Documentation - UIResponder](https://developer.apple.com/documentation/uikit/uiresponder)
- [Apple Developer Documentation - UISegmentedControl](https://developer.apple.com/documentation/uikit/uisegmentedcontrol)