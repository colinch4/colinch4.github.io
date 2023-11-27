---
layout: post
title: "[swift] IGListSectionController와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListKit은 iOS 개발자들에게 새로운 방식의 컬렉션 뷰 관리를 제공합니다. IGListKit은 IGListSectionController라는 개념을 도입하여 복잡한 컬렉션 뷰 로직을 단순화하고 유지보수성을 향상시킬 수 있습니다. Swift 프로젝트에서 IGListKit을 사용할 때는 IGListSectionController와의 연동이 중요한 부분입니다. 이 글에서는 IGListSectionController와 Swift IGListKit의 연동 방법에 대해 알아보겠습니다.

## IGListSectionController란 무엇인가요?

IGListSectionController는 IGListKit에서 컬렉션 뷰의 섹션을 관리하는 데 사용되는 객체입니다. 각각의 섹션은 하나의 IGListSectionController에 의해 관리되며, 이를 통해 섹션에 대한 데이터 제공, 레이아웃 정의, 및 셀 구성을 담당할 수 있습니다. IGListSectionController는 뷰 컨트롤러이므로, UIViewController를 상속받아 사용할 수도 있습니다.

## IGListKit과의 연동 방법

1. IGListSectionController를 선언하고 데이터 소스를 구현합니다.

```swift
class MySectionController: NSObject, ListSectionController {
    var data: [String] = []

    func numberOfItems() -> Int {
        return data.count
    }

    func cellForItem(at index: Int) -> UICollectionViewCell {
        // 셀 구성 및 반환
        let cell = collectionContext!.dequeueReusableCell(of: MyCell.self, for: self, at: index) as! MyCell
        cell.textLabel.text = data[index]
        return cell
    }

    func didUpdate(to object: Any) {
        // 데이터 업데이트
        guard let data = object as? [String] else { return }
        self.data = data
    }
}
```

2. IGListAdapter를 생성하고 데이터를 연결합니다.

```swift
class ViewController: UIViewController, ListAdapterDataSource {
    var adapter: ListAdapter!

    override func viewDidLoad() {
        super.viewDidLoad()

        let collectionView = UICollectionView(frame: CGRect.zero, collectionViewLayout: UICollectionViewFlowLayout())
        view.addSubview(collectionView)
        
        adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self, workingRangeSize: 0)
        adapter.collectionView = collectionView
        adapter.dataSource = self

        fetchData()
    }

    func fetchData() {
        // 데이터 가져오기 및 adapter에 연결
        let data = ["Item 1", "Item 2", "Item 3"]
        adapter.performUpdates(animated: true, completion: nil)
    }

    // MARK: ListAdapterDataSource

    func objects(for listAdapter: ListAdapter) -> [ListDiffable] {
        // IGListSectionController에 전달할 데이터 반환
        return [data]
    }

    func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
        // IGListSectionController 인스턴스 생성
        return MySectionController()
    }

    func emptyView(for listAdapter: ListAdapter) -> UIView? {
        return nil
    }
}
```

IGListSectionController와 Swift IGListKit을 연동하여 컬렉션 뷰 섹션을 관리하는 간단한 예제를 살펴보았습니다. IGListSectionController를 구현하고 필요에 따라 데이터 연결을 처리하는 것으로 IGListKit의 강력한 기능을 활용할 수 있습니다.

더 자세한 내용은 IGListKit 공식 문서를 참조하시기 바랍니다. [[1]](#reference)

## 참고 자료
[1] IGListKit 문서 - [https://instagram.github.io/IGListKit/](https://instagram.github.io/IGListKit/)