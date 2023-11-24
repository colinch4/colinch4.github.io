---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView를 사용하여 데이터 로딩 상태 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

데이터 로딩 중에 사용자에게 시각적인 피드백을 제공하는 것은 앱의 사용자 경험을 향상시키는 중요한 기능입니다. NVActivityIndicatorView는 로딩 상태를 표시하기 위한 라이브러리로, Swift 프로젝트에서 쉽게 사용할 수 있습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView는 Cocoapods를 통해 설치할 수 있습니다. Cocoapods를 사용하는 방법은 다음과 같습니다.

1. 터미널을 열고 프로젝트의 루트 디렉토리로 이동합니다.
2. `pod init` 명령어를 실행하여 Podfile을 생성합니다.
3. Podfile을 수정하여 NVActivityIndicatorView를 추가합니다.

```ruby
target 'YourProject' do
  ...
  pod 'NVActivityIndicatorView'
  ...
end
```

4. `pod install` 명령어를 실행하여 NVActivityIndicatorView를 프로젝트에 설치합니다.

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용하기 위해서는 다음 단계를 따르세요.

1. 프로젝트에서 NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

3. 인스턴스의 색상과 스타일을 설정합니다. 색상은 UIColor 타입으로 지정할 수 있으며, 스타일은 NVActivityIndicatorType 열거형으로 지정할 수 있습니다.

```swift
activityIndicatorView.color = .blue
activityIndicatorView.type = .ballScaleRippleMultiple
```

4. 로딩 상태를 표시할 뷰에 인스턴스를 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.translatesAutoresizingMaskIntoConstraints = false
view.addConstraints([
    activityIndicatorView.centerXAnchor.constraint(equalTo: view.centerXAnchor),
    activityIndicatorView.centerYAnchor.constraint(equalTo: view.centerYAnchor)
])
```

5. 로딩 상태를 시작하려면 `startAnimating()` 메서드를 호출합니다.

```swift
activityIndicatorView.startAnimating()
```

6. 로딩이 완료되면 `stopAnimating()` 메서드를 호출하여 로딩 상태 표시를 중지합니다.

```swift
activityIndicatorView.stopAnimating()
```

## 요약

Swift에서 NVActivityIndicatorView를 사용하여 데이터 로딩 상태를 표시하는 방법을 알아봤습니다. NVActivityIndicatorView를 설치하고 사용하는 단계를 따라서 로딩 상태를 시각적으로 표시할 수 있습니다. NVActivityIndicatorView는 앱의 사용자 경험을 향상시키기 위한 유용한 도구입니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)