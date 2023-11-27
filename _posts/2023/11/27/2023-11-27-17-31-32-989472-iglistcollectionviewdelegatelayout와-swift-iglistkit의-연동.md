---
layout: post
title: "[swift] IGListCollectionViewDelegateLayout와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

> 이번 글에서는 `IGListCollectionViewDelegateLayout`를 사용하여 `IGListKit`와의 연동을 살펴보겠습니다.

## IGListCollectionViewDelegateLayout란?

`IGListCollectionViewDelegateLayout`는 `IGListKit`에서 제공하는 커스텀 레이아웃 클래스입니다. `UICollectionViewDelegateFlowLayout`를 대체하는 역할을 수행하며, `IGListKit`의 리스트 컨트롤러와 함께 사용할 수 있습니다.

## Swift IGListKit 프로젝트 설정

먼저, `IGListKit`을 Swift 프로젝트에 추가해야 합니다. `CocoaPods`를 사용한다면, `Podfile`에 다음과 같이 추가합니다.

```ruby
pod 'IGListKit'
```

`Carthage`를 사용한다면, `Cartfile`에 다음과 같이 추가합니다.

```ruby
github "Instagram/IGListKit" ~> 4.0
```

프로젝트 설정이 완료되면, 다음 단계로 넘어갑니다.

## IGListCollectionViewDelegateLayout 사용하기

`IGListCollectionViewDelegateLayout`를 사용하려면, 아래의 단계를 따라야 합니다.

1. `IGListSectionController`를 상속하는 커스텀 섹션 컨트롤러를 만듭니다.

```swift
class MySectionController: ListSectionController {
    // 섹션 컨트롤러의 필요한 메서드들을 구현합니다.
}
```

2. `IGListCollectionViewDelegateLayout` 인스턴스를 생성하고, 초기화합니다.

```swift
let layout = IGListCollectionViewDelegateLayout()
```

3. `layout`의 `delegate` 프로퍼티를 섹션 컨트롤러로 설정합니다.

```swift
layout.delegate = self
```

4. `IGListAdapter`를 초기화하고, 위에서 생성한 `layout`를 인자로 전달합니다.

```swift
let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: self, workingRangeSize: 0)
adapter.collectionViewDelegate = layout
adapter.collectionViewDataSource = self
```

## IGListCollectionViewDelegateLayout 메서드 구현

`IGListCollectionViewDelegateLayout`의 `collectionView:layout:sizeForItemAtIndexPath:` 메서드를 구현하여 각 아이템의 크기를 반환해야 합니다.

```swift
func listAdapter(_ listAdapter: ListAdapter, sizeForItemAt index: Int, controller: ListSectionController) -> CGSize {
    // 아이템의 크기를 계산하고 반환합니다.
    return CGSize(width: 100, height: 100)
}
```

다른 메서드들도 필요에 따라 구현할 수 있습니다.

## 마무리

이제 `IGListCollectionViewDelegateLayout`를 활용하여 `IGListKit`를 사용하는 방법에 대해 알아보았습니다. `IGListKit`은 복잡한 컬렉션 뷰 레이아웃을 구현하고 처리하는 우수한 라이브러리입니다. 기능을 확장하거나 개선할 때 유용한 도구로 사용할 수 있습니다.

더 자세한 사용법과 설정에 대해서는 `IGListKit`의 공식 문서를 참고하시기 바랍니다.

- [IGListKit 공식 Github 저장소](https://github.com/Instagram/IGListKit)
- [IGListKit 공식 문서](https://iglistkit.dev/)

Happy coding!