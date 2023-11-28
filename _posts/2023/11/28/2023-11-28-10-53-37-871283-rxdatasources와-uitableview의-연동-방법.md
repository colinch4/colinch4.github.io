---
layout: post
title: "[swift] RxDataSources와 UITableView의 연동 방법"
description: " "
date: 2023-11-28
tags: [swift]
comments: true
share: true
---

UITableView와 RxSwift를 함께 사용하여 데이터를 동적으로 표시하는 경우에는 RxDataSources를 사용하는 것이 좋습니다. RxDataSources는 UITableView를 관리하기위한 유용한 기능을 제공하여 코드를 간결하게 유지하면서 데이터를 관리 할 수 있습니다.

## RxDataSources 설치

RxDataSources를 사용하기 위해서는 먼저 RxSwift와 RxCocoa를 설치해야합니다. CocoaPods를 사용하고 있다면 Podfile에 다음과 같은 종속성을 추가하십시오:

```swift
pod 'RxSwift', '~> 6.0'
pod 'RxCocoa', '~> 6.0'
pod 'RxDataSources', '~> 6.0'
```

그런 다음, 터미널에서 `pod install` 명령어를 실행하여 RxDataSources를 설치합니다.

## RxDataSources 사용하기

RxDataSources를 사용하여 UITableView와 연동하려면 다음의 단계를 따르세요:

1. UITableView에 대한 dataSource를 정의합니다. 이는 UITableViewDataSource 프로토콜을 준수하는 클래스입니다. 이 클래스는 tableView(_:cellForRowAt:) 메서드를 구현하여 각 행에 대한 셀을 반환해야합니다.

```swift
class MyDataSource: NSObject, UITableViewDataSource {
    // 각 행에 대한 셀을 반환하는 메서드 구현
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        // 셀 반환
    }
}
```

2. RxDataSources를 사용하여 데이터를 바인딩하고 UITableView에 연결합니다. 이에는 `items` observable, `configureCell` 클로저 및 `animated` 파라미터가 필요합니다.

```swift
import RxSwift
import RxCocoa
import RxDataSources

// 테스트 데이터
let items = Observable.just([
    "Item 1",
    "Item 2",
    "Item 3"
])

let dataSource = RxTableViewSectionedReloadDataSource<SectionModel<String, String>>(
    configureCell: { dataSource, tableView, indexPath, item in
        let cell = tableView.dequeueReusableCell(withIdentifier: "Cell", for: indexPath)
        cell.textLabel?.text = item
        return cell
    })

items
    .bind(to: tableView.rx.items(dataSource: dataSource))
    .disposed(by: disposeBag)
```

위의 예제에서 `SectionModel<String, String>`은 섹션 헤더와 아이템을 나타내는 모델입니다.

3. 데이터를 변경하려면 새로운 데이터로 observable을 업데이트하거나 append, insert, delete 작업 등을 수행할 수 있습니다.

```swift
let newItems = ["New Item 1", "New Item 2"]
items.onNext(newItems)
```

위의 예제에서는 단일 섹션을 사용했지만, RxDataSources를 사용하여 다른 유형의 테이블 뷰 (ex: 다중 섹션, 세부 정보 셀)와 함께 작업할 수도 있습니다. 자세한 내용은 RxDataSources GitHub 페이지를 참조하십시오.

## 결론

RxDataSources를 사용하여 UITableView와 연동하면 데이터 표시 및 관리가 훨씬 간편해집니다. 위의 단계를 따라하면 RxDataSources를 시작할 수 있고, 다양한 유형의 데이터 표시를 구현할 수 있습니다.