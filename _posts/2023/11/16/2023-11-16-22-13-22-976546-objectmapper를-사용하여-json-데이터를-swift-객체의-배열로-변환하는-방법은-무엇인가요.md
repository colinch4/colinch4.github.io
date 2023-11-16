---
layout: post
title: "[swift] ObjectMapper를 사용하여 JSON 데이터를 Swift 객체의 배열로 변환하는 방법은 무엇인가요?"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

1. ObjectMapper 설치: 
   ObjectMapper는 Swift에서 JSON 데이터를 쉽게 매핑할 수 있도록 도와주는 라이브러리입니다. CocoaPods를 사용하여 ObjectMapper를 프로젝트에 추가하세요. Podfile에 다음 라인을 추가한 후, 터미널에서 `pod install`을 실행하세요:

   ```
   pod 'ObjectMapper'
   ```

2. Swift 객체 구현:
   ObjectMapper를 사용하려는 Swift 객체를 구현합니다. 예를 들어, 다음과 같이 User 객체를 구현해봅시다:

   ```swift
   import ObjectMapper

   struct User: Mappable {
       var name: String?
       var age: Int?

       init?(map: Map) {}

       mutating func mapping(map: Map) {
           name <- map["name"]
           age <- map["age"]
       }
   }
   ```

3. JSON 데이터를 Swift 객체로 변환:
   ObjectMapper를 사용하여 JSON 데이터를 Swift 객체의 배열로 변환하는 방법은 다음과 같습니다:

   ```swift
   import ObjectMapper

   // JSON 데이터 (예시)
   let json = """
   [
       {
           "name": "John",
           "age": 25
       },
       {
           "name": "Jane",
           "age": 30
       }
   ]
   """

   if let data = json.data(using: .utf8) {
       do {
           // ObjectMapper를 사용하여 JSON 데이터를 Swift 객체의 배열로 변환
           let users = try JSONDecoder().decode([User].self, from: data)
           // 변환된 객체 사용
           for user in users {
               print(user.name)
               print(user.age)
           }
       } catch {
           print("Error: \(error.localizedDescription)")
       }
   }
   ```

   위의 예제에서는 ObjectMapper에서 제공하는 `JSONDecoder`를 사용하여 JSON 데이터를 Swift 객체의 배열로 변환합니다. 변환된 객체를 사용하여 이름과 나이를 출력하는 예시가 포함되어 있습니다.

   이제 ObjectMapper를 사용하여 JSON 데이터를 Swift 객체의 배열로 변환하는 방법을 알게 되었습니다! 자세한 내용은 [ObjectMapper GitHub 저장소](https://github.com/tristanhimmelman/ObjectMapper)를 참조하세요.