---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용한 네트워크 통신 및 데이터 매핑 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift Moya와 ObjectMapper 라이브러리를 사용하여 네트워크 통신을 수행하고, JSON 데이터를 매핑하는 방법에 대해 다루어보겠습니다.

## Moya 소개

Moya는 AlamoFire 기반의 네트워크 추상화 라이브러리입니다. 이 라이브러리는 네트워크 요청을 정의하고 관리하는 데 도움을 줍니다.

Moya는 각각의 타겟(Target) 단위로 네트워크 요청을 정의하며, 타겟은 endpoint, 파라미터, 헤더 등의 정보를 포함합니다. Moya를 사용하면 네트워크 관련 로직을 추상화하고, 반복적인 부분을 줄일 수 있습니다.

## ObjectMapper 소개

ObjectMapper는 JSON 데이터를 Swift 객체로 매핑하기 위한 라이브러리입니다. Swift에서 JSON 데이터를 다루는 기능을 제공하며, 데이터를 자동으로 객체로 변환하거나 객체를 JSON으로 변환하는 기능을 제공합니다.

ObjectMapper는 JSON 데이터의 key와 Swift 객체의 프로퍼티를 매핑하기 위해 주석을 사용하거나, 매핑 방식을 구성하는 방법 등 다양한 기능을 제공합니다.

## 예제 코드

아래는 Moya와 ObjectMapper을 사용하여 네트워크 통신과 데이터 매핑을 수행하는 예제 코드입니다.

```swift
import Moya
import ObjectMapper

// 네트워크 요청을 정의하는 타겟
enum ServiceAPI {
    case getUsers
}

extension ServiceAPI: TargetType {
    var baseURL: URL {
        return URL(string: "https://example.com/api")!
    }
    
    var path: String {
        switch self {
        case .getUsers:
            return "/users"
        }
    }
    
    var method: Moya.Method {
        return .get
    }
    
    var sampleData: Data {
        return Data()
    }
    
    var task: Task {
        return .requestPlain
    }
    
    var headers: [String: String]? {
        return nil
    }
}

// MoyaProvider를 생성하여 타겟에 대한 네트워크 처리를 담당
let provider = MoyaProvider<ServiceAPI>()

// 네트워크 통신 함수
func getUsers(completion: @escaping ([User]?, Error?) -> ()) {
    provider.request(.getUsers) { result in
        switch result {
        case .success(let response):
            do {
                let users = try response.mapObject(type: [User].self)
                completion(users, nil)
            } catch {
                completion(nil, error)
            }
        case .failure(let error):
            completion(nil, error)
        }
    }
}

// User 모델 클래스
class User: Mappable {
    var name: String?
    var age: Int?
    
    required init?(map: Map) {
        
    }
    
    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
    }
}

// 네트워크 통신 예제 사용
getUsers { users, error in
    if let error = error {
        print("Error: \(error)")
    } else {
        if let users = users {
            for user in users {
                print("Name: \(user.name ?? ""), Age: \(user.age ?? 0)")
            }
        }
    }
}
```

위 예제 코드에서는 `ServiceAPI`라는 타겟을 정의하고, 해당 타겟에 대한 엔드포인트, 파라미터, 헤더 정보를 구현합니다. 데이터 매핑을 위해 `User`라는 모델 클래스도 정의되어 있습니다.

`getUsers` 함수는 MoyaProvider를 사용하여 네트워크 통신을 수행하고, 데이터 매핑을 진행합니다. 네트워크 통신 결과와 매핑된 데이터를 클로저를 통해 반환합니다.

위 예제 코드를 실행하면 getUsers 함수를 통해 서버에서 사용자 데이터를 가져와 출력합니다.

이와 같이 Swift Moya와 ObjectMapper을 사용하면 더욱 간편하게 네트워크 통신을 구현하고, JSON 데이터를 매핑할 수 있습니다.

## 참고 자료

- [Moya 공식 GitHub 저장소](https://github.com/Moya/Moya)
- [ObjectMapper 공식 GitHub 저장소](https://github.com/tristanhimmelman/ObjectMapper)