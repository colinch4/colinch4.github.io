---
layout: post
title: "[swift] 색상과 크기를 변경할 수 있는 NVActivityIndicatorView"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

오늘은 `NVActivityIndicatorView`를 사용하여 색상과 크기를 변경할 수 있는 방법을 알아보겠습니다. `NVActivityIndicatorView`는 Swift를 위한 라이브러리로, 로딩 인디케이터를 구현할 수 있습니다. 기본 값은 회색 작은 원으로 표시되지만, 우리는 이를 원하는 색상과 크기로 변경해볼 것입니다.

## NVActivityIndicatorView 소개

`NVActivityIndicatorView`는 쉽게 사용할 수 있고 커스터마이징 가능한 로딩 인디케이터입니다. 예를 들어, 네트워크 요청이나 로딩 중에 앱에서 인디케이터를 표시할 때 유용합니다.

## 설치

`NVActivityIndicatorView`를 사용하려면, 먼저 다음과 같이 CocoaPods을 사용하여 프로젝트에 라이브러리를 설치해야 합니다:

```
pod 'NVActivityIndicatorView'
```

설치가 완료되었다면, `.xcworkspace` 파일을 열어서 사용할 준비가 된 것입니다.

## 사용 방법

`NVActivityIndicatorView`를 사용하기 위해 먼저, 인디케이터를 표시할 뷰 컨트롤러에 다음과 같이 `import`문을 추가해야 합니다:

```swift
import NVActivityIndicatorView
```

그 후, `NVActivityIndicatorView` 객체를 생성하고 원하는 옵션을 설정합니다. 원하는 크기를 설정하기 위해 `type` 속성을 사용할 수 있습니다. 예를 들어, `.ballScaleRipple` 또는 `.lineSpinFadeLoader` 등을 설정할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleRipple)
```

만약, 색상을 변경하고 싶다면, 다음과 같이 `color` 속성을 사용하여 설정할 수 있습니다.

```swift
activityIndicatorView.color = UIColor.red
```

또한, 애니메이션 속도를 조절하려면, `animationDuration` 속성을 사용할 수 있습니다.

```swift
activityIndicatorView.animationDuration = 1.0
```

인디케이터를 표시하려면, 다음과 같이 뷰에 추가하고 시작하면 됩니다:

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

인디케이터를 중지하려면, 다음과 같이 하면 됩니다:

```swift
activityIndicatorView.stopAnimating()
```

## 마치며

이번에는 `NVActivityIndicatorView`를 사용하여 색상과 크기를 변경할 수 있는 방법에 대해 알아보았습니다. 이 라이브러리를 사용하면 간단한 로딩 인디케이터를 쉽게 구현할 수 있으며, 원하는 스타일, 색상과 크기로 변경할 수도 있습니다. 라이브러리의 홈페이지를 참조하여 더 많은 커스터마이징 옵션을 알아보세요.

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)