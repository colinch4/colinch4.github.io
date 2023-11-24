---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 함께 사용할 수 있는 애니메이션 효과 대체 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

애플리케이션의 사용자 인터페이스를 향상시키기 위해 애니메이션 효과는 중요한 요소입니다. NVActivityIndicatorView는 Swift에서 많이 사용되는 애니메이션 라이브러리 중 하나입니다. 그러나 NVActivityIndicatorView를 대체할 수 있는 다른 옵션들도 있습니다. 이 글에서는 Swift에서 NVActivityIndicatorView와 함께 사용할 수 있는 애니메이션 효과 대체 방법에 대해 알아보겠습니다.

## 1. Lottie

Lottie는 Airbnb에서 만든 오픈 소스 애니메이션 라이브러리입니다. 이 라이브러리는 JSON 형식으로 되어있는 에셋 파일을 사용하여 애니메이션을 구현합니다. Lottie 파일은 After Effects나 Bodymovin 플러그인을 사용하여 생성할 수 있습니다. Lottie는 다양한 애니메이션 효과를 제공하며 간단하게 사용할 수 있습니다. Lottie는 CocoaPods를 통해 쉽게 프로젝트에 추가할 수 있습니다.

```swift
// Podfile
platform :ios, '11.0'
use_frameworks!

target 'YourAppName' do
  pod 'lottie-ios'
end
```

## 2. Animation with UIView

UIView 클래스는 Swift에서 애니메이션을 구현하는 데 가장 기본적인 방법입니다. UIView의 애니메이션 사용을 위해 `animate(withDuration:animations:)` 메서드를 사용할 수 있습니다. 이 메서드는 지정된 시간 동안 뷰의 속성을 애니메이션화합니다.

```swift
UIView.animate(withDuration: 0.3, animations: {
    // 애니메이션 효과를 주고자 하는 뷰의 속성 변경
    self.myView.alpha = 0
    self.myView.transform = CGAffineTransform(scaleX: 0.5, y: 0.5)
}) { (completed) in
    // 애니메이션이 완료되면 실행되는 코드
    self.myView.removeFromSuperview()
}
```

## 3. Core Animation

Core Animation은 iOS 애플리케이션의 애니메이션을 조작하기 위한 고수준 프레임워크입니다. Core Animation은 Layer 객체를 사용하여 애니메이션을 적용합니다. CALayer 클래스의 애니메이션 메서드와 프로퍼티를 사용하여 애니메이션을 지정할 수 있습니다.

```swift
let animation = CABasicAnimation(keyPath: "position")
animation.fromValue = NSValue(cgPoint: CGPoint(x: 0, y: 0))
animation.toValue = NSValue(cgPoint: CGPoint(x: 100, y: 100))
animation.duration = 1.0
animation.repeatCount = .infinity
myLayer.add(animation, forKey: "position")
```

## 4. UIKit Dynamics

UIKit Dynamics는 물리 엔진을 사용하여 View의 동작을 시뮬레이션하는 기능을 제공합니다. 애니메이션에 마찰, 탄성, 중력 등의 물리적인 특성을 추가할 수 있습니다. UIDynamicAnimator와 UIDynamicBehavior 클래스를 사용하여 UIKit Dynamics를 구현할 수 있습니다.

```swift
let animator = UIDynamicAnimator(referenceView: self.view)
let gravityBehavior = UIGravityBehavior(items: [myView])
animator.addBehavior(gravityBehavior)
```

이 외에도 Swift에서 애니메이션 효과를 구현하는 다양한 방법이 있습니다. NVActivityIndicatorView 외에도 Lottie, UIView 애니메이션, Core Animation, UIKit Dynamics를 사용하여 다양한 애니메이션 효과를 적용할 수 있습니다. 프로젝트의 요구 사항과 개발자의 취향에 따라 적합한 방법을 선택할 수 있습니다.

참고 링크:
- [Lottie - Airbnb's animation library](https://github.com/airbnb/lottie-ios)
- [UIView.animate(withDuration:animations:)](https://developer.apple.com/documentation/uikit/uiview/1622460-animate)
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html)
- [UIKit Dynamics](https://developer.apple.com/documentation/uikit/animation_and_haptics/uikit_dynamics)