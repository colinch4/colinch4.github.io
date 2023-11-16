---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 시작 및 중지하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 애플리케이션에서 사용할 수 있는 매우 유용한 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 애니메이션을 제공하며, 애플리케이션의 사용자 인터페이스를 개선하는 데 도움이 됩니다. 이번 블로그 포스트에서는 Swift에서 NVActivityIndicatorView 애니메이션을 시작하고 중지하는 방법을 알아보겠습니다.

## NVActivityIndicatorView 설치

먼저 NVActivityIndicatorView를 설치해야 합니다. CocoaPods를 통해 설치하는 것이 가장 간단한 방법입니다. Podfile에 다음과 같이 NVActivityIndicatorView를 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령을 실행하여 라이브러리를 설치합니다:

```shell
pod install
```

## NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 import 합니다:

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 초기화합니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 60, height: 60), type: .ballScaleRippleMultiple, color: .blue, padding: nil)
```

- `frame`: 애니메이션 뷰의 프레임을 설정합니다.
- `type`: 사용할 애니메이션 스타일을 선택합니다.
- `color`: 애니메이션의 색상을 설정합니다.
- `padding`: 애니메이션 뷰의 여백을 설정하며, 기본값은 `nil`입니다.

3. 애니메이션을 표시하고 싶은 뷰에 NVActivityIndicatorView를 추가합니다:

```swift
view.addSubview(activityIndicatorView)
```

4. 애니메이션을 시작하거나 중지할 때에는 다음 메서드를 호출합니다:

```swift
activityIndicatorView.startAnimating()  // 애니메이션 시작
activityIndicatorView.stopAnimating()   // 애니메이션 중지
```

5. 필요한 경우 NVActivityIndicatorView의 옵션을 변경하고자 한다면, 다음과 같은 메서드를 사용합니다:

```swift
activityIndicatorView.color = .red   // 애니메이션 색상 변경
activityIndicatorView.type = .ballPulse   // 애니메이션 스타일 변경
```

위와 같은 방법으로 Swift에서 NVActivityIndicatorView 애니메이션을 시작하고 중지하는 방법을 알아보았습니다. 이를 적용하여 로딩 인디케이터를 만들고 사용자 인터페이스를 개선할 수 있습니다.

더 자세한 사항은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하십시오.