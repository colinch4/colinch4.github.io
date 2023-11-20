---
layout: post
title: "[swift] Swift SkeletonView CollectionView에서 사용하기"
description: " "
date: 2023-11-20
tags: [swift]
comments: true
share: true
---

CollectionView는 iOS 앱에서 아이템을 그리드 형태로 표시하는 데 사용되는 중요한 UI 요소입니다. SkeletonView라는 라이브러리를 사용하면 CollectionView를 사용할 때 스켈레톤 로딩 효과를 간단하게 구현할 수 있습니다.

## SkeletonView 소개

SkeletonView는 iOS 프로젝트에서 로딩 중에 데이터가 표시되는 대신 placeholder를 보여주는 라이브러리입니다. 이를 통해 사용자가 스켈레톤 로딩 효과를 볼 수 있고, 앱이 데이터를 불러오는 동안 사용자 경험을 향상할 수 있습니다.

## CollectionView에 SkeletonView 적용하기

1. 첫 번째로, SkeletonView 라이브러리를 프로젝트에 추가해야 합니다. 이를 위해서는 `Podfile`에 다음과 같이 추가하고 `pod install`을 실행하세요.

```swift
pod 'SkeletonView'
```

2. CollectionView의 `delegate`와 `dataSource`를 설정한 다음, SkeletonView를 적용할 CollectionViewCell을 만들어야 합니다. 이를 위해 아래의 코드를 참조하여 새로운 클래스를 만들어보세요.

```swift
import UIKit
import SkeletonView

class MyCollectionViewCell: UICollectionViewCell {
    // 셀 내부 구성요소 정의
    
    override func awakeFromNib() {
        super.awakeFromNib()
        
        // Skeleton View 설정
        self.showAnimatedGradientSkeleton()
        // Skeleton View의 효과 스타일과 속성을 설정할 수도 있습니다.
        // self.isSkeletonable = true
        // self.skeletonCornerRadius = 10
        // ...
    }
    
    func configure(with data: MyDataModel) {
        // 셀의 데이터를 설정하는 로직 구현
        // 셀이 데이터를 받아올 때 SkeletonView를 숨김 처리할 수 있습니다.
        self.hideSkeleton()
    }
}
```

3. CollectionView에서 SkeletonView가 나타날 뷰를 콜렉션뷰의 `cellForItemAt` 메서드에서 설정합니다. 스켈레톤 로딩 효과를 제거하고 데이터를 표시하는 코드와 함께 SkeletonView를 숨김 처리해야 합니다. 이렇게하면 데이터가 로딩되는 동안 스켈레톤 로딩 효과를 사용할 수 있습니다.

```swift
func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
    let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "MyCollectionViewCell", for: indexPath) as! MyCollectionViewCell
    
    cell.configure(with: myData[indexPath.row])
    
    return cell
}
```

4. 마지막으로, ViewController에서 CollectionView를 로드할 때 SkeletonView를 활성화해야 합니다. 이를 위해 아래의 코드를 참조하여 구현해보세요.

```swift
import UIKit
import SkeletonView

class MyViewController: UIViewController, UICollectionViewDelegate, UICollectionViewDataSource {
    
    @IBOutlet weak var collectionView: UICollectionView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        self.collectionView.delegate = self
        self.collectionView.dataSource = self
        
        // SkeletonView 설정
        collectionView.showSkeleton()
        // SkeletonView의 효과 스타일과 속성을 설정할 수도 있습니다.
        // collectionView.isSkeletonable = true
        // collectionView.skeletonCornerRadius = 10
        // ...
    }
}
```

이제 CollectionView에서 SkeletonView를 사용하여 스켈레톤 로딩 효과를 구현할 수 있습니다. 효과적인 스켈레톤 로딩을 제공하여 사용자 경험을 향상시킬 수 있습니다.

## 결론

SkeletonView는 iOS 앱에서 CollectionView에서 스켈레톤 로딩 효과를 구현하는 데 도움을 줄 수 있는 훌륭한 라이브러리입니다. CollectionViewCell과 CollectionView에서 SkeletonView를 설정하면 데이터 로딩 중에 사용자에게 시각적인 피드백을 제공할 수 있습니다.

## 참고 자료

- [SkeletonView 공식 문서](https://github.com/Juanpe/SkeletonView)