---
layout: post
title: "[swift] IGListEmptyCollectionContext와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListEmptyCollectionContext는 IGListKit에서 제공하는 기능 중 하나로, 데이터가 비어있을 때의 화면을 커스터마이징할 수 있게 해줍니다. 이 기능을 Swift에서 사용하는 방법을 알아보겠습니다.

### IGListEmptyCollectionContext란?

IGListEmptyCollectionContext는 IGListKit의 기능 중 하나로, 데이터가 비어있을 때의 뷰를 커스터마이징할 수 있는 컨텍스트입니다. IGListEmptyCollectionContext를 사용하면 데이터가 없을 때 별도의 뷰를 보여줄 수 있으며, 이를 통해 사용자에게 더 나은 경험을 제공할 수 있습니다.

### IGListEmptyCollectionContext 사용 방법

1. 먼저 IGListEmptyCollectionContext를 사용하기 위해 IGListKit을 프로젝트에 추가해야 합니다. IGListKit은 Cocoapods나 Carthage를 통해 쉽게 추가할 수 있습니다.

2. IGListEmptyCollectionContext를 사용할 뷰 컨트롤러에 IGListAdapter를 초기화해야 합니다. IGListAdapter는 IGListEmptyCollectionContext를 사용하여 빈 데이터 상태를 처리하는 데 필요한 기능을 제공합니다.

```swift
let adapter = IGListAdapter(updater: IGListAdapterUpdater(), viewController: self, workingRangeSize: 0)
```

3. IGListAdapter에 `emptyViewForListAdapter(_:)` 메소드를 구현하여 빈 데이터 상태일 때 보여줄 뷰를 반환합니다.

```swift
func emptyView(for listAdapter: IGListAdapter) -> UIView? {
    let emptyView = MyCustomEmptyView()
    return emptyView
}
```

4. 이제 데이터를 관리하는 ListSectionController 클래스에서 데이터가 비어있는지 여부를 확인하고, 비어있는 경우에는 UICollectionViewDelegateFlowLayout 프로토콜의 `collectionContext(_:, cellFor:, at:)` 메소드를 호출하여 뷰를 업데이트할 수 있습니다.

```swift
func collectionContext(_ collectionContext: IGListCollectionContext, cellFor sectionController: IGListSectionController, at index: Int) -> UICollectionViewCell {
    if data.isEmpty {
        collectionContext.emptyViewDelegate?.collectionView(collectionContext.collectionView, viewForEmpty: sectionController, at: index)
    }
    // ...
}
```

### 예제 코드

아래는 IGListEmptyCollectionContext를 사용하여 데이터가 비어있을 때 표시될 뷰를 커스터마이징하는 예제 코드입니다.

```swift
import IGListKit

class MyViewController: UIViewController, ListAdapterDataSource {

    let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self, workingRangeSize: 0)

    var data: [String] = []

    override func viewDidLoad() {
        super.viewDidLoad()

        adapter.dataSource = self
        adapter.collectionView = collectionView
    }

    // MARK: - ListAdapterDataSource
    
    func objects(for listAdapter: ListAdapter) -> [ListDiffable] {
        return data as [ListDiffable]
    }
    
    func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
        return MySectionController()
    }
    
    func emptyView(for listAdapter: ListAdapter) -> UIView? {
        let emptyView = MyCustomEmptyView()
        return emptyView
    }

    // ...

}
```

### 참고 자료

- IGListKit 공식 문서: [https://github.com/Instagram/IGListKit](https://github.com/Instagram/IGListKit)
- IGListEmptyCollectionContext 공식 문서: [https://github.com/Instagram/IGListKit/blob/master/docs/EMPTY.md](https://github.com/Instagram/IGListKit/blob/master/docs/EMPTY.md)