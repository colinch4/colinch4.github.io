---
layout: post
title: "[swift] IGListCollectionContext와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListCollectionContext는 IGListKit에서 사용되는 중요한 개념 중 하나입니다. IGListCollectionContext는 UICollectionView의 데이터 소스와 컬렉션 아이템을 관리하고 업데이트하는 데 사용됩니다. IGListKit의 Swift 버전에 대한 IGListCollectionContext와의 연동 방법을 알아보겠습니다.

## IGListCollectionContext란?

IGListCollectionContext는 IGListKit에서 주요한 역할을 담당하는 인터페이스입니다. 이 인터페이스는 UICollectionView의 데이터 소스 및 레이아웃을 관리하고 업데이트하는 기능을 제공합니다. IGListCollectionContext를 사용하면 즉시 데이터 변경을 반영할 수 있으며, 성능을 향상시키고 복잡한 레이아웃을 쉽게 처리할 수 있습니다.

## IGListCollectionContext와 IGListKit의 연동

IGListCollectionContext와 Swift IGListKit를 연동하기 위해서는 다음 단계를 따라야 합니다.

1. IGListCollectionContext protocol을 채택하도록 클래스에서 확장
2. 컬렉션 아이템을 표시할 셀 클래스를 생성
3. IGListAdapter 객체 생성 후 IGListAdapterDataSource를 구현
4. IGListAdapter에 IGListCollectionContext 할당 및 갱신 로직 구현

다음은 간단한 예제 코드입니다.

```swift
import IGListKit

class MyViewController: UIViewController, IGListCollectionContext {

    var collectionView: UICollectionView?
    var items: [Any] = []

    override func viewDidLoad() {
        super.viewDidLoad()

        // 컬렉션 뷰 생성 및 설정
        let layout = UICollectionViewFlowLayout()
        collectionView = UICollectionView(frame: .zero, collectionViewLayout: layout)
        collectionView?.backgroundColor = .white

        // IGListCollectionContext 설정
        collectionView?.delegate = self
        collectionView?.dataSource = self

        // IGListAdapter 객체 생성
        let adapter = IGListAdapter(updater: IGListAdapterUpdater(), viewController: self, workingRangeSize: 0)

        // IGListCollectionContext 할당 및 갱신 로직 구현
        adapter.collectionView = collectionView
        adapter.dataSource = self
        
        // ...
    }

    // IGListCollectionContext 프로토콜 구현
    func reloadData(completion: ((Bool) -> Void)?) {
        collectionView?.reloadData()
        completion?(true)
    }

    func reloadSections(sections: [Int], completion: ((Bool) -> Void)?) {
        collectionView?.reloadSections(IndexSet(sections))
        completion?(true)
    }

    // ...
}

// IGListAdapterDataSource 프로토콜 구현
extension MyViewController: IGListAdapterDataSource {

    func objects(for listAdapter: IGListAdapter) -> [IGListDiffable] {
        return items as? [IGListDiffable] ?? []
    }

    func listAdapter(_ listAdapter: IGListAdapter, sectionControllerFor object: Any) -> IGListSectionController {
        // IGListSectionController 객체 생성 및 반환
        return MySectionController()
    }

    func emptyView(for listAdapter: IGListAdapter) -> UIView? {
        return nil
    }
}

// IGListSectionController 프로토콜 구현
class MySectionController: IGListSectionController {

    var object: Any?

    override init() {
        super.init()
        // ...  
    }

    // IGListSectionController 프로토콜 메소드 구현
    override func numberOfItems() -> Int {
        // ...
    }

    override func cellForItem(at index: Int) -> UICollectionViewCell {
        // ...
    }

    override func sizeForItem(at index: Int) -> CGSize {
        // ...
    }

    override func didUpdate(to object: Any) {
        self.object = object
        // ...
    }
}
```

위의 코드는 IGListCollectionContext와 Swift IGListKit를 연동하는 간단한 예제입니다. IGListCollectionContext를 구현하는 View Controller에서 UICollectionView를 생성하고 IGListAdapter를 생성한 후, IGListAdapterDataSource를 통해 데이터 및 섹션 컨트롤러를 제공합니다. 

IGListAdapter의 collectionView와 dataSource 프로퍼티를 설정해주고, IGListCollectionContext의 메소드를 구현하여 데이터 변경시 collectionView를 갱신하도록 합니다.

이제 IGListCollectionContext를 사용하여 IGListKit의 강력한 기능을 Swift에서도 사용할 수 있습니다.

## 참고 자료
- [IGListKit GitHub Repository](https://github.com/Instagram/IGListKit)
- [IGListCollectionContext Documentation](https://github.com/Instagram/IGListKit/blob/master/Source/Common/IGListCollectionContext.h)