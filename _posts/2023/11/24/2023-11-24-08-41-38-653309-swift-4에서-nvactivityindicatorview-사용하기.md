---
layout: post
title: "[swift] Swift 4에서 NVActivityIndicatorView 사용하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift 4에서 NVActivityIndicatorView를 사용하는 방법에 대해 알아보겠습니다.

## NVActivityIndicatorView란?

NVActivityIndicatorView는 iOS 앱에서 로딩 인디케이터를 표시하기 위한 오픈 소스 라이브러리입니다. 이 라이브러리는 다양한 로딩 스타일과 색상을 제공하며, 간편한 세팅과 사용이 가능합니다.

## 설치

NVActivityIndicatorView를 설치하기 위해서는 우선 CocoaPods를 사용해야 합니다. Podfile에 다음과 같이 NVActivityIndicatorView를 추가합니다.

```
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 다음 명령어를 실행하여 팟을 설치합니다.

```
pod install
```

## 사용 방법

1. 필요한 파일에 import 구문을 추가합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 초기화합니다.

```swift
let frame = CGRect(x: 0, y: 0, width: 50, height: 50)
let activityIndicatorView = NVActivityIndicatorView(frame: frame)
```

3. 원하는 로딩 스타일과 색상을 설정합니다.

```swift
activityIndicatorView.type = .ballScaleRippleMultiple
activityIndicatorView.color = UIColor.red
```

4. 로딩 인디케이터를 표시하거나 숨깁니다.

```swift
activityIndicatorView.startAnimating()
activityIndicatorView.stopAnimating()
```

## 추가 설정

NVActivityIndicatorView를 추가로 설정할 수 있는 옵션들이 있습니다. 자세한 내용은 [공식 GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)를 참조하시기 바랍니다.

## 참고 자료

- [NVActivityIndicatorView GitHub 레포지토리](https://github.com/ninjaprox/NVActivityIndicatorView)
- [CocoaPods](https://cocoapods.org/)
- [Swift](https://swift.org/)

이제 Swift 4에서 NVActivityIndicatorView를 사용하는 방법에 대해 알아보았습니다. 간단하게 설치하고 설정하면 다양한 스타일과 색상의 로딩 인디케이터를 사용할 수 있습니다.