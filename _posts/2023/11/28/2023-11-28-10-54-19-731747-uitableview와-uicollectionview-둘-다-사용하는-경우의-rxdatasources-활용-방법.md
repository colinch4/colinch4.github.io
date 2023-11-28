---
layout: post
title: "[swift] UITableView와 UICollectionView 둘 다 사용하는 경우의 RxDataSources 활용 방법"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

많은 iOS 앱에서 UITableView와 UICollectionView를 함께 사용하는 경우가 많습니다. 이 두 가지 컴포넌트는 데이터소스를 관리하는 방식이 다르기 때문에 개발자가 일관된 방식으로 데이터를 표시하고 업데이트하기 어려울 수 있습니다. 그러나 RxDataSources를 사용하면 간편하게 데이터를 관리하고 표시할 수 있습니다. 이제 UITableView와 UICollectionView 둘 다 사용하는 경우에 RxDataSources를 활용하는 방법을 살펴보겠습니다.

## RxDataSources 소개

RxDataSources는 RxSwift의 일부로 제공되는 라이브러리입니다. 이 라이브러리는 UITableView와 UICollectionView의 데이터소스를 관리하기 위한 다양한 유틸리티 클래스와 함수를 제공합니다. 이를 통해 RxSwift 스트림을 사용하여 데이터를 효율적으로 표시하고 업데이트할 수 있습니다.

## 설치

RxDataSources를 사용하기 위해 우선 RxSwift와 RxCocoa를 프로젝트에 추가해야 합니다. 이후에는 Cocoapods나 Carthage를 사용하여 RxDataSources를 설치하면 됩니다.

```swift
pod 'RxSwift'
pod 'RxCocoa'
pod 'RxDataSources'
```

## UITableView와 UICollectionView 모두 사용하기

UITableView와 UICollectionView를 함께 사용하는 경우, 각각에 대한 데이터 소스를 따로 만들어야 합니다. 아래의 예제 코드를 통해 UITableView와 UICollectionView에 RxDataSources를 적용하는 방법을 알아보겠습니다.

### UITableView

```swift
import UIKit
import RxSwift
import RxCocoa
import RxDataSources

class TableViewController: UITableViewController {
    private let disposeBag = DisposeBag()
    private let items = PublishSubject<[String]>()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // RxDataSources를 사용하여 데이터 소스 생성
        let dataSource = RxTableViewSectionedReloadDataSource<SectionModel<String, String>>(
            // 섹션 설정
            configureCell: { dataSource, tableView, indexPath, item in
                let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
                cell.textLabel?.text = item
                return cell
            }
        )
        
        // 데이터 소스 바인딩
        items.bind(to: tableView.rx.items(dataSource: dataSource))
            .disposed(by: disposeBag)
        
        // 데이터 추가
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            self.items.onNext(["Item 1", "Item 2", "Item 3"])
        }
    }
}
```

### UICollectionView

```swift
import UIKit
import RxSwift
import RxCocoa
import RxDataSources

class CollectionViewController: UICollectionViewController {
    private let disposeBag = DisposeBag()
    private let items = PublishSubject<[String]>()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // RxDataSources를 사용하여 데이터 소스 생성
        let dataSource = RxCollectionViewSectionedReloadDataSource<SectionModel<String, String>>(
            // 섹션 설정
            configureCell: { dataSource, collectionView, indexPath, item in
                let cell = collectionView.dequeueReusableCell(withReuseIdentifier: "Cell", for: indexPath)
                cell.textLabel?.text = item
                return cell
            }
        )
        
        // 데이터 소스 바인딩
        items.bind(to: collectionView.rx.items(dataSource: dataSource))
            .disposed(by: disposeBag)
        
        // 데이터 추가
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            self.items.onNext(["Item 1", "Item 2", "Item 3"])
        }
    }
}
```

## 결론

UITableView와 UICollectionView를 함께 사용하는 경우에도 RxDataSources를 사용하여 데이터를 효율적으로 관리하고 표시할 수 있습니다. RxDataSources는 복잡한 작업을 단순화하여 개발자가 더욱 효과적으로 UI를 구성하고 업데이트할 수 있도록 도와줍니다.