---
layout: post
title: "[swift] IGListCollectionViewDelegateLayout와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

Swift IGListKit은 매우 강력한 iOS 라이브러리로, 컬렉션 뷰를 사용하여 복잡한 데이터를 표시하고 관리하는 것을 도와줍니다. IGListCollectionViewDelegateLayout는 IGListKit과 함께 사용되어 컬렉션 뷰의 레이아웃을 제어하는 역할을 합니다. 이번 글에서는 IGListCollectionViewDelegateLayout와 Swift IGListKit을 통합하는 방법에 대해 알아보겠습니다.

## IGListCollectionViewDelegateLayout 소개

IGListCollectionViewDelegateLayout은 UICollectionViewDelegateFlowLayout를 확장한 프로토콜입니다. IGListKit은 IGListCollectionViewDelegateLayout을 사용하여 컬렉션 뷰에 섹션과 아이템의 크기와 간격을 제어합니다. IGListCollectionViewDelegateLayout을 사용하면 다양한 레이아웃을 지원하는 IGListKit에서 섹션과 아이템의 크기를 동적으로 조정할 수 있습니다.

## IGListCollectionViewDelegateLayout 사용하기

IGListCollectionViewDelegateLayout을 사용하려면 다음 단계를 수행해야 합니다.

1. IGListCollectionViewDelegateLayout을 채택하는 클래스를 생성합니다.
```swift
class MyLayoutDelegate: NSObject, IGListCollectionViewDelegateLayout {
    // IGListCollectionViewDelegateLayout 메서드를 구현합니다.
}
```

2. 컬렉션 뷰 인스턴스를 생성하고 델리게이트에 MyLayoutDelegate를 할당합니다.
```swift
let collectionView = UICollectionView(frame: .zero, collectionViewLayout: UICollectionViewFlowLayout())
collectionView.collectionViewLayout = MyLayoutDelegate()
collectionView.dataSource = self // IGListKit의 데이터 소스 설정
collectionView.delegate = self // IGListKit의 델리게이트 설정
```

3. MyLayoutDelegate에서 필요한 메서드를 구현합니다. IGListKit은 이 메서드를 사용하여 섹션과 아이템의 크기와 간격을 조정합니다.
```swift
func collection(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
    // 아이템의 크기를 반환합니다.
}

func collection(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, insetForSectionAt section: Int) -> UIEdgeInsets {
    // 섹션의 여백을 반환합니다.
}

func collection(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumLineSpacingForSectionAt section: Int) -> CGFloat {
    // 섹션의 아이템 사이의 최소 라인 간격을 반환합니다.
}

func collection(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, minimumInteritemSpacingForSectionAt section: Int) -> CGFloat {
    // 섹션의 아이템 사이의 최소 열 간격을 반환합니다.
}
```

## IGListCollectionViewDelegateLayout와 IGListKit 연동하기

IGListKit과 IGListCollectionViewDelegateLayout을 연동하려면 다음 단계를 수행해야 합니다.

1. IGListKit의 ListAdapter 인스턴스를 생성합니다.
```swift
let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self, workingRangeSize: 0)
adapter.collectionView = collectionView
adapter.dataSource = self
```

2. IGListKit의 ListAdapterDataSource를 구현하여 데이터를 제공합니다.
```swift
extension MyViewController: ListAdapterDataSource {
    func objects(for listAdapter: ListAdapter) -> [ListDiffable] {
        // 반환할 데이터 배열을 생성합니다.
    }
    
    func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
        // 섹션 컨트롤러를 반환합니다.
    }
    
    func emptyView(for listAdapter: ListAdapter) -> UIView? {
        // 데이터가 없을 때 표시할 뷰를 반환합니다.
    }
}
```

3. IGListCollectionViewDelegateLayout의 메서드를 구현하여 레이아웃을 제어합니다.
```swift
class MyLayoutDelegate: NSObject, IGListCollectionViewDelegateLayout {
    // IGListCollectionViewDelegateLayout 메서드를 구현합니다.
}
```

IGListCollectionViewDelegateLayout과 Swift IGListKit을 연동하면 IGListKit에서 자동으로 섹션과 아이템의 크기와 간격을 처리할 수 있습니다. IGListCollectionViewDelegateLayout을 사용하여 IGListKit에서 제공하는 다양한 레이아웃 옵션을 활용하여 앱의 사용자 인터페이스를 개선할 수 있습니다.

## 참고 문서

- [IGListKit GitHub Repository](https://github.com/Instagram/IGListKit)
- [IGListCollectionViewDelegateLayout Documentation](https://docs.iglistkit.org/api/Protocols/IGListCollectionViewDelegateLayout.html)