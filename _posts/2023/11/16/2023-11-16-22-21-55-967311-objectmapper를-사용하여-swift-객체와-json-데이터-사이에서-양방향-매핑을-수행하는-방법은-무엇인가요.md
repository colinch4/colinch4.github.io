---
layout: post
title: "[swift] ObjectMapper를 사용하여 Swift 객체와 JSON 데이터 사이에서 양방향 매핑을 수행하는 방법은 무엇인가요?"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

# ObjectMapper란?
ObjectMapper는 Swift 언어를 위한 JSON 매핑 라이브러리로, Swift 객체와 JSON 데이터 사이에서의 양방향 매핑을 편리하게 수행할 수 있게 도와줍니다.

# 설치
ObjectMapper를 사용하기 위해서는 먼저 CocoaPods 또는 Swift Package Manager를 통해 프로젝트에 라이브러리를 설치해야 합니다.

## CocoaPods를 통한 설치

1. 터미널을 열고 프로젝트 디렉토리로 이동합니다.
2. `Podfile`을 생성하고 아래의 내용을 추가합니다.

```ruby
platform :ios, '9.0'
use_frameworks!

target 'YourTargetName' do
  pod 'ObjectMapper'
end
```

3. 터미널에서 `pod install`을 실행하여 설치합니다.

## Swift Package Manager를 통한 설치

1. Xcode 프로젝트를 엽니다.
2. `File` > `Swift Packages` > `Add Package Dependency`를 선택합니다.
3. 아래의 URL을 입력하고 `Next`를 클릭합니다.
   - https://github.com/tristanhimmelman/ObjectMapper.git
4. 버전 선택을 하고 `Next`를 클릭합니다.
5. `Add`를 클릭하여 라이브러리를 추가합니다.

# 사용법

## Swift 객체를 JSON으로 변환하기

```swift
import ObjectMapper

class Person: Mappable {
    var name: String?
    var age: Int?
    
    required init?(map: Map) {}
    
    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
    }
}

let person = Person()
person.name = "John Doe"
person.age = 30

let json = Mapper<Person>().toJSONString(person)
print(json) // {"name": "John Doe", "age": 30}
```

위의 예제에서는 `Person` 클래스를 정의하고 `Mappable` 프로토콜을 구현합니다. `Mappable` 프로토콜을 구현하기 위해 `required init?(map: Map)`과 `func mapping(map: Map)` 메서드를 구현해야 합니다. `mapping(map: Map)` 메서드에서는 속성과 JSON 키를 매핑하기 위해 `<-` 연산자를 사용합니다.

`Mapper<Person>().toJSONString(person)`의 형태로 `Person` 객체를 JSON 문자열로 변환할 수 있습니다.

## JSON을 Swift 객체로 변환하기

```swift
let jsonString = "{\"name\": \"Jane Smith\", \"age\": 25}"

if let person = Mapper<Person>().map(JSONString: jsonString) {
    print(person.name) // Jane Smith
    print(person.age) // 25
}
```

위의 예제에서는 JSON 문자열을 `Person` 객체로 변환하는 방법을 보여줍니다. `Mapper<Person>().map(JSONString: jsonString)`의 형태로 JSON 문자열을 `Person` 객체로 변환할 수 있습니다.

# 결론
ObjectMapper를 사용하면 Swift 객체와 JSON 데이터 사이에서 손쉽게 매핑을 수행할 수 있습니다. ObjectMapper의 강력한 기능을 활용하여 JSON 매핑 작업을 더욱 편리하게 처리할 수 있습니다. 추가로 ObjectMapper에는 배열 매핑, 날짜 형식 변환 등 다양한 기능이 있으니 필요한 경우 공식 문서를 참고해보시기 바랍니다.