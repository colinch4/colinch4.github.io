---
layout: post
title: "[swift] IGListBindingSectionControllerDataSource와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 소개
`IGListBindingSectionControllerDataSource`는 IGListKit의 핵심 요소 중 하나입니다. 이는 `IGListBindingSectionController`와 데이터 소스를 관리하는 데 사용됩니다. 

Swift에서 IGListKit를 사용할 때, `IGListBindingSectionControllerDataSource`를 연동하는 방법에 대해 알아보겠습니다.

## IGListBindingSectionControllerDataSource 구현하기
`IGListBindingSectionControllerDataSource`를 구현하기 위해서는 다음 세 가지 메서드를 구현해야 합니다.

### `sectionController(_:viewModelsFor:)`
이 메서드는 `IGListBindingSectionController`가 관리하는 아이템의 뷰 모델 배열을 반환합니다. 

```swift
func sectionController(_ sectionController: ListBindingSectionController<ListDiffable>, viewModelsFor object: Any) -> [ListDiffable] {
    // object를 기반으로 뷰 모델 배열을 생성하여 반환합니다.
    // 예: object에서 필요한 데이터를 추출하거나 계산하여 뷰 모델 배열을 생성합니다.
    return viewModels
}
```

### `sectionController(_:didUpdate:)`
이 메서드는 `IGListBindingSectionController`가 뷰 컨트롤러의 뷰를 업데이트하는 데 사용됩니다. 

```swift
func sectionController(_ sectionController: ListBindingSectionController<ListDiffable>, didUpdateViewModels viewModels: [ListDiffable]) {
    // 뷰 모델 배열이 업데이트되었을 때 실행되는 코드를 여기에 작성합니다.
    // 예: 뷰 컨트롤러의 뷰를 업데이트하는 로직을 작성합니다.
}
```

### `sectionController(_:didSelect:)`
이 메서드는 `IGListBindingSectionController`의 아이템이 선택되었을 때 실행됩니다.

```swift
func sectionController(_ sectionController: ListBindingSectionController<ListDiffable>, didSelectItemAt index: Int, viewModel: Any) {
    // 아이템이 선택되었을 때 실행되는 코드를 여기에 작성합니다.
    // 예: 선택한 아이템에 대한 작업을 수행합니다.
}
```

## 연동하기
`IGListBindingSectionControllerDataSource`를 연동하려면 다음 단계를 따르세요.

1. `IGListBindingSectionControllerDataSource` 프로토콜을 채택합니다.

```swift
class MySectionController: ListBindingSectionController<MyViewModel>, IGListBindingSectionControllerDataSource {
    // ...
}
```

2. `IGListBindingSectionController` 인스턴스를 생성합니다.

```swift
let sectionController = MySectionController()
```

3. `IGListBindingSectionController` 인스턴스에 `dataSource`를 설정합니다.

```swift
sectionController.dataSource = self
```

4. `IGListAdapter`의 `moduleAdapter`에 `IGListBindingSectionController` 인스턴스를 추가합니다.

```swift
adapter.collectionViewUpdater = ListCollectionViewUpdater()
adapter.dataSource = self
adapter.collectionView = collectionView

let sectionController = MySectionController()
adapter.collectionViewDelegate = sectionController
adapter.moduleAdapter = ListAdapterUpdater()

adapter.moduleAdapter?.add(sectionController)
```

## 결론
이제 Swift에서 IGListKit을 사용할 때, `IGListBindingSectionControllerDataSource`를 연동하는 방법을 알게 되었습니다. 이를 활용하여 IGListKit를 보다 효과적으로 사용할 수 있습니다.

## 참고 자료
- [IGListKit Documentation](https://github.com/Instagram/IGListKit)
- [IGListBindingSectionControllerDataSource Protocol Reference](https://instagram.github.io/IGListKit/Protocols/IGListBindingSectionControllerDataSource.html)