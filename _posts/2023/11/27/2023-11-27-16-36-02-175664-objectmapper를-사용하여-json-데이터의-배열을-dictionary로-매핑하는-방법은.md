---
layout: post
title: "[swift] ObjectMapper를 사용하여 JSON 데이터의 배열을 Dictionary로 매핑하는 방법은?"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

ObjectMapper는 Swift에서 JSON 데이터를 객체로 매핑하는 라이브러리입니다. JSON 배열을 Dictionary로 매핑하기 위해 ObjectMapper에 몇 가지 설정을 추가해야 합니다.

먼저, ObjectMapper를 프로젝트에 추가해야 합니다. CocoaPods를 사용하는 경우, Podfile에 다음 줄을 추가하고 터미널에서 `pod install` 명령을 실행하여 설치할 수 있습니다.

```
pod 'ObjectMapper'
```

이제 JSON 데이터의 배열을 Dictionary로 매핑하기 위해 다음과 같이 ObjectMapper를 사용할 수 있습니다.

```swift
import ObjectMapper

let jsonString = """
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

struct Person: Mappable {
    var name: String?
    var age: Int?

    init?(map: Map) {

    }

    mutating func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
    }
}

if let jsonData = jsonString.data(using: .utf8) {
    if let people = Mapper<Person>().mapArray(JSONString: jsonString) {
        var dictionary: [String: Any] = [:]

        for person in people {
            if let name = person.name, let age = person.age {
                dictionary[name] = age
            }
        }

        print(dictionary)
    }
}
```

위의 예제에서는 ObjectMapper를 사용하여 JSON 데이터를 Person 객체의 배열로 매핑합니다. 이후, Person 객체의 name과 age를 사용하여 Dictionary에 매핑합니다.

이를 실행하면 다음과 같은 결과가 출력됩니다.

```
["John": 25, "Jane": 30]
```

따라서, ObjectMapper를 사용하여 JSON 데이터의 배열을 Dictionary로 매핑하는 방법을 알아보았습니다.

참고 문서: [ObjectMapper GitHub 페이지](https://github.com/tristanhimmelman/ObjectMapper)