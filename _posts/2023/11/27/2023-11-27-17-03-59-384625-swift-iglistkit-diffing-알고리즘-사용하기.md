---
layout: post
title: "[swift] Swift IGListKit Diffing 알고리즘 사용하기"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

안녕하세요! 이번에는 Swift와 IGListKit을 함께 사용하여 Diffing 알고리즘을 적용하는 방법에 대해 알아보겠습니다.

## IGListKit이란?

IGListKit은 Instagram에서 개발한 iOS 앱의 데이터 업데이트를 처리하기 위한 티에스팩트(Twistspect) 개발자들의 오픈소스 프로젝트입니다. IGListKit은 UICollectionView를 기반으로하여 복잡한 데이터 표현과 업데이트를 처리하기 위한 도구를 제공합니다.

## Diffing 알고리즘 적용하기

Diffing 알고리즘은 이전 데이터와 현재 데이터를 비교하여 변경된 내용을 찾아내는 알고리즘입니다. IGListKit은 알고리즘을 효율적으로 구현하였고 이를 사용할 수 있습니다.

```swift
import IGListKit

class MyViewController: UIViewController, ListAdapterDataSource {
    private var data: [User] = []
    private let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: nil)
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        adapter.dataSource = self
        
        // ... 데이터를 초기화하고 adapter에 등록하는 코드
        
        // 기존에 데이터를 업데이트할 때 사용한 코드
        // self.data = newData
        // adapter.reloadData()
        
        // Diffing 알고리즘을 사용하여 데이터 업데이트하기
        let diff = ListDiff(oldArray: data, newArray: newData, option: .equality)
        let update = diff.forBatchUpdates()
        data = newData
        adapter.performUpdates(animated: true, completion: nil)
    }
    
    // ... ListAdapterDataSource를 구현한 코드
}
```

위의 예시 코드에서는 `data`라는 배열에 이전 데이터가 저장되어 있고, `newData`라는 배열에 현재 데이터가 저장되어 있다고 가정합니다. Diffing 알고리즘을 사용하기 위해서는 이전 데이터와 현재 데이터를 이용하여 `ListDiff` 인스턴스를 생성해야 합니다.

`ListDiff` 인스턴스를 생성할 때 `oldArray`에 이전 데이터 배열, `newArray`에 현재 데이터 배열, `option`에 비교 방법을 지정합니다. `equality` 옵션을 사용하면 IGListKit이 배열 요소를 비교할 때 `===`를 사용하여 비교합니다.

`ListDiff` 인스턴스를 생성하고 나면 `forBatchUpdates()` 메소드를 호출하여 변경된 내용을 확인할 수 있습니다. `forBatchUpdates()` 메소드는 `ListBatchUpdate` 인스턴스를 반환하고, 변경된 세부 사항을 확인하고 해당 변경 사항을 반영할 수 있습니다.

변경된 데이터를 반영하기 위해 `data` 배열을 업데이트하고, `performUpdates(animated:completion:)` 메소드를 호출하여 변경 사항을 애니메이션으로 반영합니다.

## 결론

이렇게 Swift와 IGListKit을 함께 사용하여 Diffing 알고리즘을 적용하는 방법을 알아보았습니다. IGListKit은 데이터의 변경 사항을 효율적으로 처리할 수 있는 다양한 도구를 제공하므로, 복잡한 데이터 업데이트 로직을 쉽게 구현할 수 있습니다. IGListKit을 사용하여 앱의 성능을 향상시키고 사용자 경험을 개선해보세요!

## 참고 자료

- IGListKit 공식 GitHub 페이지: [https://github.com/Instagram/IGListKit](https://github.com/Instagram/IGListKit)
- IGListKit 문서: [https://instagram.github.io/IGListKit/](https://instagram.github.io/IGListKit/)