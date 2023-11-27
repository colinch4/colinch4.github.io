---
layout: post
title: "[swift] IGListCollectionViewDelegateLayout와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListCollectionViewDelegateLayout는 IGListKit에서 제공하는 UICollectionViewFlowLayout의 하위 클래스입니다. 이를 사용하면 UICollectionView의 레이아웃과 관련된 작업을 더 쉽게 처리할 수 있습니다.

## IGListCollectionViewDelegateLayout 설치

Swift IGListKit를 사용하기 위해 다음과 같이 CocoaPods를 사용하여 IGListKit을 설치합니다.

```ruby
pod 'IGListKit'
```

## IGListCollectionViewDelegateLayout 사용법

IGListCollectionViewDelegateLayout은 UICollectionViewDelegateFlowLayout 프로토콜을 구현하고 있으며, IGListAdapter를 사용하는 IGListViewController에서 사용할 수 있습니다.

먼저, IGListCollectionViewDelegateLayout을 만들어보겠습니다.

```swift
import IGListKit

class MyCollectionViewDelegateLayout: IGListCollectionViewDelegateLayout {
  
  func collectionView(
    _ collectionView: UICollectionView,
    layout collectionViewLayout: UICollectionViewLayout,
    sizeForItemAt indexPath: IndexPath
  ) -> CGSize {
    // 셀의 크기를 계산하여 반환하는 로직 작성
    return CGSize(width: 100, height: 100)
  }
  
  // 다른 UICollectionViewDelegateFlowLayout 메서드도 구현 가능
  
}
```

그리고, IGListAdapter와 함께 사용하기 위해 해당 IGListViewController에 delegate를 설정합니다.

```swift
class MyListViewController: IGListViewController {
  
  let adapter = IGListAdapter(updater: IGListAdapterUpdater(), viewController: self)
  let collectionViewDelegateLayout = MyCollectionViewDelegateLayout()
  
  override func viewDidLoad() {
    super.viewDidLoad()
    
    // ...
    
    adapter.collectionViewDelegate = collectionViewDelegateLayout
    
    // ...
    
    adapter.collectionView = collectionView
    
    // ...
  }
  
  // ...
  
}
```

위에서 작성한 MyCollectionViewDelegateLayout을 IGListAdapter의 collectionViewDelegate로 설정함으로써, 해당 뷰 컨트롤러에서 IGListCollectionViewDelegateLayout을 사용할 수 있게 됩니다.

## 결론

IGListCollectionViewDelegateLayout는 IGListKit을 통해 UICollectionView에 레이아웃을 적용하기 위한 편리한 방법을 제공합니다. IGListAdapter와 함께 사용하여 UICollectionView의 레이아웃과 관련된 작업을 더욱 간편하게 처리할 수 있습니다.

## 참고 자료

- [IGListKit GitHub Repository](https://github.com/Instagram/IGListKit)
- [IGListKit Getting Started](https://instagram.github.io/IGListKit/)
- [UICollectionViewDelegateFlowLayout](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout)