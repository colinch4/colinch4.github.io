---
layout: post
title: "[swift] IGListUpdatingDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

> IGListUpdatingDelegate는 IGListKit에서 제공하는 프로토콜로, 리스트 데이터의 업데이트를 관리하기 위해 사용됩니다. 이 블로그 포스트에서는 IGListUpdatingDelegate와 Swift IGListKit의 연동 방법을 알아보겠습니다.

## IGListUpdatingDelegate란?

IGListUpdatingDelegate는 IGListKit에서 리스트 데이터의 변경을 처리하는 데 사용되는 중요한 프로토콜입니다. 이 프로토콜은 섹션 및 항목의 삽입, 삭제, 이동 등의 변경 사항을 관리합니다.

## Swift IGListKit와의 연동 방법

Swift에서 IGListUpdatingDelegate를 사용하기 위해 몇 가지 단계를 따라야 합니다. 먼저 IGListUpdatingDelegate 프로토콜을 채택하고, 해당 프로토콜에서 정의된 함수들을 구현해야 합니다.

```swift
class MyListViewController: UIViewController, IGListUpdatingDelegate {
    // ...

    // IGListUpdatingDelegate 프로토콜의 메서드 구현
    func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
        // 섹션 컨트롤러 반환
    }

    func listAdapter(_ listAdapter: ListAdapter, willDelete object: Any, at index: Int) {
        // 객체 삭제 전 실행할 작업 수행
    }

    // ...
}
```

위의 예제 코드에서는 MyListViewController 클래스가 IGListUpdatingDelegate를 채택하고, 해당 프로토콜에서 정의된 두 가지 메서드를 구현하고 있습니다. `listAdapter(_:sectionControllerFor:)` 메서드는 섹션 컨트롤러를 반환하고, `listAdapter(_:willDelete:at:)` 메서드는 객체를 삭제하기 전에 수행할 작업을 정의합니다.

구현한 MyListViewController에서 IGListAdapter와 연결하고, IGListKit의 업데이트 메서드를 호출하여 리스트 데이터를 업데이트할 수 있습니다.

```swift
class MyListViewController: UIViewController, IGListUpdatingDelegate {
    let adapter: ListAdapter

    override func viewDidLoad() {
        super.viewDidLoad()

        // ...

        // IGListAdapter 생성
        adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self)
        adapter.collectionView = collectionView
        adapter.dataSource = self
        adapter.delegate = self

        // ...
    }

    // ...
}
```

위의 예제 코드에서는 ListAdapter를 생성하고, collectionView와 연결한 뒤, dataSource와 delegate로 MyListViewController 자신을 지정하고 있습니다.

## 결론

IGListUpdatingDelegate는 IGListKit의 핵심 프로토콜 중 하나로, 리스트 데이터의 변경을 관리하는 데 사용됩니다. Swift에서 IGListUpdatingDelegate를 사용하기 위해서는 해당 프로토콜을 채택하고, 필요한 메서드를 구현해야 합니다. 이번 블로그 포스트에서는 IGListUpdatingDelegate와 Swift IGListKit의 연동 방법을 알아보았습니다.

## 참고 자료
- [IGListKit Documentation](https://instagram.github.io/IGListKit/)
- [IGListKit GitHub Repository](https://github.com/Instagram/IGListKit)