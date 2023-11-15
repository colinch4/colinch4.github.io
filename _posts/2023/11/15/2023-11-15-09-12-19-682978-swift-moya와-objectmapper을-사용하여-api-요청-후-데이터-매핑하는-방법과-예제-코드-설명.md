---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용하여 API 요청 후 데이터 매핑하는 방법과 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 Moya와 ObjectMapper을 함께 사용하여 API 요청 후 데이터를 매핑하는 방법에 대해 알아보겠습니다. Moya는 네트워크 요청을 쉽게 처리할 수 있도록 도와주는 네트워크 추상화 라이브러리이며, ObjectMapper는 JSON 데이터를 객체로 매핑하는 라이브러리입니다.

## Moya와 ObjectMapper 설치

Moya와 ObjectMapper을 사용하기 위해서는 먼저 Cocoapods를 통해 라이브러리를 설치해야 합니다. 

```bash
$ pod init
```

```ruby
# Podfile

use_frameworks!

target 'YourProjectName' do
    pod 'Moya', '~> 14.0'
    pod 'ObjectMapper', '~> 4.2'
end
```

```bash
$ pod install
```

## 모델 클래스 생성

API 요청 후 매핑할 데이터를 담을 모델 클래스를 생성합니다. 예를 들어, 서버에서 받아온 사용자 정보를 매핑할 `User` 클래스를 만들어봅시다.

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

위의 예제 코드에서는 `Mappable` 프로토콜을 구현하고, JSON 데이터에서 매핑할 속성들을 선언하고 매핑합니다.

## Moya Provider 생성

Moya의 `MoyaProvider`를 사용해 API 요청을 처리하기 위해 Provider를 생성합니다. 예를 들어, 사용자 정보를 가져오는 API를 호출하는 Provider를 만들어봅시다.

```swift
import Moya

let provider = MoyaProvider<YourAPI>()
```

## API 요청

Provider를 이용하여 API 요청을 보내고, ObjectMapper를 사용하여 데이터를 매핑합니다. 예를 들어, 사용자 정보를 가져오는 API 호출 후 데이터를 매핑하는 함수를 작성해봅시다.

```swift
import Moya

func fetchUserData(completion: @escaping (User?, Error?) -> ()) {
    provider.request(.getUser) { result in
        switch result {
        case .success(let response):
            do {
                let user = try response.mapObject(User.self)
                completion(user, nil)
            } catch {
                completion(nil, error)
            }
        case .failure(let error):
            completion(nil, error)
        }
    }
}
```

위의 예제 코드에서는 `provider.request`로 API 요청을 보내고, `response.mapObject`를 사용하여 JSON 데이터를 `User` 객체로 매핑합니다. 

## 데이터 사용

매핑된 데이터를 사용하기 위해 API 요청 함수를 호출하고, 반환된 데이터를 처리할 수 있습니다.

```swift
fetchUserData { (user, error) in
    if let user = user {
        print("User ID: \(user.id)")
        print("User Name: \(user.name)")
        print("User Email: \(user.email)")
    } else if let error = error {
        print("Error: \(error.localizedDescription)")
    }
}
```

위의 예제 코드에서는 `fetchUserData`를 호출하여 사용자 정보를 가져온 뒤, 매핑된 데이터를 사용합니다.

## 결론

위의 예제 코드를 참고하여 Moya와 ObjectMapper를 함께 사용하여 API 요청 후 데이터를 매핑하는 방법에 대해 알아보았습니다. 이를 통해 더 간편하고 효율적인 네트워크 요청과 데이터 매핑을 할 수 있습니다.