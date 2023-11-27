---
layout: post
title: "[swift] IGListSingleSectionController와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 소개
IGListKit은 Instagram에서 개발한 UICollectionView를 사용하는데 도움이 되는 오픈 소스 라이브러리입니다. IGListSingleSectionController는 IGListKit의 하위 클래스로, 단일 섹션을 처리하는 데 사용됩니다.

이번 포스트에서는 IGListSingleSectionController와 Swift IGListKit을 함께 사용하는 방법을 알아보겠습니다.

## IGListKit 및 IGListSingleSectionController 설치

먼저, IGListKit을 설치해야 합니다. IGListKit은 Cocoapods를 통해 설치할 수 있습니다. Podfile에 다음과 같이 추가합니다.

```ruby
pod 'IGListKit'
```

그런 다음 터미널에서 다음 명령을 실행하여 의존성을 설치합니다.

```shell
$ pod install
```

IGListSingleSectionController는 IGListKit의 일부이므로 별도의 설치가 필요하지 않습니다.

## IGListSingleSectionController 생성

IGListSingleSectionController를 사용하려면 먼저 IGListBindingSectionController를 상속하는 클래스를 생성해야 합니다. 이 클래스는 IGListSingleSectionController에 데이터 소스 및 델리게이트 역할을 하게 됩니다.

```swift
class MySingleSectionController: IGListBindingSectionController<MyObject>, IGListBindingSectionControllerDataSource, IGListBindingSectionControllerSelectionDelegate {
    
    override init() {
        super.init()
        
        dataSource = self
        selectionDelegate = self
    }
    
    // 데이터 소스 및 델리게이트 메소드 구현
    // ...
}
```

위 예제의 MyObject는 IGListDiffable 프로토콜을 따르는 데이터 모델입니다. IGListDiffable 프로토콜은 CellForRow 메소드에서 셀을 생성할 수 있으며, 섹션 컨트롤러 내의 이벤트를 처리할 수 있도록 합니다.

## IGListAdapter 설정

IGListSingleSectionController를 사용하기 위해 IGListAdapter를 설정해야 합니다. IGListAdapter는 IGListKit의 핵심 클래스로, UICollectionView와 IGListBindingSectionController를 연결하는 역할을 합니다.

```swift
let adapter = IGListAdapter(updater: IGListAdapterUpdater(), viewController: self)
adapter.collectionView = collectionView
adapter.dataSource = self

// 섹션 컨트롤러 등록
adapter.collectionViewDelegate = self
adapter.collectionViewDataSource = self
```

위 예제에서 self는 현재 ViewController를 가리킵니다.

## 섹션 컨트롤러 등록

마지막으로 IGListAdapter의 collectionViewDelegate 및 collectionViewDataSource 메소드를 구현하여 섹션 컨트롤러를 등록해야 합니다.

```swift
extension MyViewController: IGListAdapterDelegate, IGListAdapterDataSource {
    
    func objects(for listAdapter: IGListAdapter) -> [IGListDiffable] {
        // 데이터 모델 반환
    }
    
    func listAdapter(_ listAdapter: IGListAdapter, sectionControllerFor object: Any) -> IGListSectionController {
        // IGListSingleSectionController 인스턴스 생성 및 반환
    }
    
    func emptyView(for listAdapter: IGListAdapter) -> UIView? {
        // 비어있는 경우 표시될 뷰 반환 (옵션)
    }
    
}
```

위 예제에서 MyViewController는 IGListBindingSectionController의 데이터 소스 및 델리게이트 역할을 합니다. objects(for:) 메소드를 통해 섹션 컨트롤러에 표시할 데이터 모델을 반환하고, listAdapter(_:sectionControllerFor:) 함수에서 IGListSingleSectionController 인스턴스를 생성하여 반환합니다.

## 결론

이제 IGListSingleSectionController와 Swift IGListKit을 함께 사용하는 방법에 대해 알아보았습니다. IGListSingleSectionController를 사용하면 UICollectionView에서 단일 섹션을 처리하는 데 편리한 방법을 제공합니다. IGListKit을 사용하여 보다 유연하고 모듈화된 UICollectionView를 구현할 수 있습니다.

더 자세한 사항은 [IGListKit 공식 문서](https://instagram.github.io/IGListKit/)를 참조하십시오.