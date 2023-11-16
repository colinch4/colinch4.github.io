---
layout: post
title: "[swift] SwiftyJSON을 사용하여 JSON 데이터를 CoreData에 저장하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 개요
이번 글에서는 SwiftyJSON 라이브러리를 사용하여 JSON 데이터를 파싱하고 CoreData를 이용하여 데이터를 저장하는 방법을 알아보겠습니다. Swift에는 Codable이라는 기능이 있지만, JSON 데이터의 구조가 복잡하거나 중첩된 경우에는 SwiftyJSON과 함께 사용하면 편리합니다.

## SwiftyJSON 소개
SwiftyJSON은 JSON 데이터를 쉽게 다룰 수 있도록 도와주는 Swift 라이브러리입니다. SwiftyJSON을 사용하면 JSON 데이터를 파싱하고 필요한 값을 추출하기 위해 번거로운 작업들을 단순화할 수 있습니다.

## 설치하기
SwiftyJSON은 CocoaPods를 통해 설치할 수 있습니다. 프로젝트의 Podfile에 다음 코드를 추가하고 `pod install` 명령어를 실행하면 됩니다.

```swift
pod 'SwiftyJSON'
```

## CoreData 설정하기
CoreData를 사용하기 위해선 프로젝트에 CoreData를 활성화해야 합니다. 프로젝트 타겟을 선택하고 "Capabilities" 탭으로 이동한 후 "Core Data" 스위치를 켜주면 됩니다. CoreData를 활성화한 후, 데이터 모델을 생성하여 필요한 엔티티와 속성을 정의해야 합니다.

## JSON 데이터 파싱하기
SwiftyJSON을 사용하여 JSON 데이터를 파싱하기 위해 다음과 같은 단계를 거칩니다.

1. SwiftyJSON을 import 합니다.
```swift
import SwiftyJSON
```
2. JSON 데이터를 먼저 String 형태로 변환합니다.
```swift
let jsonString = """
{
    "name": "John",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}
"""

guard let jsonData = jsonString.data(using: .utf8) else {
    return
}
```
3. JSON 데이터를 SwiftyJSON 객체로 변환합니다.
```swift
let json = try! JSON(data: jsonData)
```
4. 필요한 값들을 추출합니다.
```swift
let name = json["name"].stringValue
let age = json["age"].intValue
let city = json["address"]["city"].stringValue
```

## CoreData에 데이터 저장하기
JSON 데이터를 파싱한 후에는 CoreData를 이용하여 데이터를 저장할 수 있습니다. CoreData는 관계형 데이터베이스로, 데이터를 영구적으로 저장하고 관리하는 기능을 제공합니다.

CoreData를 사용하여 데이터를 저장하기 위해 다음과 같은 단계를 거칩니다.

1. CoreData의 데이터 컨텍스트를 가져옵니다.
```swift
let appDelegate = UIApplication.shared.delegate as! AppDelegate
let context = appDelegate.persistentContainer.viewContext
```
2. 새로운 데이터 엔티티를 생성하고 값을 설정합니다.
```swift
let entity = NSEntityDescription.entity(forEntityName: "Person", in: context)!
let person = NSManagedObject(entity: entity, insertInto: context)
person.setValue(name, forKey: "name")
person.setValue(age, forKey: "age")
person.setValue(city, forKey: "city")
```
3. 데이터를 저장합니다.
```swift
do {
    try context.save()
} catch let error as NSError {
    print("Could not save. \(error), \(error.userInfo)")
}
```

## 결론
이번 글에서는 SwiftyJSON을 사용하여 JSON 데이터를 파싱하고 CoreData를 이용하여 데이터를 저장하는 방법을 알아보았습니다. SwiftyJSON은 JSON 데이터의 파싱을 간편하게 해주는 라이브러리이며, CoreData는 데이터를 영구적으로 저장하고 관리하는데 사용됩니다. 이러한 기술들을 함께 활용하면 더욱 효과적인 데이터 관리를 할 수 있습니다.

참고: [SwiftyJSON GitHub](https://github.com/SwiftyJSON/SwiftyJSON), [CoreData Apple Developer Documentation](https://developer.apple.com/documentation/coredata)