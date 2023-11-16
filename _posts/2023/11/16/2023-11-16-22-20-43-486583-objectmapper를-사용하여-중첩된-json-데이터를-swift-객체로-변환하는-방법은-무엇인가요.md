---
layout: post
title: "[swift] ObjectMapper를 사용하여 중첩된 JSON 데이터를 Swift 객체로 변환하는 방법은 무엇인가요?"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

Swift에서 JSON 데이터를 Swift 객체로 변환하려면 ObjectMapper라는 라이브러리를 사용할 수 있습니다. ObjectMapper를 사용하면 JSON 데이터를 Swift 객체로 변환하고 역으로 Swift 객체를 JSON 데이터로 변환할 수 있습니다. 중첩된 JSON 데이터를 처리해야하는 경우 ObjectMapper가 제공하는 편리한 기능을 활용할 수 있습니다.

먼저 ObjectMapper를 프로젝트에 포함시키기위해 CocoaPods 또는 Swift Package Manager를 사용하여 ObjectMapper를 설치해야합니다. CocoaPods를 사용하는 경우 Podfile에 다음 줄을 추가하고 pod install을 실행합니다.

```ruby
pod 'ObjectMapper'
```

Swift Package Manager를 사용하는 경우 Package.swift 파일에 다음 종속성을 추가합니다.

```swift
dependencies: [
    .package(url: "https://github.com/tristanhimmelman/ObjectMapper.git", from: "4.2.0")
]
```

다음으로 ObjectMapper를 사용하여 중첩된 JSON 데이터를 Swift 객체로 변환하는 방법을 살펴 보겠습니다. JSON 데이터는 다음과 같다고 가정해봅시다.

```json
{
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "country": "USA"
  }
}
```

Swift 객체를 정의하고 ObjectMapper로 JSON 데이터를 매핑하는 방법은 다음과 같습니다.

```swift
import ObjectMapper

class User: Mappable {
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

// JSON 데이터를 Swift 객체로 변환
let jsonString = """
{
  "name": "John Doe",
  "age": 30,
  "address": {
    "street": "123 Main St",
    "city": "New York",
    "country": "USA"
  }
}
"""

if let user = Mapper<User>().map(JSONString: jsonString) {
    print(user.name) // John Doe
    print(user.age) // 30
    print(user.address?.street) // 123 Main St
    print(user.address?.city) // New York
    print(user.address?.country) // USA
}
```

위의 예제에서는 User 및 Address 클래스를 사용하여 Swift 객체를 정의했습니다. User 클래스는 ObjectMapper의 Mappable 프로토콜을 구현하고 mapping(map:) 함수를 사용하여 JSON 데이터와 Swift 객체 간의 매핑을 정의합니다. Address 클래스도 동일한 방식으로 정의됩니다.

JSON 데이터를 Swift 객체로 변환하기 위해 Mapper<User>().map(JSONString:) 메소드를 사용합니다. 이 메소드는 주어진 JSON 문자열을 사용하여 User 객체를 생성하고 매핑합니다. 이후에는 Swift 객체의 프로퍼티를 사용하여 JSON 데이터에 액세스할 수 있습니다.

마찬가지로 Swift 객체를 JSON 데이터로 변환 할 수도 있습니다. ObjectMapper의 toJSONString() 메소드를 사용하여 Swift 객체를 JSON 문자열로 변환 할 수 있습니다.

```swift
let user = User()
user.name = "John Doe"
user.age = 30
user.address = Address()
user.address?.street = "123 Main St"
user.address?.city = "New York"
user.address?.country = "USA"

if let jsonString = Mapper().toJSONString(user) {
    print(jsonString)
}
```

위의 예제에서는 User 객체를 생성하여 프로퍼티에 값을 설정 한 다음 ObjectMapper의 toJSONString() 메소드를 사용하여 JSON 문자열로 변환합니다.

이제 ObjectMapper를 사용하여 중첩된 JSON 데이터를 Swift 객체로 변환하는 방법에 대해 알게되었습니다. ObjectMapper를 사용하면 JSON 데이터와 Swift 객체 간에 간편하게 매핑 할 수 있으므로 Swift 개발자에게 유용한 도구가 될 수 있습니다.

참고 자료:
- [ObjectMapper GitHub 페이지](https://github.com/tristanhimmelman/ObjectMapper)