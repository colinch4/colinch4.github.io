---
layout: post
title: "[swift] NVActivityIndicatorView를 이용한 사용자 친화적인 로딩 인디케이터 구현하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

앱 또는 웹 페이지에서 데이터를 가져오거나 처리할 때, 사용자에게 로딩 중임을 알려주는 인디케이터는 매우 중요합니다. NVActivityIndicatorView는 Swift에서 쉽게 사용할 수 있는 로딩 인디케이터 라이브러리입니다. 이번 블로그 포스트에서는 NVActivityIndicatorView를 사용하여 사용자 친화적인 로딩 인디케이터를 구현하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 중임을 나타내기 위해 사용되는 인디케이터입니다. 다양한 스타일과 색상으로 제공되며, 간단한 코드로 어떤 뷰나 컴포넌트에도 추가할 수 있습니다. 다양한 로딩 상태에 따라 사용자에게 시각적인 피드백을 제공하여 더 나은 사용자 경험을 제공할 수 있습니다.

## NVActivityIndicatorView 설치하기

NVActivityIndicatorView를 사용하기 위해서는 먼저 Cocoapods를 이용하여 프로젝트에 라이브러리를 추가해야 합니다. Podfile에 다음과 같이 추가합니다:

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## NVActivityIndicatorView 사용하기

1. 먼저, 사용하고자 하는 뷰 컨트롤러에서 NVActivityIndicatorView를 import합니다:

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 생성하기 위해 다음과 같은 코드를 사용할 수 있습니다:

```swift
let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
let activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .ballSpinFadeLoader, color: .black)
```

3. 생성된 NVActivityIndicatorView를 원하는 뷰에 추가합니다:

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
activityIndicatorView.startAnimating()
```

4. 로딩이 완료되면 NVActivityIndicatorView를 숨기기 위해서 다음 코드를 사용합니다:

```swift
activityIndicatorView.stopAnimating()
activityIndicatorView.removeFromSuperview()
```

## NVActivityIndicatorView 스타일 및 색상 변경하기

NVActivityIndicatorView는 다양한 스타일과 색상을 제공합니다. 스타일은 `NVActivityIndicatorType`에서 확인할 수 있으며, 색상은 UIColor를 사용하여 지정할 수 있습니다. 다음은 예시 코드입니다:

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: frame, type: .lineScalePulseOut, color: UIColor(red: 0.5, green: 0.8, blue: 0.2, alpha: 1.0))
```

## NVActivityIndicatorView 참고 자료

- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView): 라이브러리의 공식 GitHub 저장소입니다. 다양한 사용 예시와 문서를 참고할 수 있습니다.

이제 NVActivityIndicatorView를 사용하여 사용자 친화적인 로딩 인디케이터를 쉽게 구현할 수 있습니다. 추가적인 옵션 및 스타일 변경은 공식 문서를 참고하여 사용해보세요.