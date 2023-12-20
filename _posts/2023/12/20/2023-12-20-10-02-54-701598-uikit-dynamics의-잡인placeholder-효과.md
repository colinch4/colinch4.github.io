---
layout: post
title: "[swift] UIKit Dynamics의 잡인(placeholder) 효과"
description: " "
date: 2023-12-20
tags: [swift]
comments: true
share: true
---

UIKit Dynamics는 iOS 앱에 물리적 특성을 추가하는 데 사용되는 강력한 프레임워크입니다. 잡인(placeholder)은 사용자가 특정 위치에 뷰를 드래그하고 놓았을 때 원래 위치로 돌아가도록 하는 효과입니다.

이 효과를 구현하려면 다음 단계를 따릅니다.

### 1. UIDynamicAnimator 만들기
UIKit Dynamics를 사용하려면 `UIDynamicAnimator`를 만들어야 합니다. 이는 물리 시뮬레이션을 관리하는 핵심 객체입니다. 

```swift
let animator = UIDynamicAnimator(referenceView: self.view)
```

### 2. UICollisionBehavior 추가
`UICollisionBehavior`는 뷰들이 충돌하고 반발할 수 있도록 해줍니다.
```swift
let collision = UICollisionBehavior(items: [yourView])
collision.translatesReferenceBoundsIntoBoundary = true
animator.addBehavior(collision)
```

### 3. UIAttachmentBehavior 만들기
`UIAttachmentBehavior`는 뷰를 다른 뷰나 점에 '부착'시킵니다. 이를 이용하여 잡인(placeholder) 효과를 구현할 수 있습니다.
```swift
let attachment = UIAttachmentBehavior(item: yourView, attachedToAnchor: yourAnchorPoint)
animator.addBehavior(attachment)
```

위의 단계를 따라하면 사용자가 뷰를 드래그하고 놓았을 때 물리적인 효과를 통해 뷰가 원래의 위치로 돌아가는 잡인(placeholder) 효과를 구현할 수 있습니다.

참조: [Apple Developer Documentation - UIDynamicAnimator](https://developer.apple.com/documentation/uikit/uidynamicanimator), [Apple Developer Documentation - UICollisionBehavior](https://developer.apple.com/documentation/uikit/uicollisionbehavior), [Apple Developer Documentation - UIAttachmentBehavior](https://developer.apple.com/documentation/uikit/uiattachmentbehavior)