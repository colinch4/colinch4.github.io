---
layout: post
title: "[swift] Swift IGListKit과 RxSwift의 결합"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 IGListKit과 RxSwift를 함께 사용하는 방법을 알아보겠습니다. 

## IGListKit 소개

IGListKit은 Instagram에서 개발한 라이브러리로, 복잡한 리스트 인터페이스를 처리하고 업데이트하는 데 사용됩니다. IGListKit은 성능 최적화를 위해 Diffing 알고리즘을 사용하며, UICollectionView의 사용을 편리하게 만들어줍니다.

## RxSwift 소개

RxSwift는 Swift에서 함수형 프로그래밍과 반응형 프로그래밍을 지원하기 위한 라이브러리입니다. Observable, Observer, Subject 등의 개념을 제공하여 데이터 흐름을 쉽게 관리할 수 있습니다.

## IGListKit과 RxSwift의 결합

IGListKit과 RxSwift를 함께 사용하면 UI 업데이트를 자동으로 처리하고, 데이터의 변화를 쉽게 감지하여 업데이트할 수 있습니다.

먼저, IGListKit의 `IGListAdapterDataSource` 프로토콜을 구현하여 데이터를 제공합니다. IGListAdapterDataSource는 `objects(for:)` 메서드를 구현하여 섹션과 아이템의 데이터를 반환합니다. 이때, RxSwift의 Observable을 사용하여 데이터를 제공할 수 있습니다.

```swift
import IGListKit
import RxSwift

class MyListAdapter: NSObject, IGListAdapterDataSource {
    
    let disposeBag = DisposeBag()
    let items: BehaviorSubject<[MyItem]> = BehaviorSubject<[MyItem]>(value: [])

    func objects(for listAdapter: IGListAdapter) -> [IGListDiffable] {
        // BehaviorSubject로부터 Observable을 생성하여 데이터를 반환합니다.
        return try! items.value()
    }
    
    // ...
}
```

다음으로, RxSwift의 `Observable`을 사용하여 데이터를 업데이트합니다. 이때, IGListKit의 `IGListAdapter`의 `performUpdates(animated:completion:)` 메서드를 사용하여 UI를 업데이트합니다.

```swift
class MyViewController: UIViewController {
    
    let disposeBag = DisposeBag()
    let myListAdapter = MyListAdapter()
    
    func observeData() {
        // RxSwift를 사용하여 데이터 변화를 감지합니다.
        myListAdapter.items
            .asObservable()
            .subscribe(onNext: { [weak self] _ in
                // 데이터 변화가 있을 때마다 IGListAdapter를 통해 UI를 업데이트합니다.
                self?.myListAdapter.performUpdates(animated: true, completion: nil)
            })
            .disposed(by: disposeBag)
    }
    
    // ...
}
```

위 코드에서 `observeData()` 메서드는 `myListAdapter`의 `items` Observable을 구독하고, 데이터 변화가 있을 때마다 UI를 업데이트하는 역할을 합니다.

## 결론

Swift에서 IGListKit과 RxSwift를 결합하여 복잡한 리스트 인터페이스에서의 데이터 업데이트를 간편하고 효율적으로 처리할 수 있습니다. IGListKit의 성능 최적화와 RxSwift의 반응형 프로그래밍의 장점을 함께 활용하여 개발 효율성을 높일 수 있습니다.

## 참고 자료

- IGListKit GitHub 저장소: [https://github.com/Instagram/IGListKit](https://github.com/Instagram/IGListKit)
- RxSwift GitHub 저장소: [https://github.com/ReactiveX/RxSwift](https://github.com/ReactiveX/RxSwift)