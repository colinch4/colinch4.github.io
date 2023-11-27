---
layout: post
title: "[swift] IGListDisplayDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 개요

이번 포스트에서는 IGListDisplayDelegate와 Swift IGListKit을 사용하여 데이터 표시와 상호작용을 관리하는 방법에 대해 알아보겠습니다. IGListKit은 Instagram에서 개발된 디자인 패턴을 기반으로 한 UICollectionView의 확장 기능이며, IGListDisplayDelegate는 IGListKit에서 사용되는 중요한 프로토콜 중 하나입니다.

## IGListDisplayDelegate

IGListDisplayDelegate는 IGListKit에서 데이터 표시 및 상호작용을 관리하기 위해 사용되는 프로토콜입니다. 이 프로토콜을 구현하여 사용자 정의 뷰 컨트롤러를 만들고, UICollectionView에 데이터를 표시하는 방법을 제어할 수 있습니다.

이 프로토콜은 다음과 같은 메서드를 가지고 있습니다:

```swift
protocol IGListDisplayDelegate: AnyObject {
    func listAdapter(_ listAdapter: ListAdapter, willDisplay object: Any, at index: Int)
    func listAdapter(_ listAdapter: ListAdapter, didEndDisplaying object: Any, at index: Int)
    func listAdapter(_ listAdapter: ListAdapter, didDisplay object: Any, at index: Int)
    func listAdapter(_ listAdapter: ListAdapter, willBeginDragging object: Any)
    func listAdapter(_ listAdapter: ListAdapter, didEndDragging object: Any, willDecelerate decelerate: Bool)
    //...
}
```

이 메서드들은 데이터가 표시되기 전과 표시된 후의 상태 변화를 감지하기 위해 사용됩니다. 예를 들어, `willDisplay` 메서드는 특정 데이터가 화면에 나타나기 직전에 호출되고, `didEndDisplaying` 메서드는 해당 데이터가 화면에서 사라진 후에 호출됩니다.

## IGListDisplayDelegate 사용 예시

다음은 IGListDisplayDelegate를 구현하여 사용자 정의 뷰 컨트롤러에 데이터를 표시하는 예시입니다:

```swift
import UIKit
import IGListKit

class MyViewController: UIViewController, ListDisplayDelegate {
    private let data: [String] = ["Item 1", "Item 2", "Item 3"]
    
    private lazy var adapter: ListAdapter = {
        return ListAdapter(updater: ListAdapterUpdater(), viewController: self, workingRangeSize: 0)
    }()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        adapter.collectionView = collectionView
        adapter.dataSource = self
        adapter.displayDelegate = self
    }
    
    // MARK: - ListDisplayDelegate
    
    func listAdapter(_ listAdapter: ListAdapter, willDisplay object: Any, at index: Int) {
        print("Will display object \(object) at index \(index)")
    }
    
    func listAdapter(_ listAdapter: ListAdapter, didEndDisplaying object: Any, at index: Int) {
        print("Did end displaying object \(object) at index \(index)")
    }
    
    // MARK: - ListAdapterDataSource
    
    func objects(for listAdapter: ListAdapter) -> [ListDiffable] {
        return data
    }
    
    func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
        // Your section controller implementation here
    }
}
```

위의 예시 코드에서는 `MyViewController`라는 사용자 정의 뷰 컨트롤러에 IGListDisplayDelegate를 구현하고 있습니다. `willDisplay`와 `didEndDisplaying` 메서드에서는 해당 데이터를 출력합니다.

## 결론

이번 포스트에서는 IGListDisplayDelegate를 사용하여 UICollectionView에서 데이터 표시와 상호작용을 관리하는 방법에 대해 알아보았습니다. IGListKit은 다양한 디자인 패턴과 기능을 제공하여 복잡한 컬렉션 뷰를 조작하기 쉬운 인터페이스를 제공합니다. IGListDisplayDelegate를 사용하면 목록의 상태 변화를 감지하고, 이를 활용한 사용자 정의 로직을 구현할 수 있습니다.

더 많은 정보를 원하시면 [IGListKit 공식 문서](https://github.com/Instagram/IGListKit)를 참고하시기 바랍니다.