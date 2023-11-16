---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 크기와 모양 선택하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션의 크기와 모양을 선택하는 방법에 대해 알아보겠습니다. NVActivityIndicatorView는 iOS 앱에서 로딩 표시기를 만들기 위해 사용되는 라이브러리입니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift로 작성된 iOS와 tvOS를 위한 로딩 표시기입니다. 이 라이브러리는 다양한 모양과 크기의 로딩 표시기를 지원하여 앱의 디자인에 맞게 선택할 수 있습니다.

## 설치

먼저, NVActivityIndicatorView를 사용하기 위해 프로젝트에 의존성을 추가해야합니다. CocoaPods를 사용하고 있다면, Podfile에 다음과 같이 작성하고 pod install을 실행하십시오.

```
pod 'NVActivityIndicatorView'
```

CocoaPods를 사용하지 않는다면, 수동으로 프로젝트에 NVActivityIndicatorView를 추가할 수 있습니다. GitHub 저장소에서 최신 버전의 프로젝트를 다운로드한 다음, 프로젝트에 추가해주세요.

## 애니메이션 크기 선택하기

NVActivityIndicatorView는 다양한 크기를 지원합니다. 따라서 원하는 크기로 애니메이션을 조정할 수 있습니다. 이를 위해서는 NVActivityIndicatorView의 `size` 속성을 사용하면 됩니다.

다음은 NVActivityIndicatorView의 크기를 `large`로 설정하는 예시입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballScaleRippleMultiple, color: .red, padding: nil)
activityIndicatorView.size = .large
```

애니메이션의 크기를 조정하는 것은 앱의 디자인 요구에 따라 달라질 수 있습니다. 따라서 원하는 크기를 설정하여 앱에 적합한 로딩 표시기를 만들 수 있습니다.

## 애니메이션 모양 선택하기

NVActivityIndicatorView는 다양한 애니메이션 모양을 지원합니다. 로딩 표시기의 디자인을 변경하기 위해서는 NVActivityIndicatorView의 `type` 속성을 사용해야 합니다.

다음은 NVActivityIndicatorView의 모양을 `ballScaleRippleMultiple`로 설정하는 예시입니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballScaleRippleMultiple, color: .red, padding: nil)
```

NVActivityIndicatorView의 `type` 속성에는 다양한 모양이 있으며, 앱의 디자인에 가장 적합한 모양을 선택할 수 있습니다. 또한, 애니메이션 표시기의 색상과 여백도 선택할 수 있습니다.

## 결론

이 글에서는 Swift에서 NVActivityIndicatorView를 사용하여 애니메이션의 크기와 모양을 선택하는 방법에 대해 알아보았습니다. 이제 원하는 크기와 모양으로 로딩 표시기를 만들어 앱에 적용할 수 있을 것입니다. NVActivityIndicatorView의 다양한 옵션들을 사용하여 앱의 로딩 표시기를 더욱 멋지게 꾸밀 수도 있습니다.

더 자세한 정보는 [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.