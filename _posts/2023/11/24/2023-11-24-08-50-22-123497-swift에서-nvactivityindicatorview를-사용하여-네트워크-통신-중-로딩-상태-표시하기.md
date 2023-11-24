---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 네트워크 통신 중 로딩 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

Swift에서 네트워크 통신을 할 때 사용자에게 로딩 상태를 시각적으로 보여주는 것은 매우 중요합니다. 이를 위해 NVActivityIndicatorView 라이브러리를 사용할 수 있습니다. NVActivityIndicatorView는 다양한 스타일의 로딩 인디케이터를 제공하여 사용자에게 직관적이고 멋진 로딩 애니메이션을 보여줄 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해 Cocoapods를 이용해서 라이브러리를 설치해야 합니다. 

1. `Podfile`에 다음과 같은 코드를 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

2. 터미널에서 다음 명령어를 실행하여 Cocoapods를 설치합니다:

```bash
pod install
```

## NVActivityIndicatorView 사용하기

1. 먼저, NVActivityIndicatorView를 import합니다:

```swift
import NVActivityIndicatorView
```

2. 다음으로, 로딩 상태를 보여줄 view를 생성합니다. 보통은 UIViewController의 view에 추가하는 것이 일반적입니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: nil)
self.view.addSubview(activityIndicatorView)
```

3. 네트워크 요청을 시작하기 전에 로딩 상태를 표시하기 위해 `startAnimating()` 메소드를 호출합니다:

```swift
activityIndicatorView.startAnimating()
```

4. 네트워크 요청이 완료되었다면, 로딩 상태를 제거하기 위해 `stopAnimating()` 메소드를 호출합니다:

```swift
activityIndicatorView.stopAnimating()
```

## NVActivityIndicatorView 스타일 변경하기

NVActivityIndicatorView는 다양한 스타일을 제공합니다. `type` 파라미터를 통해 스타일을 변경할 수 있습니다. 

예를 들어, 다음과 같은 스타일을 사용할 수 있습니다:

- `ballSpinFadeLoader`: 원형 로딩 인디케이터
- `ballPulse`: 파동 모양의 로딩 인디케이터
- `lineScale`: 선이 변하는 로딩 인디케이터

```swift
NVActivityIndicatorType.ballSpinFadeLoader
NVActivityIndicatorType.ballPulse
NVActivityIndicatorType.lineScale
```

`color` 파라미터를 통해 로딩 인디케이터의 색상을 변경할 수 있습니다. 원하는 컬러로 변경하여 직접 지정할 수 있습니다.

## 결론

NVActivityIndicatorView는 Swift에서 네트워크 통신 중 로딩 상태를 표시하는 간편하고 멋진 방법입니다. 위에서 설명한 방법을 따라 자신만의 로딩 애니메이션을 만들어보세요. 더 자세한 내용은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 확인해보세요.