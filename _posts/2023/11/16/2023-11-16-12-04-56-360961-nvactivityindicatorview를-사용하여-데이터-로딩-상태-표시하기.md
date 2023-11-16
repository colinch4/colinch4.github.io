---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 데이터 로딩 상태 표시하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱에서 데이터를 로딩하는 동안 사용자에게 로딩 상태를 시각적으로 표시하는 것은 좋은 사용자 경험을 제공하는데 도움이 됩니다. NVActivityIndicatorView는 iOS에서 데이터 로딩 중에 사용자에게 로딩 상태를 표시하는 데 도움이 되는 라이브러리입니다. 이번 블로그 포스트에서는 NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 표시하는 방법을 살펴보겠습니다.

### NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS에서 사용자에게 로딩 상태를 시각적으로 표시하기 위한 애니메이션 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 애니메이션을 제공하며, 간단한 코드로 쉽게 사용할 수 있습니다.

### NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 이용하여 라이브러리를 설치해야 합니다. Podfile에 다음과 같은 내용을 추가하고, 터미널에서 `pod install` 명령을 실행하세요.

```
pod 'NVActivityIndicatorView'
```

### NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 초기화하고 원하는 스타일과 크기를 설정합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)
```

3. 원하는 위치에 NVActivityIndicatorView를 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
activityIndicatorView.startAnimating()
```

4. 데이터 로딩이 완료되면 NVActivityIndicatorView를 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

### 추가적인 옵션 및 사용법

- NVActivityIndicatorView를 커스터마이징하여 원하는 스타일과 색상을 지정할 수 있습니다. `type` 및 `color` 파라미터를 변경하여 다양한 스타일과 색상을 사용해보세요.
- NVActivityIndicatorView의 크기와 위치를 조정할 수 있습니다. frame을 설정하여 크기와 위치를 조절할 수 있습니다.
- NVActivityIndicatorView가 다른 View 위에 표시되도록 하려면 `view.bringSubviewToFront(activityIndicatorView)`를 사용하세요.

이제 NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 표시하는 방법을 알게 되었습니다. 이를 활용하여 앱의 사용자 경험을 향상시켜보세요.

### 참고 자료

- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)