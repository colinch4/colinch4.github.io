---
layout: post
title: "[ios] Fetch Request와 Fetching Data"
description: " "
date: 2023-12-15
tags: [ios]
comments: true
share: true
---

메모리나 로컬 storage에서 데이터를 검색하거나 불러오는 것은 iOS 앱 개발에서 매우 중요한 작업입니다. iOS 앱에서 데이터를 불러오기 위해 Fetch Request 및 데이터 fetching 작업에 대해 알아봅시다.

## Fetch Request란 무엇인가요?
Fetch Request는 CoreData 프레임워크를 사용하여 데이터베이스로부터 데이터를 검색하는 데 사용되는 객체입니다. CoreData를 사용하면 관리되는 객체 컨텍스트에서 식별되는 데이터를 더 쉽게 검색할 수 있습니다.

## 데이터 Fetching을 위한 과정
1. **관리 객체 컨텍스트에 쿼리 작성**: Core Data의 관리 객체 컨텍스트를 사용하여 데이터베이스로 쿼리를 작성합니다.

    ```swift
    let fetchRequest: NSFetchRequest<EntityName> = EntityName.fetchRequest()
    fetchRequest.predicate = // Add predicate for filtering
    fetchRequest.sortDescriptors = // Add sort descriptors
    ```

2. **Fetch Request 실행**: 작성한 Fetch Request를 사용하여 데이터를 검색합니다.

    ```swift
    do {
        let result = try context.fetch(fetchRequest)
        for data in result {
            // Process fetched data
        }
    } catch {
        // Handle fetch error
    }
    ```

## Fetch Request를 사용한 데이터 검색
Fetch Request를 사용하여 CoreData 데이터베이스로부터 데이터를 검색하는 예시를 살펴봅시다.

```swift
let context = (UIApplication.shared.delegate as! AppDelegate).persistentContainer.viewContext
let fetchRequest: NSFetchRequest<EntityName> = EntityName.fetchRequest()
fetchRequest.predicate = NSPredicate(format: "attribute == %@", argumentArray: [value])
do {
    let result = try context.fetch(fetchRequest)
    for data in result {
        // Process fetched data
    }
} catch {
    // Handle fetch error
}
```

이제 Fetch Request 및 데이터 fetching을 통해 iOS 앱에서 데이터를 효율적으로 검색할 수 있을 것입니다. CoreData를 사용하면 데이터베이스로부터 검색된 데이터를 쉽게 다룰 수 있습니다.

더 깊게 공부하고 싶은 분들을 위해 아래 참고 자료를 확인해보세요.

## 참고 자료
- [Core Data - Apple Developer Documentation](https://developer.apple.com/documentation/coredata)
- [Core Data Programming Guide - Apple Developer Documentation](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/)
  
iOS 앱 개발을 위한 Fetch Request 및 데이터 Fetching에 대해 알아 보았습니다. 이제 데이터 검색을 통해 앱에 필요한 정보를 효율적으로 활용할 수 있을 것입니다.