---
layout: post
title: "[swift] NVActivityIndicatorView의 사용 예시와 코드 설명"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

![NVActivityIndicatorView Logo](https://raw.githubusercontent.com/ninjaprox/NVActivityIndicatorView/master/NVActivityIndicatorView/Resources/logo.png)

NVActivityIndicatorView는 Swift로 작성된 로딩 인디케이터 라이브러리로, 앱이 비동기 작업을 수행할 때 사용자에게 진행 상태를 시각적으로 보여줄 수 있습니다. 이 블로그 포스트에서는 NVActivityIndicatorView를 사용하는 예시와 코드를 설명하겠습니다.

## 설치

먼저, Cocoapods를 사용하여 NVActivityIndicatorView를 프로젝트에 설치해야 합니다. Podfile에 다음과 같은 라인을 추가합니다:

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 Cocoapods를 업데이트하고 라이브러리를 설치합니다:

```bash
$ pod install
```

## 사용 예시

1. `NVActivityIndicatorView`를 import 해줍니다:

```swift
import NVActivityIndicatorView
```

2. `NVActivityIndicatorView` 인스턴스를 생성합니다. 인스턴스를 생성할 때, 프레임 크기와 스타일을 설정할 수 있습니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50),
                                                  type: .circleStrokeSpin)
```

3. 필요한 곳에서 `NVActivityIndicatorView`를 추가합니다. 보통은 네트워크 요청이나 데이터 로딩 중에 표시됩니다:

```swift
self.view.addSubview(activityIndicatorView)
activityIndicatorView.startAnimating()
```

4. 작업이 완료되면 `NVActivityIndicatorView`를 제거합니다:

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## 스타일 설정

`NVActivityIndicatorView`는 다양한 스타일을 제공합니다. 다음은 몇 가지 예시입니다:

- `ballPulse`
- `ballClipRotate`
- `ballRotate`
- `lineScale`
- `cubeTransition`

스타일을 변경하려면 `type` 매개변수를 통해 지정합니다. 예를 들어, 다음과 같이 스타일을 변경할 수 있습니다:

```swift
activityIndicatorView.type = .ballClipRotate
```

더 많은 스타일과 옵션에 대한 설명은 [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하세요.

## 요약

이제 NVActivityIndicatorView를 사용하여 앱에서 로딩 인디케이터를 표시하는 방법에 대해 알아보았습니다. 이 예제를 사용하여 앱의 비동기 작업을 더 사용자 친화적으로 만들어보세요. NVActivityIndicatorView의 다양한 기능을 사용하여 인디케이터의 스타일을 변경할 수도 있습니다. 라이브러리에 대한 자세한 정보는 NVActivityIndicatorView의 GitHub 페이지를 참조하세요.

## 참고 자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)