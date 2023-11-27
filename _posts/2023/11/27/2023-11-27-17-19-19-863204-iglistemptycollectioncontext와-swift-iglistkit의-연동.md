---
layout: post
title: "[swift] IGListEmptyCollectionContext와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListKit은 iOS 앱에서 목록 기반의 사용자 인터페이스를 구현하기 위한 강력한 프레임워크입니다. IGListEmptyCollectionContext는 IGListKit의 일부로서, 빈 목록 상태에서 보여줄 컨텐츠를 제어하는 데 사용됩니다. 이번 글에서는 IGListEmptyCollectionContext와 Swift IGListKit의 연동에 대해 알아보겠습니다.

## IGListEmptyCollectionContext란?

IGListEmptyCollectionContext는 빈 목록(CollectionView) 상태에서 사용자에게 보여줄 컨텐츠를 관리하는 데 사용됩니다. 이는 목록에 데이터가 없는 경우에 사용자에게 적합한 메시지, 이미지, 애니메이션 등을 보여줄 수 있는 기능을 제공합니다.

## IGListEmptyCollectionContext와 연동하기

IGListKit는 IGListCollectionViewDelegateEmptyState 프로토콜을 통해 IGListEmptyCollectionContext를 사용할 수 있습니다. 이를 위해서는 다음 단계를 따라야 합니다.

### 단계 1: 프로토콜 구현

```swift
class MyListViewController: UIViewController, IGListCollectionViewDelegateEmptyState {
    // ...
}
```

### 단계 2: Empty Collection Context 생성

```swift
let emptyCollectionContext = IGListEmptyCollectionContext(delegate: self)
```

### 단계 3: Empty Collection Delegate 메서드 구현

```swift
func emptyView(for listAdapter: ListAdapter) -> UIView? {
    // 빈 컬렉션 상태에서 보여줄 뷰 반환
    return MyEmptyView()
}
```

위의 코드에서 `MyEmptyView`는 빈 컬렉션 상태에서 보여줄 사용자 정의 뷰를 나타냅니다. 이 뷰는 빈 컬렉션 컨텍스트에 의해 자동적으로 표시되며, 애니메이션 효과를 추가할 수도 있습니다.

### 단계 4: ListAdapter에 Empty Collection Context 설정

```swift
let listAdapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self, workingRangeSize: 0)
listAdapter.collectionViewDelegate = self
listAdapter.emptyCollectionContext = emptyCollectionContext
listAdapter.collectionView = collectionView
```

위의 코드에서 `listAdapter`는 IGListKit의 핵심 클래스인 ListAdapter를 초기화하는 과정을 나타냅니다. `emptyCollectionContext`를 `listAdapter`의 `emptyCollectionContext` 속성에 설정하여 빈 컬렉션 컨텍스트를 연동합니다. 또한, `collectionViewDelegate` 속성도 현재 뷰 컨트롤러 자체로 설정해야 합니다.

## 정리

이제 IGListEmptyCollectionContext와 Swift IGListKit를 연동하는 방법을 배웠습니다. 이를 통해 앱에서 빈 목록 상태에서 적절한 피드백을 사용자에게 제공할 수 있게 되었습니다. IGListEmptyCollectionContext의 다양한 기능을 활용하여 사용자 경험을 향상시킬 수 있습니다.

참고 자료:
- [IGListKit GitHub 리포지토리](https://github.com/Instagram/IGListKit)
- [IGListEmptyCollectionContext 문서](https://instagram.github.io/IGListKit/Classes/IGListEmptyCollectionContext.html)