---
layout: post
title: "[swift] IGListCollectionViewDelegateLayout와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 IGListCollectionViewDelegateLayout와 Swift IGListKit을 함께 사용하는 방법에 대해 알아보겠습니다.

## IGListCollectionViewDelegateLayout 이란?

IGListCollectionViewDelegateLayout은 Instagram에서 개발한 IGListKit의 일부입니다. 이는 UICollectionViewDelegateFlowLayout을 대체하는 인터페이스로, IGListKit에 특화된 커스텀 레이아웃을 구현할 수 있도록 해줍니다. IGListCollectionViewDelegateLayout을 사용하면 UICollectionViewDelegateFlowLayout에서 제공하는 다양한 레이아웃 기능을 사용할 수 있으며, IGListKit의 강력한 데이터 관리 기능과 함께 사용할 수 있습니다.

## Swift IGListKit 연동하기

Step 1: IGListCollectionViewDelegateLayout 구현하기

먼저, IGListCollectionViewDelegateLayout을 사용하기 위해 커스텀 레이아웃을 구현해야 합니다. 예를 들어, 다음과 같이 UICollectionViewCell의 크기를 동적으로 설정하는 커스텀 레이아웃을 구현해보겠습니다.

```swift
class DynamicSizeLayout: NSObject, IGListCollectionViewDelegateLayout {
    func collectionView(
        _ collectionView: UICollectionView,
        layout collectionViewLayout: UICollectionViewLayout,
        sizeForItemAt index: Int,
        constrainedTo size: CGSize
    ) -> CGSize {
        // UICollectionViewCell의 크기를 동적으로 계산하여 반환하는 로직
    }
}
```

Step 2: IGListAdapter 설정하기

다음 단계는 IGListAdapter를 설정하여 IGListCollectionViewDelegateLayout과 연결하는 것입니다. IGListAdapter는 IGListKit의 핵심 클래스로, 데이터 관리와 뷰 갱신을 담당합니다.

```swift
let adapter = IGListAdapter(
    updater: IGListAdapterUpdater(),
    viewController: self,
    workingRangeSize: 0
)
adapter.collectionView = collectionView
adapter.collectionViewDelegate = DynamicSizeLayout()
adapter.dataSource = self // IGListAdapterDataSource를 구현한 클래스
```

위의 코드에서 `DynamicSizeLayout()`을 `adapter.collectionViewDelegate`에 할당하여 IGListCollectionViewDelegateLayout과 연결합니다.

Step 3: IGListAdapterDataSource 구현하기

마지막 단계는 IGListAdapterDataSource 프로토콜을 구현하여 데이터를 제공하는 클래스를 작성하는 것입니다. 이 데이터 소스 클래스는 collectionView의 섹션과 항목을 정의하고, 데이터를 반환하는 역할을 합니다.

```swift
extension YourViewController: IGListAdapterDataSource {
    func objects(
        for listAdapter: IGListAdapter
    ) -> [IGListDiffable] {
        // 데이터 배열을 반환하는 로직
    }
    
    func listAdapter(
        _ listAdapter: IGListAdapter,
        sectionControllerFor object: Any
    ) -> IGListSectionController {
        // 섹션 컨트롤러를 반환하는 로직
    }
    
    func emptyView(
        for listAdapter: IGListAdapter
    ) -> UIView? {
        // 뷰가 비었을 때 표시할 빈 상태 뷰를 반환하는 로직
    }
}
```

위의 코드에서 `listAdapter(_:sectionControllerFor:)` 메소드는 IGListKit에서 IGListSectionController를 반환하는 역할을 합니다. 이 섹션 컨트롤러는 특정 섹션에 대한 뷰와 데이터를 관리하고 표시하는 역할을 합니다.

## 결론

이제 IGListCollectionViewDelegateLayout와 Swift IGListKit을 함께 사용하는 방법에 대해 알게 되었습니다. IGListCollectionViewDelegateLayout을 사용하여 UICollectionView의 레이아웃을 커스터마이징하고, IGListAdapter와 IGListAdapterDataSource를 통해 IGListKit의 강력한 데이터 관리 기능을 활용할 수 있습니다. IGListKit은 많은 데이터를 다루는 애플리케이션에서 성능과 관리 용이성을 향상시킬 수 있는 좋은 선택입니다.