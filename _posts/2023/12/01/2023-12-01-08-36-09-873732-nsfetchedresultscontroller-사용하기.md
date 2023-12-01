---
layout: post
title: "[swift] NSFetchedResultsController 사용하기"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

Core Data는 iOS 앱에서 데이터를 관리하고 영구 저장하는 데 사용되는 프레임워크입니다. `NSFetchedResultsController`는 Core Data와 함께 사용되며, 데이터베이스의 변경 내용을 추적하고 관리하는 데 도움을 줍니다.

## 1. `NSFetchedResultsController` 소개

`NSFetchedResultsController`는 데이터베이스에서 데이터를 가져와 테이블 뷰 또는 컬렉션 뷰와 같은 UI 컴포넌트와 함께 사용할 수 있는 컨트롤러입니다. 이를 통해 데이터의 변경을 모니터링하고 자동으로 UI에 반영할 수 있습니다.

## 2. `NSFetchedResultsController` 설정하기

`NSFetchedResultsController`를 사용하려면 다음 단계를 따라야 합니다.

### 단계 1: `NSFetchRequest` 설정하기

`NSFetchRequest`는 데이터베이스에서 데이터를 가져오는 데 사용되는 객체입니다. 필요한 속성, 정렬 기준 및 필터링 조건을 설정할 수 있습니다. 아래는 간단한 예시입니다.

```swift
let request: NSFetchRequest<Item> = Item.fetchRequest()
request.sortDescriptors = [NSSortDescriptor(key: "name", ascending: true)]
request.predicate = NSPredicate(format: "category == %@", selectedCategory)
```

### 단계 2: `NSFetchedResultsController` 설정하기

`NSFetchedResultsController`를 생성하고 설정해야 합니다. 이를 통해 데이터 변경을 추적하고 UI에 업데이트를 적용할 수 있습니다. 아래는 간단한 예시입니다.

```swift
let fetchedResultsController: NSFetchedResultsController<Item> = NSFetchedResultsController(
    fetchRequest: request,
    managedObjectContext: context,
    sectionNameKeyPath: nil,
    cacheName: nil
)
fetchedResultsController.delegate = self
```

### 단계 3: `NSFetchedResultsControllerDelegate` 구현하기

`NSFetchedResultsControllerDelegate`를 구현하여 데이터 변경 시 알림을 받고 UI를 업데이트합니다. 아래는 몇 가지 주요 메서드입니다.

```swift
func controllerWillChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
    tableView.beginUpdates()
}

func controller(_ controller: NSFetchedResultsController<NSFetchRequestResult>, didChange anObject: Any, 
                at indexPath: IndexPath?, for type: NSFetchedResultsChangeType, newIndexPath: IndexPath?) {
    switch type {
    case .insert:
        tableView.insertRows(at: [newIndexPath!], with: .fade)
    case .delete:
        tableView.deleteRows(at: [indexPath!], with: .fade)
    case .update:
        tableView.reloadRows(at: [indexPath!], with: .fade)
    case .move:
        tableView.moveRow(at: indexPath!, to: newIndexPath!)
    }
}

func controllerDidChangeContent(_ controller: NSFetchedResultsController<NSFetchRequestResult>) {
    tableView.endUpdates()
}
```

## 3. `NSFetchedResultsController` 사용하기

위의 설정을 마친 후, `NSFetchedResultsController`가 데이터 변경을 모니터링하고 UI에 반영됩니다. 변경 이벤트가 발생할 때마다 `NSFetchedResultsControllerDelegate`에 구현된 메서드가 호출되어 UI가 업데이트됩니다.

```swift
do {
    try fetchedResultsController.performFetch()
    tableView.reloadData()
} catch {
    print("Error performing fetch: \(error)")
}
```

이제 `NSFetchedResultsController`를 사용하여 Core Data의 데이터를 손쉽게 관리할 수 있습니다.

## 결론

`NSFetchedResultsController`는 Core Data와 함께 사용되어 데이터베이스의 변경 내용을 추적하고 UI에 자동으로 반영하는 데 도움을 줍니다. 이를 통해 앱의 데이터 관리를 간편하게 처리할 수 있습니다.