---
layout: post
title: "[swift] IGListWorkingRangeDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 소개
Swift IGListKit는 iOS 앱에서 복잡한 목록을 처리하기위한 강력한 도구입니다. IGListWorkingRangeDelegate는 IGListKit에서 제공하는 옵션 중 하나로, 스크롤 작업을 보다 효과적으로 처리하는 데 도움을 줍니다. 이번 게시물에서는 IGListWorkingRangeDelegate와 Swift IGListKit의 연동 방법을 알아보겠습니다.

## IGListWorkingRangeDelegate란?
IGListWorkingRangeDelegate는 IGListKit에서 스크롤 작업의 효율성을 향상시키기 위해 도입된 인터페이스입니다. 이를 사용하면 셀이 나타나고 사라질 때마다 작업을 수행할 수 있습니다. 작업 범위 내에 들어오는 셀에 대해 추가 작업을 수행할 수 있으며, 작업 범위를 벗어나는 셀에 대해서는 필요한 작업을 수행할 수 있습니다.

## IGListWorkingRangeDelegate 적용하기
IGListWorkingRangeDelegate를 사용하기 위해서는 다음의 단계를 따라야 합니다.

### 1. Working Range Delegate 구현
먼저, 스크롤 작업을 처리할 Working Range Delegate를 구현해야 합니다. 다음과 같이 작성합니다:

```swift
class MyWorkingRangeDelegate: NSObject, IGListWorkingRangeDelegate {
    func listAdapter(_ listAdapter: IGListAdapter, sectionControllerWillEnterWorkingRange sectionController: IGListSectionController) {
        // 작업 범위에 셀이 나타날 때 수행할 작업을 구현합니다.
    }
    
    func listAdapter(_ listAdapter: IGListAdapter, sectionControllerDidExitWorkingRange sectionController: IGListSectionController) {
        // 작업 범위를 벗어나는 셀에 대해 수행할 작업을 구현합니다.
    }
}
```

### 2. List Adapter에 Working Range Delegate 할당
다음으로, IGListAdapter에 앞서 작성한 Working Range Delegate를 할당해야 합니다. 다음과 같이 작성합니다:

```swift
let adapter = IGListAdapter(updater: IGListAdapterUpdater(), viewController: self, workingRangeDelegate: MyWorkingRangeDelegate(), objectTransitionBlock: nil, isEqualBlock: nil)
```

### 3. 작업 범위 활성화
마지막으로, 작업 범위를 활성화해야 합니다. 다음과 같이 작성합니다:

```swift
adapter.collectionView = collectionView
adapter.dataSource = self
adapter.willDisplayHandler = { (cell, _, _, _) in
    // 셀이 화면에 표시될 때마다 수행할 작업을 구현합니다.
}
```

## 결론
IGListWorkingRangeDelegate는 IGListKit의 강력한 기능 중 하나로, 스크롤 작업을 더 효율적으로 처리할 수 있도록 도와줍니다. 이번 게시물에서는 IGListWorkingRangeDelegate와 Swift IGListKit의 연동 방법을 알아보았습니다. IGListWorkingRangeDelegate를 사용하여 앱의 목록을 더욱 원활하게 처리할 수 있습니다.

## 참고 자료
- [IGListKit 공식 문서](https://instagram.github.io/IGListKit/)
- [IGListWorkingRangeDelegate 문서](https://instagram.github.io/IGListKit/Protocols/IGListWorkingRangeDelegate.html)