---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView로 로그인 화면 로딩 효과 구현하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

로그인 화면이나 데이터를 로딩하는 동안에는 사용자에게 로딩 중임을 알리는 시각적인 피드백을 보여줄 수 있습니다. 이를 위해 NVActivityIndicatorView 라이브러리를 사용하여 로딩 화면 효과를 구현할 수 있습니다.

## NVActivityIndicatorView란?
NVActivityIndicatorView는 Swift에서 로딩 화면 효과를 생성하기 위한 오픈 소스 라이브러리입니다. 이 라이브러리는 간단하고 매끄러운 애니메이션 효과를 제공하며, 로딩 화면을 구현하는 데 사용할 수 있습니다.

## 설치하기
CocoaPods를 사용하여 NVActivityIndicatorView를 설치할 수 있습니다. Podfile에 다음과 같이 라이브러리를 추가하고, 터미널에서 `pod install` 명령을 실행하면 됩니다.

```ruby
pod 'NVActivityIndicatorView'
```

## 사용 방법
1. 프로젝트에서 NVActivityIndicatorView를 import합니다.

```swift
import NVActivityIndicatorView
```

2. NVActivityIndicatorView를 로딩 화면을 표시할 뷰에 추가합니다.

```swift
// 로딩 화면을 표시할 뷰
let containerView = UIView(frame: CGRect(x: 0, y: 0, width: 100, height: 100))
containerView.center = view.center
view.addSubview(containerView)

// NVActivityIndicatorView 인스턴스 생성
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50))
activityIndicatorView.center = containerView.center
containerView.addSubview(activityIndicatorView)

// 로딩 화면 컬러 설정
activityIndicatorView.color = .white

// 로딩 화면 시작
activityIndicatorView.startAnimating()
```

3. 로딩이 완료된 경우 NVActivityIndicatorView를 제거합니다.

```swift
// 로딩 화면 중단
activityIndicatorView.stopAnimating()

// 로딩 화면을 표시하는 뷰 제거
containerView.removeFromSuperview()
```

## 정리
Swift에서 NVActivityIndicatorView를 사용하여 로그인 화면에 로딩 효과를 구현하는 방법에 대해 알아보았습니다. 이러한 시각적인 피드백을 통해 사용자에게 로딩 중임을 알리면서 UI를 향상시킬 수 있습니다. NVActivityIndicatorView는 매우 유용한 라이브러리이며, 다양한 로딩 화면 디자인을 지원합니다. 자신의 프로젝트에 맞게 사용해보세요!

## 참고 자료
- [NVActivityIndicatorView - GitHub](https://github.com/ninjaprox/NVActivityIndicatorView)