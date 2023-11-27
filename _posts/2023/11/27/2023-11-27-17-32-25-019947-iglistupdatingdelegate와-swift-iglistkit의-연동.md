---
layout: post
title: "[swift] IGListUpdatingDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

이번 글에서는 IGListKit 라이브러리와 Swift에서 IGListUpdatingDelegate를 연동하는 방법에 대해 알아보겠습니다.

## IGListKit이란?

IGListKit은 Instagram에서 사용하는 UI컴포넌트 라이브러리로, 콜렉션 뷰를 통해 복잡한 화면을 손쉽게 구성할 수 있도록 도와주는 도구입니다. IGListUpdatingDelegate는 이러한 IGListKit에서 사용되는 프로토콜 중 하나로, 데이터의 업데이트를 관리하는 역할을 합니다.

## IGListUpdatingDelegate 사용하기

먼저, IGListKit을 프로젝트에 추가해주어야 합니다. IGListKit은 CocoaPods나 Carthage를 통해 설치할 수 있습니다. 설치가 완료되면, IGListUpdatingDelegate 프로토콜을 사용해 업데이트 관리를 구현할 수 있습니다.

```swift
import IGListKit

// Update를 수행하는 클래스
class MyListUpdater: NSObject, IGListUpdatingDelegate {
    
    // 업데이트 관련 메서드 구현
    func performUpdateWithCollectionView(collectionView: UICollectionView, fromObjects: [Any], 
                                         toObjects: [Any], completion: IGListUpdatingCompletion?){
        
        // 데이터 업데이트 로직 구현
        // fromObjects와 toObjects 비교하여 적절한 업데이트 로직 수행
        
        // 업데이트 완료 후에 completion 핸들러 호출
        completion?()
    }
}

// IGListKit 사용하기
let updater = MyListUpdater()
let adapter = ListAdapter(updater: updater, viewController: self)
```

위의 예제 코드에서는 `MyListUpdater`라는 클래스가 IGListUpdatingDelegate 프로토콜을 채택하여, `performUpdateWithCollectionView` 메서드를 구현하고 있습니다. 

이 메서드를 통해 데이터의 업데이트 로직을 구현하고, 업데이트가 완료된 후에는 `completion` 핸들러를 호출하여 IGListKit에 업데이트 완료를 알립니다. 

마지막으로, `ListAdapter` 클래스를 사용하여 업데이트 관련 동작을 수행하는 `updater` 객체를 지정해주면, IGListKit의 업데이트 동작을 사용할 수 있게 됩니다.

## 마무리

이번 포스트에서는 IGListKit 라이브러리와 Swift에서 IGListUpdatingDelegate를 연동하는 방법에 대해 알아보았습니다. IGListKit을 사용하면 복잡한 UI 컴포넌트를 쉽게 구현할 수 있으며, IGListUpdatingDelegate를 통해 데이터의 업데이트를 효율적으로 관리할 수 있습니다. IGListKit에 대해 더 알고 싶다면 공식 문서를 참고해보시기 바랍니다.

참고: [IGListKit 공식 문서](https://github.com/Instagram/IGListKit)