---
layout: post
title: "[swift] IGListDiffKit와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 소개

IGListKit은 Instagram에서 개발한 iOS용 리스트 컨트롤러 프레임워크로, 복잡한 셀 갱신 로직을 간편하게 처리할 수 있습니다. IGListKit은 IGListDiffKit이라는 라이브러리를 내부적으로 사용하여 데이터 소스의 변경 사항을 효율적으로 처리합니다. 이번 포스트에서는 IGListDiffKit와 Swift IGListKit을 함께 사용하는 방법을 알아보겠습니다.

## IGListDiffKit 설치하기

먼저, IGListDiffKit을 프로젝트에 설치해야 합니다. IGListDiffKit은 CocoaPods를 통해 쉽게 설치할 수 있습니다. Podfile에 다음과 같은 코드를 추가합니다:

```ruby
pod 'IGListDiffKit'
```

그리고 터미널에서 `pod install` 명령을 실행하여 IGListDiffKit을 설치합니다.

## IGListKit와 연동하기

IGListKit은 IGListDiffKit을 내부적으로 사용하므로, IGListKit 프레임워크를 설치하면 IGListDiffKit도 함께 설치됩니다. 아래의 코드를 사용하여 IGListKit을 프로젝트에 추가합니다:

```swift
import IGListKit
```

## 데이터 소스 구현하기

IGListKit를 사용하려면 데이터 소스를 구현해야 합니다. 데이터 소스는 IGListAdapterDataSource 프로토콜을 준수해야 하며, 다음과 같은 메서드를 구현해야 합니다:

```swift
extension YourViewController: IGListAdapterDataSource {
    func objects(for listAdapter: IGListAdapter) -> [IGListDiffable] {
        // 데이터 소스의 객체 배열을 반환합니다.
    }
    
    func listAdapter(_ listAdapter: IGListAdapter, sectionControllerFor object: Any) -> IGListSectionController {
        // 섹션 컨트롤러를 생성하여 반환합니다.
    }
    
    func emptyView(for listAdapter: IGListAdapter) -> UIView? {
        // 데이터가 없을 때 표시할 뷰를 반환합니다.
    }
}
```

## IGListAdapter 설정하기

다음으로, IGListAdapter를 설정해야 합니다. IGListAdapter를 초기화하고, 데이터 소스와 컬렉션 뷰를 연결합니다. 아래의 코드를 사용하여 IGListAdapter를 설정합니다:

```swift
let adapter = IGListAdapter(updater: IGListAdapterUpdater(), viewController: self, workingRangeSize: 0)
adapter.collectionView = collectionView
adapter.dataSource = self
```

## IGListDiffable 구현하기

마지막으로, 리스트 갱신을 위해 IGListDiffable 프로토콜을 구현해야 합니다. IGListDiffable 프로토콜을 준수하는 클래스는 diffIdentifier 속성을 구현해야 하며, 이 속성은 해당 객체를 구분하는 식별자 역할을 합니다. 아래의 코드처럼 IGListDiffable 프로토콜을 구현하세요:

```swift
class YourObject: NSObject, IGListDiffable {
    let id: String
    
    init(id: String) {
        self.id = id
    }
    
    // MARK: - IGListDiffable
    
    func diffIdentifier() -> NSObjectProtocol {
        return id as NSObjectProtocol
    }
    
    func isEqual(toDiffableObject object: IGListDiffable?) -> Bool {
        guard let object = object as? YourObject else {
            return false
        }
        return id == object.id
    }
}
```

## 결론

IGListDiffKit은 IGListKit 내부에서 사용되어 데이터 변화를 효율적으로 처리하는 라이브러리입니다. 이번 포스트에서는 IGListDiffKit와 Swift IGListKit의 연동 방법에 대해 알아보았습니다. IGListDiffKit을 사용하여 복잡한 셀 갱신 로직을 간편하게 처리할 수 있으며, IGListKit과 함께 사용하면 더욱 강력한 리스트 컨트롤러를 만들 수 있습니다.