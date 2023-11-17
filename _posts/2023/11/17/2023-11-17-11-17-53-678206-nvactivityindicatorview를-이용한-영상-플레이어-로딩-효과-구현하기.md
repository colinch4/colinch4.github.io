---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 영상 플레이어 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 `NVActivityIndicatorView` 라이브러리를 사용하여 영상 플레이어 로딩 효과를 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

`NVActivityIndicatorView`는 iOS용 적용 가능한 로딩 인디케이터 라이브러리입니다. 이 라이브러리는 간편하게 커스텀할 수 있으며, 다양한 스타일과 색상의 로딩 인디케이터를 제공합니다.

![NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView/raw/master/Media/demo.gif)

## 설치 방법

`NVActivityIndicatorView`는 CocoaPods을 통해 설치할 수 있습니다. `Podfile`에 다음의 내용을 추가하여 설치합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그 후, 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 프로젝트에 추가합니다.

## 사용 방법

1. `NVActivityIndicatorView`를 import합니다.

```swift
import NVActivityIndicatorView
```

2. `NVActivityIndicatorView` 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .white, padding: .none)
```

3. `NVActivityIndicatorView`를 화면에 추가합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
activityIndicatorView.startAnimating()
```

4. 로딩이 끝난 후, `NVActivityIndicatorView`를 제거합니다.

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 커스터마이징

`NVActivityIndicatorView`는 다양한 속성을 가지고 있어 커스터마이징이 가능합니다. 

아래는 일부 속성의 예시입니다.

- `type`: 로딩 인디케이터의 스타일을 설정합니다. `.ballSpinFadeLoader`, `.lineScalePulseOut`, `.ballClipRotateMultiple` 등이 있습니다.
- `color`: 로딩 인디케이터의 색상을 설정합니다.
- `padding`: 로딩 인디케이터와 테두리 간의 간격을 설정합니다.

더 많은 커스터마이징 옵션은 [공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)를 확인하세요.

## 결론

이번 포스트에서는 `NVActivityIndicatorView` 라이브러리를 사용하여 영상 플레이어 로딩 효과를 구현하는 방법에 대해 알아보았습니다. `NVActivityIndicatorView`는 편리하게 사용할 수 있고, 다양한 스타일의 로딩 인디케이터를 제공하여 사용자에게 멋진 로딩 효과를 제공할 수 있습니다.