---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드에 변경 불가 속성 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 ObjectMapper는 JSON 데이터를 Swift 객체로 변환하고 Swift 객체를 JSON 데이터로 다시 변환하는 작업을 도와줍니다. ObjectMapper를 사용하여 JSON 데이터에 변경 불가 속성을 추가하는 방법을 알아보겠습니다.

## ObjectMapper 설치

먼저 ObjectMapper를 설치해야 합니다. CocoaPods를 사용하는 경우 `Podfile`에 다음과 같이 ObjectMapper를 추가합니다.

```ruby
pod 'ObjectMapper'
```

그런 다음 터미널에서 다음 명령을 실행하여 설치합니다.

```bash
pod install
```

## 불변 속성 추가

불변 속성을 추가하기 전에 Swift 객체를 정의해야 합니다. 예를 들어, 다음과 같이 `Person` 클래스를 정의해보겠습니다.

```swift
import ObjectMapper

class Person: ImmutableMappable {
    let name: String
    let age: Int

    required init(map: Map) throws {
        self.name = try map.value("name")
        self.age = try map.value("age")
    }

    func mapping(map: Map) {
        name >>> map["name"]
        age >>> map["age"]
    }
}
```

위의 코드에서 `Person` 클래스는 `ImmutableMappable` 프로토콜을 준수하도록 선언되었습니다. 이는 ObjectMapper에게 이 클래스의 속성이 변경 불가능하다는 것을 알려줍니다.

`Person` 클래스의 속성은 `let`으로 선언되었으므로 생성자에서 속성을 초기화하고 매핑 함수에서 매핑 작업을 수행합니다. `>>>` 연산자를 사용하여 매핑 작업을 수행할 속성을 지정합니다.

## JSON 데이터 변환

이제 ObjectMapper를 사용하여 JSON 데이터를 `Person` 객체로 변환해보겠습니다. 다음은 JSON 데이터를 가져온 다음 `Person` 객체로 변환하는 코드입니다.

```swift
import ObjectMapper

let jsonString = "{\"name\": \"John\", \"age\": 25}"
if let person = Mapper<Person>().map(JSONString: jsonString) {
    print("Name: \(person.name)")
    print("Age: \(person.age)")
} else {
    print("Failed to parse JSON")
}
```

위의 코드에서 `Mapper<Person>().map(JSONString: jsonString)`를 사용하여 JSON 문자열을 `Person` 객체로 변환합니다. 변환에 성공하면 `person` 객체에 접근하여 `name` 및 `age` 속성을 출력합니다.

## 결론

Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드에 변경 불가 속성을 추가하는 방법에 대해 알아보았습니다. ObjectMapper는 간편한 JSON 변환을 가능하게 해주므로 복잡한 JSON 데이터를 다루는 데 유용한 도구입니다.