---
layout: post
title: "[swift] IGListUpdatingDelegateConformance와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListKit은 iOS 애플리케이션에서 복잡한 목록 화면을 구현하기 위한 강력한 도구입니다. IGListKit을 사용하여 목록을 업데이트하고 뷰를 자동으로 업데이트하는 데 사용되는 델리게이트 프로토콜 중 하나인 `IGListUpdatingDelegate`를 살펴보겠습니다.

## IGListUpdatingDelegate 프로토콜

`IGListUpdatingDelegate` 프로토콜은 `UICollectionView`와 함께 사용되어 목록을 업데이트하고 뷰를 업데이트하는 데 필요한 메소드를 정의합니다. IGListKit에는 `IGListAdapter` 클래스가 있으며, 이들 메소드는 대부분 `IGListAdapter`에 의해 구현됩니다.

중요한 `IGListUpdatingDelegate` 메소드 몇 가지는 다음과 같습니다.

### `- (void)listAdapter:(IGListAdapter *)listAdapter didApplySectionChanges:(NSArray<id<IGListSectionController>> *)sectionControllers`
> 이 메소드는 섹션 컨트롤러 내에서 발생한 변경 내용이 애니메이션과 함께 적용된 후 호출됩니다. 

### `- (void)listAdapter:(IGListAdapter *)listAdapter willUpdateObjects:(NSArray *)objects`
> 이 메소드는 섹션 컨트롤러의 데이터 소스가 변경되기 전에 호출됩니다. 이 메소드를 사용하여 섹션 컨트롤러의 데이터 소스를 준비하거나, 다른 작업을 수행할 수 있습니다.

### `- (void)listAdapter:(IGListAdapter *)listAdapter didUpdateObjects:(NSArray *)objects`
> 이 메소드는 섹션 컨트롤러의 데이터 소스가 변경된 후 호출됩니다. 이 메소드를 사용하여 데이터 소스 변경 후 추가 작업을 수행할 수 있습니다.

## IGListUpdatingDelegate와 IGListAdapter의 연동

`IGListAdapter`는 IGListKit과 함께 사용되는 주요 클래스입니다. `IGListAdapter`는 `UICollectionView`와 데이터 소스를 관리하면서 `IGListUpdatingDelegate`를 구현하여 목록 업데이트를 처리합니다.

```swift
class MyListAdapter: NSObject, IGListAdapterDataSource, IGListUpdatingDelegate {
    // ...

    func objects(for listAdapter: IGListAdapter) -> [IGListDiffable] {
        // 데이터 소스를 반환하는 로직 구현
        return // 반환할 데이터 소스
    }

    // ...

    func listAdapter(_ listAdapter: IGListAdapter, willUpdateObjects objects: [Any]) {
        // 객체 업데이트 이전에 필요한 작업 수행
    }

    func listAdapter(_ listAdapter: IGListAdapter, didUpdateObjects objects: [Any]) {
        // 객체 업데이트 이후에 추가 작업 수행
    }
}
```

위의 예제에서는 `MyListAdapter` 클래스가 `IGListAdapterDataSource`와 `IGListUpdatingDelegate` 프로토콜을 구현하고 있습니다. `objects(for:)` 메소드를 구현하여 데이터 소스를 반환하고, `willUpdateObjects(_:)`와 `didUpdateObjects(_:)` 메소드에서 업데이트 이전과 이후에 수행할 작업을 처리합니다.

## 참고 자료

- [IGListUpdatingDelegate Documentation](https://instagram.github.io/IGListKit/Protocols/IGListUpdatingDelegate.html)
- [IGListAdapter Documentation](https://instagram.github.io/IGListKit/Classes/IGListAdapter.html)
- [IGListKit Github Repository](https://github.com/instagram/IGListKit)