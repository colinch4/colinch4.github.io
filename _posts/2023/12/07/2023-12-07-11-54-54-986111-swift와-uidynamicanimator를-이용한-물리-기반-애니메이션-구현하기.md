---
layout: post
title: "[swift] Swift와 UIDynamicAnimator를 이용한 물리 기반 애니메이션 구현하기"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

물리 기반 애니메이션은 객체들 간의 물리적 상호작용을 시뮬레이션하여 자연스러운 움직임을 만들어내는 기술입니다. Swift에서는 UIDynamicAnimator를 사용하여 물리 기반 애니메이션을 구현할 수 있습니다.

## 1. UIDynamicAnimator란?

UIDynamicAnimator는 iOS에서 제공되는 물리 기반 애니메이션을 구현하기 위한 클래스입니다. 움직이는 객체들 간의 상호작용을 모델링하고, 이를 시뮬레이션하여 애니메이션을 생성합니다.

## 2. 물리 기반 애니메이션 구현하기 예제

아래는 Swift에서 UIDynamicAnimator를 사용하여 물리 기반 애니메이션을 구현하는 예제 코드입니다.

```swift
import UIKit

class ViewController: UIViewController {
    
    var dynamicAnimator: UIDynamicAnimator!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 애니메이션을 적용할 뷰를 생성
        let boxView = UIView(frame: CGRect(x: 100, y: 100, width: 100, height: 100))
        boxView.backgroundColor = .red
        view.addSubview(boxView)
        
        // UIDynamicAnimator 인스턴스 생성
        dynamicAnimator = UIDynamicAnimator(referenceView: view)
        
        // 애니메이션에 적용할 동작 객체 생성
        let gravityBehavior = UIGravityBehavior(items: [boxView])
        dynamicAnimator.addBehavior(gravityBehavior)
        
        let collisionBehavior = UICollisionBehavior(items: [boxView])
        collisionBehavior.translatesReferenceBoundsIntoBoundary = true
        dynamicAnimator.addBehavior(collisionBehavior)
        
        let elasticityBehavior = UIDynamicItemBehavior(items: [boxView])
        elasticityBehavior.elasticity = 0.5
        dynamicAnimator.addBehavior(elasticityBehavior)
    }
}
```

위의 코드는 UIView에서 상속받은 ViewController 클래스를 만들고, viewDidLoad 메서드에서 물리 기반 애니메이션을 구현하는 것을 보여줍니다. 

뷰 컨트롤러에 애니메이션을 적용할 뷰를 생성하고, UIDynamicAnimator 클래스의 인스턴스를 생성하여 물리 기반 동작을 추가합니다. 여기서는 중력 동작, 충돌 동작, 탄성 동작을 추가하였습니다.

## 3. 참고 자료

- Apple Developer Documentation - [UIDynamicAnimator](https://developer.apple.com/documentation/uikit/uidynamicanimator)
- Apple Developer Documentation - [UIGravityBehavior](https://developer.apple.com/documentation/uikit/uigravitybehavior)
- Apple Developer Documentation - [UICollisionBehavior](https://developer.apple.com/documentation/uikit/uicollisionbehavior)
- Apple Developer Documentation - [UIDynamicItemBehavior](https://developer.apple.com/documentation/uikit/uidynamicitembehavior)

위의 예제 코드와 참고 자료를 참고하여, Swift와 UIDynamicAnimator를 이용하여 물리 기반 애니메이션을 구현해보세요!