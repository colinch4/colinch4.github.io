---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 속도 조절 및 애니메이션 효과 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 애플리케이션에서 사용할 수 있는 애니메이션 라이브러리입니다. 이 라이브러리로 간단하게 로딩 인디케이터나 다른 사용자 정의 애니메이션을 추가할 수 있습니다.

이번 블로그에서는 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션 속도를 조절하고 다양한 애니메이션 효과를 설정하는 방법을 알아보겠습니다.

## NVActivityIndicatorView 설치하기

먼저, Cocoapods를 사용하여 NVActivityIndicatorView를 설치해야 합니다. `Podfile`에 다음과 같이 추가하고 `pod install` 명령을 실행합니다.

```
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하려면 다음의 단계를 따라야 합니다.

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

3. 애니메이션 효과를 설정합니다. NVActivityIndicatorView는 다양한 애니메이션 스타일을 제공합니다.

```swift
activityIndicatorView.type = .ballSpinFadeLoader
```

4. 애니메이션 속도를 조절하려면 `animationDuration` 속성을 사용하여 지정할 수 있습니다. 기본값은 1입니다.

```swift
activityIndicatorView.animationDuration = 0.5
```

5. NVActivityIndicatorView를 화면에 추가하고 시작합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

6. 애니메이션을 중지하려면 `stopAnimating()` 메서드를 호출합니다.

```swift
activityIndicatorView.stopAnimating()
```

## 애니메이션 효과 설정하기

NVActivityIndicatorView는 다양한 애니메이션 효과를 제공합니다. `type` 속성을 사용하여 다른 애니메이션 스타일을 설정할 수 있습니다. 다음은 일부 애니메이션 스타일의 예입니다.

- .ballSpinFadeLoader: 공이 회전하면서 사라지는 효과
- .lineSpinFadeLoader: 선이 회전하면서 사라지는 효과
- .circleStrokeSpin: 원이 회전하면서 선이 그려지는 효과

```swift
activityIndicatorView.type = .lineSpinFadeLoader
```

## 마치며

이제 Swift에서 NVActivityIndicatorView 애니메이션의 속도를 조절하고 원하는 효과를 설정하는 방법을 알아봤습니다. NVActivityIndicatorView는 간단히 적용할 수 있는 애니메이션 라이브러리이므로 프로젝트에 사용해보시면 좋을 것입니다.

더 많은 NVActivityIndicatorView의 애니메이션 스타일과 옵션에 대한 정보는 [NVActivityIndicatorView 공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.