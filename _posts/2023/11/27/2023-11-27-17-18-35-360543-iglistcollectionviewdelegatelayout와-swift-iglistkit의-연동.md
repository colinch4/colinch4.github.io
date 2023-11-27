---
layout: post
title: "[swift] IGListCollectionViewDelegateLayout와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListCollectionViewDelegateLayout는 IGListKit에서 사용되는 UICollectionViewDelegateFlowLayout를 대신하여 사용할 수 있는 커스텀 레이아웃입니다. 이를 통해 Swift에서 IGListKit을 사용하고 UICollectionViewDelegateFlowLayout의 기능을 활용할 수 있습니다.

## IGListCollectionViewDelegateLayout이란?

IGListCollectionViewDelegateLayout은 IGListKit에서 제공하는 기능으로, UICollectionViewDelegateFlowLayout와 유사한 역할을 합니다. IGListCollectionViewDelegateLayout은 UICollectionViewLayout를 커스터마이징하여 아이템들의 배치와 크기를 조정합니다.

일반적으로 IGListCollectionViewDelegateLayout은 IGListAdapter에서 사용됩니다. IGListAdapter는 UICollectionView와 IGListKit의 데이터 소스를 연결해주는 역할을 합니다. IGListCollectionViewDelegateLayout을 사용함으로써 IGListAdapter에서 내보내는 UICollectionViewDelegateFlowLayout의 메서드를 구현하고 셀들을 형식화 할 수 있습니다.

## IGListCollectionViewDelegateLayout 사용하기

1. IGListAdapter 객체를 생성합니다.

```swift
let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self)
```

2. UICollectionViewFlowLayout 대신 IGListCollectionViewDelegateLayout을 사용하여 UICollectionView의 레이아웃을 설정합니다.

```swift
let layout = IGListCollectionViewDelegateLayout()
collectionView.collectionViewLayout = layout
```

3. IGListCollectionViewDelegateLayout의 메서드를 구현합니다.

```swift
extension YourViewController: ListCollectionViewDelegateLayout {
    func listCollectionView(_ collectionView: UICollectionView, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // 아이템의 크기 반환
        return CGSize(width: 100, height: 100)
    }
    
    func listCollectionView(_ collectionView: UICollectionView, insetForSectionAt section: Int) -> UIEdgeInsets {
        // 섹션의 여백 반환
        return UIEdgeInsets(top: 10, left: 10, bottom: 10, right: 10)
    }
    
    // 추가적인 메서드 구현 가능
}
```

위의 예시 코드에서는 sizeForItemAt 메서드와 insetForSectionAt 메서드를 구현하였습니다. sizeForItemAt 메서드는 각 아이템의 크기를 반환하고, insetForSectionAt 메서드는 섹션의 여백을 반환합니다. 이 외에도 IGListCollectionViewDelegateLayout에서 제공하는 다양한 메서드를 구현하여 커스텀 레이아웃을 만들 수 있습니다.

## 마치며

IGListCollectionViewDelegateLayout은 IGListKit에서 제공하는 유용한 기능입니다. UICollectionViewDelegateFlowLayout를 대신하여 IGListCollectionViewDelegateLayout을 사용하면서 Swift에서 IGListKit을 더욱 효과적으로 활용할 수 있습니다. IGListCollectionViewDelegateLayout의 다양한 메서드를 구현하여 원하는 레이아웃을 구성해보세요!

## References

- [IGListKit Documentation](https://instagram.github.io/IGListKit/)
- [IGListAdapter Class Reference](https://github.com/Instagram/IGListKit/blob/main/Source/IGListAdapter.h)
- [UICollectionViewDelegateFlowLayout Documentation](https://developer.apple.com/documentation/uikit/uicollectionviewdelegateflowlayout)