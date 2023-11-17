---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터에 XML 태그 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 ObjectMapper는 JSON 데이터를 간편하게 자동으로 매핑해주는 라이브러리입니다. 이 블로그 포스트에서는 ObjectMapper를 사용하여 JSON 데이터에 XML 태그를 추가하는 방법에 대해 알아보겠습니다.

## ObjectMapper 설치

`ObjectMapper`를 사용하기 위해 먼저 Cocoapods를 통해 `ObjectMapper`를 설치해야 합니다. `Podfile`에 다음과 같이 추가한 후 `pod install` 명령을 실행합니다.

```swift
pod 'ObjectMapper'
```

## XML 태그 추가하기

1. JSON 데이터 구조 정의하기

먼저, JSON 데이터의 구조를 정의해야 합니다. 예를 들어, 다음과 같은 JSON 데이터가 있다고 가정해보겠습니다.

```json
{
    "name": "John",
    "age": 25
}
```

2. XML 태그 추가를 위한 클래스 생성하기

JSON 데이터에 XML 태그를 추가하기 위해서는 ObjectMapper를 사용하여 JSON 데이터를 매핑할 클래스가 필요합니다. 예를 들어, 다음과 같이 클래스를 생성합니다.

```swift
import Foundation
import ObjectMapper

class XMLData: Mappable {
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

3. XML 태그 추가

JSON 데이터에 XML 태그를 추가하기 위해 다음과 같이 코드를 작성합니다.

```swift
// JSON 데이터 문자열
let jsonString = """
{
    "name": "John",
    "age": 25
}
"""

// JSON 데이터를 객체로 매핑
if let xmlData = Mapper<XMLData>().map(JSONString: jsonString) {
    // XML 태그 추가
    xmlData.name = "<text>\(xmlData.name ?? "")</text>"
    xmlData.age = "<number>\(xmlData.age ?? 0)</number>"
    
    // XML 태그가 추가된 JSON 데이터 출력
    let xmlString = xmlData.toJSONString(prettyPrint: true)
    print(xmlString)
}
```

위의 코드는 먼저 JSON 데이터를 `Mapper<XMLData>().map(JSONString: jsonString)`를 사용하여 객체로 매핑합니다. 그리고 XML 태그를 추가하고 태그가 추가된 JSON 데이터를 출력합니다.

## 결론

Swift에서 ObjectMapper를 사용하여 JSON 데이터에 XML 태그를 추가하는 방법에 대해 알아보았습니다. ObjectMapper는 JSON 데이터의 매핑을 쉽게 해주어 개발자들에게 편리한 기능을 제공합니다. 만약 XML 데이터를 생성하거나 활용해야 할 경우에는 ObjectMapper와 XML 태그 추가 방법을 사용해보세요.

## 참고 자료

- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)