---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용해 JSON 키-값 쌍을 객체의 속성에 매핑하는 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

JSON 데이터를 Swift 객체의 속성에 매핑하는 작업은 매우 일반적입니다. 이를 위해 Swift에서 ObjectMapper라는 라이브러리를 사용할 수 있습니다. ObjectMapper는 JSON과 Swift 객체 사이의 매핑을 쉽게 처리해주는 유용한 도구입니다. 

## ObjectMapper 설치하기

먼저, 프로젝트에 ObjectMapper를 설치해야 합니다. Swift 패키지 매니저를 사용하면 간단하게 설치할 수 있습니다. 다음 명령을 터미널에서 실행하세요:

```
$ swift package init --type=executable

$ vim Package.swift
```

Package.swift 파일을 열고 `dependencies` 배열에 다음 코드를 추가하세요:

```swift
.package(url: "https://github.com/tristanhimmelman/ObjectMapper.git", .upToNextMajor(from: "4.2.0"))
```

파일을 저장한 후 다음 명령을 실행하여 패키지를 업데이트하세요:

```
$ swift package update
```

이제 ObjectMapper가 프로젝트에 설치되었습니다.

## ObjectMapper 사용하기

JSON 데이터를 Swift 객체에 매핑하기 위해 다음 단계를 따르세요:

1. Swift 객체를 정의하고 ObjectMapper를 사용할 준비를 합니다. 예를 들어, 다음과 같은 Swift 객체를 정의합니다:

```swift
import ObjectMapper

class User: Mappable {
    var name: String?
    var age: Int?
    
    required convenience init?(map: Map) {
        self.init()
    }
    
    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
    }
}
```

2. JSON 데이터를 Swift 객체로 매핑합니다. ObjectMapper의 `map` 메소드를 사용하여 JSON 데이터와 Swift 객체를 매핑할 수 있습니다. 다음은 매핑하는 예시입니다:

```swift
import ObjectMapper

let jsonString = """
{
    "name": "John Doe",
    "age": 30
}
"""

if let user = Mapper<User>().map(JSONString: jsonString) {
    // 매핑이 성공했을 때 작업을 수행하는 코드 작성
} else {
    // 매핑 실패 시 예외 처리
}
```

위의 코드에서 `Mapper<User>().map(JSONString: jsonString)`을 사용하여 JSON 데이터를 User 객체로 매핑합니다.

## ObjectMapper에서 사용할 수 있는 다양한 매핑 방법

ObjectMapper는 여러 가지 매핑 방법을 제공합니다. 위의 예시에서는 `map` 메소드를 사용하지만, 다음과 같은 다른 메소드들도 사용할 수 있습니다:

- `map` 메소드: JSON 데이터를 Swift 객체로 매핑합니다.
- `mapArray` 메소드: JSON 배열을 Swift 객체 배열로 매핑합니다.
- `mapNested` 메소드: 중첩된 JSON 객체를 Swift 객체로 매핑합니다.
- `mapArrayNested` 메소드: 중첩된 JSON 배열을 Swift 객체 배열로 매핑합니다.

ObjectMapper의 다양한 매핑 방법에 대한 자세한 내용은 [ObjectMapper의 공식 문서](https://github.com/tristanhimmelman/ObjectMapper)를 참고하세요.

## 결론

Swift에서 ObjectMapper를 사용하여 JSON 데이터를 Swift 객체로 매핑하는 작업은 간단하고 편리합니다. ObjectMapper의 다양한 매핑 메소드를 활용하여 효율적으로 JSON 데이터를 처리할 수 있습니다.