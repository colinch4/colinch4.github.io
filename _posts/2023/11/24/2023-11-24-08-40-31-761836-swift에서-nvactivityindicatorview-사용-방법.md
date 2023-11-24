---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 사용 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 NVActivityIndicatorView를 사용하는 방법에 대해 알아보겠습니다. 

NVActivityIndicatorView는 Swift에서 쉽게 커스텀 가능한 로딩 인디케이터를 생성할 수 있는 라이브러리입니다. 

## NVActivityIndicatorView 설치

먼저, NVActivityIndicatorView를 설치해야 합니다. Cocoapods를 사용한다면, Podfile에 다음과 같이 작성합니다.

```swift
pod 'NVActivityIndicatorView'
```

그리고 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## NVActivityIndicatorView 사용하기

1. Import 문을 추가하여 NVActivityIndicatorView를 정의하는 클래스에 접근할 수 있도록 합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView 인스턴스 생성하기

로딩 인디케이터를 사용할 뷰 컨트롤러에서 NVActivityIndicatorView 인스턴스를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballSpinFadeLoader, color: .gray, padding: nil)
```

위에서 `frame`은 로딩 인디케이터의 위치와 크기를 지정하고, `type`은 로딩 인디케이터의 스타일을 선택합니다. 다양한 스타일을 적용해볼 수 있는데, 공식 문서를 참고하시기 바랍니다. `color`는 로딩 인디케이터의 색상을 지정하며, `padding`은 로딩 인디케이터 사이의 패딩 값입니다.

3. 로딩 인디케이터 업데이트하기

로딩 인디케이터를 업데이트하기 위해 다음과 같은 메서드를 사용합니다.

```swift
activityIndicatorView.startAnimating()
```

로딩 인디케이터를 시작합니다.

```swift
activityIndicatorView.stopAnimating()
```

로딩 인디케이터를 정지합니다.

4. 로딩 인디케이터 표시하기

로딩 인디케이터를 원하는 위치에 표시하기 위해서는 다음과 같은 작업을 수행합니다.

```swift
view.addSubview(activityIndicatorView)
activityIndicatorView.center = view.center
```

위의 코드에서는 로딩 인디케이터를 현재 뷰의 중앙에 위치하도록 지정합니다.

이제 NVActivityIndicatorView를 사용하여 로딩 인디케이터를 손쉽게 구현할 수 있습니다.

더 자세한 사용 방법 및 설정 옵션에 대해서는 [NVActivityIndicatorView 공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고하시기 바랍니다.