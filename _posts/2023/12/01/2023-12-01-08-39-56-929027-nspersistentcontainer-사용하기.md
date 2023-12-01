---
layout: post
title: "[swift] NSPersistentContainer 사용하기"
description: " "
date: 2023-12-01
tags: [swift]
comments: true
share: true
---

앱을 개발하다보면 데이터베이스와의 연동이 필요할 때가 있습니다. Swift에서는 Core Data를 사용하여 데이터베이스 작업을 수행할 수 있습니다. 이번 글에서는 NSPersistentContainer를 사용하여 간단하게 데이터베이스를 생성하고 관리하는 방법에 대해 알아보겠습니다.

## Core Data란?
Core Data는 애플리케이션의 객체 그래프를 영구 저장하는 프레임워크입니다. 데이터를 객체로 관리하고, 이를 영구 저장소에 저장하고 검색하는 기능을 제공합니다. CoreData는 주로 관계형 데이터베이스의 개체 관계 매핑 기술(Object Relational Mapping)을 사용하여 데이터를 관리합니다.

## NSPersistentContainer란?
NSPersistentContainer는 Core Data 스택을 구성하는 핵심 클래스입니다. 데이터베이스를 설정하고 관리하는 역할을 담당합니다. NSPersistentContainer를 사용하면 데이터베이스를 생성 및 업데이트하는 작업을 간단하게 처리할 수 있습니다.

다음은 NSPersistentContainer를 사용하여 데이터베이스 스택을 설정하는 예제 코드입니다.

```swift
import CoreData

lazy var persistentContainer: NSPersistentContainer = {
    let container = NSPersistentContainer(name: "YourDataModelName")
    container.loadPersistentStores(completionHandler: { (storeDescription, error) in
        if let error = error as NSError? {
            // 데이터베이스 로딩 중 에러 처리
        }
    }
    return container
}()
```

위 코드에서 `"YourDataModelName"`은 데이터 모델의 이름으로 수정해야 합니다. 데이터 모델 파일의 확장자는 `.xcdatamodeld`입니다.

## 데이터베이스 사용하기
NSPersistentContainer를 사용하면 다음과 같이 데이터베이스를 사용할 수 있습니다.

```swift
let context = persistentContainer.viewContext

// 데이터 저장 예제
let entity = NSEntityDescription.entity(forEntityName: "Person", in: context)!
let person = NSManagedObject(entity: entity, insertInto: context)
person.setValue("John Doe", forKey: "name")

do {
    try context.save()
} catch {
    // 데이터 저장 중 에러 처리
}

// 데이터 조회 예제
let fetchRequest = NSFetchRequest<NSManagedObject>(entityName: "Person")

do {
    let people = try context.fetch(fetchRequest)
    for person in people {
        let name = person.value(forKey: "name") as? String
        print(name)
    }
} catch {
    // 데이터 조회 중 에러 처리
}
```

데이터 저장 및 조회는 `NSManagedObjectContext`를 사용하여 처리할 수 있습니다. 위 예제에서는 `viewContext`를 사용하였습니다.

## 정리
이번 포스트에서는 NSPersistentContainer를 사용하여 Core Data를 초기화하고 데이터베이스 작업을 수행하는 방법에 대해 알아보았습니다. NSPersistentContainer를 사용하면 Core Data를 간편하게 활용할 수 있으며, 데이터베이스 작업을 효율적으로 처리할 수 있습니다.

더 많은 내용은 [Apple Documentation](https://developer.apple.com/documentation/coredata/nspersistentcontainer)을 참고하시기 바랍니다.