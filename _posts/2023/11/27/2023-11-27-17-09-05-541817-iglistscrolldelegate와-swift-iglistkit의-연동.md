---
layout: post
title: "[swift] IGListScrollDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListScrollDelegate는 IGListKit에서 스크롤 이벤트를 처리하기 위한 프로토콜입니다. 이 프로토콜은 스크롤 뷰가 스크롤 될 때 호출되는 메서드를 정의합니다. IGListScrollDelegate를 사용하여 리스트 뷰의 스크롤 이벤트를 처리하고 원하는 작업을 수행할 수 있습니다.

이 문서에서는 IGListScrollDelegate와 Swift IGListKit를 연동하는 방법에 대해 알아보겠습니다.

## IGListScrollDelegate 구현하기

먼저, IGListScrollDelegate를 구현하기 위해 다음과 같은 단계를 따릅니다:

1. IGListScrollDelegate 프로토콜을 채택한 후, `scrollViewDidScroll(_:)` 메서드를 구현합니다. 이 메서드는 스크롤이 발생할 때마다 호출됩니다.

```swift
class MyViewController: UIViewController, IGListScrollDelegate {

    //...

    func scrollViewDidScroll(_ scrollView: UIScrollView) {
        // 스크롤 이벤트 처리
        // 원하는 작업 수행
    }

    //...

}
```

2. `scrollViewDidScroll(_:)` 메서드 내에서 원하는 작업을 수행합니다. 이 메서드에서는 스크롤이 발생할 때마다 호출되므로, 이를 이용하여 원하는 작업을 처리할 수 있습니다.

예를 들어, 사용자가 스크롤을 멈출 때까지 기다렸다가 특정 작업을 수행하고 싶다면, 다음과 같이 `scrollViewDidScroll(_:)` 메서드에서 타이머를 사용할 수 있습니다.

```swift
class MyViewController: UIViewController, IGListScrollDelegate {

    var timer: Timer?

    //...

    func scrollViewDidScroll(_ scrollView: UIScrollView) {
        timer?.invalidate()
        timer = Timer.scheduledTimer(withTimeInterval: 0.5, repeats: false, block: { (_) in
            // 타이머가 끝나면 원하는 작업 수행
        })
    }

    //...

}
```

## IGListScrollDelegate 등록하기

IGListScrollDelegate를 사용하기 위해서는 해당 프로토콜을 리스트 뷰에 등록해야 합니다. 이를 위해 다음과 같은 단계를 따릅니다:

1. IGListAdapter 인스턴스를 생성합니다.

```swift
let adapter = IGListAdapter(updater: IGListAdapterUpdater(), viewController: self)
```

2. 리스트 뷰에서 IGListScrollDelegate를 등록합니다.

```swift
adapter.scrollViewDelegate = myScrollDelegate
```

여기서 `myScrollDelegate`는 이전에 구현한 IGListScrollDelegate 프로토콜을 채택한 객체입니다.

3. 등록된 IGListScrollDelegate를 이용하여 스크롤 이벤트를 처리합니다.

```swift
class MyScrollDelegate: NSObject, IGListScrollDelegate {

    //...

    func scrollViewDidScroll(_ scrollView: UIScrollView) {
        // 스크롤 이벤트 처리
        // 원하는 작업 수행
    }

    //...

}
```

IGListAdapter에 등록된 IGListScrollDelegate는 해당 리스트 뷰의 스크롤 이벤트를 수신하고 처리합니다.

## 결론

이 문서에서는 IGListScrollDelegate와 Swift IGListKit의 연동에 대해 알아보았습니다. IGListScrollDelegate를 사용하면 리스트 뷰의 스크롤 이벤트를 쉽게 처리하고, 원하는 작업을 수행할 수 있습니다. IGListScrollDelegate를 구현하고 이를 IGListAdapter에 등록하여 원하는 스크롤 이벤트를 처리하는 방법을 익히세요.

더 자세한 내용은 [IGListKit 공식 문서](https://instagram.github.io/IGListKit/Classes/IGListScrollDelegate.html)를 참고하세요.