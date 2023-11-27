---
layout: post
title: "[swift] IGListEmptyCollectionContext와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

이 글에서는 IGListKit에서 제공하는 IGListEmptyCollectionContext를 사용하여 빈 상태의 컬렉션 뷰를 처리하는 방법에 대해 알아보겠습니다.

## IGListEmptyCollectionContext란?

IGListEmptyCollectionContext는 IGListKit에서 제공하는 기능으로, 컬렉션 뷰가 비어있는 상태일 때 화면에 표시되는 내용을 커스터마이징할 수 있습니다. 이를 통해 빈 상태에서도 사용자에게 유의미한 정보를 제공하거나 빈 상태를 시각적으로 표현할 수 있습니다.

## IGListEmptyCollectionContext 사용 방법

IGListEmptyCollectionContext를 사용하려면 다음과 같은 단계를 따르면 됩니다.

1. 먼저, IGListEmptyCollectionContextDelegate 프로토콜을 채택하고 해당 뷰 컨트롤러에서 이를 구현합니다.
2. 뷰 컨트롤러에서 registerEmptyCollectionViewDelegate 메서드를 호출하여 빈 상태 처리를 담당할 Delegate 인스턴스를 등록합니다.
3. Delegate 인스턴스에서 emptyView(for:) 메서드를 구현하여 빈 상태에서 보여줄 뷰를 반환합니다.

다음은 IGListEmptyCollectionContext를 사용하는 예시 코드입니다.

```swift
import IGListKit

class MyViewController: UIViewController, IGListEmptyCollectionContextDelegate {

    let adapter = ListAdapter(updater: ListAdapterUpdater(), viewController: nil)

    override func viewDidLoad() {
        super.viewDidLoad()

        adapter.collectionView = collectionView
        adapter.emptyCollectionContextDelegate = self

        // ...

        // 빈 상태에서 보여줄 뷰를 등록
        adapter.registerEmptyView(EmptyView.self)

        // ...
    }

    // 빈 상태에서 보여줄 뷰를 반환하는 메서드 구현
    func emptyView(for listAdapter: ListAdapter) -> UIView? {
        // 빈 상태에서 보여줄 뷰를 생성하고 반환
        return EmptyView()
    }
}
```

위 코드에서는 MyViewController에서 IGListEmptyCollectionContextDelegate 프로토콜을 채택하고 emptyView(for:) 메서드를 구현합니다. 이 메서드에서는 빈 상태에서 보여줄 EmptyView 인스턴스를 반환하도록 구현되어 있습니다.

또한, adapter.emptyCollectionContextDelegate를 MyViewController로 설정하여 MyViewController에서 빈 상태 처리를 담당하도록 합니다.

## 결론

IGListEmptyCollectionContext는 IGListKit에서 제공하는 유용한 기능 중 하나로, 빈 상태의 컬렉션 뷰를 처리하는데 도움을 줍니다. 이를 이용하여 빈 상태에서도 사용자에게 유의미한 정보를 제공하거나 빈 상태를 시각적으로 표현할 수 있습니다. IGListKit를 사용하는 경우, IGListEmptyCollectionContext를 활용하여 좀 더 풍부한 사용자 경험을 제공해보세요.