---
layout: post
title: "[swift] AlamofireObjectMapper를 사용해 JSON 배열 데이터를 객체 배열로 매핑하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

앱에서 REST API를 통해 서버로부터 받아온 JSON 배열 데이터를 Swift 객체 배열로 매핑하는 작업은 일반적으로 많이 사용됩니다. 이를 간편하게 처리하기 위해 Alamofire와 ObjectMapper를 함께 사용할 수 있습니다. 이번 포스트에서는 AlamofireObjectMapper를 사용하여 JSON 배열 데이터를 객체 배열로 매핑하는 방법에 대해 알아보겠습니다.

## 1. Alamofire 및 ObjectMapper 및 AlamofireObjectMapper 설치

먼저 Alamofire, ObjectMapper, 그리고 AlamofireObjectMapper를 설치해야 합니다. 이 작업을 위해 가장 흔히 사용되는 패키지 관리자인 CocoaPods를 사용해 보겠습니다. Podfile에 다음과 같이 라이브러리를 추가해주세요.

```swift
pod 'Alamofire'
pod 'ObjectMapper'
pod 'AlamofireObjectMapper'
```

그리고 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## 2. 모델 클래스 생성과 ObjectMapper 프로토콜 구현

이제 JSON 데이터를 매핑할 모델 클래스를 생성해야 합니다. 예를 들어, 서버에서 받아온 JSON 데이터가 다음과 같다고 가정해봅시다.

```json
[
  {
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "email": "janesmith@example.com"
  }
]
```

위의 데이터와 매핑될 `User` 클래스를 다음과 같이 구현해봅시다.

```swift
import ObjectMapper

class User: Mappable {
  var id: Int?
  var name: String?
  var email: String?

  required init?(map: Map) {
  }

  func mapping(map: Map) {
    id <- map["id"]
    name <- map["name"]
    email <- map["email"]
  }
}
```

이번 예시에서는 ObjectMapper의 `Mappable` 프로토콜을 사용하여 매핑을 구현합니다. `Mappable` 프로토콜을 채택하고, `required init?(map: Map)` 메서드와 `mapping(map: Map)` 메서드를 구현하는 것을 볼 수 있습니다.

## 3. Alamofire를 사용하여 JSON 데이터 요청하고 매핑하기

이제 Alamofire를 사용하여 서버로부터 JSON 데이터를 요청하고, ObjectMapper를 사용하여 매핑하는 작업을 수행해보겠습니다.

```swift
import Alamofire
import AlamofireObjectMapper

func fetchUsers(completion: @escaping ([User]?) -> Void) {
  let url = "https://api.example.com/users"

  Alamofire.request(url).responseArray { (response: DataResponse<[User]>) in
    if let users = response.result.value {
      completion(users)
    } else {
      completion(nil)
    }
  }
}
```

`fetchUsers` 함수는 서버로부터 JSON 데이터를 요청하고, `Alamofire.request(url)`을 사용하여 요청을 보냅니다. 그리고 `responseArray` 메서드를 호출하면 JSON 데이터가 `User` 객체 배열로 매핑됩니다. 매핑된 결과는 `response.result.value`를 통해 확인할 수 있습니다.

## 4. 데이터 사용하기

이제 `fetchUsers` 함수로부터 받아온 객체 배열을 사용할 수 있습니다. 예를 들어, 다음과 같이 출력해보겠습니다.

```swift
fetchUsers { (users) in
  if let users = users {
    for user in users {
      print("Name: \(user.name ?? ""), Email: \(user.email ?? "")")
    }
  } else {
    print("Failed to fetch users.")
  }
}
```

위의 예시 코드를 실행하면 다음과 같은 출력 결과를 얻을 수 있습니다.

```
Name: John Doe, Email: johndoe@example.com
Name: Jane Smith, Email: janesmith@example.com
```

## 결론

이번 포스트에서는 Alamofire 및 ObjectMapper를 사용하여 JSON 배열 데이터를 Swift 객체 배열로 매핑하는 방법에 대해 알아보았습니다. AlamofireObjectMapper를 사용하면 네트워크 요청과 데이터 매핑을 효율적으로 처리할 수 있으며 코드의 가독성도 높일 수 있습니다.