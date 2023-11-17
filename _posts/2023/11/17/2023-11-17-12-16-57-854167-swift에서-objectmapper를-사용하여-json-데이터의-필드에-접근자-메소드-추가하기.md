---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드에 접근자 메소드 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 ObjectMapper는 JSON 데이터와 Swift 객체 간의 매핑을 간편하게 처리할 수 있는 라이브러리입니다. 이 라이브러리를 사용하면 JSON 데이터를 Swift 객체로 변환하거나, Swift 객체를 JSON 데이터로 변환할 때 편리하게 작업할 수 있습니다.

이번 글에서는 Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드에 접근자 메소드를 추가하는 방법에 대해 알아보겠습니다.

## ObjectMapper 설치하기

먼저 ObjectMapper를 사용하기 위해 프로젝트에 해당 라이브러리를 설치해야 합니다. ObjectMapper는 CocoaPods를 통해 설치할 수 있습니다. 

```
# Podfile

platform :ios, '9.0'
use_frameworks!

target 'YourProject' do
  pod 'ObjectMapper', '~> 4.2'
end
```

위의 Podfile을 수정하고 터미널에서 `pod install` 명령어를 실행하여 ObjectMapper를 설치하세요.

## JSON 데이터와 매핑할 Swift 객체 모델링하기

Swift 객체에 JSON 데이터의 필드 값을 매핑하기 위해서는 ObjectMapper를 사용하여 Swift 객체를 모델링해야 합니다.

```swift
import ObjectMapper

struct User: Mappable {
    var name: String?
    var email: String?
    
    init?(map: Map) { }
    
    mutating func mapping(map: Map) {
        name <- map["name"]
        email <- map["email"]
    }
}
```

위의 코드에서 `User` 구조체는 `Mappable` 프로토콜을 채택하고 있습니다. `Mappable` 프로토콜을 채택함으로써 ObjectMapper에 필요한 매핑 작업을 수행할 수 있습니다. 

`name`과 `email` 필드는 JSON 데이터에서 매핑될 필드들을 나타냅니다. `<-` 연산자를 사용하여 JSON 데이터 필드와 Swift 객체의 프로퍼티를 매핑합니다.

## 필드에 접근자 메소드 추가하기

이제 ObjectMapper를 사용하여 JSON 데이터와 Swift 객체를 매핑하는 작업을 진행할 때 필드에 접근자 메소드를 추가해보겠습니다.

```swift
import ObjectMapper

struct User: Mappable {
    var name: String?
    var email: String?
    
    init?(map: Map) { }
    
    mutating func mapping(map: Map) {
        name <- map["name"]
        email <- map["email"]
    }
    
    func getName() -> String {
        return name ?? ""
    }
    
    func getEmail() -> String {
        return email ?? ""
    }
}
```

위의 코드에서 `getName()`과 `getEmail()` 메소드는 각각 `name`과 `email` 필드에 접근하여 값을 반환하는 메소드입니다.

이제 ObjectMapper를 사용하여 JSON 데이터를 `User` 객체로 매핑하고, 접근자 메소드를 통해 필드 값을 가져올 수 있습니다.

```swift
let json = "{\"name\":\"John Doe\",\"email\":\"johndoe@example.com\"}"
if let user = Mapper<User>().map(JSONString: json) {
    let name = user.getName()
    let email = user.getEmail()
    print("Name: \(name), Email: \(email)")
}
```

위의 코드에서는 JSON 데이터를 `User` 객체로 매핑하고, `getName()`과 `getEmail()` 메소드를 호출하여 필드 값을 가져옵니다.

## 결론

이번 글에서는 Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드에 접근자 메소드를 추가하는 방법에 대해 알아보았습니다. ObjectMapper를 사용하면 JSON 데이터와 Swift 객체 간의 매핑 작업을 간편하게 처리할 수 있으며, 필요에 따라 접근자 메소드를 추가하여 필드 값을 가져올 수 있습니다.

더 자세한 정보나 ObjectMapper의 다른 기능에 대해서는 [ObjectMapper GitHub 페이지](https://github.com/tristanhimmelman/ObjectMapper)에서 확인해보세요.