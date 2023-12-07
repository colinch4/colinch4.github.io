---
layout: post
title: "[swift] Swift와 UIInterpolatingMotionEffect를 이용한 애니메이션 효과 구현하기"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UIInterpolatingMotionEffect는 iOS 앱에서 모션 효과를 적용하기 위해 사용되는 클래스입니다. 이를 활용하면 기기의 움직임에 따라 뷰의 변화를 주어 동적인 애니메이션 효과를 구현할 수 있습니다.

## 시작하기 전에

이 예제는 Swift 프로그래밍 언어를 사용하여 iOS 앱에서 UIInterpolatingMotionEffect를 구현하는 방법을 보여줍니다. 따라서 Xcode와 iOS 앱 개발에 대한 기본 지식이 필요합니다. 이 예제에서는 iOS 13 이상의 버전을 대상으로 합니다.

## 예제 코드

```swift
import UIKit

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // UIInterpolatingMotionEffect를 생성하고 움직임을 감지할 속성을 설정합니다.
        let motionEffect = UIInterpolatingMotionEffect(keyPath: "center.x", type: .tiltAlongHorizontalAxis)
        
        // 움직임의 최대 효과 크기를 설정합니다. 값이 클수록 더 큰 움직임이 발생합니다.
        motionEffect.maximumRelativeValue = 50
        
        // 최소 효과 크기를 설정합니다. 값이 작을수록 더 작은 움직임에도 효과가 적용됩니다.
        motionEffect.minimumRelativeValue = -50
        
        // 애니메이션 효과를 적용할 뷰를 선택합니다.
        let viewToApplyEffect = self.view
        
        // 애니메이션 효과를 뷰에 설정합니다.
        viewToApplyEffect.addMotionEffect(motionEffect)
    }
}
```

위의 예제 코드는 UIViewController에 UIInterpolatingMotionEffect를 적용하는 방법을 보여줍니다. 움직임을 감지할 속성으로 "center.x"를 설정하였으며, 수평 축을 기준으로 효과를 적용합니다. 움직임의 최대 크기는 50이며, 최소 크기는 -50입니다.

`viewDidLoad()` 메서드에서 UIInterpolatingMotionEffect를 생성한 후, 해당 애니메이션 효과를 적용할 뷰에 추가합니다.

## 결과 확인하기

위의 예제 코드를 사용하여 iOS 앱을 실행시키면, 기기를 기울일 때 뷰가 움직이는 효과를 확인할 수 있습니다. 기기를 오른쪽으로 기울이면 뷰가 오른쪽으로 이동하고, 왼쪽으로 기울이면 뷰가 왼쪽으로 이동합니다.

## 결론

Swift 프로그래밍 언어와 UIInterpolatingMotionEffect 클래스를 사용하여 iOS 앱에서 동적인 애니메이션 효과를 구현하는 방법을 살펴보았습니다. 이를 응용하여 앱의 사용성을 향상시킬 수 있으며, UI 요소에 살아있는 느낌을 줄 수 있습니다. 자세한 내용은 Apple 공식 문서를 참조하시기 바랍니다.

## 참고 자료

- [UIInterpolatingMotionEffect - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiinterpolatingmotioneffect)
- [Creating a Parallax Effect - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/animations_and_transitions/using_motion_effects_to_create_parallax_effects)