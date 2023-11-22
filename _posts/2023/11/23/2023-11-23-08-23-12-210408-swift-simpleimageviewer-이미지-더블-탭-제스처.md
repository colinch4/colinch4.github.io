---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 더블 탭 제스처"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift로 간단한 이미지 뷰어를 만들 때 이미지에 더블 탭 제스처를 추가하는 방법을 알아보겠습니다. 

### 1. UITapGestureRecognizer 생성

```swift
let doubleTapGesture = UITapGestureRecognizer(target: self, action: #selector(handleDoubleTap(_:)))
doubleTapGesture.numberOfTapsRequired = 2
```

위의 코드는 UITapGestureRecognizer를 생성하고, 더블 탭 제스처를 처리하는 셀렉터 메서드를 지정한 뒤, 더블 탭이 두 번 되었을 때 동작하도록 설정한 것입니다.

### 2. 이미지 뷰에 제스처 추가

```swift
imageView.isUserInteractionEnabled = true
imageView.addGestureRecognizer(doubleTapGesture)
```

위의 코드는 이미지 뷰의 사용자 상호 작용 설정을 true로 변경한 뒤, 이미지 뷰에 우리가 만든 doubleTapGesture를 추가하는 것입니다.

### 3. 더블 탭 제스처 처리 메서드

```swift
@objc func handleDoubleTap(_ gesture: UITapGestureRecognizer) {
    // 더블 탭 제스처가 발생했을 때 동작할 내용을 작성해주세요.
    // 예를 들면 이미지를 확대하거나 축소하는 등의 동작을 구현할 수 있습니다.
}
```

위의 코드는 더블 탭 제스처가 발생했을 때 동작할 메서드입니다. 이 메서드에서 작성한 동작에 따라 이미지를 확대하거나 축소하는 등의 원하는 동작을 구현할 수 있습니다.

### 참고 자료

- [UITapGestureRecognizer - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uitapgesturerecognizer)
- [Handling UITapGestureRecognizer in Swift](https://www.andrewcbancroft.com/2015/07/08/how-to-make-an-image-double-tappable-in-swift/)