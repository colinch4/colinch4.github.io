---
layout: post
title: "[swift] Swift Core Animation에 easing 애니메이션 적용하기"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

Core Animation은 iOS 애플리케이션에서 애니메이션을 쉽게 생성하고 관리할 수 있는 라이브러리입니다. Core Animation의 힘과 유연성을 활용하여 easing 효과를 적용하여 애니메이션을 더 부드럽고 자연스럽게 만들 수 있습니다.

## easing 애니메이션 이란?

easing 애니메이션은 시작과 끝의 속도를 조절하여 애니메이션의 움직임을 보다 자연스럽게 만드는 기법입니다. 기본적인 easing 함수로는 Linear, Ease-in, Ease-out 등 다양한 종류가 있습니다. 이러한 easing 함수를 사용하여 Core Animation의 애니메이션에 부드러운 움직임을 적용할 수 있습니다.

## Core Animation의 easing 애니메이션 적용 예제

아래는 Core Animation을 사용하여 easing 애니메이션을 적용하는 예제 코드입니다.

```swift
import UIKit

func startAnimation() {
    let animation = CAKeyframeAnimation(keyPath: "position")
    animation.values = [
        NSValue(cgPoint: CGPoint(x: 0, y: 0)),
        NSValue(cgPoint: CGPoint(x: 200, y: 100)),
        NSValue(cgPoint: CGPoint(x: 300, y: 200)),
        NSValue(cgPoint: CGPoint(x: 400, y: 300))
    ]
    // easing 함수 설정
    let timingFunctions = [
        CAMediaTimingFunction(name: CAMediaTimingFunctionName.easeIn),
        CAMediaTimingFunction(name: CAMediaTimingFunctionName.easeOut),
        CAMediaTimingFunction(name: CAMediaTimingFunctionName.easeInEaseOut),
        CAMediaTimingFunction(name: CAMediaTimingFunctionName.default)
    ]
    animation.timingFunctions = timingFunctions

    let layer = CALayer()
    layer.frame = CGRect(x: 0, y: 0, width: 50, height: 50)
    layer.backgroundColor = UIColor.red.cgColor
    view.layer.addSublayer(layer)

    animation.duration = 2.0
    animation.repeatCount = Float.infinity
    layer.add(animation, forKey: "position")
}
```

위의 코드는 view의 layer에 easing 애니메이션을 적용하는 예제입니다. animation.values를 통해 애니메이션 움직임의 시작과 끝을 정의하고, animation.timingFunctions를 통해 easing 함수를 설정합니다. 마지막으로, layer에 애니메이션을 추가하여 실행합니다.

## 참고 문서

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html)