---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 함께 사용할 수 있는 애니메이션 효과 대체 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Swift에서 애니메이션 효과를 주기 위해 NVActivityIndicatorView를 자주 사용하는 개발자들이 많습니다. 그러나 NVActivityIndicatorView는 일부 화면에서 비교적 속도가 느려지고 성능 이슈가 발생할 수도 있습니다. 이 경우, NVActivityIndicatorView의 대체 방법을 찾아보는 것이 좋습니다.

## CATransition 사용하기

CATransition은 Core Animation의 일부분으로, 화면 전환과 같은 애니메이션 효과를 제공하는데 사용됩니다. NVActivityIndicatorView와 비교해보면 CATransition은 일반적으로 더 가볍고 빠른 성능을 보여줍니다.

```swift
let transition = CATransition()
transition.duration = 1.0
transition.timingFunction = CAMediaTimingFunction(name: .easeInEaseOut)
transition.type = .fade

view.layer.add(transition, forKey: nil)
```

위의 코드에서는 1초 동안의 페이드 애니메이션을 적용한 예시입니다. 필요한 애니메이션 효과에 따라 duration, timingFunction, type 등을 적절히 변경하여 사용할 수 있습니다.

## Lottie 사용하기

Lottie는 Airbnb에서 개발한 애니메이션 라이브러리로, JSON 형식의 애니메이션 파일을 재생할 수 있습니다. NVActivityIndicatorView와는 달리 Lottie는 더 다양한 애니메이션 효과를 제공하며, 애니메이션의 성능 역시 우수합니다.

Lottie를 사용하기 위해 다음과 같이 설치하고 애니메이션 파일을 추가해야 합니다.

```swift
import Lottie

let animationView = AnimationView(name: "animation")
animationView.loopMode = .loop
animationView.play()

view.addSubview(animationView)
```

위의 코드에서는 "animation"이라는 이름의 애니메이션 파일을 반복 재생하는 예시입니다. 필요한 애니메이션 파일을 준비하여 애니메이션 효과를 적용할 수 있습니다.

## 결론

NVActivityIndicatorView를 대체할 수 있는 다양한 애니메이션 효과를 위해 CATransition과 Lottie를 활용할 수 있습니다. 각각의 특성과 성능을 고려하여 프로젝트에 적합한 방법을 선택해보세요.