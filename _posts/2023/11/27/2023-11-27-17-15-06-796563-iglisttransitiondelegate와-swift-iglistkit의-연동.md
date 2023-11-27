---
layout: post
title: "[swift] IGListTransitionDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListKit는 많은 iOS 애플리케이션에서 사용되는 강력한 라이브러리로, UICollectionView의 데이터 관리 및 레이아웃 업데이트를 단순화합니다. IGListKit는 IGListAdapter를 통해 해당 데이터 관리를 처리하고, Swift에서도 사용할 수 있습니다. IGListKit을 사용하면 데이터 모델이 변경될 때 애니메이션 효과로 UICollectionView를 업데이트할 수 있습니다.

그러나 IGListKit은 UICollectionView의 전환 효과를 제어하는 데 있어 조금 힘들 수 있습니다. IGListTransitionDelegate를 사용하면 UICollectionView의 전환 효과를 더욱 쉽게 커스터마이징할 수 있습니다.

## IGListTransitionDelegate 설정

첫 번째로, IGListKit과 IGListTransitionDelegate를 함께 사용하려면 아래와 같이 IGListAdapter를 초기화 할 때 `transitionDelegate`를 설정해주어야 합니다.

```swift
let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self, workingRangeSize: 0)
adapter.dataSource = self
adapter.collectionViewDelegate = self
adapter.transitionDelegate = self
```

## IGListTransitionDelegate 구현

IGListTransitionDelegate를 구현하기 위해서는 `IGListTransitionDelegate` 프로토콜을 채택하고, 다음과 같은 3가지 메서드를 구현해야 합니다.

### 1. `listAdapter(_:willDisplay:for:cell:at:)`

해당 메서드는 셀이 표시되기 이전에 호출되는 메서드입니다. 여기서 `transition(from:to:container:completion:)` 메서드를 사용하여 전환 효과를 적용할 수 있습니다.

```swift
func listAdapter(_ listAdapter: ListAdapter, willDisplay sectionController: ListSectionController, for object: Any, cell: UICollectionViewCell, at index: Int) {
    let fromViews = [cell.contentView]
    let toViews = [cell.contentView]
    
    adapter.transition(from: fromViews, to: toViews, container: cell.contentView) { (completed) in
        // 전환 완료 시 실행될 코드
    }
}
```

### 2. `listAdapter(_:didEndDisplaying:for:cell:at:)`

해당 메서드는 셀의 표시가 종료된 후 호출되는 메서드입니다. 여기에서 전환 효과를 제거할 수 있습니다.

```swift
func listAdapter(_ listAdapter: ListAdapter, didEndDisplaying sectionController: ListSectionController, for object: Any, cell: UICollectionViewCell, at index: Int) {
    adapter.removeTransition(for: cell.contentView)
}
```

### 3. `listAdapter(_:transitionBehaviorFor:at:in:on:)`

해당 메서드는 전환 동작 및 속성을 반환하는 메서드입니다. 기본적으로는 `.automatic` 동작을 반환하도록 구현되어 있으며, 필요에 따라 커스터마이즈할 수 있습니다.

```swift
func listAdapter(_ listAdapter: ListAdapter, transitionBehaviorFor sectionController: ListSectionController, at index: Int, in controller: UIViewController) -> ListSectionControllerInteractiveTransitionBehavior {
    return .automatic
}
```

## 예제

다음은 IGListTransitionDelegate를 사용하여 UICollectionView의 전환 효과를 컨트롤하는 예제입니다.

```swift
import IGListKit

class MyViewController: UIViewController, ListAdapterDataSource, ListAdapterDelegate, IGListTransitionDelegate {
    
    private let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self, workingRangeSize: 0)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        adapter.dataSource = self
        adapter.collectionViewDelegate = self
        adapter.transitionDelegate = self
        
        // ...
    }
    
    // ...
    
    // IGListTransitionDelegate 구현
    
    func listAdapter(_ listAdapter: ListAdapter, willDisplay sectionController: ListSectionController, for object: Any, cell: UICollectionViewCell, at index: Int) {
        let fromViews = [cell.contentView]
        let toViews = [cell.contentView]
        
        adapter.transition(from: fromViews, to: toViews, container: cell.contentView) { (completed) in
            // 전환 완료 시 실행될 코드
        }
    }
    
    func listAdapter(_ listAdapter: ListAdapter, didEndDisplaying sectionController: ListSectionController, for object: Any, cell: UICollectionViewCell, at index: Int) {
        adapter.removeTransition(for: cell.contentView)
    }
    
    func listAdapter(_ listAdapter: ListAdapter, transitionBehaviorFor sectionController: ListSectionController, at index: Int, in controller: UIViewController) -> ListSectionControllerInteractiveTransitionBehavior {
        return .automatic
    }
    
    // ...
    
}
```

IGListTransitionDelegate를 사용하면 IGListKit을 더욱 유연하게 사용할 수 있으며, UICollectionView의 전환 효과를 조정할 수 있습니다. IGListKit 공식 문서에서 자세한 내용을 확인할 수 있습니다.

참고:
- [IGListKit GitHub Repository](https://github.com/Instagram/IGListKit)
- [IGListKit Documentation](https://instagram.github.io/IGListKit/)