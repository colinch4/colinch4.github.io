---
layout: post
title: "[swift] ObjectMapper를 사용하여 JSON 데이터와 Swift 객체 간에 데이터를 어떻게 변환할 수 있나요?"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

많은 경우에, JSON 데이터와 Swift 객체 간의 데이터 변환이 필요합니다. 이를 위해 Swift에서는 ObjectMapper라는 유용한 라이브러리를 사용할 수 있습니다. ObjectMapper는 JSON 데이터를 Swift 객체로 매핑하고, Swift 객체를 JSON 데이터로 직렬화하는 작업을 쉽게 수행할 수 있는 도구입니다.

다음은 ObjectMapper를 사용하여 JSON 데이터와 Swift 객체 간의 데이터 변환 방법입니다.

1. ObjectMapper 설치하기
   ObjectMapper를 사용하려면 프로젝트에 ObjectMapper 라이브러리를 설치해야 합니다. CocoaPods를 사용하신다면, Podfile에 다음과 같이 추가하고 `pod install` 명령을 실행합니다.

   ```shell
   pod 'ObjectMapper'
   ```

   Carthage나 Swift Package Manager를 사용하신다면 해당 도구의 문서를 참조하여 ObjectMapper를 설치하세요.

2. Swift 객체 정의하기
   첫 번째 단계는 JSON 데이터를 매핑할 Swift 객체의 구조를 정의하는 것입니다. 예를 들어, 다음과 같은 JSON 데이터가 있다고 가정해봅시다.

   ```json
   {
     "name": "John Doe",
     "age": 30,
     "email": "john.doe@example.com"
   }
   ```

   해당 JSON 데이터를 매핑할 Swift 객체를 정의해봅시다.

   ```swift
   import ObjectMapper

   class Person: Mappable {
       var name: String?
       var age: Int?
       var email: String?

       required init?(map: Map) {
       }

       func mapping(map: Map) {
           name <- map["name"]
           age <- map["age"]
           email <- map["email"]
       }
   }
   ```

   `Mappable` 프로토콜을 채택한 `Person` 클래스를 정의합니다. `mapping` 메서드를 사용하여 각 프로퍼티를 JSON 데이터의 키에 매핑시킵니다.

3. JSON 데이터를 Swift 객체로 변환하기
   ObjectMapper를 사용하여 JSON 데이터를 Swift 객체로 변환하는 방법은 간단합니다. 다음과 같이 ObjectMapper의 `map` 메서드를 사용하면 됩니다.

   ```swift
   let json = """
   {
     "name": "John Doe",
     "age": 30,
     "email": "john.doe@example.com"
   }
   """

   if let person = Mapper<Person>().map(JSONString: json) {
       print(person.name) // John Doe
       print(person.age) // 30
       print(person.email) // john.doe@example.com
   }
   ```

   `JSONString` 매개변수에는 변환할 JSON 데이터를 전달하면 됩니다. 변환된 객체를 사용하여 원하는 작업을 수행할 수 있습니다.

4. Swift 객체를 JSON 데이터로 직렬화하기
   ObjectMapper를 사용하여 Swift 객체를 JSON 데이터로 직렬화하는 방법도 간단합니다. `toJSON` 메서드를 사용하면 됩니다.

   ```swift
   let person = Person()
   person.name = "John Doe"
   person.age = 30
   person.email = "john.doe@example.com"

   if let jsonString = person.toJSONString() {
       print(jsonString)
   }
   ```

   `toJSONString` 메서드는 Swift 객체를 JSON 문자열로 직렬화합니다. 직렬화된 JSON 문자열을 사용하여 원하는 작업을 수행할 수 있습니다.

위에서 설명한 방법을 사용하여 ObjectMapper를 사용하여 JSON 데이터와 Swift 객체 간에 데이터를 변환할 수 있습니다. ObjectMapper는 다양한 매핑 기능을 제공하므로 복잡한 데이터 구조도 간편하게 매핑할 수 있습니다. ObjectMapper의 자세한 내용은 [공식 문서](https://github.com/tristanhimmelman/ObjectMapper)를 참조하세요.