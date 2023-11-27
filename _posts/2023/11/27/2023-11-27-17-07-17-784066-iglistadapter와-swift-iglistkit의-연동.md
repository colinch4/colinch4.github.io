---
layout: post
title: "[swift] IGListAdapter와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

이번 글에서는 IGListAdapter와 Swift IGListKit의 연동에 대해 알아보겠습니다. IGListAdapter는 IGListKit에서 가장 중요한 컴포넌트 중 하나로, 데이터를 제공하여 리스트 뷰를 업데이트하는 역할을 합니다. Swift에서 IGListAdapter를 사용하기 위해서는 몇 가지 단계를 따라야 합니다.

## 1. IGListAdapter 초기화

IGListAdapter를 사용하기 위해 가장 먼저 해야 할 일은 IGListAdapter를 초기화하는 것입니다. IGListAdapter는 IGListCollectionContext 객체와 함께 사용됩니다. 이를 통해 데이터 소스와 컬렉션 뷰를 연결할 수 있습니다. IGListCollectionContext에서는 섹션의 개수, 섹션 내 아이템의 개수 등을 관리할 수 있습니다.

```swift
let adapter = IGListAdapter(updater: IGListAdapterUpdater(), viewController: self, workingRangeSize: 0)
adapter.collectionView = self.collectionView
adapter.dataSource = self
```

이렇게 초기화한 `adapter`를 통해 IGListAdapter를 사용할 수 있습니다.

## 2. IGListAdapterDataSource 구현

다음으로 해야 할 일은 IGListAdapterDataSource 프로토콜을 구현하는 것입니다. IGListAdapterDataSource는 IGListAdapter에 데이터를 제공하는 역할을 합니다. Swift에서 IGListAdapterDataSource를 구현할 때는 다음과 같은 함수를 구현해야 합니다.

```swift
extension ViewController: IGListAdapterDataSource {
    func objects(for listAdapter: IGListAdapter) -> [IGListDiffable] {
        // 데이터 소스에서 IGListDiffable 객체의 배열을 반환하는 로직을 작성합니다.
    }
    
    func listAdapter(_ listAdapter: IGListAdapter, sectionControllerFor object: Any) -> IGListSectionController {
        // IGListAdapter에서 사용할 섹션 컨트롤러를 생성하여 반환하는 로직을 작성합니다.
    }
    
    func emptyView(for listAdapter: IGListAdapter) -> UIView? {
        // IGListCollectionView에 데이터가 없을 때 표시할 뷰를 반환하는 로직을 작성합니다.
    }
}
```

`objects(for:)` 함수에서는 IGListDiffable 객체의 배열을 반환해야 합니다. 이 객체들은 컬렉션 뷰에 표시될 데이터를 의미합니다. `listAdapter(_:sectionControllerFor:)` 함수에서는 객체에 대한 섹션 컨트롤러를 생성하여 반환해야 합니다. 이 섹션 컨트롤러는 객체를 컬렉션 뷰에 어떻게 표시할지를 정의합니다. `emptyView(for:)` 함수에서는 컬렉션 뷰에 데이터가 없을 때 표시할 뷰를 반환해야 합니다.

## 3. IGListAdapterDelegate 구현 (선택 사항)

IGListAdapterDelegate는 IGListAdapter의 동작을 커스터마이징하기 위해 사용됩니다. 필요한 경우 IGListAdapterDelegate를 구현하여 IGListAdapter 동작을 커스터마이징할 수 있습니다.
```swift
extension ViewController: IGListAdapterDelegate {
    func listAdapter(_: IGListAdapter, willDisplay sectionController: IGListSectionController, cell: UICollectionViewCell, at index: Int) {
        // 셀이 화면에 보여질 때 호출되는 로직을 작성합니다.
    }
    
    // 다른 IGListAdapterDelegate 메서드도 필요한 경우에 구현합니다.
}
```

IGListAdapterDelegate에서 제공하는 메서드들을 사용하여 원하는 동작을 수행할 수 있습니다.

이렇게 IGListAdapter와 Swift IGListKit을 연동함으로써, 리스트 뷰의 데이터 업데이트와 관련된 작업을 효율적으로 처리할 수 있습니다. IGListAdapter와 IGListKit을 적절히 활용하여 좀 더 성능이 우수한 리스트 뷰를 구현할 수 있습니다.

더 자세한 내용을 알고 싶다면, [IGListKit GitHub 페이지](https://github.com/Instagram/IGListKit)를 참고해주세요.