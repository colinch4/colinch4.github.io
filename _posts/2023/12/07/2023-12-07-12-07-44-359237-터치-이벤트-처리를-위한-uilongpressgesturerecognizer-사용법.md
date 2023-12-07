---
layout: post
title: "[swift] 터치 이벤트 처리를 위한 UILongPressGestureRecognizer 사용법"
description: " "
date: 2023-12-07
tags: [swift]
comments: true
share: true
---

최근 iOS 앱을 개발하면서 터치 이벤트를 처리하기 위해 UILongPressGestureRecognizer 클래스를 사용하게 되었습니다. 이번 포스트에서는 UILongPressGestureRecognizer를 사용하여 터치 이벤트를 처리하는 방법을 알아보겠습니다.

## UILongPressGestureRecognizer란?

UILongPressGestureRecognizer는 사용자가 화면을 길게 누르고 있는 동안 발생하는 이벤트를 감지하는 제스처 인식기입니다. 사용자가 화면을 길게 누르고 있으면 UILongPressGestureRecognizer에서 제공하는 액션을 실행할 수 있습니다.

## 사용 방법

1. UILongPressGestureRecognizer 객체 생성

먼저, UILongPressGestureRecognizer 객체를 생성해야 합니다. 아래의 예제 코드를 참고하여 UILongPressGestureRecognizer 객체를 생성하세요.

```swift
let longPressRecognizer = UILongPressGestureRecognizer(target: self, action: #selector(handleLongPress(_:)))
```

위의 코드에서 `target`은 이벤트 처리를 담당할 객체를 지정하고, `action`은 이벤트 처리 메서드를 선택합니다. 메서드는 `@objc` 키워드로 선언되어야 하며, 매개변수로 `UILongPressGestureRecognizer` 객체를 받아야합니다.

2. 제스처 인식기에 객체 추가

다음으로, UILongPressGestureRecognizer 객체를 제스처 인식기에 추가해야 합니다. 아래의 코드를 참고하여 제스처 인식기에 UILongPressGestureRecognizer 객체를 추가하세요.

```swift
yourView.addGestureRecognizer(longPressRecognizer)
```

위의 코드에서 `yourView`는 제스처 인식기가 적용될 뷰를 지정합니다. 이렇게 하면 해당 뷰에서 발생하는 길게 누르기 제스처 이벤트를 감지할 수 있습니다.

3. 이벤트 처리 메서드 작성

이제 길게 누르기 제스처 이벤트를 처리할 메서드를 작성해야 합니다. 이벤트 처리 메서드는 `@objc` 키워드로 선언되어야 하며, 매개변수로 `UILongPressGestureRecognizer` 객체를 받아야합니다. 아래의 예제 코드를 참고하여 이벤트 처리 메서드를 작성하세요.

```swift
@objc func handleLongPress(_ gesture: UILongPressGestureRecognizer) {
    if gesture.state == .began {
        // 길게 누르기 제스처가 시작되었을 때 처리할 코드 작성
    } else if gesture.state == .ended {
        // 길게 누르기 제스처가 끝났을 때 처리할 코드 작성
    }
}
```

위의 코드에서는 `gesture.state`를 사용하여 제스처 상태를 확인하고, 시작 및 종료 이벤트에 해당하는 코드를 작성하면 됩니다. 

4. 이벤트 처리

이제 길게 누르기 제스처 이벤트를 처리할 준비가 모두 되었습니다. `handleLongPress` 메서드에서 이벤트를 처리하는 원하는 코드를 작성하세요.

## 결론

이번 포스트에서는 UILongPressGestureRecognizer를 사용하여 터치 이벤트를 처리하는 방법을 알아보았습니다. UILongPressGestureRecognizer는 사용자가 화면을 길게 누르고 있는 동안 발생하는 이벤트를 감지할 수 있습니다. 이를 통해 사용자의 터치 동작을 적절한 방식으로 인식하고 처리할 수 있습니다.

더 많은 정보를 원한다면 [Apple 개발자 문서](https://developer.apple.com/documentation/uikit/uilongpressgesturerecognizer)를 참고해보세요.