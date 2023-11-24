---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView로 조건부 로딩 인디케이터 표시하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

로딩 인디케이터는 사용자에게 어떤 작업이 진행 중임을 알리는데 사용됩니다. 이번에는 Swift에서 NVActivityIndicatorView를 사용하여 조건부로 로딩 인디케이터를 표시하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 사용 가능한 로딩 인디케이터 라이브러리입니다. NVActivityIndicatorView는 다양한 스타일과 설정 옵션을 제공하며, 간편하게 사용할 수 있습니다.

## 설치

먼저, NVActivityIndicatorView를 설치하기 위해 CocoaPods를 사용합니다. Podfile에 다음과 같은 내용을 추가합니다.

```ruby
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 다운로드 받습니다.

## 사용 방법

1. 먼저, 로딩 인디케이터를 표시할 뷰를 생성합니다.

```swift
import NVActivityIndicatorView

let loadingView = UIView(frame: CGRect(x: 0, y: 0, width: 80, height: 80))

let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40))
activityIndicatorView.center = CGPoint(x: loadingView.frame.width / 2, y: loadingView.frame.height / 2)
activityIndicatorView.type = .ballRotateChase
activityIndicatorView.color = .gray

loadingView.addSubview(activityIndicatorView)
```

2. 조건에 따라 로딩 인디케이터를 표시하거나 숨깁니다.

```swift
// 로딩 인디케이터를 숨기는 함수
func hideLoadingIndicator() {
    activityIndicatorView.stopAnimating()
    loadingView.removeFromSuperview()
}

// 로딩 인디케이터를 표시하는 함수
func showLoadingIndicator() {
    view.addSubview(loadingView)
    activityIndicatorView.startAnimating()
}

// 조건에 따라 로딩 인디케이터를 표시하거나 숨깁니다.
if condition {
    showLoadingIndicator()
} else {
    hideLoadingIndicator()
}
```

위의 코드에서 `if condition` 문장은 조건에 따라 로딩 인디케이터를 표시할지 숨길지를 결정합니다. `showLoadingIndicator()` 함수는 로딩 인디케이터를 표시하고, `hideLoadingIndicator()` 함수는 로딩 인디케이터를 숨깁니다.

## 사용자 정의 설정

NVActivityIndicatorView는 다양한 스타일과 설정 옵션을 제공합니다. `activityIndicatorView`의 프로퍼티를 변경하여 사용자 정의 설정을 할 수 있습니다. 아래는 몇 가지 사용 예시입니다.

- `activityIndicatorView.type`: 로딩 인디케이터의 스타일을 설정합니다. 예를 들어, `.ballRotateChase`는 공이 회전하는 스타일입니다.
- `activityIndicatorView.color`: 로딩 인디케이터의 색상을 설정합니다.

자세한 내용은 NVActivityIndicatorView의 공식 문서를 참고하시기 바랍니다.

## 참고 자료

- [NVActivityIndicatorView GitHub Repository](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView/blob/master/README.md)

이제 Swift에서 NVActivityIndicatorView를 사용하여 조건부 로딩 인디케이터를 표시하는 방법에 대해 알아보았습니다. 이를 통해 사용자에게 로딩 상태를 시각적으로 알려주어 좋은 사용자 경험을 제공할 수 있습니다.