---
layout: post
title: "[swift] IGListCollectionViewDelegateLayout와 Swift IGListKit의 연동"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 소개
그동안 시각적인 컬렉션 뷰를 구현하기 위해 UICollectionViewLayout을 사용해오셨을 것입니다. 그러나 이렇게 하려면 많은 코드와 복잡한 로직을 작성해야 했습니다. 이에 대한 대안으로 Airbnb에서 개발한 IGListKit이라는 오픈 소스 라이브러리가 있습니다. IGListKit은 컬렉션 뷰를 처리하는데 필요한 많은 기능을 제공하며, IGListCollectionViewDelegateLayout은 이 라이브러리와 함께 사용하는데 특화된 UICollectionViewLayout을 의미합니다.

## Swift IGListKit의 기본 설치
Swift IGListKit을 사용하기 위해 CocoaPods를 이용하여 프로젝트에 추가해야 합니다. 터미널에서 프로젝트 루트 경로로 이동한 후, 아래의 명령을 실행하면 됩니다.

```bash
$ pod init
```

그리고 생성된 **Podfile**에 아래의 내용을 추가합니다.

```ruby
pod 'IGListKit'
```

마지막으로 아래의 명령을 실행하여 IGListKit을 설치합니다.

```bash
$ pod install
```

## IGListCollectionViewDelegateLayout 사용하기
IGListCollectionViewDelegateLayout은 IGListKit에서 컬렉션 뷰를 구성하는데 사용되는 레이아웃 클래스입니다. 이 레이아웃 클래스는 IGListKit을 위해 특별히 설계되었으며, IGListCollectionViewDelegateLayout과 함께 컬렉션 뷰를 사용하면 IGListKit의 많은 장점을 활용할 수 있습니다.

### IGListCollectionViewDelegateLayout의 주요 기능
1. 동적인 셀 크기 지원
2. 유연한 셀 배치
3. 일관된 섹션 삽입 및 삭제
4. 섹션 인터렉션 지원

### 사용 예시
먼저, IGListCollectionViewDelegateLayout을 사용하기 위해 UICollectionViewLayout을 대체해야 합니다. 다음과 같이 코드를 작성합니다.

```swift
class MyViewController: UIViewController {
    
    let collectionView = UICollectionView(frame: .zero, collectionViewLayout: UICollectionViewFlowLayout())
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // IGListCollectionViewDelegateLayout 설정
        collectionView.collectionViewLayout = ListCollectionViewLayout(stickyHeaders: false, topContentInset: 0, stretchToEdge: true)
    }
}
```

위 코드에서는 ListCollectionViewLayout을 이용하여 IGListCollectionViewDelegateLayout을 사용하고 있습니다. 이렇게 설정하면 IGListKit의 많은 장점을 사용할 수 있습니다.

### 활용 예시
IGListCollectionViewDelegateLayout을 사용하면 다양한 뷰 및 셀의 크기를 동적으로 조정할 수 있습니다. 또한 섹션의 배치와 인터렉션을 통해 사용자 경험을 향상시킬 수 있습니다.

아래는 섹션별로 다른 배치 스타일을 가지는 예제 코드입니다.

```swift
extension MyViewController: ListAdapterDataSource {
    
    func objects(for listAdapter: ListAdapter) -> [ListDiffable] {
        return myDataArray
    }
    
    func listAdapter(_ listAdapter: ListAdapter, sectionControllerFor object: Any) -> ListSectionController {
        return MySectionController()
}

class MySectionController: ListSectionController {
    
    override init() {
        super.init()
        inset = UIEdgeInsets(top: 10, left: 10, bottom: 10, right: 10)
        minimumLineSpacing = 10
        minimumInteritemSpacing = 10
    }
    
    override func cellForItem(at index: Int) -> UICollectionViewCell {
        // 셀을 반환하는 코드
    }
    
    override func sizeForItem(at index: Int) -> CGSize {
        // 셀 크기를 반환하는 코드
    }
}
```

위 코드는 IGListCollectionViewDelegateLayout을 사용하여 섹션에 다양한 배치 스타일을 적용한 예시입니다. IGListKit을 사용하면 이와 같은 복잡한 레이아웃 로직을 간단하게 구현할 수 있습니다.

## 요약
IGListCollectionViewDelegateLayout는 IGListKit과 함께 사용되는 독특한 UICollectionViewLayout 클래스입니다. IGListKit의 장점을 활용하면서 유연하고 동적인 셀 크기, 섹션 배치 및 인터렉션을 구현할 수 있습니다. IGListCollectionViewDelegateLayout을 사용하여 시각적인 컬렉션 뷰를 효율적으로 구현해보세요.

## 참고 자료
- [IGListKit GitHub 페이지](https://github.com/Instagram/IGListKit)
- [IGListCollectionViewDelegateLayout 공식 문서](https://instagram.github.io/IGListKit/Classes/IGListCollectionViewDelegateLayout.html)