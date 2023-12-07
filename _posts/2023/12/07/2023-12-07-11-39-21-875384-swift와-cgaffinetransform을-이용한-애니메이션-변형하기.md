---
layout: post
title: "[swift] Swift와 CGAffineTransform을 이용한 애니메이션 변형하기"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

애니메이션은 사용자 인터페이스를 향상시키고 상호 작용을 더 흥미롭게 만드는 데 중요한 역할을 합니다. Swift에서는 CGAffineTransform를 사용하여 여러 가지 변형을 적용하여 애니메이션 효과를 만들 수 있습니다. 이번 글에서는 Swift에서 CGAffineTransform을 사용하여 도형에 애니메이션 효과를 적용하는 방법을 알아보겠습니다.

## CGAffineTransform 소개

CGAffineTransform는 2D 그래픽 변환을 나타내는 구조체입니다. 이 구조체는 크기 조정, 회전, 이동 등 다양한 변형을 적용할 수 있습니다. CGAffineTransform은 Core Graphics 프레임워크에서 사용되기 때문에 UIKit을 사용하는 iOS 애플리케이션에서 사용할 수 있습니다.

## 애니메이션 변형 예제

```swift
import UIKit

class ViewController: UIViewController {
    let shapeView = UIView(frame: CGRect(x: 100, y: 100, width: 100, height: 100))
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        shapeView.backgroundColor = .red
        view.addSubview(shapeView)
        
        // 초기 위치와 변형 설정
        shapeView.transform = CGAffineTransform(scaleX: 0.5, y: 0.5)
        
        // 변형 애니메이션 설정
        UIView.animate(withDuration: 2.0, delay: 0.0, options: .curveEaseInOut, animations: {
            self.shapeView.transform = CGAffineTransform(rotationAngle: .pi / 4)
        }, completion: nil)
    }
}
```

위 예제는 UIView를 사용하여 도형을 그린 후, CGAffineTransform을 사용하여 도형에 애니메이션 효과를 적용하는 예제입니다. 

먼저, 뷰 컨트롤러의 viewDidLoad() 메서드에서 shapeView를 생성하고 초기 위치와 변형을 설정합니다. 여기서는 도형의 크기를 0.5배 축소하고, 뷰의 중앙에 위치시킵니다.

그리고 UIView의 animate(withDuration:delay:options:animations:completion:) 메서드를 사용하여 변형 애니메이션을 설정합니다. 여기서는 도형을 45도 회전시키도록 하였습니다. 애니메이션의 시간은 2초로 설정되었습니다.

애니메이션은 지정된 시간 동안 실행되고, curveEaseInOut 옵션을 통해 애니메이션의 시작과 끝 부분이 부드럽게 이루어지도록 설정되었습니다.

## 결론

Swift에서는 CGAffineTransform을 사용하여 UIView에 다양한 애니메이션 효과를 적용할 수 있습니다. 변형을 사용하여 크기 조정, 회전, 이동 등의 효과를 만들어낼 수 있습니다. 애니메이션은 사용자 인터페이스를 더욱 생동감 있게 만들어주므로, 애플리케이션 개발에 있어서 활용할 수 있는 유용한 기능입니다.

참고 자료:
- [Apple Developer Documentation - CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgaffinetransform)