---
layout: post
title: "[swift] NVActivityIndicatorView의 크기 및 위치 조정 방법"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift로 개발된 로딩 인디케이터 라이브러리입니다. 이 라이브러리를 사용하여 앱에서 로딩 표시기를 구현할 수 있습니다. NVActivityIndicatorView는 다양한 스타일의 로딩 인디케이터를 제공하며, 이러한 인디케이터의 크기와 위치를 조정할 수 있습니다.

## 크기 조정하기
NVActivityIndicatorView의 크기는 `size` 속성을 사용하여 조정할 수 있습니다. `size` 속성은 `NVActivityIndicatorView.DEFAULT_BLOCKER_SIZE`로 초기화되며, `CGFloat` 형식의 너비와 높이 값을 가집니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 60, height: 60), type: .ballSpinFadeLoader, color: .white, padding: nil)
indicatorView.size = CGSize(width: 80, height: 80)
```

위 예시에서는 `indicatorView`를 초기화하고, 크기를 60x60에서 80x80으로 조정하고 있습니다.

## 위치 조정하기
NVActivityIndicatorView의 위치는 일반적인 `UIView` 객체와 마찬가지로 `frame` 속성을 사용하여 조정할 수 있습니다. `frame` 속성은 `CGRect` 형식의 x, y, width, height 값을 가집니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 100, y: 100, width: 80, height: 80), type: .ballSpinFadeLoader, color: .white, padding: nil)
```

위 예시에서는 `indicatorView`를 x좌표 100, y좌표 100으로 이동시키고 있습니다.

## 요약
NVActivityIndicatorView의 크기와 위치를 조정하기 위해 `size` 속성과 `frame` 속성을 사용할 수 있습니다. `size` 속성을 이용하여 인디케이터의 크기를 조절하고, `frame` 속성을 이용하여 인디케이터의 위치를 조절할 수 있습니다.

더 많은 정보를 원하신다면, 아래의 공식 GitHub 저장소를 참고하시기 바랍니다.

- [NVActivityIndicatorView GitHub 저장소](https://github.com/ninjaprox/NVActivityIndicatorView)