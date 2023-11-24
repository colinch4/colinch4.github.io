---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 데이터 로딩 및 상태 표시 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

## 소개

iOS 앱 개발에서 데이터 로딩 및 상태 표시는 매우 중요한 요소입니다. 사용자에게 어떤 작업이 진행 중인지 알려주고, 사용자 경험을 향상시키는 역할을 합니다. 이를 위해 NVActivityIndicatorView는 매우 유용한 라이브러리입니다. NVActivityIndicatorView는 다양한 스타일의 로딩 애니메이션을 제공하며, 간편하게 사용할 수 있습니다.

## 설치

NVActivityIndicatorView를 사용하기 위해서는 먼저 프로젝트에 라이브러리를 설치해야 합니다. Cocoapods를 사용하는 경우, Podfile에 다음과 같이 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

설치를 완료한 후, 프로젝트를 업데이트합니다.

## 사용 방법

1. 먼저, NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 데이터 로딩이 필요한 뷰 컨트롤러에 NVActivityIndicatorView 프로퍼티를 추가합니다.

```swift
var activityIndicator: NVActivityIndicatorView!
```

3. viewDidLoad() 메서드에서 NVActivityIndicatorView를 초기화하고, 뷰에 추가합니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()

    // NVActivityIndicatorView 초기화
    activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballScale, color: .blue, padding: nil)

    // 뷰에 추가
    view.addSubview(activityIndicator)
}
```

4. 데이터 로딩이 시작되는 시점에서 NVActivityIndicatorView를 애니메이션을 시작합니다.

```swift
activityIndicator.startAnimating()
```

5. 데이터 로딩이 완료되면 NVActivityIndicatorView를 애니메이션을 종료합니다.

```swift
activityIndicator.stopAnimating()
```

## 애니메이션 스타일

NVActivityIndicatorView는 다양한 스타일의 애니메이션을 제공합니다. `type` 파라미터를 통해 스타일을 지정할 수 있으며, 다음과 같은 스타일이 있습니다.

- ballPulse
- ballClipRotate
- ballClipRotatePulse
- ballClipRotateMultiple
- ballRotate
- squareSpin
- cubeTransition
- lineScale
- lineScaleParty
- ballScaleMultiple

```swift
activityIndicator = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballPulse, color: .blue, padding: nil)
```

## 결론

NVActivityIndicatorView는 데이터 로딩 및 상태 표시를 위한 강력하고 유연한 라이브러리입니다. 다양한 스타일의 애니메이션과 간단한 사용법으로 빠르게 앱에 적용할 수 있습니다. 사용자 경험을 향상시키기 위해, NVActivityIndicatorView를 활용해보세요.

## 참고 문서

- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 문서](https://github.com/ninjaprox/NVActivityIndicatorView/blob/master/README.md)