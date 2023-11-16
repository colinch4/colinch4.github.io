---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 시간을 시각적으로 표현하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

앱이나 웹사이트에서 데이터를 로딩할 때 사용자에게 직관적으로 로딩 중임을 알려주는 시각적인 표현이 필요할 수 있습니다. 이를 위해 NVActivityIndicatorView를 사용하여 간단하고 멋진 로딩 인디케이터를 만들 수 있습니다. NVActivityIndicatorView는 Swift로 개발된 오픈 소스 라이브러리로, 화면 로딩을 시각적으로 표현하기 위한 다양한 스타일의 인디케이터를 제공합니다.

## NVActivityIndicatorView 설치

NVActivityIndicatorView를 사용하기 위해 먼저 Cocoapods를 사용하여 프로젝트에 라이브러리를 설치해야 합니다. 프로젝트 디렉토리에서 Podfile을 열고 다음 라인을 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그런 다음 터미널에서 프로젝트 디렉토리로 이동하여 다음 명령을 입력합니다.

```bash
pod install
```

Cocoapods를 사용하여 NVActivityIndicatorView를 설치합니다.

## NVActivityIndicatorView 사용

NVActivityIndicatorView를 사용하려면 다음 단계를 따르십시오.

1. NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .red, padding: nil)
```

`frame`은 인디케이터의 크기와 위치를 지정하는 데 사용됩니다. `type`은 인디케이터의 스타일을 지정합니다. `color`는 인디케이터의 색상을 지정합니다. `padding`은 인디케이터의 내부 여백을 지정하는 데 사용됩니다. 각각의 값을 필요에 따라 조정하십시오.

3. NVActivityIndicatorView를 화면에 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
activityIndicatorView.startAnimating()
```

`addSubview()` 메서드를 사용하여 `activityIndicatorView`를 view에 추가하고, `center` 프로퍼티를 사용하여 화면 중앙에 배치합니다. `startAnimating()` 메서드를 호출하여 인디케이터를 시작합니다.

4. 로딩이 완료되면 NVActivityIndicatorView를 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

`stopAnimating()` 메서드를 호출하여 인디케이터를 중지하고, `removeFromSuperview()` 메서드를 사용하여 view에서 제거합니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)

위의 단계를 따라 NVActivityIndicatorView를 사용하여 화면 로딩 시간을 시각적으로 표현할 수 있습니다. 다양한 스타일의 인디케이터를 사용하여 사용자에게 직관적인 로딩 화면을 제공하십시오. NVActivityIndicatorView의 다양한 옵션과 스타일을 사용하여 앱 또는 웹사이트의 사용자 경험을 향상시킬 수 있습니다.