---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UIRotationGestureRecognizer 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

iOS 앱을 개발하다 보면 터치 이벤트 처리가 필요한 경우가 많이 있습니다. 이 중에서도 원하는 뷰를 회전시키기 위해 UIRotationGestureRecognizer를 사용하는 방법에 대해 알아보겠습니다.

## UIRotationGestureRecognizer란?

UIRotationGestureRecognizer는 사용자의 두 손가락을 사용하여 뷰를 회전시킬 수 있는 제스처 인식기입니다. 이를 통해 사용자는 회전 동작을 인식하여 앱에 반응하도록 할 수 있습니다.

## UIRotationGestureRecognizer를 사용한 터치 이벤트 처리

다음은 UIRotationGestureRecognizer를 사용하여 터치 이벤트를 처리하는 간단한 예제입니다.

```swift
import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let rotationGestureRecognizer = UIRotationGestureRecognizer(target: self, action: #selector(handleRotation(_:)))
        self.view.addGestureRecognizer(rotationGestureRecognizer)
    }

    @objc func handleRotation(_ sender: UIRotationGestureRecognizer) {
        // 회전 제스처 처리 코드 작성
        let rotation = sender.rotation
        // 회전각을 이용하여 뷰를 회전시킬 수 있음
        
        if sender.state == .ended {
            // 회전 제스처 종료 시 처리할 코드 작성
        }
    }
}
```

위 코드에서는 뷰 컨트롤러의 viewDidLoad 메서드에서 UIRotationGestureRecognizer를 생성하고 해당 제스처를 인식할 때 호출할 메서드를 설정합니다. handleRotation 메서드에서는 회전 제스처의 각도를 사용하여 뷰를 회전시킬 수 있습니다. 또한, 제스처가 종료될 때 추가적인 처리를 하고 싶다면 if 문을 사용하여 처리할 수 있습니다.

## 결과 확인

위 예제 코드를 실행하여 앱을 실행한 후, 두 손가락을 사용하여 뷰를 회전시켜보세요. 회전 제스처에 따라 뷰가 회전될 것입니다. 또한 회전 제스처가 종료될 때 추가적인 동작이 수행되도록 코드를 작성할 수 있습니다.

이처럼 UIRotationGestureRecognizer를 사용하면 사용자의 회전 제스처를 인식하여 뷰를 회전시킬 수 있습니다. 다양한 제스처 인식기를 활용하여 앱에 다양한 터치 이벤트 처리 기능을 추가할 수 있습니다.

## 참고 자료
- [Apple Developer Documentation - UIRotationGestureRecognizer](https://developer.apple.com/documentation/uikit/uirotationgesturerecognizer)