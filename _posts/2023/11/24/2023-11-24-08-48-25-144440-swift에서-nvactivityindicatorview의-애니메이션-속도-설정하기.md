---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView의 애니메이션 속도 설정하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Swift에서는 NVActivityIndicatorView를 사용하여 로딩 인디케이터를 쉽게 구현할 수 있습니다. NVActivityIndicatorView는 다양한 애니메이션 스타일과 옵션을 제공하며 사용자 정의할 수도 있습니다.

이번 포스트에서는 NVActivityIndicatorView의 애니메이션 속도를 설정하는 방법에 대해 알아보겠습니다.

### NVActivityIndicatorView 속도 설정하기

NVActivityIndicatorView의 애니메이션 속도는 duration 속성을 통해 설정할 수 있습니다. duration은 애니메이션의 한 싸이클이 완료되는 데에 걸리는 시간을 나타내는 속성입니다. 

예를 들어, 애니메이션 한 싸이클을 완료하는 데에 1초가 걸릴 경우 다음과 같이 duration을 설정할 수 있습니다:

```swift
let activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .circleStrokeSpin, color: .red)
activityIndicator.duration = 1.0
```

만약 애니메이션 속도를 더 느리게 하려면 duration을 늘리고, 더 빠르게 하려면 duration을 줄일 수 있습니다.

### NVActivityIndicatorView 속도 조절하기

NVActivityIndicatorView의 기본 속도는 duration 값을 통해 설정되지만, 다른 속도 조절 옵션도 제공됩니다.

NVActivityIndicatorView 내부에서는 CADisplayLink를 사용하여 애니메이션을 업데이트하고 화면을 다시 그립니다. 따라서, CADisplayLink의 frameInterval 속성을 조절하여 애니메이션 속도를 조절할 수 있습니다. frameInterval 값이 작을수록 애니메이션 속도가 빨라지고, 클수록 느려집니다.

다음은 frameInterval을 설정하여 애니메이션 속도를 조절하는 예시입니다:

```swift
let activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .circleStrokeSpin, color: .red)
activityIndicator.frameInterval = 2
```

위의 예시는 애니메이션 속도를 절반으로 줄입니다. 따라서, frameInterval 값을 적절히 조절하여 원하는 애니메이션 속도를 설정할 수 있습니다.

### 마무리

이번 포스트에서는 Swift에서 NVActivityIndicatorView의 애니메이션 속도를 설정하는 방법에 대해 알아보았습니다. NVActivityIndicatorView를 사용하여 로딩 인디케이터를 손쉽게 구현하고 애니메이션 속도를 조절하는 방법을 익히셨으면 좋겠습니다.

### 참고 자료

- [NVActivityIndicatorView Github Repository](https://github.com/ninjaprox/NVActivityIndicatorView)