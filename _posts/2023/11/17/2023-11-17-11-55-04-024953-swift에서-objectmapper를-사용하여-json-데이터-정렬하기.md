---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터 정렬하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 ObjectMapper는 JSON 데이터를 객체로 매핑하는 데 사용되는 매우 강력한 라이브러리입니다. 이 라이브러리를 사용하면 JSON 데이터를 쉽게 객체로 변환하고, 객체를 다시 JSON 데이터로 변환할 수 있습니다. 이번에는 ObjectMapper를 사용하여 JSON 데이터를 정렬하는 방법에 대해 알아보겠습니다.

## 1. ObjectMapper 라이브러리 추가하기
먼저, ObjectMapper 라이브러리를 프로젝트에 추가해야 합니다. ObjectMapper를 사용하기 위해 CocoaPods를 설치하고, Podfile에 아래의 라인을 추가합니다.

```ruby
pod 'ObjectMapper'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 다운로드하고 프로젝트에 추가합니다.

## 2. JSON 데이터를 객체로 변환하기
우선, ObjectMapper를 사용하여 JSON 데이터를 객체로 변환하는 방법에 대해 알아보겠습니다. 아래는 JSON 데이터를 매핑할 User 클래스의 예시입니다.

```swift
import ObjectMapper

class User: Mappable {
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

위의 예시에서는 User 클래스가 Mappable 프로토콜을 채택하고, `name`과 `age` 프로퍼티를 매핑하도록 설정되어 있습니다. 이제 ObjectMapper를 사용하여 JSON 데이터를 객체로 변환해보겠습니다.

```swift
import ObjectMapper

let jsonString = "{\"name\":\"John\",\"age\":25}"
if let user = Mapper<User>().map(JSONString: jsonString) {
    print("User name: \(user.name ?? "")")
    print("User age: \(user.age ?? 0)")
}
```

위의 코드는 전달된 jsonString을 사용하여 User 객체를 생성하고, 객체의 프로퍼티를 통해 JSON 데이터를 출력합니다.

## 3. 객체를 JSON 데이터로 변환하기
이번에는 ObjectMapper를 사용하여 객체를 JSON 데이터로 변환하는 방법에 대해 알아보겠습니다. 아래의 예시는 User 객체를 JSON 데이터로 변환하는 방법을 보여줍니다.

```swift
import ObjectMapper

let user = User()
user.name = "John"
user.age = 25

if let jsonString = Mapper().toJSONString(user) {
    print("JSON String: \(jsonString)")
}
```

위의 코드는 User 객체를 사용하여 JSON 데이터를 생성합니다. `toJSONString` 메서드를 사용하여 User 객체를 JSON 문자열로 변환하고, 변환된 JSON 문자열을 출력합니다.

## 4. JSON 데이터 정렬하기
JSON 데이터를 정렬하려면 ObjectMapper의 `sortKeys` 옵션을 사용하면 됩니다. 아래의 예시는 `sortKeys` 옵션을 사용하여 JSON 데이터를 정렬하는 방법을 보여줍니다.

```swift
import ObjectMapper

let jsonString = "{\"b\":\"456\",\"a\":\"123\"}"
if let sortedJSON = Mapper().parseJSONString(jsonString, keyMapping: ["a", "b"]) {
    print("JSON String: \(sortedJSON)")
}
```

위의 코드는 전달된 jsonString을 사용하여 JSON 데이터를 생성하고, `parseJSONString` 메서드를 사용하여 JSON 데이터를 정렬합니다. 정렬된 JSON 데이터를 출력합니다.

## 결론
Swift에서 ObjectMapper를 사용하여 JSON 데이터를 객체로 매핑하고, 객체를 다시 JSON 데이터로 변환하는 방법에 대해 알아보았습니다. 또한 ObjectMapper의 `sortKeys` 옵션을 사용하여 JSON 데이터를 정렬하는 방법도 알아보았습니다. ObjectMapper는 JSON 데이터와 객체 간의 변환을 쉽게 처리할 수 있도록 도와주는 강력한 도구입니다.