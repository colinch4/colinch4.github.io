---
layout: post
title: "[swift] NVActivityIndicatorView와 함께 사용할 수 있는 레이아웃 옵션 소개"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 iOS 개발자들이 좋아하는 로딩 인디케이터 라이브러리입니다. 이 라이브러리는 다양한 스타일의 로딩 인디케이터를 제공하며, 사용하기도 매우 간편합니다. 

하지만, NVActivityIndicatorView의 기본적인 레이아웃 옵션도 사용자에게 유연성을 제공합니다. 이번에는 몇 가지 주요한 레이아웃 옵션들에 대해서 소개해보겠습니다.

## 원형 인디케이터의 크기 조절

NVActivityIndicatorView는 디폴트로 원형 로딩 인디케이터를 제공합니다. 이때, 원형 인디케이터의 크기를 조절할 수 있습니다. 크기 조절을 위해서는 `size` 속성을 사용합니다.

```swift
let indicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .ballScaleMultiple, color: .red, padding: nil)
indicatorView.size = CGSize(width: 100, height: 100)
view.addSubview(indicatorView)
```
위의 예시에서는 원형 인디케이터의 크기를 `CGSize(width: 100, height: 100)`로 설정하였습니다.

## 인디케이터의 위치 설정

로딩 인디케이터의 위치를 설정하는 것도 가능합니다. `contentInset` 프로퍼티를 사용하여 인디케이터의 위치를 지정할 수 있습니다.

```swift
indicatorView.contentInset = UIEdgeInsets(top: 100, left: 0, bottom: 0, right: 0)
```
위의 예시에서는 인디케이터를 상단으로 100포인트 이동시켰습니다.

## 인디케이터의 패딩 조절

NVActivityIndicatorView는 각각의 로딩 스타일에 따라 간격이 다를 수 있습니다. 이때, `padding` 속성을 사용하여 인디케이터의 패딩을 조절할 수 있습니다.

```swift
indicatorView.padding = 20
```
위의 예시에서는 인디케이터와 경계 사이의 간격을 20포인트로 설정하였습니다.

## 마무리

이렇게 몇 가지 레이아웃 옵션을 이용해서 NVActivityIndicatorView를 사용하면, 원하는 로딩 인디케이터를 만들 수 있습니다. 이러한 유연한 레이아웃 옵션들을 이용하여 앱에 멋진 로딩 화면을 구현해보세요.

더 많은 옵션에 대해서는 [NVActivityIndicatorView 공식 문서](https://github.com/ninjaprox/NVActivityIndicatorView)를 참고해주세요.