---
layout: post
title: "[swift] IGListDiffKit와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListDiffKit는 데이터 변경 사항을 감지하고 효율적으로 리스트를 업데이트하는 데 사용되는 도구입니다. Swift에서 IGListDiffKit와 IGListKit을 함께 사용하면 더욱 효율적이고 성능이 우수한 리스트 업데이트를 구현할 수 있습니다. 이번 글에서는 IGListKit을 Swift 앱에 통합하는 방법을 알아보겠습니다.

## IGListDiffKit 및 IGListKit 설치

먼저, IGListDiffKit와 IGListKit을 프로젝트에 설치해야 합니다. CocoaPods를 사용해 다음과 같이 Podfile에 추가합니다.

```ruby
pod 'IGListDiffKit'
pod 'IGListKit'
```

설치를 완료한 후, Xcode에서 프로젝트를 열고 `import IGListKit`을 추가합니다.

## IGListDiffable 프로토콜 준수

Swift에서 IGListKit을 사용하기 위해선 리스트 아이템이 `IGListDiffable` 프로토콜을 준수해야 합니다. 이 프로토콜은 항목이 다른 항목과 비교될 수 있도록 만들어주는 역할을 합니다.

```swift
class MyListItem: NSObject {
    let id: Int
    let name: String

    init(id: Int, name: String) {
        self.id = id
        self.name = name
    }
}

extension MyListItem: IGListDiffable {
    func isEqual(toDiffableObject object: IGListDiffable?) -> Bool {
        guard let object = object as? MyListItem else { return false }
        return id == object.id
    }

    func diffIdentifier() -> NSObjectProtocol {
        return id as NSObjectProtocol
    }
}
```

위의 예시에서는 `MyListItem`이라는 클래스가 `IGListDiffable` 프로토콜을 준수하도록 확장하였습니다. `isEqual(toDiffableObject:)` 메서드는 다른 객체와 비교할 때 사용되며, `diffIdentifier()` 메서드는 변경 사항을 추적하기 위한 식별자를 반환합니다.

## ListAdapter 생성 및 설정

다음으로, `ListAdapter`를 생성하고 데이터 소스를 설정해야 합니다. `ListAdapter`는 리스트를 관리하고 변경 사항을 추적하는 데 사용됩니다.

```swift
class MyViewController: UIViewController {
    let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self)
    let collectionView = UICollectionView(frame: .zero, collectionViewLayout: UICollectionViewFlowLayout())

    var data = [MyListItem]()

    override func viewDidLoad() {
        super.viewDidLoad()

        adapter.collectionView = collectionView
        adapter.dataSource = self
    }
}

extension MyViewController: ListAdapterDataSource {
    func objects(for listAdapter: ListAdapter) -> [ListDiffable] {
        return data
    }

    func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
        return MySectionController()
    }

    func emptyView(for listAdapter: ListAdapter) -> UIView? {
        return nil
    }
}
```

위의 예시에서는 `MyViewController`에서 `ListAdapter`를 생성하고, `UICollectionView`를 생성하여 데이터 소스를 설정하였습니다. `objects(for:)` 메서드는 리스트의 데이터를 반환하고, `listAdapter(_:sectionControllerFor:)` 메서드는 각 항목에 대한 `ListSectionController`를 반환합니다. `emptyView(for:)` 메서드는 리스트가 비어있을 때 표시될 뷰를 반환합니다.

## 섹션 컨트롤러 생성

마지막으로, `ListSectionController`를 생성하여 각 항목의 뷰를 설정해야 합니다.

```swift
class MySectionController: ListSectionController {
    var item: MyListItem?

    override func cellForItem(at index: Int) -> UICollectionViewCell {
        guard let item = item else { fatalError("Item not available") }

        let cell = collectionContext!.dequeueReusableCell(of: MyCell.self, for: self, at: index) as! MyCell
        cell.configure(with: item)
        return cell
    }

    override func sizeForItem(at index: Int) -> CGSize {
        guard let item = item else { fatalError("Item not available") }

        // 항목의 크기를 반환하는 로직 작성
        // ...

        return CGSize(width: collectionView.bounds.width, height: height)
    }

    override func didSelectItem(at index: Int) {
        // 항목 선택 시 동작 작성
        // ...
    }
}
```

위의 예시에서는 `MySectionController` 클래스를 생성하고, `cellForItem(at:)`, `sizeForItem(at:)`, `didSelectItem(at:)` 메서드를 구현합니다. 각 메서드는 해당 항목의 셀, 크기, 선택 동작을 정의합니다.

## 결론

이제 IGListDiffKit와 IGListKit을 Swift 앱에 통합하는 방법을 살펴보았습니다. IGListKit을 사용하면 데이터 변경 사항을 효율적으로 관리하고, IGListDiffKit을 사용하여 성능이 우수한 리스트 업데이트를 구현할 수 있습니다. IGListKit의 강력한 기능을 활용하여 좋은 사용자 경험을 제공할 수 있는 앱을 개발해보세요.

더 많은 자세한 내용은 [공식 IGListKit 문서](https://github.com/Instagram/IGListKit)를 참고하시기 바랍니다.