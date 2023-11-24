---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 애니메이션 내비게이션 효과 적용하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱에 동적이고 멋진 시각적 효과를 추가하기 위해 NVActivityIndicatorView를 사용할 수 있습니다. 이 블로그 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션 내비게이션 효과를 적용하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 오픈 소스 애니메이션 인디케이터 라이브러리입니다. 다양한 스타일과 크기의 로딩 인디케이터를 제공하며, 간단한 코드로 쉽게 사용할 수 있습니다. 이 라이브러리는 Core Animation을 기반으로하여 높은 성능의 애니메이션을 제공합니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 위해 먼저 CocoaPods를 설치해야 합니다. `Podfile`에 다음과 같은 라인을 추가한 후 터미널에서 `pod install` 명령어를 실행합니다.

```ruby
pod 'NVActivityIndicatorView'
```

이제 프로젝트에서 NVActivityIndicatorView를 사용할 준비가 되었습니다.

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 초기화합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: 0)
```

- `frame`: 애니메이션 뷰의 프레임입니다.
- `type`: 애니메이션 스타일을 설정합니다. 여기서는 `.ballSpinFadeLoader`를 사용하였습니다.
- `color`: 애니메이션 색상을 설정합니다. 여기서는 파란색을 사용하였습니다.
- `padding`: 애니메이션 뷰와 테두리 사이의 여백을 설정합니다. 여기서는 0으로 설정하였습니다.

3. 뷰에 NVActivityIndicatorView를 추가합니다. 예를 들어, 내비게이션 바에 애니메이션 뷰를 추가하고, 로딩 중임을 나타내기 위해 시작할 수 있습니다.

```swift
navigationItem.titleView = activityIndicatorView
activityIndicatorView.startAnimating()
```

4. 애니메이션을 중지하고 제거하기 위해 다음 코드를 사용할 수 있습니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

NVActivityIndicatorView를 사용하여 애니메이션 내비게이션 효과를 적용하는 방법에 대해 알아보았습니다. 이 라이브러리는 다양한 스타일의 애니메이션을 제공하기 때문에 원하는 디자인과 아름다운 애니메이션을 구현할 수 있습니다. 자세한 내용은 [NVActivityIndicatorView GitHub repository](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조해주세요.