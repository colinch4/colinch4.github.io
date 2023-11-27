---
layout: post
title: "[swift] IGListSectionMap와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListSectionMap은 IGListKit에서 사용되는 중요한 개념 중 하나입니다. IGListSectionMap은 데이터 소스와 셀 프로바이더를 연결하는 역할을 합니다. 이를 통해 IGListKit은 데이터를 적절한 셀로 매핑하고 화면에 표시할 수 있습니다.

## IGListSectionMap이란?

IGListSectionMap은 IGListKit의 핵심 요소 중 하나로, 섹션과 셀 프로바이더 간의 매핑을 관리합니다. IGListKit은 UICollectionView를 기반으로 한 UI를 구성하는데, IGListSectionMap은 UICollectionView의 UICollectionViewDataSource를 구현하는 데 사용됩니다. IGListSectionMap은 섹션 수, 각 섹션의 아이템 수, 각 아이템의 셀 프로바이더 등을 추적하고 관리합니다.

## IGListSectionMap와 IGListKit의 연동

Swift로 IGListKit을 사용하는 경우, IGListSectionMap은 IGListBindingSectionController를 통해 연동됩니다. 이를 통해 IGListBindingSectionController는 데이터 소스와 아이템에 대한 업데이트를 관리하고 IGListSectionMap에 반영합니다. IGListBindingSectionController는 IGListSectionType 프로토콜을 구현해야하며, IGListSectionMap은 이를 통해 섹션 매핑을 처리합니다.

### IGListBindingSectionController 예시

```swift
class MyBindingSectionController: IGListBindingSectionController<ListDiffable> {
    override init() {
        super.init()
        dataSource = self
        updater = self
    }
    
    // 섹션과 아이템의 유니크한 식별자를 반환하는 메소드
    override func sectionController(for object: Any) -> IGListSectionController? {
        // 섹션과 아이템에 따라 적절한 IGListSectionController를 반환한다.
    }
    
    // NSAttributedString을 반환하여 셀을 업데이트하는 메소드
    override func cellForItem(at index: Int) -> UICollectionViewCell {
        // 셀을 초기화하고 데이터를 바인딩하여 반환한다.
    }
    
    // IGListBindable 프로토콜을 구현한 뷰 모델을 반환하는 메소드
    override func viewModel(for item: Any) -> ListDiffable {
        // 해당 아이템에 대한 뷰 모델을 반환한다.
    }
    
    // IGListDiffable 프로토콜을 구현한 객체의 배열을 반환하는 메소드
    override func objects(for listAdapter: IGListAdapter) -> [ListDiffable] {
        // 데이터 소스에 대한 변경된 객체 배열을 반환한다.
    }
}
```

IGListBindingSectionController를 이용하면 UIView를 셀에 바인딩하거나 데이터를 업데이트하는데 매우 유용한 기능을 제공합니다. IGListBindingSectionController를 사용하면 IGListSectionMap에 대한 연동을 쉽게 설정할 수 있고, 데이터 소스의 변경에 따라 화면을 업데이트할 수 있습니다.

## 결론

IGListSectionMap는 IGListKit에서 데이터 소스와 셀 프로바이더의 연결을 관리하는 역할을 합니다. Swift에서 IGListKit을 사용할 때는 IGListSectionMap을 IGListBindingSectionController를 통해 연동할 수 있습니다. IGListBindingSectionController를 사용하면 IGListSectionMap에 대한 설정과 화면 업데이트를 간편하게 처리할 수 있습니다. IGListSectionMap은 IGListKit을 효율적으로 사용할 수 있도록 도와준다는 점에서 개발자에게 유용한 도구입니다.

참고 문서: [IGListSectionMap 공식 문서](https://instagram.github.io/IGListKit/api/7.0/CoreData/Classes/IGListSectionMap.html)