---
layout: post
title: "[swift] NVActivityIndicatorView를 활용한 지도 명소 검색 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 블로그 포스트에서는 NVActivityIndicatorView를 사용하여 지도에서 명소를 검색할 때 로딩 효과를 구현하는 방법을 알아보겠습니다.

## 1. NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 사용할 수 있는 로딩 인디케이터 라이브러리입니다. 이 라이브러리를 사용하면 간단하게 다양한 스타일과 색상의 로딩 효과를 구현할 수 있습니다.

## 2. NVActivityIndicatorView 설치하기

NVActivityIndicatorView 라이브러리를 설치하기 위해 먼저 CocoaPods를 사용해야 합니다. Podfile에 다음과 같이 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 3. NVActivityIndicatorView 사용하기

### 3.1 NVActivityIndicatorView 초기화

먼저, NVActivityIndicatorView를 초기화해야 합니다. 다음과 같은 코드를 사용하여 초기화합니다.

```swift
import NVActivityIndicatorView

let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballSpinFadeLoader, color: .gray, padding: nil)
```

### 3.2 NVActivityIndicatorView 추가 및 애니메이션 시작

다음으로, NVActivityIndicatorView를 뷰에 추가하고 애니메이션을 시작해야 합니다. 예를 들어, 검색 버튼을 눌렀을 때 로딩 효과를 보여주고 싶다면 다음과 같은 코드를 사용합니다.

```swift
searchButton.addTarget(self, action: #selector(searchButtonTapped), for: .touchUpInside)

@objc func searchButtonTapped() {
    view.addSubview(activityIndicatorView)
    activityIndicatorView.startAnimating()
    
    // 검색 로직 실행
    
    activityIndicatorView.stopAnimating()
    activityIndicatorView.removeFromSuperview()
}
```

### 3.3 NVActivityIndicatorView 스타일 및 색상 설정

NVActivityIndicatorView의 스타일과 색상은 `type`과 `color` 매개변수를 통해 설정할 수 있습니다. 다양한 스타일과 색상을 사용할 수 있으며, 자세한 내용은 NVActivityIndicatorView의 공식 문서를 참조하시기 바랍니다.

## 4. 마무리

이제 NVActivityIndicatorView를 사용하여 지도 명소 검색 로딩 효과를 구현하는 방법에 대해 알아보았습니다. NVActivityIndicatorView는 간단하게 사용할 수 있는 로딩 인디케이터 라이브러리로, 앱의 사용자 경험을 향상시킬 수 있습니다. 참고로, 이 포스트에서 사용한 예제 코드는 실제 앱에 맞게 수정해야 합니다.

- 참고: [NVActivityIndicatorView 공식 GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)