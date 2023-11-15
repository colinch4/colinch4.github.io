---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 이용한 REST API 통신 처리 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift의 Moya 라이브러리와 ObjectMapper 라이브러리를 이용하여 REST API 통신을 처리하는 방법을 알아보겠습니다. 

## Moya란?

Moya는 Swift 기반의 네트워킹 라이브러리로, Alamofire를 기반으로 구현되어 있습니다. Moya는 네트워킹을 추상화하여 간편한 코드 작성과 유지보수를 가능하게 해줍니다.

## ObjectMapper란?

ObjectMapper는 Swift에서 JSON 데이터를 객체로 매핑하기 위한 라이브러리입니다. JSON 데이터를 간단하게 객체로 변환하거나, 객체를 JSON 데이터로 변환할 수 있게 도와줍니다.

## 예제 코드

```swift
import Moya
import ObjectMapper

// API 서비스를 정의하는 enum 타입
enum UserService {
    case getUsers
}

extension UserService: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }
    
    var path: String {
        switch self {
        case .getUsers:
            return "/users"
        }
    }
    
    var method: Moya.Method {
        switch self {
        case .getUsers:
            return .get
        }
    }
    
    var task: Task {
        switch self {
        case .getUsers:
            return .requestPlain
        }
    }
    
    var headers: [String : String]? {
        return nil
    }
    
    var sampleData: Data {
        switch self {
        case .getUsers:
            // 서버에서 반환되는 예시 데이터
            return """
            [
                {
                    "id": 1,
                    "name": "John"
                },
                {
                    "id": 2,
                    "name": "Jane"
                }
            ]
            """.data(using: .utf8)!
        }
    }
}

// MoyaProvider 초기화
let provider = MoyaProvider<UserService>()

// API 통신 예제
provider.request(.getUsers) { result in
    switch result {
    case let .success(response):
        do {
            let users = try response.mapArray(User.self)
            // 통신 결과 (User 객체 배열) 사용
            for user in users {
                print(user.name)
            }
        } catch {
            print("Error: \(error.localizedDescription)")
        }
    case let .failure(error):
        print("Error: \(error.localizedDescription)")
    }
}
```

위의 코드는 Moya를 사용하여 `UserService`라는 enum 타입으로 API 서비스를 정의하고, `TargetType` 프로토콜을 구현한 예제입니다. 

MoyaProvider를 사용하여 API 통신을 진행하고, ObjectMapper를 사용하여 JSON 데이터를 User 객체 배열로 매핑합니다. 이후 통신 결과를 사용하게 됩니다.

이 예제 코드를 실행하면 `/users` 엔드포인트에 GET 요청을 보내서 사용자 정보를 받아올 수 있습니다.

간단한 예제이지만, Moya와 ObjectMapper를 함께 사용하여 Swift에서 REST API 통신을 처리하는 방법을 알 수 있습니다.

## 결론

Moya와 ObjectMapper은 Swift에서 REST API 통신을 처리하는데 유용한 두 가지 라이브러리입니다. 이들을 함께 사용하면 편리한 코드 작성과 간편한 JSON 데이터 매핑이 가능하게 됩니다.