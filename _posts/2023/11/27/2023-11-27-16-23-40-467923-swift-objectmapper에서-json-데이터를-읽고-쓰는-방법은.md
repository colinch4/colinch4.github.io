---
layout: post
title: "[swift] Swift ObjectMapper에서 JSON 데이터를 읽고 쓰는 방법은?"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

Swift ObjectMapper는 Swift에서 JSON 데이터를 쉽게 읽고 쓸 수 있는 라이브러리입니다. 기본적으로 JSON 데이터를 객체로 매핑하거나 객체를 JSON 데이터로 변환하는 데 사용됩니다. 이번 포스트에서는 Swift ObjectMapper를 사용하여 JSON 데이터를 읽고 쓰는 방법에 대해 알아보겠습니다.

## ObjectMapper 설치

먼저 ObjectMapper를 사용하기 위해 Swift 패키지 관리자인 CocoaPods나 Swift Package Manager를 사용하여 ObjectMapper를 설치해야 합니다. 설치 방법은 다음과 같습니다.

### CocoaPods를 사용하는 경우

`Podfile`에 다음과 같은 내용을 추가합니다.

```ruby
pod 'ObjectMapper'
```

그리고 터미널에서 다음 명령어를 실행합니다.

```bash
pod install
```

### Swift Package Manager를 사용하는 경우

`Package.swift` 파일에 다음과 같이 ObjectMapper를 추가합니다.

```swift
dependencies: [
    .package(url: "https://github.com/tristanhimmelman/ObjectMapper.git", from: "4.2.0")
]
```

## ObjectMapper를 사용하여 JSON 데이터 읽기

ObjectMapper를 사용하여 JSON 데이터를 읽으려면 다음 단계를 따르세요.

1. JSON 데이터가 있는 URL 또는 파일에서 데이터를 읽습니다.

   ```swift
   guard let url = Bundle.main.url(forResource: "data", withExtension: "json"),
         let data = try? Data(contentsOf: url) else {
       return
   }
   ```

2. ObjectMapper를 사용하여 데이터를 매핑할 Swift 객체를 정의합니다. (예: `User`라는 객체)

   ```swift
   import ObjectMapper
   
   struct User: Mappable {
       var name: String?
       var age: Int?
       
       init?(map: Map) {
       }
       
       mutating func mapping(map: Map) {
           name <- map["name"]
           age <- map["age"]
       }
   }
   ```

   `Mappable` 프로토콜을 구현하여 JSON 데이터와 객체를 매핑합니다. `<-` 연산자를 사용하여 JSON 키와 객체의 속성을 연결합니다.

3. ObjectMapper를 사용하여 JSON 데이터를 객체로 변환합니다.

   ```swift
   let user = Mapper<User>().map(JSONString: data)
   ```

   위 코드는 JSON 데이터를 파싱하여 `User` 객체로 변환하는 코드입니다.

## ObjectMapper를 사용하여 JSON 데이터 쓰기

ObjectMapper를 사용하여 JSON 데이터를 쓰려면 다음 단계를 따르세요.

1. ObjectMapper를 사용하여 JSON 데이터를 매핑할 Swift 객체를 정의합니다.

   ```swift
   import ObjectMapper
   
   struct User: Mappable {
       var name: String?
       var age: Int?
       
       init?(map: Map) {
       }
       
       mutating func mapping(map: Map) {
           name <- map["name"]
           age <- map["age"]
       }
       
       func toJSONString() -> String? {
           return Mapper<User>().toJSONString(self)
       }
   }
   ```

   `Mappable` 프로토콜을 구현하여 객체와 JSON 데이터를 매핑합니다. `toJSONString()` 메서드를 추가하여 객체를 JSON 문자열로 변환합니다.

2. ObjectMapper를 사용하여 객체를 JSON 데이터로 변환합니다.

   ```swift
   let user = User(name: "John", age: 30)
   let jsonString = user.toJSONString()
   ```

   위 코드는 `User` 객체를 JSON 데이터로 변환하는 코드입니다.

이제 ObjectMapper를 사용하여 Swift에서 JSON 데이터를 쉽게 읽고 쓸 수 있습니다. ObjectMapper에는 더 많은 기능이 있으니 공식 문서를 참조하시기 바랍니다.

## References

- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)
- [ObjectMapper Documentation](https://github.com/tristanhimmelman/ObjectMapper#tojsonstringt--string)