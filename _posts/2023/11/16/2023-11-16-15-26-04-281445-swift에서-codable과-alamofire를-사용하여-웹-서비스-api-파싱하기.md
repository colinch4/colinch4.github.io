---
layout: post
title: "[swift] Swift에서 Codable과 Alamofire를 사용하여 웹 서비스 API 파싱하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift에서 Codable 프로토콜과 Alamofire 라이브러리를 조합하여 웹 서비스 API를 파싱하는 방법에 대해 알아보겠습니다.

## 1. Codable 프로토콜

Codable 프로토콜은 Swift 4부터 도입된 프로토콜로, JSON이나 Property List와 같은 외부 데이터 형식을 Swift 객체로 변환하거나, Swift 객체를 외부 데이터 형식으로 변환하는 데 사용됩니다.

Codable 프로토콜은 Codable로 선언된 객체의 프로퍼티가 자동으로 외부 데이터와 매핑되도록 해줍니다. 이를 위해서는 객체의 프로퍼티들이 Codable을 준수해야 합니다.

예를 들어, 다음과 같은 JSON 데이터가 있다고 가정해봅시다.

```json
{
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}
```

해당 JSON 데이터를 Swift 객체로 파싱하기 위해서는 다음과 같은 코드를 작성할 수 있습니다.

```swift
struct Person: Codable {
    var name: String
    var age: Int
    var email: String
}

let json = """
{
    "name": "John",
    "age": 30,
    "email": "john@example.com"
}
"""

if let data = json.data(using: .utf8) {
    let decoder = JSONDecoder()
    if let person = try? decoder.decode(Person.self, from: data) {
        print(person.name) // John
        print(person.age) // 30
        print(person.email) // john@example.com
    }
}
```

## 2. Alamofire로 API 호출하기

Alamofire는 Swift의 네트워킹 라이브러리로, HTTP 요청을 보내고 응답을 받는 기능을 제공합니다. Alamofire를 사용하면 간편하게 API 호출을 할 수 있습니다.

먼저 Alamofire를 프로젝트에 추가하고 임포트해야 합니다. 이후에는 Alamofire를 사용하여 서버의 API를 호출하고, 받아온 데이터를 Codable로 파싱할 수 있습니다.

```swift
import Alamofire

...

let url = "https://api.example.com/users"

Alamofire.request(url).responseJSON { response in
    switch response.result {
    case .success(let value):
        if let json = value as? [String: Any] {
            if let data = try? JSONSerialization.data(withJSONObject: json) {
                let decoder = JSONDecoder()
                if let users = try? decoder.decode([User].self, from: data) {
                    for user in users {
                        print(user.name)
                        print(user.age)
                        print(user.email)
                    }
                }
            }
        }
        
    case .failure(let error):
        print(error)
    }
}
```

위 예시는 API에서 사용자 목록을 받아와서 파싱한 뒤, 사용자의 이름, 나이, 이메일을 출력하는 코드입니다.

## 3. 참고 자료

- [Codable - Swift.org](https://swift.org/documentation/api-design-guidelines/#codable)
- [Alamofire - GitHub](https://github.com/Alamofire/Alamofire)

이번 글에서는 Swift에서 Codable과 Alamofire를 사용하여 웹 서비스 API를 파싱하는 방법에 대해 알아보았습니다. Codable을 사용하면 간단하게 JSON 데이터를 Swift 객체로 변환할 수 있고, Alamofire를 통해 API를 호출하고 응답을 처리할 수 있습니다.