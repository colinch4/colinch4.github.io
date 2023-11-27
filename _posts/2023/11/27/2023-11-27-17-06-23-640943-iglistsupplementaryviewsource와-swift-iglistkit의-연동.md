---
layout: post
title: "[swift] IGListSupplementaryViewSource와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

IGListKit은 Instagram에서 개발한 오픈 소스 프레임워크로, 복잡한 데이터 소스와 뷰의 관계를 관리하기 위한 강력한 기능을 제공합니다. IGListKit을 사용하면 큰 데이터 집합을 효율적으로 처리하고 강력한 컨트롤러 구조를 만들 수 있습니다.

IGListKit을 사용하는 데에는 몇 가지 클래스와 프로토콜이 있으며, 그 중 IGListSupplementaryViewSource는 추가적인 뷰 정보를 제공하는 데 사용됩니다. 이 게시물에서는 IGListSupplementaryViewSource와 Swift IGListKit의 연동 방법을 알아보겠습니다.

## IGListSupplementaryViewSource란 무엇인가요?

IGListSupplementaryViewSource는 IGListKit에서 제공하는 프로토콜로, 컬렉션 뷰에 추가적인 뷰 (서플리먼트 뷰)를 제공하는 데 사용됩니다. 이 때, 서플리먼트 뷰는 헤더, 푸터와 같은 추가적인 정보를 나타낼 수 있습니다.

## IGListSupplementaryViewSource 프로토콜 구현

IGListSupplementaryViewSource를 사용하기 위해서는 몇 가지 메서드를 구현해야 합니다. 이 메서드들은 컬렉션 뷰에게 추가적인 뷰의 크기, 설정, 등을 제공하고 관리하는 역할을 합니다.

```swift
import IGListKit

class MySupplementaryViewSource: NSObject, IGListSupplementaryViewSource {
    func supportedElementKinds() -> [String] {
        return [UICollectionElementKindSectionHeader, UICollectionElementKindSectionFooter]
    }
    
    func viewForSupplementaryElement(ofKind elementKind: String, at index: Int) -> UICollectionReusableView {
        // 서플리먼트 뷰 생성 코드
    }
    
    func sizeForSupplementaryView(ofKind elementKind: String, at index: Int) -> CGSize {
        // 서플리먼트 뷰 크기 설정 코드
    }
}
```

여기에서는 `supportedElementKinds()`, `viewForSupplementaryElement(ofKind:at:)`, `sizeForSupplementaryView(ofKind:at:)` 메서드를 구현하였습니다. `supportedElementKinds()`는 지원하는 추가적인 뷰의 종류를 배열로 반환해야 합니다. 위의 예제에서는 섹션 헤더와 섹션 푸터를 지원하도록 설정했습니다.

`viewForSupplementaryElement(ofKind:at:)` 메서드는 요청된 뷰의 종류와 위치에 따라 해당 뷰를 반환해야 합니다. 여기에서는 서플리먼트 뷰를 생성하는 코드를 작성해야 합니다.

`sizeForSupplementaryView(ofKind:at:)` 메서드는 서플리먼트 뷰의 크기를 설정하는 메서드입니다. 이 메서드에서는 각 서플리먼트 뷰의 크기를 반환해줘야 합니다.

## 컬렉션 뷰에 IGListSupplementaryViewSource 연동하기

IGListSupplementaryViewSource를 사용하기 위해선, 해당 인스턴스를 IGListAdapter에 전달해야 합니다.

```swift
import IGListKit

class MyViewController: UIViewController {
    lazy var adapter: IGListAdapter = {
        return IGListAdapter(updater: IGListAdapterUpdater(), viewController: self)
    }()

    override func viewDidLoad() {
        super.viewDidLoad()
        
        adapter.supplementaryViewSource = MySupplementaryViewSource()
    }
}
```
위의 예제 코드에서는 `adapter` 인스턴스를 생성하고, `supplementaryViewSource` 속성에 `MySupplementaryViewSource` 인스턴스를 할당하는 과정을 보여줍니다. 이렇게 하면 IGListSupplementaryViewSource와 IGListAdapter가 연결되게 됩니다.

## 결론

IGListSupplementaryViewSource는 IGListKit에서 제공하는 프로토콜로, 컬렉션 뷰에 추가적인 뷰를 제공하는 데 사용됩니다. 이 게시물에서는 IGListSupplementaryViewSource 프로토콜의 구현 방법과 IGListAdapter와의 연동 방법에 대해 알아보았습니다. IGListKit을 사용하여 강력하고 효율적인 컬렉션 뷰를 만들어보세요.

참고: 
- [IGListKit GitHub Repo](https://github.com/Instagram/IGListKit)
- [IGListKit Documentation](https://instagram.github.io/IGListKit/)
- [IGListSupplementaryViewSource Documentation](https://www.javadoc.io/doc/io.github.robbr1e.iglistkit-swift/IGListKit/latest/index.html)