---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 속도와 외관 커스터마이징하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift로 작성된 오픈 소스 라이브러리로, 다양한 종류의 인디케이터 애니메이션을 제공합니다. 이 라이브러리를 사용하면 애플리케이션에서 로딩 중이나 작업 중임을 알리기 위해 간단하고 멋진 인디케이터를 만들 수 있습니다.

이 글에서는 NVActivityIndicatorView를 사용하여 애니메이션의 속도와 외관을 커스터마이징하는 방법에 대해 알아보겠습니다.

## 설치

먼저, 프로젝트에 NVActivityIndicatorView를 설치해야 합니다. 이를 위해서는 CocoaPods를 사용하는 것이 가장 편리합니다. `Podfile`에 다음과 같이 라이브러리를 추가해주세요.

```
pod 'NVActivityIndicatorView'
```

그런 다음, 터미널에서 `pod install` 명령을 실행하여 라이브러리를 다운로드하고 프로젝트에 연결해주세요.

## 사용법

1. NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. 인디케이터를 생성하고 뷰에 추가합니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
indicatorView.center = self.view.center
self.view.addSubview(indicatorView)
indicatorView.startAnimating()
```

3. 인디케이터의 속도를 조정합니다.

NVActivityIndicatorView의 애니메이션 속도는 속성으로 제어할 수 있습니다. 기본값은 `1.0`이며, 이 값을 더 작은 값으로 설정하면 애니메이션이 느려지고, 더 큰 값으로 설정하면 애니메이션이 빨라집니다.

```swift
indicatorView.animationDuration = 0.5
```

4. 인디케이터의 외관을 커스터마이징합니다.

NVActivityIndicatorView는 다양한 외관 설정을 지원합니다. 다음은 일부 예시입니다.

- `color`: 인디케이터의 색상을 변경합니다.
- `type`: 인디케이터의 형태를 변경합니다.
- `padding`: 인디케이터의 패딩 값을 변경합니다.

```swift
indicatorView.color = UIColor.red
indicatorView.type = .circleStrokeSpin
indicatorView.padding = 10
```

5. 인디케이터를 중지시킵니다.

```swift
indicatorView.stopAnimating()
```

## 결론

NVActivityIndicatorView를 사용하면 손쉽게 로딩 인디케이터를 구현할 수 있습니다. 애니메이션의 속도와 외관을 커스터마이징하여 원하는 대로 디자인할 수 있습니다.

더 많은 옵션과 사용자 정의 설정에 대해서는 NVActivityIndicatorView의 공식 문서를 참조하시기 바랍니다. 

- NVActivityIndicatorView GitHub: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)