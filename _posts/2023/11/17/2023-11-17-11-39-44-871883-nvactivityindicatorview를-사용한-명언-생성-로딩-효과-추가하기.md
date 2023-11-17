---
layout: post
title: "[swift] NVActivityIndicatorView를 사용한 명언 생성 로딩 효과 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

안녕하세요, 오늘은 Swift에서 NVActivityIndicatorView를 사용하여 명언 생성 로딩 효과를 추가하는 방법을 알려드리겠습니다. NVActivityIndicatorView는 iOS 앱에 로딩 표시기를 쉽게 추가할 수 있는 오픈소스 라이브러리입니다.

## NVActivityIndicatorView 설치하기

먼저, Cocoapods을 사용하여 NVActivityIndicatorView를 프로젝트에 설치해야 합니다. Podfile에 아래의 코드를 추가하세요:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 아래의 명령어를 실행하여 Cocoapod을 설치하세요:

```bash
pod install
```

## NVActivityIndicatorView 사용하기

1. NVActivityIndicatorView를 import합니다:

```swift
import NVActivityIndicatorView
```

2. 로딩 효과를 추가할 UIView를 생성합니다. 평소에 명언 생성 로딩 효과를 보여줄 뷰가 있다면, 그 뷰를 사용하시면 됩니다.

```swift
let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: 80, height: 80))
loadingView.center = view.center
view.addSubview(loadingView)
```

3. NVActivityIndicatorView 인스턴스를 생성합니다. 적절한 스타일과 색상을 선택하여 해당 뷰에 추가합니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballBeat, color: .systemBlue)
loadingView.addSubview(activityIndicatorView)
```

4. 로딩 효과를 시작하려면, `startAnimating()` 메서드를 호출합니다:

```swift
activityIndicatorView.startAnimating()
```

5. 로딩이 완료되면, `stopAnimating()` 메서드를 호출하여 로딩 효과를 중지합니다:

```swift
activityIndicatorView.stopAnimating()
```

## 추가적인 설정

NVActivityIndicatorView는 다양한 스타일과 색상을 제공합니다. 위 코드에서 `type:` 및 `color:` 파라미터를 적절히 변경하여 원하는 스타일과 색상을 선택할 수 있습니다. 또한 크기도 조정할 수 있으니, 필요에 맞게 알맞은 값을 사용하시면 됩니다.

## 결론

이제 NVActivityIndicatorView를 사용하여 명언 생성 로딩 효과를 쉽게 추가할 수 있게 되었습니다. 이렇게 로딩 효과를 적용하면 사용자가 명언이 생성되기를 기다릴 때, 앱이 작동 중임을 시각적으로 알려줄 수 있습니다.

참고 자료:
- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)