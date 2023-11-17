---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터에 대소문자 구분 처리하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 JSON 데이터를 다룰 때, ObjectMapper라는 라이브러리를 사용하면 편리하게 데이터를 매핑하고 처리할 수 있습니다. 하지만 ObjectMapper는 기본적으로 대소문자를 구분하지 않습니다. 그렇기 때문에 JSON 키와 클래스의 프로퍼티 이름이 대소문자 구분이 필요한 경우에는 별도의 처리가 필요합니다.

이번 글에서는 ObjectMapper를 사용하여 JSON 데이터의 대소문자 구분을 처리하는 방법을 알아보겠습니다.

## ObjectMapper 사용법

먼저, ObjectMapper를 사용하기 위해서는 프로젝트에 ObjectMapper를 설치해야 합니다. Cocoapods를 사용한다면, Podfile에 다음과 같이 추가합니다:

```
pod 'ObjectMapper'
```

그리고 Terminal에서 `pod install` 명령어를 실행하여 ObjectMapper를 설치합니다.

설치가 완료되면, Swift 파일에서 ObjectMapper를 import하여 사용할 수 있습니다:

```swift
import ObjectMapper
```

## 대소문자 구분 처리 방법

### Option 설정을 통한 대소문자 구분

ObjectMapper는 매핑 작업 시 다양한 옵션을 제공합니다. 대소문자 구분을 위해서는 `.caseSensitive` 옵션을 설정해주면 됩니다. 아래 코드에서는 ObjectMapper의 `map` 메소드를 호출할 때, `.caseSensitive` 옵션을 설정하여 대소문자 구분을 하도록 합니다:

```swift
import ObjectMapper

struct MyModel: Mappable {
    var id: Int?
    var name: String?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        id <- (map["id", .caseSensitive(true)])
        name <- (map["name", .caseSensitive(true)])
    }
}

let jsonString = """
{
    "ID": 123,
    "Name": "John Doe"
}

if let myModel = Mapper<MyModel>().map(JSONString: jsonString) {
    print(myModel.id) // 출력: Optional(123)
    print(myModel.name) // 출력: Optional("John Doe")
}
```

위 예시에서는 JSON 데이터의 "ID" 키와 "Name" 키를 대소문자 구분하여 매핑하게 됩니다.

### JSON 매핑 시 Key 변환을 통한 대소문자 구분

또 다른 방법은 ObjectMapper의 `TransformOf` 클래스와 `TransformOf`의 `fromJSON` 메소드를 사용하여 JSON 키를 변환해주는 방법입니다. 예제 코드를 통해 살펴보겠습니다:

```swift
import ObjectMapper

struct MyModel: Mappable {
    var id: Int?
    var name: String?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        id <- (map["ID", TransformOf<Int, String>(fromJSON: { Int($0!) }, toJSON: { $0.map { String($0) } }))
        name <- (map["Name", TransformOf<String, String>(fromJSON: { $0 }, toJSON: { $0 }))
    }
}

let jsonString = """
{
    "ID": 123,
    "Name": "John Doe"
}

if let myModel = Mapper<MyModel>().map(JSONString: jsonString) {
    print(myModel.id) // 출력: Optional(123)
    print(myModel.name) // 출력: Optional("John Doe")
}
```

위 예시에서는 JSON 데이터의 "ID" 키를 Int 타입으로 변환하고, "Name" 키를 String 타입으로 변환하여 매핑하였습니다.

## 마무리

이번 글에서는 Swift에서 ObjectMapper를 사용하여 JSON 데이터의 대소문자 구분 처리 방법을 알아보았습니다. ObjectMapper는 강력하고 유용한 라이브러리이며, 다양한 옵션을 사용하여 데이터 매핑을 유연하게 처리할 수 있습니다. 대소문자 구분이 필요한 상황에서는 옵션 설정이나 키 변환을 통해 적절하게 처리하면 됩니다.

더 자세한 정보를 원하시면 ObjectMapper의 공식 문서를 참고해보세요. [참고 링크](https://github.com/tristanhimmelman/ObjectMapper)