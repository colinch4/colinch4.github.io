---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 통한 REST API 호출 및 데이터 매핑 예제"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이 예제에서는 Swift 프로그래밍 언어를 사용하여 Moya와 ObjectMapper를 활용해 REST API를 호출하고 데이터를 매핑하는 방법에 대해 알아보겠습니다.

## Moya란?

Moya는 Alamofire를 기반으로 한 네트워킹 라이브러리로, 네트워크 호출을 추상화하여 API 클라이언트를 쉽게 작성할 수 있게 해줍니다. Moya는 네트워크 요청과 응답을 정의하는 프로토콜 기반의 추상화 레이어를 제공합니다.

## ObjectMapper란?

ObjectMapper는 Swift에서 모델 객체와 JSON 데이터 간에 매핑을 쉽게 해주는 라이브러리입니다. ObjectMapper는 JSON 데이터를 모델 객체로 변환하거나, 모델 객체를 JSON 데이터로 변환할 수 있게 해줍니다.

## 예제 코드

이제 Moya와 ObjectMapper를 사용하여 REST API를 호출하고 데이터를 매핑하는 예제 코드를 살펴보겠습니다.

```swift
import Moya
import ObjectMapper

// API를 호출하기 위한 Provider 정의
let provider = MoyaProvider<MyAPIService>()

// Model 객체
struct User: Mappable {
    var name: String?
    var email: String?

    init?(map: Map) {}
    
    mutating func mapping(map: Map) {
        name <- map["name"]
        email <- map["email"]
    }
}

// API Service 정의
enum MyAPIService {
    case getUser(id: Int)
}

extension MyAPIService: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }
    
    var path: String {
        switch self {
        case .getUser(let id):
            return "/users/\(id)"
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
    
    var headers: [String : String]? {
        return nil
    }
}

// API 호출 및 데이터 매핑
provider.request(.getUser(id: 1)) { result in
    switch result {
    case .success(let response):
        do {
            let user = try response.mapObject(User.self)
            print("Name: \(user.name ?? "")")
            print("Email: \(user.email ?? "")")
        } catch {
            print("Error: \(error.localizedDescription)")
        }
    case .failure(let error):
        print("Error: \(error.localizedDescription)")
    }
}
```

위의 예제 코드는 MoyaProvider를 사용하여 /users/{id} API를 호출하고, 받아온 JSON 데이터를 User 모델 객체로 매핑하여 출력하는 예제입니다.

## 결론

이 예제를 통해 Swift에서 Moya와 ObjectMapper을 활용하여 REST API 호출과 데이터 매핑을 어떻게 수행할 수 있는지 알아보았습니다. Moya와 ObjectMapper은 Swift 개발을 더욱 간편하고 효율적으로 만들어주는 유용한 도구입니다.

더 자세한 내용은 [Moya](https://github.com/Moya/Moya)와 [ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)의 공식 문서를 참고하세요.