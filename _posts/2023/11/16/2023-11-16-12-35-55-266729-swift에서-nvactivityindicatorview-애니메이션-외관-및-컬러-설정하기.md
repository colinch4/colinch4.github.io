---
layout: post
title: "[swift] Swift에서 NVActivityIndicatorView 애니메이션 외관 및 컬러 설정하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

NVActivityIndicatorView는 Swift에서 사용할 수 있는 간단하고 유연한 애니메이션 라이브러리입니다. 이 라이브러리는 다양한 애니메이션 스타일을 제공하며 개발자가 커스터마이징할 수 있는 다양한 설정 옵션을 제공합니다. 이번 블로그 포스트에서는 NVActivityIndicatorView 애니메이션의 외관과 컬러를 설정하는 방법에 대해 알아보겠습니다.

## 외관 설정하기

NVActivityIndicatorView 인스턴스를 생성한 후에는 다양한 설정 옵션을 사용하여 애니메이션의 외관을 변경할 수 있습니다. 몇 가지 중요한 설정 옵션을 살펴보겠습니다.

### 인디케이터 스타일 변경하기

NVActivityIndicatorView는 다양한 인디케이터 스타일을 제공합니다. 인디케이터 스타일을 변경하려면 `type` 속성을 사용하면됩니다. 예를 들어, 다음과 같이 사용할 수 있습니다.

```swift
let activityIndicatorView = NVActivityIndicatorView(frame: CGRect(x: 0, y: 0, width: 50, height: 50), type: .circleStrokeSpin, color: .red, padding: nil)
```

위의 예제에서는 `type`을 `.circleStrokeSpin`으로 설정하여 동그란 모양의 스피너를 만들었습니다. 다른 스타일을 사용하려면 해당 스타일 값을 사용하면 됩니다.

### 크기 조정하기

애니메이션의 크기를 조정하려면 `size` 속성을 사용합니다. 예를 들어, 다음과 같이 사용할 수 있습니다.

```swift
activityIndicatorView.size = CGSize(width: 80, height: 80)
```

위의 예제에서는 애니메이션의 너비와 높이를 80으로 설정합니다.

## 컬러 설정하기

NVActivityIndicatorView는 애니메이션 색상을 변경할 수 있는 다양한 설정 옵션을 제공합니다. 몇 가지 중요한 설정 옵션을 살펴보겠습니다.

### 색상 변경하기

NVActivityIndicatorView의 색상을 변경하려면 `color` 속성을 사용합니다. 예를 들어, 다음과 같이 사용할 수 있습니다.

```swift
activityIndicatorView.color = .blue
```

위의 예제에서는 애니메이션의 색상을 파란색으로 변경합니다.

## 결론

이렇게 NVActivityIndicatorView에서 애니메이션 외관과 컬러를 설정하는 방법을 알아보았습니다. NVActivityIndicatorView는 간단하고 유연한 라이브러리로, 다양한 설정 옵션을 통해 사용자 정의 가능한 애니메이션을 만들 수 있습니다. 자세한 사용법은 공식 문서를 참고하시기 바랍니다.

- NVActivityIndicatorView 공식 문서: [https://github.com/ninjaprox/NVActivityIndicatorView](https://github.com/ninjaprox/NVActivityIndicatorView)