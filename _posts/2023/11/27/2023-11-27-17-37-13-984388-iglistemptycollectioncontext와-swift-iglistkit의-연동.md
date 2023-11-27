---
layout: post
title: "[swift] IGListEmptyCollectionContext와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListKit은 iOS 앱에서 복잡한 리스트 UI를 만들기 위해 사용되는 강력한 도구입니다. IGListEmptyCollectionContext는 IGListKit에서 제공하는 클래스로, 데이터가 없을 때 빈 상태의 화면을 표시하는 데 사용됩니다. 이번 블로그 포스트에서는 IGListEmptyCollectionContext와 Swift IGListKit의 연동에 대해 알아보겠습니다.

## IGListEmptyCollectionContext란?

IGListEmptyCollectionContext는 IGListKit에서 제공하는 앱의 상태에 따라 적절한 빈 상태의 컨텐츠를 표시하기 위한 클래스입니다. 이 클래스를 사용하면 데이터가 없을 때 적절한 빈 상태를 표시하거나, 에러 상태를 표시할 수 있습니다. IGListEmptyCollectionContext는 IGListCollectionView 객체와 함께 사용되며, 내부적으로 비어있는 상태를 표시하기 위한 뷰를 관리합니다.

## IGListEmptyCollectionContext의 사용법

IGListEmptyCollectionContext의 사용법은 간단합니다. 먼저, IGListCollectionView 객체를 만들어야 합니다.

```swift
let collectionView = IGListCollectionView(frame: CGRect.zero, collectionViewLayout: UICollectionViewFlowLayout())
```

그리고 IGListAdapter 생성자에 IGListCollectionView와 함께 IGListEmptyCollectionContext 객체를 전달해야 합니다.

```swift
let adapter = IGListAdapter(updater: IGListAdapterUpdater(), viewController: self, workingRangeSize: 0)
adapter.collectionView = collectionView
adapter.emptyCollectionContext = IGListEmptyCollectionContext(delegate: self)
```

이렇게 하면 IGListAdapter가 데이터 없을 때 적절한 빈 상태를 표시하기 위해 IGListEmptyCollectionContext에서 제공하는 메서드를 호출합니다.

## IGListEmptyCollectionContextDelegate

IGListEmptyCollectionContextDelegate는 IGListEmptyCollectionContext에서 상태 변경을 처리하는 데 사용되는 프로토콜입니다. 이 프로토콜의 메서드를 구현하여 데이터 없을 때 어떤 뷰를 표시할지 정의할 수 있습니다.

```swift
extension ViewController: IGListEmptyCollectionContextDelegate {
    func emptyCollectionContext(_ context: IGListEmptyCollectionContext, didUpdateWith state: IGListEmptyCollectionState) {
        switch state {
        case .empty:
            // 데이터가 없는 경우
            break
        case .populated:
            // 데이터가 있는 경우
            break
        case .error:
            // 에러가 발생한 경우
            break
        }
    }
}
```

위의 예제에서는 데이터가 없을 때, 데이터가 있는 경우, 에러가 발생한 경우에 대한 처리를 구현하도록 되어 있습니다.

## 결론

IGListEmptyCollectionContext는 IGListKit을 사용하여 빈 상태를 처리하는 강력한 도구입니다. 데이터가 없을 때 적절한 빈 상태를 표시하거나, 에러 상태를 표시하기 위해 IGListEmptyCollectionContext를 사용할 수 있습니다. IGListEmptyCollectionContextDelegate를 구현하여 데이터 없을 때 어떤 뷰를 표시할지 정의할 수 있습니다.

더 자세한 내용은 [IGListKit 문서](https://github.com/Instagram/IGListKit)를 참고하시기 바랍니다.

[참고자료]
- [IGListKit](https://github.com/Instagram/IGListKit)