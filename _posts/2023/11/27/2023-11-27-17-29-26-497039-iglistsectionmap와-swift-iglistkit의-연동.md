---
layout: post
title: "[swift] IGListSectionMap와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListSectionMap은 IGListKit에서 사용되는 매우 유용한 기능 중 하나입니다. IGListSectionMap을 사용하면 UICollectionViewCell을 선택적으로 업데이트하고 재사용할 수 있습니다. IGListSectionMap을 Swift 프로젝트에서 사용하는 방법에 대해 알아보겠습니다.

## IGListSectionMap 설명

IGListSectionMap은 section controller와 collection view cell을 매핑해주는 역할을 합니다. 매핑 정보를 통해 IGListKit은 필요한 셀만 업데이트하고 재사용할 수 있습니다. IGListSectionMap은 IGListKit의 일부이며 IGListBindingSectionController와 함께 사용됩니다.

## IGListSectionMap 사용하기

1. 먼저, IGListSectionMap을 생성합니다.

```swift
let sectionMap = IGListSectionMap()
```

2. IGListSectionMap에 section 및 해당하는 셀을 등록합니다.

```swift
sectionMap.setSection(sectionController, for: cellType)
```

여기서 `sectionController`는 IGListSectionController의 인스턴스이고, `cellType`은 해당 section에 대한 셀의 유형입니다.

3. IGListSectionMap에서 셀 타입에 따라 section controller를 가져올 수 있습니다.

```swift
let sectionController = sectionMap.sectionController(for: cellType)
```

이제 IGListSectionMap을 사용하여 셀과 section controller를 매핑할 수 있습니다.

## 예시

IGListSectionMap을 사용하여 Swift IGListKit 프로젝트에서 section과 셀을 매핑하는 예시를 살펴보겠습니다.

```swift
class MyViewController: UIViewController, ListAdapterDataSource {

    let adapter: ListAdapter = ListAdapter(updater: ListAdapterUpdater(), viewController: nil)

    lazy var sectionMap: IGListSectionMap = {
        let sectionMap = IGListSectionMap()
        sectionMap.setSection(FeedSectionController(), for: FeedCell.self)
        sectionMap.setSection(CommentSectionController(), for: CommentCell.self)
        return sectionMap
    }()

    override func viewDidLoad() {
        super.viewDidLoad()

        adapter.collectionView = collectionView
        adapter.dataSource = self
    }

    func objects(for listAdapter: ListAdapter) -> [ListDiffable] {
        ...
    }

    func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
        let cellType = type(of: object)
        let sectionController = sectionMap.sectionController(for: cellType)
        return sectionController
    }

    func emptyView(for listAdapter: ListAdapter) -> UIView? {
        ...
    }
}
```

위의 예시에서 `FeedSectionController`는 `FeedCell`을 위한 section controller이고 `CommentSectionController`는 `CommentCell`을 위한 section controller입니다. IGListSectionMap을 사용하여 각 셀에 맞는 section controller를 가져옵니다.

## 마무리

IGListSectionMap은 IGListKit 프로젝트에서 셀과 section controller를 효율적으로 매핑하는 데 도움이 됩니다. 이를 통해 필요한 셀만 업데이트하고 재사용할 수 있어 성능 향상을 이룰 수 있습니다. IGListSectionMap을 활용하여 더 나은 사용자 경험을 제공하는 Swift IGListKit 앱을 만들어보세요.

## 참고 자료
- [IGListKit GitHub](https://github.com/Instagram/IGListKit)
- [IGListSectionMap Documentation](https://instagram.github.io/IGListKit/Classes/IGListSectionMap.html)