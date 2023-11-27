---
layout: post
title: "[swift] IGListWorkingRangeDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

이번 블로그에서는 IGListWorkingRangeDelegate와 Swift IGListKit을 어떻게 연동하는지에 대해 알아보겠습니다.

## IGListWorkingRangeDelegate

IGListWorkingRangeDelegate은 IGListKit에서 제공하는 프로토콜 중 하나입니다. 이 프로토콜을 사용하면 스크롤되는 동안 특정 셀 또는 뷰의 가시성 상태를 추적할 수 있습니다. 이를 통해 앱의 성능을 최적화하고, 사용자 경험을 향상시킬 수 있습니다.

## IGListWorkingRangeDelegate의 구현

1. 먼저, IGListWorkingRangeDelegate 프로토콜을 구현하기 위해 해당 뷰 컨트롤러에 다음 코드를 추가합니다.
```swift
class MyViewController: UIViewController, IGListWorkingRangeDelegate {
    // Your code here
}
```

2. IGListWorkingRangeDelegate 프로토콜의 메서드를 구현합니다.
```swift
func listAdapter(_ listAdapter: ListAdapter, sectionControllerWillEnterWorkingRange sectionController: ListSectionController) {
    // 특정 sectionController가 working range에 들어올 때 호출되는 메서드
}

func listAdapter(_ listAdapter: ListAdapter, sectionControllerDidExitWorkingRange sectionController: ListSectionController) {
    // 특정 sectionController가 working range에서 벗어날 때 호출되는 메서드
}
```

3. 이제 해당 뷰 컨트롤러에서 IGListAdapter에 IGListWorkingRangeDelegate를 할당합니다.
```swift
class MyViewController: UIViewController, IGListWorkingRangeDelegate {
    let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        adapter.collectionView = collectionView
        adapter.dataSource = self
        adapter.workingRangeDelegate = self
    }
    
    // Your code here
}
```

위의 코드에서 `collectionView`는 IGListKit에서 사용하는 UICollectionView입니다.

## 요약

IGListWorkingRangeDelegate를 사용하면 IGListKit에서 섹션 컨트롤러의 가시성 상태를 추적할 수 있습니다. 이를 통해 앱의 성능과 사용자 경험을 개선할 수 있습니다.

더 자세한 내용은 [IGListKit 공식 문서](https://github.com/Instagram/IGListKit)를 참조하십시오.