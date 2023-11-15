---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 사용하여 네트워크 요청 및 데이터 매핑하는 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번에는 Swift에서 Moya와 ObjectMapper를 사용하여 네트워크 요청을 보내고, 응답 데이터를 매핑하는 방법을 알아보겠습니다.

## Moya란?

Moya는 Swift에서 네트워크 작업을 수행하기 위한 추상화된 네트워크 라이브러리입니다. 이 라이브러리는 Alamofire를 기반으로 하며, 네트워크 요청을 간단하게 정의하고 관리할 수 있도록 도와줍니다.

## ObjectMapper란?

ObjectMapper는 Swift에서 JSON 데이터를 객체로 매핑하는 라이브러리로, JSON 데이터를 간편하게 처리하고 모델 객체로 변환할 수 있습니다.

## 설치

먼저, Moya와 ObjectMapper를 설치해야 합니다. 두 가지 라이브러리는 CocoaPods를 통해 설치할 수 있습니다. `Podfile`에 다음과 같이 추가한 후, `pod install`을 실행하세요.

```swift
pod 'Moya'
pod 'ObjectMapper'
```

## 예제 코드

### 모델 객체 정의

먼저, 서버에서 받은 JSON 데이터를 매핑할 모델 객체를 정의합니다. 예를 들어, 다음과 같은 JSON 데이터를 받아와서 매핑할 것이라고 가정해봅시다.

```json
{
    "id": 1,
    "name": "John Doe",
    "email": "johndoe@example.com"
}
```

위 JSON 데이터를 매핑하기 위해 `User`라는 모델 객체를 만들어보겠습니다.

```swift
import ObjectMapper

class User: Mappable {
    var id: Int?
    var name: String?
    var email: String?
    
    required init?(map: Map) {}
    
    func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}
```

### 네트워크 요청 및 데이터 매핑

이제 Moya를 사용하여 네트워크 요청을 보내고, ObjectMapper를 사용하여 응답 데이터를 매핑해보겠습니다.

```swift
import Moya
import ObjectMapper

// MoyaProvider 생성
let provider = MoyaProvider<MyAPI>()

// 네트워크 요청
provider.request(.getUser(id: 1)) { result in
    switch result {
    case .success(let response):
        do {
            // ObjectMapper를 사용하여 JSON 데이터 매핑
            let user = try response.mapObject(User.self)
            
            // 매핑된 데이터 사용
            print(user.id)
            print(user.name)
            print(user.email)
        } catch {
            print("JSON 매핑에 실패하였습니다.")
        }
    case .failure(let error):
        print("네트워크 요청 실패: \(error)")
    }
}
```

위 예제 코드에서는 `MyAPI.getUser(id: 1)`라는 네트워크 요청을 보냅니다. 응답으로 받은 JSON 데이터를 ObjectMapper를 사용하여 `User` 모델 객체로 매핑한 후, 매핑된 데이터를 사용하는 방법을 보여주고 있습니다.

이와 같이 Swift에서 Moya와 ObjectMapper를 함께 사용하여 네트워크 요청과 데이터 매핑을 손쉽게 처리할 수 있습니다.

참고 자료:

- [Moya GitHub 저장소](https://github.com/Moya/Moya)
- [ObjectMapper GitHub 저장소](https://github.com/tristanhimmelman/ObjectMapper)