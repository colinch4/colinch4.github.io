---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 함께 사용할 수 있는 커스텀 애니메이션 라이브러리 소개"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱 개발을 하다보면 로딩 화면이나 작업이 진행중임을 알리기 위해 애니메이션을 사용하는 경우가 많습니다. Swift에서도 다양한 애니메이션 라이브러리가 제공되고 있는데, 이 중에서 NVActivityIndicatorView를 소개해보려고 합니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 Swift에서 사용할 수 있는 커스텀 로딩 애니메이션 라이브러리입니다. 이 라이브러리를 사용하면 다양한 모양의 로딩 애니메이션을 쉽게 구현할 수 있습니다. NVActivityIndicatorView는 iOS, tvOS, watchOS 및 macOS 플랫폼에서 사용할 수 있으며, Swift와 Objective-C 모두에서 사용할 수 있습니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 위해서는 먼저 프로젝트에 해당 라이브러리를 추가해야 합니다. 가장 손쉬운 방법은 CocoaPods를 사용하는 것입니다. Podfile에 다음과 같이 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

만약 Cocoapods를 사용하지 않는다면, [GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)에서 직접 소스 파일을 다운로드 받아 프로젝트에 추가할 수도 있습니다.

## NVActivityIndicatorView 사용하기

NVActivityIndicatorView를 사용해 커스텀 애니메이션을 구현해보겠습니다. 우선, NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

다음으로, NVActivityIndicatorView를 초기화하고 특정 위치에 추가하는 코드를 작성합니다.

```swift
let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
let activityIndicatorView = NVActivityIndicatorView(frame: frame)
view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

이제 애니메이션을 시작하기 위해 `startAnimating()` 메서드를 호출합니다. 만약 애니메이션을 종료하고 싶다면 `stopAnimating()` 메서드를 호출하면 됩니다.

NVActivityIndicatorView는 다양한 프로퍼티와 메서드를 제공하여 애니메이션의 색상, 크기, 모양 등을 조정할 수 있습니다. 자세한 내용은 [공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView#usage)를 참조하시기 바랍니다.

## 마무리

이렇게 NVActivityIndicatorView를 사용하여 Swift 애플리케이션에 커스텀 애니메이션을 쉽게 추가할 수 있습니다. 라이브러리의 다양한 옵션을 통해 자신의 애니메이션을 만들어보세요.