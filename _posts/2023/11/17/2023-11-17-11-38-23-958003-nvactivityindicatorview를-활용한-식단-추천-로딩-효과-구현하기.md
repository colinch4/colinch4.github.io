---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 식단 추천 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 개요
이번 튜토리얼에서는 NVActivityIndicatorView 라이브러리를 사용하여 식단 추천 앱의 로딩 효과를 구현하는 방법을 알아보겠습니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 로딩 인디케이터 뷰의 라이브러리입니다. 다양한 모양과 스타일로 로딩 효과를 추가할 수 있으며, 간편한 사용법으로 널리 알려져 있습니다.

## 설치 및 설정
1. CocoaPods을 사용하여 NVActivityIndicatorView를 프로젝트에 추가합니다. `Podfile`에 다음과 같이 라이브러리를 추가해주세요.

```swift
pod 'NVActivityIndicatorView'
```

2. 터미널에서 `pod install` 명령어를 입력하여 라이브러리를 설치합니다.

3. 설치가 완료되면, Xcode를 열고 프로젝트를 다시 빌드합니다.

## NVActivityIndicatorView 사용하기
1. 먼저, NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 인디케이터를 추가할 뷰를 만듭니다.

```swift
let loadingView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 100, height: 100), type: .ballSpinFadeLoader, color: .gray, padding: nil)
```

- `frame`: 로딩 인디케이터의 위치 및 크기를 정의합니다.
- `type`: 로딩 인디케이터의 모양을 선택합니다. `.ballSpinFadeLoader`는 공 모양의 스피닝 애니메이션입니다.
- `color`: 로딩 인디케이터의 색상을 지정합니다.
- `padding`: 로딩 인디케이터 내부와 경계 사이의 여백을 지정합니다. `nil`이면 기본값이 적용됩니다.

3. 로딩 인디케이터를 뷰에 추가합니다.

```swift
self.view.addSubview(loadingView)
loadingView.center = self.view.center
```

4. 로딩 인디케이터를 시작 및 중지하는 함수를 작성합니다.

```swift
func startLoading() {
    loadingView.startAnimating()
}

func stopLoading() {
    loadingView.stopAnimating()
}
```

5. 식단 추천 데이터를 로딩할 때, `startLoading()` 함수를 호출하여 로딩 인디케이터를 시작합니다. 데이터를 로딩한 후, `stopLoading()` 함수를 호출하여 로딩 인디케이터를 중지합니다.

## 마무리
이제 NVActivityIndicatorView를 사용하여 식단 추천 앱에 로딩 효과를 추가할 수 있습니다. 이 라이브러리를 사용하면 사용자에게 진행 중임을 시각적으로 알리면서 UX를 개선할 수 있습니다. NVActivityIndicatorView의 다양한 옵션과 스타일을 사용해 원하는 로딩 효과를 구현해보세요.

## 참고 자료
- NVActivityIndicatorView 공식 GitHub 저장소: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)