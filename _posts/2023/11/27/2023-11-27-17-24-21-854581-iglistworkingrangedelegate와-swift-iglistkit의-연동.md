---
layout: post
title: "[swift] IGListWorkingRangeDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

Swift에서 IGListWorkingRangeDelegate를 사용하기 위해 몇 가지 단계를 따라야 합니다. 먼저, IGListWorkingRangeDelegate를 구현하는 클래스를 생성해야 합니다. 이 클래스는 UICollectionViewDelegate와 함께 사용됩니다.

```swift
class MyWorkingRangeDelegate: NSObject, UICollectionViewDelegate, IGListWorkingRangeDelegate {
    func listAdapter(_ listAdapter: IGListAdapter!, sectionControllerWillEnterWorkingRange sectionController: IGListSectionController!) {
        // 셀이 작동 범위에 들어올 때 호출되는 콜백 메서드
        // 원하는 작업을 수행
    }
    
    func listAdapter(_ listAdapter: IGListAdapter!, sectionControllerDidExitWorkingRange sectionController: IGListSectionController!) {
        // 셀이 작동 범위를 벗어날 때 호출되는 콜백 메서드
        // 원하는 작업을 수행
    }
}
```

다음으로, IGListAdapter 인스턴스를 생성하고 IGListAdapterUpdater 인스턴스와 함께 사용하여 작동 범위 델리게이트를 설정해야 합니다.

```swift
let updater = IGListAdapterUpdater()
let adapter = IGListAdapter(updater: updater, viewController: self, workingRangeDelegate: MyWorkingRangeDelegate())
adapter.collectionView = collectionView
adapter.dataSource = self
```

마지막으로, 작동 범위 델리게이트를 사용할 IGListSectionController의 cellForItem 메서드를 업데이트해야 합니다. 이 작업은 해당 섹션 컨트롤러의 cellForItem 메서드에서 작동 범위 델리게이트를 설정하는 것으로 이루어집니다.

```swift
override func cellForItem(at index: Int) -> UICollectionViewCell {
    let cell = collectionContext!.dequeueReusableCell(withNibName: "MyCell", bundle: nil, for: self, at: index) as! MyCell
    // 셀 설정
    cell.workingRangeDelegate = workingRangeDelegate
    return cell
}
```

위의 단계를 따라 IGListWorkingRangeDelegate를 Swift IGListKit에 연동할 수 있습니다. 이를 통해 작동 범위에 해당하는 셀에 대한 액션을 수행할 수 있습니다.

참고 자료: 
- [IGListWorkingRangeDelegate 문서](https://github.com/Instagram/IGListKit/blob/main/Source/Common/IGListWorkingRangeDelegate.h)
- [IGListKit GitHub 리포지토리](https://github.com/Instagram/IGListKit)