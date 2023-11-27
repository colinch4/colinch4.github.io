---
layout: post
title: "[swift] IGListDiffKit와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

Swift IGListKit은 iOS 애플리케이션에서 복잡한 데이터 목록을 관리하고 효율적으로 표시할 수 있도록 도와주는 라이브러리입니다. IGListDiffKit은 IGListKit에 내장된 기능이며, 데이터 변경을 감지하고 전체 목록을 다시 그리는 대신 변경된 항목만 업데이트할 수 있도록 도와줍니다.

이번 블로그 포스트에서는 IGListDiffKit와 Swift IGListKit을 함께 사용하는 방법에 대해 알아보겠습니다.

## IGListKit 설치하기

먼저, 프로젝트의 의존성 관리 도구인 CocoaPods나 Swift Package Manager를 사용하여 IGListKit을 설치해야 합니다. 프로젝트의 Podfile에 다음과 같이 IGListKit을 추가하세요.

```ruby
pod 'IGListKit'
```

그리고 터미널에서 `pod install` 명령을 실행하여 IGListKit을 프로젝트에 추가하세요.

## IGListDiffKit와 IGListKit 설정하기

다음으로, IGListDiffKit와 IGListKit을 설정해야 합니다. 다음과 같이 `IGListAdapterUpdater` 객체를 생성하고 IGListKit에 할당해야 합니다.

```swift
import IGListKit

let updater = IGListAdapterUpdater()
let adapter = IGListAdapter(updater: updater, viewController: self)
adapter.dataSource = self
adapter.collectionView = collectionView
```

위 코드에서 `self`는 `IGListAdapterDataSource` 프로토콜을 구현한 클래스의 인스턴스여야 합니다. `adapter.collectionView`는 IGListKit이 사용할 UICollectionView를 지정해주어야 합니다.

## IGListDiffKit 사용하기

이제 IGListDiffKit을 사용하여 목록의 변경 사항을 처리할 수 있습니다. IGListDiffable 프로토콜을 채택하여 데이터 모델을 구현해야 합니다. IGListDiffable 프로토콜을 구현한 데이터 모델은 IGListKit이 목록을 업데이트할 때 사용할 수 있습니다.

```swift
import IGListKit

class Person: NSObject, IGListDiffable {
    let name: String
    
    init(name: String) {
        self.name = name
    }
    
    func diffIdentifier() -> NSObjectProtocol {
        return name as NSObjectProtocol
    }
    
    func isEqual(toDiffableObject object: IGListDiffable?) -> Bool {
        guard let object = object as? Person else { return false }
        return name == object.name
    }
}
```

위 코드에서 `diffIdentifier()` 메서드는 데이터 모델의 고유 식별자를 반환해야 합니다. `isEqual(toDiffableObject:)` 메서드는 데이터 모델 간의 동등성을 판단하는 로직을 구현해야 합니다.

## IGListDiffKit 데이터 소스 구현하기

마지막으로, IGListDiffKit의 데이터 소스를 구현해야 합니다. 데이터 소스는 IGListKit이 목록의 데이터를 어떻게 가져오고 업데이트할지를 지정하는 역할을 합니다.

```swift
import IGListKit

class MyDataSource: NSObject, IGListAdapterDataSource {
    var data = [Person]() // 데이터 모델 배열
    
    override init() {
        super.init()
        // 데이터 모델 초기화
    }
    
    func objects(for listAdapter: IGListAdapter) -> [IGListDiffable] {
        return data as [IGListDiffable]
    }
    
    func listAdapter(_ listAdapter: IGListAdapter, sectionControllerFor object: Any) -> IGListSectionController {
        // 섹션 컨트롤러 반환
    }
    
    func emptyView(for listAdapter: IGListAdapter) -> UIView? {
        // 빈 목록을 표시할 뷰 반환
    }
}
```

위 코드에서 `objects(for:)` 메서드는 IGListKit이 목록에 표시할 데이터를 반환해야 합니다. `listAdapter(_:sectionControllerFor:)` 메서드는 IGListKit이 데이터 모델과 섹션 컨트롤러를 연결할 때 호출됩니다. `emptyView(for:)` 메서드는 데이터가 비어있을 때 표시될 뷰를 반환해야 합니다.

## 결론

이제 IGListDiffKit와 Swift IGListKit을 함께 사용하는 방법을 알게 되었습니다. IGListDiffKit을 사용하면 데이터 변경에 따른 목록의 부하를 줄일 수 있고, 애플리케이션의 성능을 향상시킬 수 있습니다. IGListDiffKit의 장점을 최대한 활용하여 iOS 애플리케이션의 데이터 목록 관리를 효율적으로 해보세요.

## 참고 자료

- [IGListKit GitHub](https://github.com/Instagram/IGListKit)
- [IGListKit 기술 문서](https://instagram.github.io/IGListKit/)
- [IGListDiffKit 기술 문서](https://instagram.github.io/IGListKit/Classes/IGListDiffKit.html)