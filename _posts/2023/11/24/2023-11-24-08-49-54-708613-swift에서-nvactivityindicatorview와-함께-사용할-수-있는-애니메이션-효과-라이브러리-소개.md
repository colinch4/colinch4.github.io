---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView와 함께 사용할 수 있는 애니메이션 효과 라이브러리 소개"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

이번에는 Swift 언어로 앱의 로딩화면이나 다양한 작업 진행 상황을 나타내는 애니메이션 효과를 구현하는데 도움을 주는 NVActivityIndicatorView 라이브러리에 대해 알아보겠습니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 iOS 애플리케이션에서 사용할 수 있는 간단하고 가볍게 사용할 수 있는 애니메이션 효과 라이브러리입니다. 이 라이브러리는 다양한 종류의 로딩 스피너(styling spinner)를 제공하며, 색상과 크기를 커스터마이징 할 수 있습니다.

## 사용법

### 1. 라이브러리 설치
NVActivityIndicatorView를 사용하기 위해서는 먼저 Cocoapods를 이용하여 프로젝트에 라이브러리를 설치해야 합니다. Podfile에 다음과 같이 추가해줍니다.

```swift
pod 'NVActivityIndicatorView'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

### 2. NVActivityIndicatorView 추가하기
NVActivityIndicatorView를 사용할 ViewController에서 해당 라이브러리를 import 해줍니다.

```swift
import NVActivityIndicatorView
```

그리고 애니메이션 효과를 추가할 UIView를 생성합니다.

```swift
let animationView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
```

### 3. 애니메이션 효과 설정하기

애니메이션 효과를 설정하기 위해 NVActivityIndicatorView 클래스의 다양한 메소드를 사용할 수 있습니다. 몇 가지 예시를 살펴보겠습니다.

#### 1) 로딩 스피너 스타일 설정하기

```swift
animationView.type = .ballBeat
```

다양한 로딩 스피너 스타일을 사용할 수 있으며, `type` 속성을 이용하여 설정할 수 있습니다. 

#### 2) 애니메이션 색상 설정하기

```swift
animationView.color = UIColor.red
```

`color` 속성을 이용하여 애니메이션의 색상을 설정할 수 있습니다.

#### 3) 애니메이션 크기 설정하기

```swift
animationView.frame = CGRect(x: 0, y: 0, width: 100, height: 100)
```

`frame` 속성을 이용하여 애니메이션의 크기를 설정할 수 있습니다.

### 4. 애니메이션 시작 및 중지하기

```swift
animationView.startAnimating() // 애니메이션 시작
animationView.stopAnimating() // 애니메이션 중지
```

위의 코드를 사용하여 애니메이션을 시작하고, 중지할 수 있습니다.

## 마무리
Swift에서 NVActivityIndicatorView 라이브러리를 사용하면 간단하게 다양한 애니메이션 효과를 구현할 수 있습니다. 이 라이브러리의 다양한 설정 옵션을 통해 앱의 디자인에 맞게 로딩 스피너를 커스터마이징할 수 있습니다. 참고로 라이브러리의 자세한 사용법은 [공식 GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)에서 확인할 수 있습니다.

위에서 설명한 내용을 참고하여 프로젝트에서 NVActivityIndicatorView를 사용해보세요. 앱의 사용자 경험을 향상시킬 수 있는 멋진 애니메이션 효과를 구현할 수 있을 것입니다.