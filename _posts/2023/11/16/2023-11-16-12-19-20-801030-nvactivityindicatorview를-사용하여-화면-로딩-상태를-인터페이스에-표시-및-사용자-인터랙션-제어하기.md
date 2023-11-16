---
layout: post
title: "[swift] NVActivityIndicatorView를 사용하여 화면 로딩 상태를 인터페이스에 표시 및 사용자 인터랙션 제어하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

![NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView/raw/master/Gif/1.gif)

## 소개

NVActivityIndicatorView는 Swift로 작성된 오픈 소스 라이브러리로, 화면 로딩 상태를 표시하고 사용자 인터랙션을 제어하는 데 도움을 줍니다. 이 라이브러리는 다양한 로딩 효과와 커스터마이징 옵션을 제공하여 애플리케이션에 적합한 로딩 화면을 만들 수 있습니다.

## 설치

CocoaPods를 사용하여 NVActivityIndicatorView를 설치합니다. Podfile에 다음의 코드를 추가합니다.

```swift
pod 'NVActivityIndicatorView'
```

그런 다음 터미널에서 다음 명령을 실행합니다.

```bash
pod install
```

## 사용 방법

1. NVActivityIndicatorView를 import 합니다.

```swift
import NVActivityIndicatorView
```

2. 로딩 상태를 표시할 뷰를 생성합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballPulse, color: .red, padding: nil)
```

- frame: 로딩 표시 뷰의 위치와 크기를 지정합니다.
- type: 로딩 효과의 종류를 선택합니다. 다양한 로딩 효과 중 하나를 선택할 수 있습니다.
- color: 로딩 효과의 색상을 설정합니다.
- padding: 로딩 효과 주위에 추가적인 여백을 설정할 수 있습니다. 필요한 경우 nil로 설정할 수 있습니다.

3. 로딩 상태를 인터페이스에 표시합니다.

```swift
activityIndicatorView.startAnimating()
```

4. 로딩 상태를 중지하고 숨깁니다.

```swift
activityIndicatorView.stopAnimating()
```

## 커스터마이징

NVActivityIndicatorView는 다양한 커스터마이징 옵션을 제공합니다. 로딩 효과, 색상, 크기 등을 변경하여 애플리케이션에 맞는 로딩 화면을 만들 수 있습니다.

- 로딩 효과 변경하기

```swift
activityIndicatorView.type = .ballRotateChase
```

- 색상 변경하기

```swift
activityIndicatorView.color = .blue
```

- 크기 변경하기

```swift
activityIndicatorView.frame = CGRect(x: 0, y: 0, width: 70, height: 70)
```

위와 같이 커스터마이징 옵션을 사용하여 로딩 화면을 변경할 수 있습니다.

## 참고자료

- [NVActivityIndicatorView GitHub 페이지](https://github.com/ninjaprox/NVActivityIndicatorView)
- [NVActivityIndicatorView 문서](http://cocoadocs.org/docsets/NVActivityIndicatorView)