---
layout: post
title: "[swift] IGListBindingSectionController와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListBindingSectionController는 IGListKit의 컨트롤러 중 하나로, 데이터 바인딩 및 컨트롤러의 업데이트를 처리하는 기능을 제공합니다. 이 문서에서는 IGListBindingSectionController를 Swift IGListKit과 연동하는 방법에 대해 알아보겠습니다.

## IGListBindingSectionController 개요

IGListBindingSectionController는 IGListSectionController를 구현하는 클래스입니다. IGListBindingSectionController는 섹션 내의 객체를 표시하기 위해 사용되며, 섹션 컨트롤러에 객체를 바인딩하여 데이터 변경에 대한 업데이트를 처리할 수 있습니다.

섹션 컨트롤러에서 사용하는 데이터 객체는 IGListBindable 프로토콜을 채택해야 합니다. 이 프로토콜은 IGListBindingSectionController가 해당 객체의 업데이트를 처리할 수 있도록 필요한 메서드를 정의합니다.

## IGListBindingSectionController와 IGListKit의 연동

### 1. IGListKit 설치하기

Swift IGListKit을 사용하기 위해서는 먼저 프로젝트에 IGListKit을 설치해야 합니다. 이를 위해 CocoaPods를 사용할 수 있으며, Podfile에 다음과 같은 의존성을 추가합니다:

```ruby
pod 'IGListKit'
```

### 2. IGListBindingSectionController 구현하기

다음으로, IGListBindingSectionController를 구현해야 합니다. 이를 위해 다음 코드를 참고하여 섹션 컨트롤러를 작성합니다:

```swift
class MyBindingSectionController: IGListBindingSectionController<MyObject>, IGListBindingSectionControllerDataSource {

    override init() {
        super.init()
        dataSource = self
    }

    override func sizeForItem(at index: Int) -> CGSize {
        // 항목의 크기 반환
        return CGSize(width: 100, height: 100)
    }

    override func cellForItem(at index: Int) -> UICollectionViewCell {
        // 셀 반환
        guard let cell = collectionContext?.dequeueReusableCell(of: MyCell.self, for: self, at: index) as? MyCell else {
            fatalError()
        }
        
        return cell
    }

    // IGListBindingSectionControllerDataSource 메서드 구현
    func sectionController(_ sectionController: IGListBindingSectionController<Any>, viewModelsFor object: Any) -> [IGListDiffable] {
        // 바인딩할 뷰 모델을 생성하여 반환
        guard let object = object as? MyObject else { return [] }
        return [object]
    }

    func sectionController(_ sectionController: IGListBindingSectionController<Any>, didSelectItemAt index: Int, viewModel: Any) {
        // 항목 선택 시 동작 처리
    }
}
```

### 3. DataSource와 Delegate 설정하기

마지막으로, IGListBindingSectionController를 DataSource와 Delegate에 연결해야 합니다. IGListBindingSectionController를 사용하는 ViewController에서 다음과 같은 코드를 사용하여 연동합니다:

```swift
class MyViewController: UIViewController, ListAdapterDataSource {
    private var adapter: ListAdapter!

    override func viewDidLoad() {
        super.viewDidLoad()

        adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self)
        adapter.collectionView = collectionView
        adapter.dataSource = self
    }
    
    // ListAdapterDataSource 메서드 구현
    func objects(for listAdapter: ListAdapter) -> [ListDiffable] {
        // IGListBindable한 객체들로 구성된 배열을 반환
        return [...]
    }
    
    func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
        // 바인딩에 사용할 섹션 컨트롤러를 반환
        return MyBindingSectionController()
    }
    
    func emptyView(for listAdapter: ListAdapter) -> UIView? {
        // 리스트가 비어있을 때 표시할 뷰 반환
        return nil
    }
}
```

위의 코드에서 `collectionView`는 IGListKit의 컬렉션 뷰입니다. 이를 통해 섹션 컨트롤러와 바인딩된 객체들을 표시할 수 있습니다.

## 결론

이 문서에서는 IGListBindingSectionController와 Swift IGListKit의 연동 방법을 살펴보았습니다. IGListBindingSectionController를 사용하면 IGListKit을 통해 더 유연하고 강력한 데이터 바인딩을 구현할 수 있습니다.

더 자세한 내용은 IGListKit의 공식 문서를 참고하시기 바랍니다.

## 참고 자료

- [IGListKit 공식 문서](https://github.com/Instagram/IGListKit)