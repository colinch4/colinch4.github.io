---
layout: post
title: "[swift] IGListWorkingRangeDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListWorkingRangeDelegate는 IGListKit에서 제공하는 프로토콜 중 하나로, 작업 범위 작동에 대한 알림 메서드를 제공합니다. 이 기능을 사용하여 화면에서 셀이 작동 범위에 들어왔는지 떠났는지를 알 수 있습니다.

Swift의 IGListKit에서 IGListWorkingRangeDelegate를 구현하는 방법을 알아봅시다.

## IGListWorkingRangeDelegate 구현하기

1. 먼저, IGListWorkingRangeDelegate 프로토콜을 채택하고자 하는 ViewController에 프로토콜 선언을 추가합니다.

```swift
class MyViewController: UIViewController, IGListWorkingRangeDelegate {
    ...
}
```

2. IGListWorkingRangeDelegate 프로토콜을 구현하는 `listAdapter(_:willBeginWorkingRangeFor:)` 메서드를 추가합니다. 이 메서드는 작동 범위가 시작될 때 호출됩니다.

```swift
extension MyViewController {
    func listAdapter(_ listAdapter: ListAdapter, willBeginWorkingRangeFor sectionController: ListSectionController) {
        // 작업 범위가 시작될 때 호출되는 로직을 구현합니다.
    }
}
```

3. `listAdapter(_:didEndWorkingRangeFor:)` 메서드를 추가하여 작업 범위가 끝날 때 호출되는 로직을 구현할 수도 있습니다.

```swift
extension MyViewController {
    func listAdapter(_ listAdapter: ListAdapter, didEndWorkingRangeFor sectionController: ListSectionController) {
        // 작업 범위가 끝날 때 호출되는 로직을 구현합니다.
    }
}
```

## IGListWorkingRangeDelegate의 활용

IGListWorkingRangeDelegate를 활용하면 작동 범위 안에 있는 셀의 로딩, 비동기 작업 등을 관리할 수 있습니다. 예를 들어, 페이징된 데이터를 로드해야 하는 경우, 작동 범위 안에 있는 셀들을 감지해서 데이터를 로드하는 로직을 실행할 수 있습니다.

```swift
func listAdapter(_ listAdapter: ListAdapter, willBeginWorkingRangeFor sectionController: ListSectionController) {
    // 작업 범위가 시작될 때 데이터를 로드하는 로직을 구현합니다.
    if let sectionController = sectionController as? MySectionController {
        sectionController.loadMoreData()
    }
}
```

이와 같이 IGListWorkingRangeDelegate를 사용하여 작동 범위 관리를 간편하고 효율적으로 처리할 수 있습니다.

자세한 내용은 IGListKit 문서를 참조해 주세요.

## 참고 자료

- IGListKit 문서: [https://github.com/Instagram/IGListKit](https://github.com/Instagram/IGListKit)