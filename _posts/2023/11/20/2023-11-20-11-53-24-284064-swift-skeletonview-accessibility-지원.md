---
layout: post
title: "[swift] Swift SkeletonView Accessibility 지원"
description: " "
date: 2023-11-20
tags: [swift]
comments: true
share: true
---

## 소개
Swift SkeletonView는 사용자에게 로딩 중임을 시각적으로 보여주는 라이브러리입니다. 하지만 기본적으로는 접근성(Accessibility)을 제공하지 않습니다. 이번 글에서는 Swift SkeletonView에 접근성을 추가하는 방법에 대해 알아보겠습니다.

## 접근성 추가 방법
Swift SkeletonView에 접근성을 추가하기 위해서는 몇 가지 작업이 필요합니다.

### 1. SkeletonView에 대한 접근성 특성 지정
SkeletonView에 대한 접근성 특성을 지정하여 스크린 리더가 해당 요소에 대한 정보를 명확하게 전달할 수 있도록 해야합니다. 접근성 특성은 `accessibilityLabel`, `accessibilityHint`, `accessibilityTraits`를 이용하여 설정할 수 있습니다. 예를 들면 다음과 같습니다:

```swift
yourView.isAccessibilityElement = true
yourView.accessibilityLabel = "로딩 중입니다."
yourView.accessibilityHint = "로딩이 완료될 때까지 잠시 기다려주세요."
yourView.accessibilityTraits = .staticText
```

### 2. 텍스트 또는 이미지 리소스 대체
Swift SkeletonView는 기본적으로 텍스트 또는 이미지 리소스를 대신하여 스크린 리더가 읽어줄 수 있는 텍스트로 제공해야 합니다. 이는 접근성을 향상시키기 위해 필요한 작업입니다. 예를 들면 다음과 같습니다:

```swift
let skeletonLabel = UILabel()
skeletonLabel.text = "로딩 중" // 로딩 중을 나타내는 텍스트로 리소스를 대체
skeletonLabel.accessibilityLabel = "로딩 중입니다."
```

### 3. 로딩 상태 업데이트 시점에 접근성 업데이트
로딩 상태가 변경될 때마다 접근성 정보를 업데이트해야 합니다. 예를 들면 다음과 같습니다:

```swift
func updateLoadingState(_ isLoading: Bool) {
    if isLoading {
        yourView.accessibilityLabel = "로딩 중입니다."
    } else {
        yourView.accessibilityLabel = "로딩이 완료되었습니다."
    }
}
```

## 요약
이제 Swift SkeletonView에 접근성을 추가하는 방법에 대해 알아보았습니다. 접근성을 통해 사용자 경험을 향상시키고 모든 사용자가 앱을 동등하게 이용할 수 있도록 할 수 있습니다.

## 참고 자료
- [Swift SkeletonView GitHub 페이지](https://github.com/Juanpe/SkeletonView)
- [iOS Accessibility 가이드](https://developer.apple.com/accessibility/ios/)