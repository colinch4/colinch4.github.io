---
layout: post
title: "[swift] IGListSingleSectionController와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 소개

IGListSingleSectionController는 IGListKit의 핵심 컴포넌트 중 하나로, 단일 섹션 데이터를 처리하고 표시하는 데 사용됩니다. 이 게시물에서는 IGListSingleSectionController를 Swift IGListKit와 연동하는 방법을 알아보겠습니다.

## IGListSingleSectionController 시작하기

IGListSingleSectionController는 IGListSectionController를 상속하여 사용할 수 있습니다.

```swift
class MySingleSectionController: ListSectionController {
    var data: MyDataModel?
    
    override func numberOfItems() -> Int {
        return 1
    }
    
    override func cellForItem(at index: Int) -> UICollectionViewCell {
        guard let cell = collectionContext?.dequeueReusableCell(of: MyCell.self, for: self, at: index) as? MyCell else {
            fatalError("Unable to dequeue cell")
        }
        cell.configure(with: data)
        return cell
    }
    
    override func sizeForItem(at index: Int) -> CGSize {
        guard let context = collectionContext, let data = data else {
            return .zero
        }
        return CGSize(width: context.containerSize.width, height: data.cellHeight)
    }
    
    override func didUpdate(to object: Any) {
        data = object as? MyDataModel
    }
}
```

위의 예시에서 MySingleSectionController는 ListSectionController를 상속하고 있습니다. 이 클래스에서는 데이터를 처리하고, 셀을 생성하고, 셀 크기를 계산하며, 데이터 업데이트를 처리합니다. 

## IGListSingleSectionController 연동하기

IGListSingleSectionController를 사용하기 위해선 ListAdapter에 등록해주어야 합니다. 

```swift
let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self)
adapter.collectionView = collectionView
adapter.dataSource = self
```

또한 `ListAdapterDataSource` 프로토콜을 채택하여 IGListSingleSectionController를 제공해야 합니다.

```swift
extension ViewController: ListAdapterDataSource {
    func objects(for listAdapter: ListAdapter) -> [ListDiffable] {
        return [myDataModel]
    }
    
    func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
        return MySingleSectionController()
    }
    
    func emptyView(for listAdapter: ListAdapter) -> UIView? {
        return nil
    }
}
```

위의 예시에서 objects(for:) 함수는 섹션별 데이터 배열을 반환하고, listAdapter(_:sectionControllerFor:) 함수에서 IGListSingleSectionController를 생성하여 반환합니다.

## 결론

IGListSingleSectionController는 IGListKit의 강력한 기능 중 하나로, 단일 섹션 데이터를 처리하고 표시하는 데 유용합니다. 이번 게시물에서는 IGListSingleSectionController와 Swift IGListKit의 연동 방법을 알아보았습니다. 자세한 내용은 IGListKit 공식 문서를 참조하시기 바랍니다.

---

참고 자료:
- [IGListKit GitHub Repository](https://github.com/Instagram/IGListKit)
- [IGListKit Documentation](https://instagram.github.io/IGListKit/)
- [Raywenderlich Tutorial on IGListKit](https://www.raywenderlich.com/5195-iglistkit-tutorial-better-uicollectionviews)