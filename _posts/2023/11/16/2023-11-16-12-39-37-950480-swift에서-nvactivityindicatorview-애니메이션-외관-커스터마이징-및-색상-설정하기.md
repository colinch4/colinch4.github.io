---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 외관 커스터마이징 및 색상 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 강력한 애니메이션 라이브러리입니다. 이 라이브러리를 사용하면 간단하게 다양한 유형의 로딩 애니메이션을 만들 수 있습니다. NVActivityIndicatorView는 외부 라이브러리로 사용되기 때문에 라이브러리를 설치하고 프로젝트에 추가해야 합니다.

## 1. NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 설치하기 위해 먼저 CocoaPods를 사용하여 프로젝트에 라이브러리를 추가합니다. Podfile에 다음과 같은 코드를 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 라이브러리를 설치합니다:

```bash
pod install
```

## 2. NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해 먼저 import 문을 추가합니다:

```swift
import NVActivityIndicatorView
```

다음으로 NVActivityIndicatorView의 인스턴스를 만들고 원하는 위치에 추가합니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .blue, padding: nil)
view.addSubview(activityIndicatorView)
```

위 코드에서 `type`은 애니메이션의 유형을 선택하는 열거형 값입니다. `color`는 애니메이션의 색상을 지정하는 속성입니다. `padding`은 애니메이션 뷰의 여백을 설정하는 속성입니다.

애니메이션을 시작하려면 다음과 같이 `startAnimating()` 메서드를 호출하면 됩니다:

```swift
activityIndicatorView.startAnimating()
```

애니메이션을 중지하려면 `stopAnimating()` 메서드를 호출합니다:

```swift
activityIndicatorView.stopAnimating()
```

## 3. NVActivityIndicatorView 외관 커스터마이징

NVActivityIndicatorView를 외관을 커스터마이징하기 위해서는 `color`, `padding`, `type` 등 다양한 속성을 조정할 수 있습니다. 다음은 몇 가지 예시입니다.

### 3.1. 색상 변경하기

```swift
activityIndicatorView.color = .red
```

### 3.2. 애니메이션 유형 변경하기

```swift
activityIndicatorView.type = .circleStrokeSpin
```

### 3.3. 패딩 설정하기

```swift
activityIndicatorView.padding = 20
```

## 4. 마무리

이제 Swift에서 NVActivityIndicatorView 애니메이션을 외관 커스터마이징하고 색상을 설정하는 방법에 대해 알아보았습니다. 이 라이브러리를 사용하면 로딩 애니메이션을 효과적으로 추가할 수 있습니다. 자세한 내용은 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.