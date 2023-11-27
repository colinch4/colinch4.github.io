---
layout: post
title: "[swift] IGListTransitionDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListKit은 iOS 앱에서 유연한 리스트 화면을 구성하기 위한 강력한 라이브러리입니다. 이 라이브러리는 IGListTransitionDelegate를 이용하여 화면 전환 시 리스트 상태를 보존할 수 있습니다. 이번 글에서는 IGListTransitionDelegate와 Swift IGListKit의 연동 방법에 대해 알아보겠습니다.

## IGListTransitionDelegate란?

IGListTransitionDelegate는 IGListController와 함께 작동하는 프로토콜입니다. 이 프로토콜을 이용하면 화면 전환 시 IGListController가 현재 보이는 항목의 상태를 보존하고, 다시 화면으로 돌아올 때 항목의 상태를 복원할 수 있습니다.

## IGListTransitionDelegate 구현하기

먼저 IGListTransitionDelegate를 구현하기 위해 다음 스텝을 따라주세요.

1. IGListTransitionDelegate 프로토콜을 채택해주세요.

```swift
class YourViewController: UIViewController, IGListTransitionDelegate {
    // ...
}
```

2. IGListTransitionDelegate의 메서드를 구현해주세요.

```swift
extension YourViewController {
    func transitionWillStart() {
        // 화면 전환 이전에 할 작업들을 처리합니다.
    }

    func transitionDidEnd() {
        // 화면 전환 이후에 필요한 작업들을 처리합니다.
    }

    func listAdapter(_ listAdapter: ListAdapter, willDisplay object: AnyObject, at index: Int) {
        // 리스트의 아이템이 화면에 표시될 때 호출됩니다.
        // 여기에서 아이템의 상태를 저장하거나 업데이트할 수 있습니다.
    }
}
```

3. IGListTransitionDelegate를 사용할 IGListController를 초기화합니다.

```swift
let yourListController = YourListController()
yourListController.transitionDelegate = self
```

이제 IGListTransitionDelegate를 구현했으니 화면 전환 시 리스트 상태를 보존하고 복원할 준비가 완료되었습니다.

## IGListTransitionDelegate 사용하기

이제 IGListTransitionDelegate를 사용하여 리스트 상태를 보존하고 복원하는 방법에 대해 알아보겠습니다.

1. IGListTransitionDelegate를 사용할 리스트 컨트롤러를 정의합니다.

```swift
class YourListController: ListAdapterDataSource {
    // ...
}
```

2. ListAdapter의 dataSource 속성을 설정하고 IGListTransitionDelegate를 채택합니다.

```swift
let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self)
adapter.dataSource = self
adapter.transitionDelegate = transitionDelegate // 이전에 구현한 IGListTransitionDelegate
```

3. 리스트 컨트롤러에서 데이터 소스를 구현합니다.

```swift
extension YourListController {
    func objects(for listAdapter: ListAdapter) -> [ListDiffable] {
        // 리스트에 표시할 데이터를 반환합니다.
    }

    func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
        // 새로운 section controller를 생성해 반환합니다.
    }

    func emptyView(for listAdapter: ListAdapter) -> UIView? {
        // 리스트가 비어있을 때 표시할 뷰를 반환합니다.
    }
}
```

IGListTransitionDelegate를 구현하고 사용하는 방법에 대해 알아보았습니다. 이제 IGListKit으로 유연하고 성능이 좋은 리스트 화면을 구성할 수 있게 되었습니다.

더 자세한 내용은 [IGListKit 문서](https://github.com/Instagram/IGListKit)를 참고하세요.