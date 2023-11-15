---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용하여 API 요청 후 데이터 매핑하는 방법과 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

## 개요
Swift에서 API 요청 후 받아온 데이터를 매핑하기 위해 Moya와 ObjectMapper를 함께 사용할 수 있습니다. Moya는 Alamofire를 기반으로 한 네트워크 추상화 라이브러리이며, ObjectMapper는 JSON 데이터와 Swift 모델 사이의 매핑을 담당하는 라이브러리입니다. 이 두 라이브러리를 함께 사용하여 API 요청 후 받아온 JSON 데이터를 Swift 객체로 변환할 수 있습니다.

## Moya와 ObjectMapper 설치
먼저 프로젝트에 Moya와 ObjectMapper를 설치해야 합니다. Swift Package Manager를 사용하는 경우 `Package.swift` 파일에 다음 종속성을 추가하세요:

```swift
dependencies: [
    .package(url: "https://github.com/Moya/Moya.git", from: "14.0.0"),
    .package(url: "https://github.com/tristanhimmelman/ObjectMapper.git", from: "4.2.0")
]
```

그리고 프로젝트의 Target 설정에도 Moya와 ObjectMapper를 추가해주세요.

## API 요청 및 데이터 매핑 예제 코드
이제 Moya와 ObjectMapper를 사용하여 API 요청 후 데이터를 매핑하는 방법을 예제 코드로 설명하겠습니다.

```swift
import Moya
import ObjectMapper

// API 요청을 위한 Provider 생성
let provider = MoyaProvider<API>()

// API 요청에 대한 Enum 정의
enum API {
    case getUser(id: Int)
}

// Moya의 TargetType Protocol 구현
extension API: TargetType {
    var baseURL: URL { return URL(string: "https://api.example.com")! }
    var path: String {
        switch self {
        case .getUser(let id):
            return "/user/\(id)"
        }
    }
    var method: Moya.Method { return .get }
    var sampleData: Data { return Data() }
    var task: Task { return .requestPlain }
    var headers: [String : String]? { return nil }
}

// ObjectMapper의 Mappable Protocol 구현
struct User: Mappable {
    var id: Int?
    var name: String?
    var email: String?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}

// API 요청 후 데이터 매핑 함수 정의
func fetchUser(id: Int) {
    provider.request(.getUser(id: id)) { result in
        switch result {
        case .success(let response):
            do {
                let user = try response.map(to: User.self)
                print(user)
            } catch {
                print("Error: \(error)")
            }
        case .failure(let error):
            print("Error: \(error)")
        }
    }
}

// API 요청 예시
fetchUser(id: 1)
```

위의 예제 코드에서 `API` Enum은 API 요청의 종류를 정의합니다.`getUser` 케이스는 `/user/{id}` 엔드포인트에 GET 요청을 수행합니다.

`User` 구조체는 받아온 JSON 데이터를 매핑할 Swift 모델로, `Mappable` 프로토콜을 준수하며 `mapping(map:)` 메서드를 구현합니다.

`fetchUser` 함수는 `provider.request`를 사용하여 API 요청을 보내고, 응답을 매핑하여 `User` 객체로 변환합니다. 성공한 경우 매핑된 `User` 객체를 출력하며, 실패한 경우 에러 메시지를 출력합니다.

## 결론
Swift Moya와 ObjectMapper은 API 요청 후 데이터 매핑을 쉽게 처리할 수 있도록 도와주는 강력한 라이브러리입니다. 이러한 라이브러리를 사용하면 네트워킹 코드를 간결하게 작성하고, 받아온 데이터를 쉽게 Swift 모델로 매핑할 수 있습니다.