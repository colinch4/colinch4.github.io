---
layout: post
title: "[swift] RxDataSources와 UICollectionView의 연동 방법"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

## 소개
RxDataSources는 RxSwift의 일부로, UITableView와 UICollectionView와 같은 데이터 소스를 관리하기 위한 라이브러리입니다. 이 라이브러리를 사용하면 데이터 소스와 RxSwift를 조합하여 쉽게 UI 요소를 업데이트할 수 있습니다. 이번 포스트에서는 RxDataSources를 사용하여 UICollectionView와 연동하는 방법을 알아보겠습니다.

## 설치
RxDataSources를 사용하기 위해 우선 RxSwift와 RxCocoa를 프로젝트에 추가해야 합니다. CocoaPods를 사용한다면 Podfile에 다음과 같은 의존성을 추가합니다.

```
pod 'RxSwift'
pod 'RxCocoa'
pod 'RxDataSources'
```

RxSwift, RxCocoa, RxDataSources를 설치하기 위해 터미널에서 `pod install` 명령을 실행하면 됩니다.

## 사용 방법
1. UICollectionViewDelegateFlowLayout을 구현합니다.
```swift
extension YourViewController: UICollectionViewDelegateFlowLayout {
    // UICollectionViewDelegateFlowLayout의 필요한 메소드들을 구현합니다.
    // ...
}
```

2. UICollectionView에 필요한 DataSource와 Delegate를 선언합니다.
```swift
let dataSource = RxCollectionViewSectionedReloadDataSource<SectionModel<String, YourItemType>>(
    configureCell: { dataSource, collectionView, indexPath, item in
        // 셀을 구성하는 코드를 작성합니다.
    },
    configureSupplementaryView: { dataSource, collectionView, kind, indexPath in
        // 보조 뷰를 구성하는 코드를 작성합니다.
        // 예: 헤더 뷰, 푸터 뷰
    })

let delegate = UICollectionViewDelegateFlowLayoutProxy(delegate: self)
```

3. UICollectionView에 DataSource와 Delegate를 설정합니다.
```swift
collectionView.rx.setDelegate(delegate).disposed(by: disposeBag)
collectionView.rx.modelSelected(YourItemType.self).subscribe(onNext: { item in
    // 셀 선택 이벤트 처리를 작성합니다.
}).disposed(by: disposeBag)

let items = Observable.just([
    SectionModel(model: "Section 1", items: [item1, item2, item3]),
    SectionModel(model: "Section 2", items: [item4, item5, item6])
])

// 데이터 소스를 적용합니다.
items.bind(to: collectionView.rx.items(dataSource: dataSource)).disposed(by: disposeBag)
```

4. 필요한 경우 UICollectionViewDelegateFlowLayout의 메소드를 구현하고, 레이아웃을 조정합니다.
```swift
extension YourViewController: UICollectionViewDelegateFlowLayout {
    func collectionView(_ collectionView: UICollectionView, layout collectionViewLayout: UICollectionViewLayout, sizeForItemAt indexPath: IndexPath) -> CGSize {
        // 셀의 사이즈를 반환하는 코드를 작성합니다.
    }
}
```

## 결론
이제 RxDataSources를 사용하여 UICollectionView를 쉽게 관리하는 방법을 알게 되었습니다. RxDataSources는 데이터 소스 관리를 단순화하는 강력한 도구이며, RxSwift와 조합하여 앱의 반응형 UI를 구현하는 데 효과적으로 사용할 수 있습니다.

## 참고자료
- [RxSwift](https://github.com/ReactiveX/RxSwift)
- [RxDataSources](https://github.com/RxSwiftCommunity/RxDataSources)