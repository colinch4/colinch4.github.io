---
layout: post
title: "[swift] Swift에서 Codable과 Alamofire를 사용하여 API 호출 및 JSON 파싱하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 목차
- [소개](#소개)
- [Codable](#Codable)
- [Alamofire](#Alamofire)
- [API 호출 및 JSON 파싱 예시](#API-호출-및-JSON-파싱-예시)
- [참고 자료](#참고-자료)

## 소개
Swift에서는 Codable과 Alamofire를 함께 사용하여 API를 호출하고 JSON 데이터를 파싱할 수 있습니다. 이는 간편하게 데이터를 전송하고 처리하기 위해 널리 사용되는 방법입니다. Codable은 Swift 4부터 도입된 프로토콜로, 데이터를 직렬화하고 역직렬화하는 데 사용됩니다. Alamofire는 Swift에서 네트워킹 작업을 쉽게 처리할 수 있도록 도와주는 오픈 소스 라이브러리입니다.

## Codable
Codable은 Swift의 프로토콜로, 객체를 JSON 데이터로 변환하거나 JSON 데이터를 객체로 변환할 때 사용됩니다. Codable을 사용하면 JSON 데이터의 키와 객체의 프로퍼티를 일치시켜 간단하게 변환할 수 있습니다. Codable을 구현하는 객체는 `Codable` 프로토콜을 채택하고, 프로퍼티에는 `CodingKey`를 사용하여 매핑할 JSON 키를 지정해야 합니다.

```swift
struct Person: Codable {
    var name: String
    var age: Int
}

let json = """
{
    "name": "John",
    "age": 25
}
""".data(using: .utf8)

let decoder = JSONDecoder()
let person = try decoder.decode(Person.self, from: json)
print(person.name) // John
print(person.age) // 25
```

## Alamofire
Alamofire는 Swift에서 HTTP 네트워킹을 편리하게 처리하기 위한 오픈 소스 라이브러리입니다. Alamofire를 사용하면 API 호출, 인증, 파라미터 전달 등의 작업을 간단하게 수행할 수 있습니다.

```swift
Alamofire.request("https://api.example.com/users").responseJSON { response in
    if let json = response.value as? [String: Any] {
        // JSON 파싱
    }
}
```

## API 호출 및 JSON 파싱 예시
앞서 소개한 Codable과 Alamofire를 함께 사용하여 API를 호출하고 JSON 데이터를 파싱하는 예시 코드입니다.

```swift
struct User: Codable {
    var id: Int
    var name: String
    var email: String
}

Alamofire.request("https://api.example.com/users").responseJSON { response in
    if let json = response.value as? [[String: Any]] {
        let decoder = JSONDecoder()
        let users = try decoder.decode([User].self, from: json)
        
        for user in users {
            print(user.name)
        }
    }
}
```

위의 코드는 API에서 받아온 JSON 배열을 `[User]` 배열로 파싱하여 사용자명을 출력하는 예시입니다.

## 참고 자료
- [Codable - Apple Developer Documentation](https://developer.apple.com/documentation/swift/codable)
- [Alamofire - GitHub](https://github.com/Alamofire/Alamofire)