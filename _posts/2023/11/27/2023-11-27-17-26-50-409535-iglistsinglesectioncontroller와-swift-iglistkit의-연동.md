---
layout: post
title: "[swift] IGListSingleSectionController와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

📝 [IGListKit](https://github.com/Instagram/IGListKit)는 Swift 기반의 iOS 애플리케이션에서 컬렉션 뷰의 데이터 소스와 뷰 컨트롤러를 간단하게 연동할 수 있도록 도와주는 매우 유용한 프레임워크입니다. 이번 글에서는 IGListKit의 `IGListSingleSectionController`를 사용하여 어떻게 Swift 프로젝트에서 IGListKit를 연동하는지 살펴보겠습니다.

## IGListSingleSectionController란?

📚 `IGListSingleSectionController`는 IGListKit에서 제공하는 스크롤 가능한 컨텐츠를 가진 단일 섹션 컨트롤러입니다. 이 컨트롤러는 단일 데이터 원본을 사용하여 컬렉션 뷰의 한 섹션을 구성합니다. IGListSingleSectionController는 컬렉션 뷰의 데이터 소스 및 델리게이트에 대한 구현을 캡슐화하여 사용자 코드를 간소화하고 재사용성을 높여줍니다.

## IGListSingleSectionController 사용하기

IGListKit를 사용하기 위해서는 먼저 IGListKit 프레임워크를 프로젝트에 추가해야 합니다. IGListKit를 설치한 후, IGListKit 프레임워크를 import 해줍니다.

```swift
import IGListKit
```

다음으로, IGListKit에서 제공하는 `IGListSingleSectionController`를 서브클래싱하여 사용자 정의 섹션 컨트롤러를 구현합니다. 섹션 컨트롤러는 `IGListSectionController` 프로토콜을 준수해야 합니다.

```swift
class MySectionController: IGListSingleSectionController<DemoDataModel> {
    // 섹션 컨트롤러의 구현 내용
}

// 섹션 컨트롤러에 필요한 데이터 모델
struct DemoDataModel {
    let title: String
    let subtitle: String
}
```

이제 섹션 컨트롤러에서 컬렉션 뷰의 셀 및 헤더/푸터 뷰를 구성할 수 있습니다. 이를 위해서는 `IGListSingleSectionController`의 메서드들을 오버라이딩하여 사용자 정의해야 합니다.

```swift
class MySectionController: IGListSingleSectionController<DemoDataModel> {
    // 섹션 컨트롤러의 구현 내용

    override func cellForItem(at index: Int) -> UICollectionViewCell {
        let cell = collectionContext.dequeueReusableCell(of: DemoCell.self, for: self, at: index)
        // 셀 구성
        return cell
    }

    override func sizeForItem(at index: Int) -> CGSize {
        // 셀 크기 반환
    }
}
```

마지막으로, IGListKit와 데이터 소스를 연동하기 위해 `IGListAdapter`를 설정합니다.

```swift
let adapter = IGListAdapter(updater: IGListAdapterUpdater(), viewController: self, workingRangeSize: 0)
adapter.collectionView = collectionView
adapter.dataSource = self

extension YourViewController: IGListAdapterDataSource {
    func objects(for listAdapter: IGListAdapter) -> [IGListDiffable] {
        // 데이터 반환
    }

    func listAdapter(_ listAdapter: IGListAdapter, sectionControllerFor object: Any) -> IGListSectionController {
        // 해당 object에 대한 섹션 컨트롤러 반환
    }

    func emptyView(for listAdapter: IGListAdapter) -> UIView? {
        // 없을 경우의 뷰 반환
    }
}
```

위의 코드에서 `objects(for:)` 메서드에서는 섹션 컨트롤러에 연결할 데이터 `IGListDiffable`의 배열을 반환해야 합니다. 또한 `listAdapter(_:sectionControllerFor:)` 메서드에서는 데이터에 따라 적절한 섹션 컨트롤러를 반환해야 합니다.

IGListKit를 이용하여 컬렉션 뷰를 더 쉽게 관리할 수 있으며, `IGListSingleSectionController`를 사용하여 섹션 컨트롤러를 구성하면 코드를 더 간결하고 유지보수하기 쉽게 만들 수 있습니다. IGListKit의 다양한 기능과 유연성을 활용하여 애플리케이션의 컬렉션 뷰를 개선해보세요!

## 맺음말

이번 글에서는 IGListSingleSectionController와 Swift IGListKit의 연동 방법에 대해 알아보았습니다. IGListKit는 다양한 기능과 유연성을 제공하여 iOS 애플리케이션에서 컬렉션 뷰를 관리하는 데 매우 유용한 도구입니다. IGListKit를 사용하여 애플리케이션의 사용자 경험을 향상시키고 코드를 더 깔끔하게 유지해보세요!

🔗 [참고 자료](https://github.com/Instagram/IGListKit)