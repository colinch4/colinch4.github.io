---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 중첩된 JSON 데이터 매핑하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 ObjectMapper 라이브러리를 사용하여 중첩된 JSON 데이터를 매핑하는 방법에 대해 알아보겠습니다. ObjectMapper는 매우 강력하고 유용한 라이브러리로, JSON 데이터를 Swift 객체로 변환하거나 Swift 객체를 JSON 데이터로 변환하는 작업을 쉽게 처리할 수 있습니다.

## ObjectMapper 설치하기

먼저 ObjectMapper를 프로젝트에 설치해야 합니다. Cocoapods를 사용하는 경우, Podfile에 다음과 같이 ObjectMapper를 추가하세요.

```
pod 'ObjectMapper'
```

설치 후, 프로젝트를 업데이트합니다.

```
pod install
```

CocoaPods를 사용하지 않는 경우, ObjectMapper의 GitHub 저장소에서 소스 코드를 다운로드한 후 프로젝트에 수동으로 추가할 수도 있습니다.

## JSON 데이터 모델링

JSON 데이터를 매핑하기 전에, Swift 클래스를 생성하여 JSON 데이터의 구조를 모델링해야 합니다. 예를 들어, 다음과 같은 JSON 데이터를 매핑한다고 가정해봅시다.

```json
{
    "name": "John",
    "age": 25,
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "country": "USA"
    }
}
```

이 JSON 데이터를 매핑하기 위해, 다음과 같이 Swift 클래스를 만듭니다.

```swift
import ObjectMapper

class Person: Mappable {
    var name: String?
    var age: Int?
    var address: Address?

    required init?(map: Map) {
    }

    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
        address <- map["address"]
    }
}

class Address: Mappable {
    var street: String?
    var city: String?
    var country: String?

    required init?(map: Map) {
    }

    func mapping(map: Map) {
        street <- map["street"]
        city <- map["city"]
        country <- map["country"]
    }
}
```

위의 코드에서, Person 클래스와 Address 클래스는 ObjectMapper의 Mappable 프로토콜을 따릅니다. Mappable 프로토콜은 매핑 작업에 필요한 초기화 및 매핑 메서드를 정의하는데 사용됩니다. 

## JSON 데이터 매핑하기

이제 ObjectMapper를 사용하여 JSON 데이터를 매핑해보겠습니다. 다음은 JSON 데이터를 Swift 클래스로 매핑하는 코드입니다.

```swift
import ObjectMapper

let jsonString = """
    {
        "name": "John",
        "age": 25,
        "address": {
            "street": "123 Main St",
            "city": "New York",
            "country": "USA"
        }
    }
"""

if let person = Mapper<Person>().map(JSONString: jsonString) {
    print(person.name) // John
    print(person.age) // 25
    print(person.address?.street) // 123 Main St
    print(person.address?.city) // New York
    print(person.address?.country) // USA
} else {
    print("Mapping failed")
}
```

위의 코드에서, JSON 데이터를 문자열로 표현한 뒤 `Mapper<Person>().map(JSONString: jsonString)` 메서드를 사용하여 JSON 데이터를 Person 객체로 매핑합니다. 매핑이 성공하면 해당 객체의 속성에 액세스할 수 있습니다.

## 결론

이제 Swift에서 ObjectMapper를 사용하여 중첩된 JSON 데이터를 간단하게 매핑하는 방법을 알아보았습니다. ObjectMapper를 사용하면 복잡한 JSON 데이터를 Swift 객체로 쉽게 변환할 수 있습니다. 더 많은 ObjectMapper의 기능과 세부 사항은 [공식 문서](https://github.com/tristanhimmelman/ObjectMapper)를 참조하시기 바랍니다.