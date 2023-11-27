---
layout: post
title: "[swift] IGListUpdatingDelegate와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListKit은 iOS 애플리케이션에서 복잡한 리스트 화면을 처리하기 위한 강력한 라이브러리입니다. IGListUpdatingDelegate는 IGListKit의 중요한 프로토콜 중 하나로, 리스트에서 발생하는 업데이트를 처리하는 역할을 합니다. 이번 포스트에서는 IGListUpdatingDelegate와 Swift IGListKit의 연동 방법에 대해 알아보겠습니다.

## IGListUpdatingDelegate란?

IGListUpdatingDelegate는 IGListAdapter가 업데이트 이벤트를 처리하기 위해 구현해야하는 프로토콜입니다. 이 프로토콜은 리스트의 데이터 소스가 변화할 때 발생하는 업데이트 이벤트를 처리하기 위해 사용됩니다. IGListUpdatingDelegate를 구현함으로써 리스트의 변화를 감지하고 화면에 반영할 수 있습니다.

## IGListUpdatingDelegate 구현 방법

아래는 IGListUpdatingDelegate를 구현하는 간단한 예제입니다. 

```swift
class MyAdapter: NSObject, IGListAdapterDataSource, IGListUpdatingDelegate {

  var data: [String] = ["Apple", "Banana", "Orange"]

  // 데이터 소스 구현
  func objects(for listAdapter: IGListAdapter) -> [IGListDiffable] {
    return data
  }

  func listAdapter(_ listAdapter: IGListAdapter, sectionControllerFor object: Any) -> IGListSectionController {
    return MySectionController()
  }

  func emptyView(for listAdapter: IGListAdapter) -> UIView? {
    return nil
  }

  // 업데이트 이벤트 처리
  func listAdapter(_ listAdapter: IGListAdapter, willUpdate objects: [Any], at index: Int) {
    print("리스트 업데이트 시작")
  }

  func listAdapter(_ listAdapter: IGListAdapter, didUpdate objects: [Any], at index: Int) {
    print("리스트 업데이트 완료")
  }
}
```

위의 예제에서는 MyAdapter 클래스가 IGListUpdatingDelegate를 구현하고 있습니다. objects(for:) 메서드를 통해 데이터를 반환하고, listAdapter(_:sectionControllerFor:) 메서드를 통해 섹션 컨트롤러를 반환합니다. emptyView(for:) 메서드는 빈 화면을 처리하는 데 사용됩니다.

또한, listAdapter(_:willUpdate:at:)와 listAdapter(_:didUpdate:at:) 메서드를 구현해서 리스트 업데이트 이벤트를 처리할 수 있습니다.

## IGListUpdatingDelegate와 IGListAdapter의 연동

IGListUpdatingDelegate는 IGListAdapter 클래스와 함께 사용되어야 합니다. 아래는 IGListKit을 사용하여 리스트를 화면에 표시하는 방법을 보여주는 예제입니다.

```swift
class ViewController: UIViewController {

  private var collectionView: UICollectionView?

  override func viewDidLoad() {
    super.viewDidLoad()

    let layout = UICollectionViewFlowLayout()
    collectionView = UICollectionView(frame: view.bounds, collectionViewLayout: layout)
    view.addSubview(collectionView!)

    // 리스트 어댑터 생성
    let adapter = IGListAdapter(updater: IGListReloadDataUpdater(), viewController: self)
    adapter.dataSource = MyAdapter()

    // 컬렉션 뷰와 어댑터 연동
    adapter.collectionView = collectionView

    // 데이터 업데이트
    DispatchQueue.global().async {
      // 새로운 데이터 업데이트
      let newData: [String] = // 새로운 데이터 조회 로직

      DispatchQueue.main.async {
        adapter.performUpdates(animated: true, completion: nil)
      }
    }
  }
}
```

위의 예제에서는 ViewController 클래스가 IGListAdapter와 연동하여 리스트를 화면에 표시하고, 데이터 업데이트를 수행하는 방법을 보여줍니다. 

먼저, 어댑터를 생성하고 dataSource에 MyAdapter 클래스를 지정합니다. 그리고 어댑터의 collectionView 속성을 컬렉션 뷰와 연결합니다. 마지막으로, 데이터 업데이트를 수행하기 위해 performUpdates(animated:completion:) 메서드를 호출하여 리스트의 변화를 감지하고 화면에 반영합니다.

## 마무리

IGListUpdatingDelegate는 IGListKit에서 리스트의 업데이트 이벤트를 다루기 위해 사용되는 중요한 프로토콜입니다. 이번 포스트에서는 IGListUpdatingDelegate의 구현 방법과 IGListAdapter와의 연동 방법에 대해 알아보았습니다. IGListKit을 사용하여 복잡한 리스트 화면을 구현할 때 IGListUpdatingDelegate를 적절히 활용하면 효율적인 개발이 가능할 것입니다.

참고 자료: [IGListKit 공식 문서](https://github.com/Instagram/IGListKit)