---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UICollectionView에서의 UIResponder 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

UICollectionView는 iOS 앱에서 다양한 형식의 콘텐츠 및 레이아웃을 표시하기 위해 사용되는 매우 유용한 컨트롤입니다. 터치 이벤트 처리를 위해 UICollectionViewCell에 대한 UIResponder를 구현해야 할 때가 있습니다. 이번 포스트에서는 UICollectionView에서의 UIResponder 사용법에 대해 알아보겠습니다.

## UIResponder란?

UIResponder는 iOS 앱에서 이벤트를 처리하는 기본 클래스입니다. 화면상의 사용자 동작 및 터치 이벤트를 처리하기 위해 UIResponder를 서브클래싱하여 이벤트 메소드를 구현할 수 있습니다.

## UICollectionView에서 UIResponder 구현하기

UICollectionViewCell에 대한 UIResponder 구현을 위해 다음 단계를 따르세요.

### 단계 1: UICollectionViewCell 서브클래싱

UICollectionViewCell을 서브클래싱하여 사용자 정의 셀을 만듭니다. 즉, UICollectionViewCell을 상속받는 클래스를 생성합니다.

```swift
class CustomCell: UICollectionViewCell {
    // 셀에 대한 커스텀 로직을 구현합니다.
}
```

### 단계 2: UIResponder 이벤트 메소드 구현

CustomCell 클래스에서 UIResponder를 상속받아 UIResponder 이벤트 메소드를 구현합니다. 다음은 일반적으로 사용되는 몇 가지 UIResponder 이벤트 메소드입니다.

#### 터치 이벤트 메소드

```swift
override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
    super.touchesBegan(touches, with: event)
    // 터치가 시작될 때 호출됩니다.
}

override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
    super.touchesMoved(touches, with: event)
    // 터치가 이동될 때 호출됩니다.
}

override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
    super.touchesEnded(touches, with: event)
    // 터치가 끝날 때 호출됩니다.
}
```

#### 제스처 이벤트 메소드

```swift
override func gestureRecognizerShouldBegin(_ gestureRecognizer: UIGestureRecognizer) -> Bool {
    // 해당 제스처의 시작을 허용할지 여부를 반환합니다.
    return true
}

override func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer) -> Bool {
    // 동시에 인식될 제스처들의 처리를 허용할지 여부를 반환합니다.
    return true
}
```

위의 이벤트 메소드를 CustomCell 클래스에 추가하여 필요한 터치 및 제스처 이벤트를 처리할 수 있습니다.

## 결론

UICollectionView에서 UIResponder를 사용하여 터치 이벤트를 처리하는 방법에 대해 살펴보았습니다. UIResponder를 이용하면 UICollectionView 내에서 발생하는 사용자 동작을 캡처하고, 해당 동작에 대한 로직을 구현할 수 있습니다. UIResponder를 상속받는 클래스를 구현하고, 터치 및 제스처 이벤트 메소드를 재정의함으로써 커스텀 UICollectionView 셀을 만들 수 있습니다.

참고 자료:
- [Apple Developer Documentation - UIResponder](https://developer.apple.com/documentation/uikit/uiresponder)