---
layout: post
title: "[swift] NVActivityIndicatorView의 다양한 애니메이션 스타일"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

**NVActivityIndicatorView**는 Swift에서 제공하는 애니메이션 라이브러리로, 로딩 인디케이터나 프로그레스 바를 쉽게 추가할 수 있습니다. 이 라이브러리는 다양한 애니메이션 스타일을 제공하므로, 애플리케이션의 디자인에 맞게 선택할 수 있습니다.

## 1. 설치

NVActivityIndicatorView는 CocoaPods를 통해 쉽게 설치할 수 있습니다. 아래의 명령을 터미널에 입력하여 Podfile에 라이브러리를 추가하고, 설치하세요.

```ruby
pod 'NVActivityIndicatorView'
```

## 2. 사용법

NVActivityIndicatorView를 사용하기 위해서는 몇 가지 단계를 거쳐야 합니다.

**1.** 원하는 뷰 컨트롤러에서 `import NVActivityIndicatorView`를 추가하여 라이브러리를 불러옵니다.

**2.** 애니메이션을 추가할 컨테이너 뷰를 생성합니다. 예를 들어, `containerView`라는 이름의 UIView를 생성합니다.

```swift
let containerView = UIView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))
containerView.center = view.center
view.addSubview(containerView)
```

**3.** NVActivityIndicatorView를 생성하고, 컨테이너 뷰에 추가합니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballRotateChase, color: .red, padding: nil)
containerView.addSubview(activityIndicatorView)
```

**4.** NVActivityIndicatorView의 애니메이션을 시작하고 정지하는 메서드를 호출합니다.

```swift
activityIndicatorView.startAnimating()
// 애니메이션 시작

activityIndicatorView.stopAnimating()
// 애니메이션 정지
```

## 3. 다양한 애니메이션 스타일

NVActivityIndicatorView는 다양한 애니메이션 스타일을 제공합니다. 몇 가지 대표적인 예시를 소개하겠습니다.

### - ballPulse

![ballPulse](https://github.com/ninjaprox/NVActivityIndicatorView/raw/master/Resources/ ballPulse.gif)

```
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .ballPulse, color: .red, padding: nil)
```

### - lineScale

![lineScale](https://github.com/ninjaprox/NVActivityIndicatorView/raw/master/Resources/ lineScale.gif)

```
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .lineScale, color: .red, padding: nil)
```

### - pacman

![pacman](https://github.com/ninjaprox/NVActivityIndicatorView/raw/master/Resources/ pacman.gif)

```
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 40, height: 40), type: .pacman, color: .red, padding: nil)
```

## 4. 참고

- NVActivityIndicatorView 공식 GitHub 저장소: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)