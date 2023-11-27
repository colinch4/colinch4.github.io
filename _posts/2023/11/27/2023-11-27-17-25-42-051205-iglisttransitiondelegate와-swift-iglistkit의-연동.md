---
layout: post
title: "[swift] IGListTransitionDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

Swift IGListKit은 UICollectionView를 사용하여 복잡한 데이터 표시와 상호작용을 위한 강력한 도구입니다. IGListKit은 데이터의 변경을 추적하고 화면에 반영하는 데 효율적입니다. IGListTransitionDelegate는 IGListKit의 기능을 확장하여 콘텐츠 전환과 애니메이션에 대한 세밀한 제어를 제공합니다.

### IGListTransitionDelegate 이해하기

IGListTransitionDelegate는 IGListKit에서 제공하는 프로토콜로, 컨트롤러 간의 콘텐츠 전환 및 애니메이션을 처리하는 데 사용됩니다. IGListTransitionDelegate를 구현하면 뷰 컨트롤러 간의 콘텐츠 전환을 자유롭게 제어할 수 있습니다. 

### IGListTransitionDelegate를 Swift IGListKit에 연동하기

Swift IGListKit에서 IGListTransitionDelegate를 사용하려면 몇 가지 단계를 거쳐야 합니다.

1. IGListKit과 IGListTransitionDelegate를 프로젝트에 추가합니다. Cocoapods를 사용한다면 `pod 'IGListKit'`과 `pod 'IGListTransitionDelegate'`를 Podfile에 추가합니다.

2. IGListSectionController에 애니메이션을 구현하기 위해 IGListTransitionDelegate 프로토콜을 준수하는 클래스를 생성합니다.

```swift
class MyListSectionController: ListSectionController, IGListTransitionDelegate {
    
    // IGListTransitionDelegate 프로토콜 구현
    func sectionController(
        _ sectionController: ListSectionController,
        shouldTransitionFrom oldObject: Any,
        to newObject: Any,
        atIndex index: Int
    ) -> Bool {
        // 데이터의 변경 여부에 따라 전환 여부를 결정할 수 있는 로직 구현
        let oldData = oldObject as! MyDataModel
        let newData = newObject as! MyDataModel
        return oldData.shouldAnimateTransition(to: newData)
    }
    
    func sectionController(
        _ sectionController: ListSectionController,
        animationControllerForObject object: Any
    ) -> ListSectionControllerAnimatedTransitioning? {
        // 애니메이션 컨트롤러를 반환할 수 있는 메서드 구현
        let animationController = MyListAnimatingTransitionController()
        return animationController
    }
    
    // ...
}
```

3. 애니메이션 컨트롤러를 구현하기 위해 `ListSectionControllerAnimatedTransitioning` 프로토콜을 준수하는 클래스를 생성합니다.

```swift
class MyListAnimatingTransitionController: NSObject, ListSectionControllerAnimatedTransitioning {
    
    // ListSectionControllerAnimatedTransitioning 프로토콜 구현
    func transitionDuration(
        _ controller: ListSectionController,
        from oldObject: Any?,
        to newObject: Any?
    ) -> TimeInterval {
        // 전환 애니메이션의 시간을 반환
        return 0.3
    }
    
    func animate(
        _ controller: ListSectionController,
        from oldObject: Any?,
        to newObject: Any?,
        completionHandler: @escaping (Bool) -> Void
    ) {
        // 전환 애니메이션을 구현
        UIView.animate(withDuration: 0.3) {
            // 애니메이션 코드 구현
        } completion: { finished in
            completionHandler(finished)
        }
    }
    
    // ...
}
```

4. 이제, `MyListSectionController`를 IGListKit 데이터 소스에 추가하고 이를 사용하여 UICollectionView를 구성합니다.

### 결론

IGListTransitionDelegate를 사용하여 Swift IGListKit에서 콘텐츠 전환과 애니메이션을 제어할 수 있습니다. IGListTransitionDelegate를 구현하는 클래스를 생성하고, 애니메이션 컨트롤러를 구현하여 IGListKit의 강력한 기능을 적극 활용할 수 있습니다.