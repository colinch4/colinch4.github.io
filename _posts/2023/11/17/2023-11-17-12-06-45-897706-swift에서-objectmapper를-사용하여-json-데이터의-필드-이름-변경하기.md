---
layout: post
title: "[swift] Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드 이름 변경하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 ObjectMapper 라이브러리는 JSON 데이터를 Swift 객체로 매핑하기 위한 강력한 도구입니다. 이 라이브러리는 JSON 키와 Swift 객체의 프로퍼티 이름이 서로 일치하지 않을 때 유용하게 사용될 수 있습니다. 이번 블로그 포스트에서는 ObjectMapper를 사용하여 JSON 데이터의 필드 이름을 원하는 대로 변경하는 방법을 알아보겠습니다.

## ObjectMapper 설치하기

먼저 ObjectMapper를 사용하기 위해서는 프로젝트에 해당 라이브러리를 설치해야 합니다. 방법은 크게 두 가지입니다. 첫 번째 방법은 CocoaPods를 사용하여 설치하는 것이며, 두 번째 방법은 Swift Package Manager를 이용하는 것입니다.

### CocoaPods로 설치하기
CocoaPods를 사용하려면 먼저 Podfile을 생성하고 다음과 같이 ObjectMapper를 추가해야 합니다.

```ruby
platform :ios, '9.0'
use_frameworks!

target 'YourApp' do
    pod 'ObjectMapper'
end
```

그런 다음 터미널에서 `pod install` 명령을 실행하여 ObjectMapper를 설치합니다.

### Swift Package Manager로 설치하기
Swift Package Manager는 Xcode 11부터 기본적으로 제공되는 패키지 관리 도구입니다. 다음과 같이 Package.swift 파일을 생성하고 ObjectMapper를 추가해야 합니다.

```swift
// swift-tools-version:5.1

import PackageDescription

let package = Package(
    name: "YourApp",
    dependencies: [
        .package(url: "https://github.com/tristanhimmelman/ObjectMapper.git", from: "4.2.0")
    ],
    targets: [
        .target(
            name: "YourApp",
            dependencies: ["ObjectMapper"]
        )
    ]
)
```

그런 다음 Xcode에서 Package.swift 파일을 열고 프로젝트를 빌드하여 ObjectMapper를 설치합니다.

## ObjectMapper를 사용한 JSON 매핑

설치가 완료되면 ObjectMapper를 사용하여 JSON 데이터를 Swift 객체로 매핑할 수 있습니다. JSON 데이터와 매핑할 Swift 객체를 만들고, 필드 이름이 변경된 프로퍼티를 선언합니다.

```swift
import ObjectMapper

class User: Mappable {
    var username: String?
    var email: String?

    required init?(map: Map) {
    }

    // JSON 데이터와 매핑하여 필드 이름 변경하기
    func mapping(map: Map) {
        username <- map["name"]
        email <- map["email_address"]
    }
}
```

위의 코드에서는 JSON 데이터의 "name" 필드를 Swift 객체의 "username" 프로퍼티에 매핑하고, "email_address" 필드를 "email" 프로퍼티에 매핑하는 예시입니다.

## JSON 데이터에서 Swift 객체로 매핑하기

JSON 데이터를 Swift 객체로 매핑하기 위해서는 ObjectMapper의 `map` 메서드를 사용합니다. 다음은 매핑 예시입니다.

```swift
let json = """
{
    "name": "John",
    "email_address": "john@example.com"
}
"""

if let user = Mapper<User>().map(JSONString: json) {
    print(user.username) // 출력 결과: "John"
    print(user.email) // 출력 결과: "john@example.com"
}
```

위의 코드에서는 JSON 데이터를 `User` 객체로 매핑하고, 매핑된 객체의 프로퍼티 값을 출력하는 예시입니다.

## 결론

이번 블로그 포스트에서는 Swift에서 ObjectMapper를 사용하여 JSON 데이터의 필드 이름을 원하는 대로 변경하는 방법을 소개했습니다. ObjectMapper는 매우 유용한 라이브러리이며, JSON 데이터와 Swift 객체 간의 매핑 작업을 효과적으로 수행할 수 있도록 도와줍니다.

더 많은 정보를 원한다면, [ObjectMapper GitHub 저장소](https://github.com/tristanhimmelman/ObjectMapper)에 방문하여 문서와 예시 코드를 참고하실 수 있습니다.