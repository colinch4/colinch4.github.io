---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 커스텀 로딩 인디케이터 생성하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

홈페이지나 모바일 애플리케이션에서 로딩 인디케이터를 사용하면 사용자들에게 작업이 진행 중임을 시각적으로 전달할 수 있습니다. NVActivityIndicatorView는 Swift로 작성된 로딩 인디케이터 라이브러리로, 다양한 스타일과 커스텀 옵션을 제공합니다.

이번 튜토리얼에서는 NVActivityIndicatorView를 사용하여 커스텀 로딩 인디케이터를 생성하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView 설치하기

CocoaPods을 사용하여 NVActivityIndicatorView를 설치할 수 있습니다. 프로젝트의 Podfile에 다음 라인을 추가한 후 `pod install` 명령어를 실행합니다.

```ruby
pod 'NVActivityIndicatorView'
```

## NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. 인디케이터를 생성합니다. 다음과 같이 인디케이터의 크기와 색상, 스타일을 지정할 수 있습니다.

```swift
let indicatorView = NVActivityIndicatorView(
    frame: CGRect(x: 0, y: 0, width: 50, height: 50),
    type: .ballScaleRippleMultiple,
    color: .red,
    padding: nil
)
```

3. 인디케이터를 특정 뷰에 추가합니다.

```swift
view.addSubview(indicatorView)
indicatorView.center = view.center
```

4. 인디케이터를 시작하고 중지할 때에는 다음과 같이 사용합니다.

```swift
indicatorView.startAnimating()

// 작업이 완료된 후 인디케이터를 중지하기 위해 호출합니다.
indicatorView.stopAnimating()
```

커스텀 로딩 인디케이터를 생성하는 방법에 대해 간단히 알아보았습니다. NVActivityIndicatorView는 다양한 스타일과 옵션을 제공하여 프로젝트에 적합한 인디케이터를 만들 수 있습니다.

NVActivityIndicatorView에 대한 자세한 내용은 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.