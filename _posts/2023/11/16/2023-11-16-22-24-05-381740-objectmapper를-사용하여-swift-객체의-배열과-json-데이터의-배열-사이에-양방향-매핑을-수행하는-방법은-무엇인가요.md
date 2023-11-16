---
layout: post
title: "[swift] ObjectMapper를 사용하여 Swift 객체의 배열과 JSON 데이터의 배열 사이에 양방향 매핑을 수행하는 방법은 무엇인가요?"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

1. ObjectMapper 설치하기:
   ObjectMapper를 사용하기 위해 먼저 프로젝트에 ObjectMapper를 설치해야 합니다. CocoaPods를 사용한다면, Podfile에 다음과 같이 추가합니다.

   ```ruby
   pod 'ObjectMapper'
   ```

   그리고 `pod install` 명령을 터미널에서 실행하여 설치합니다.

2. Swift 객체 정의하기:
   매핑을 수행하기 위해 매핑할 Swift 객체를 정의해야 합니다. 예를 들어, 다음과 같은 `Person` 객체를 정의합니다.

   ```swift
   import ObjectMapper

   class Person: Mappable {
       var name: String?
       var age: Int?

       required init?(map: Map) {

       }

       func mapping(map: Map) {
           name <- map["name"]
           age <- map["age"]
       }
   }
   ```

   `Mappable` 프로토콜을 채택하여 ObjectMapper의 매핑 기능을 사용할 수 있습니다. `name`과 `age` 변수는 JSON 데이터의 `name`과 `age` 키와 매핑됩니다.

3. 객체 배열과 JSON 배열 간 매핑하기:
   ObjectMapper를 사용하여 객체 배열과 JSON 배열 간의 매핑을 수행하려면 다음과 같은 방법을 이용할 수 있습니다.

   - 객체 배열 → JSON 배열: `toJSONArray()` 메서드를 사용하여 객체 배열을 JSON 배열로 변환할 수 있습니다.

     ```swift
     let people: [Person] = [...] // 객체 배열 초기화
     let json = Mapper<Person>().toJSONArray(people)
     ```

   - JSON 배열 → 객체 배열: `mapArray(JSONString:)` 메서드를 사용하여 JSON 배열을 객체 배열로 변환할 수 있습니다.

     ```swift
     let jsonString = "[{\"name\":\"Alice\",\"age\":25},{\"name\":\"Bob\",\"age\":30}]"
     let people = Mapper<Person>().mapArray(JSONString: jsonString)
     ```

     이때, `JSONString:` 뒤에는 JSON 문자열이 입력되어야 합니다.

   각각의 방법은 ObjectMapper를 사용하여 Swift 객체 배열과 JSON 데이터 배열 간의 양방향 매핑을 손쉽게 수행할 수 있게 해줍니다.

자세한 내용은 ObjectMapper의 문서를 참조하세요. [참조 링크](https://github.com/tristanhimmelman/ObjectMapper)