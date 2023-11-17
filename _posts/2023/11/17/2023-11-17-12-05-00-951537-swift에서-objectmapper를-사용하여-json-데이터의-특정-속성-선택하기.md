---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터의 특정 속성 선택하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 ObjectMapper는 JSON 데이터를 객체로 매핑하는 데 사용되는 강력한 라이브러리입니다. 이 라이브러리를 사용하면 JSON 데이터의 특정 속성을 선택하고 해당 속성 값을 가져올 수 있습니다. 이번 블로그 포스트에서는 ObjectMapper를 사용하여 JSON 데이터의 특정 속성을 선택하는 방법에 대해 알아보겠습니다.

## ObjectMapper 소개

ObjectMapper는 Swift에서 사용되는 JSON 매핑 라이브러리로, JSON 데이터와 Swift 객체 사이의 매핑을 담당합니다. 이 라이브러리를 사용하면 JSON 데이터를 Swift 객체로 쉽게 변환하거나, Swift 객체를 JSON 데이터로 변환할 수 있습니다.

## JSON 데이터에서 특정 속성 선택하기

JSON 데이터에서 특정 속성을 선택하려면 ObjectMapper의 `map` 기능을 사용해야 합니다. 다음은 ObjectMapper를 사용하여 JSON 데이터에서 특정 속성을 선택하는 예제 코드입니다.

```swift
import ObjectMapper

struct Customer: Mappable {
    var name: String?
    var age: Int?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
    }
}

func selectPropertyFromJSON(json: String) -> Customer? {
    guard let customer = Mapper<Customer>().map(JSONString: json) else {
        return nil
    }
  
    return customer
}

let jsonString = "{\"name\":\"John\", \"age\":30, \"address\":\"New York\"}"
if let customer = selectPropertyFromJSON(json: jsonString) {
    print("Name: \(customer.name)")
    print("Age: \(customer.age)")
}
```

위의 예제 코드에서는 `Customer`라는 구조체를 정의하고, ObjectMapper를 사용하여 JSON 데이터를 `Customer` 객체로 매핑합니다. `name`과 `age`라는 속성을 선택하고 값을 가져오기 위해 매핑 함수를 정의합니다. 

`selectPropertyFromJSON` 함수는 주어진 JSON 문자열을 입력으로 받아 ObjectMapper를 사용하여 `Customer` 객체로 변환합니다. 변환된 객체가 정상적으로 생성된 경우 `name`과 `age` 속성의 값을 출력합니다.

이제 위의 예제 코드를 실행하면, 다음과 같은 출력 결과를 볼 수 있습니다.

```
Name: John
Age: 30
```

## 결론

Swift에서 ObjectMapper를 사용하여 JSON 데이터의 특정 속성을 선택하는 방법에 대해 알아보았습니다. ObjectMapper는 JSON 데이터와 Swift 객체 사이의 변환을 간편하게 처리할 수 있는 강력한 도구입니다. JSON 데이터의 특정 속성을 쉽게 선택해서 활용할 수 있도록 ObjectMapper를 적극적으로 활용해보세요.

---

### 참고 자료

- [ObjectMapper GitHub 페이지](https://github.com/tristanhimmelman/ObjectMapper)
- [ObjectMapper 사용 예제](https://iosdevcenters.blogspot.com/2017/05/how-to-use-objectmapper-in-swift-30.html)