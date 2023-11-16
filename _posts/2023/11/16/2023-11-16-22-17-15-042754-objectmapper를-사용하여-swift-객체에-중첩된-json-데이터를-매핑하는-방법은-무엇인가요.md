---
layout: post
title: "[swift] ObjectMapper를 사용하여 Swift 객체에 중첩된 JSON 데이터를 매핑하는 방법은 무엇인가요?"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

1. ObjectMapper 설치하기
   - ObjectMapper를 사용하려면 먼저 프로젝트에 ObjectMapper를 설치해야 합니다. 이를 위해 CocoaPods를 사용할 수 있습니다. Podfile에 다음과 같이 추가한 후, terminal에서 `pod install` 명령을 실행하세요:

   ```
   pod 'ObjectMapper', '~> 4.0'
   ```

2. 모델 클래스 생성하기
   - ObjectMapper를 사용하여 JSON 데이터를 매핑하기 위해 모델 클래스를 생성해야 합니다. 중첩된 JSON 데이터의 구조에 맞추어 필요한 속성과 타입을 정의해야 합니다.

   예를 들어, 다음과 같은 JSON 데이터가 있다고 가정해 봅시다:

   ```json
   {
       "name": "John",
       "age": 25,
       "address": {
           "street": "123 ABC Street",
           "city": "New York"
       }
   }
   ```

   Swift에서는 다음과 같이 모델 클래스를 생성할 수 있습니다:

   ```swift
   import ObjectMapper

   class Person: Mappable {
       var name: String?
       var age: Int?
       var address: Address?

       required init?(map: Map) {}

       func mapping(map: Map) {
           name <- map["name"]
           age <- map["age"]
           address <- map["address"]
       }
   }

   class Address: Mappable {
       var street: String?
       var city: String?

       required init?(map: Map) {}

       func mapping(map: Map) {
           street <- map["street"]
           city <- map["city"]
       }
   }
   ```

3. JSON 데이터를 모델로 매핑하기
   - ObjectMapper를 사용하여 JSON 데이터를 생성한 모델 객체로 매핑할 수 있습니다. 예를 들어, 다음과 같은 JSON 데이터가 있다고 가정해 봅시다:

   ```swift
   let json = """
   {
       "name": "John",
       "age": 25,
       "address": {
           "street": "123 ABC Street",
           "city": "New York"
       }
   }
   """
   ```

   다음과 같이 ObjectMapper를 사용하여 JSON 데이터를 모델로 매핑할 수 있습니다:

   ```swift
   if let person = Person(JSONString: json) {
       print(person.name) // 출력: John
       print(person.age) // 출력: 25
       print(person.address?.street) // 출력: 123 ABC Street
       print(person.address?.city) // 출력: New York
   }
   ```

   이렇게 매핑된 모델 객체를 사용하여 필요한 작업을 수행할 수 있습니다.

이제 Swift 객체에 중첩된 JSON 데이터를 ObjectMapper를 사용하여 매핑하는 방법을 알게 되었습니다. ObjectMapper는 많은 강력한 기능을 제공하므로, 자세한 내용은 [ObjectMapper GitHub 저장소](https://github.com/tristanhimmelman/ObjectMapper)에서 확인할 수 있습니다.