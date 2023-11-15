---
layout: post
title: "[swift] Swift Moya를 통한 REST API 통신과 ObjectMapper를 사용한 데이터 매핑 예제"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이 예제는 Swift Moya를 사용하여 REST API 통신을 수행하고, ObjectMapper를 사용하여 데이터를 매핑하는 방법을 보여줍니다.

## 목차
- [Moya 소개](#moya-소개)
- [ObjectMapper 소개](#objectmapper-소개)
- [Swift Moya 및 ObjectMapper 설정](#swift-moya-및-objectmapper-설정)
- [REST API 통신](#rest-api-통신)
- [데이터 매핑](#데이터-매핑)
- [참고 자료](#참고-자료)

## Moya 소개

[Moya](https://github.com/Moya/Moya)는 Swift에서 네트워킹을 처리하기 위한 추상화된 네트워크 라이브러리입니다. Moya는 Alamofire를 기반으로 만들어졌으며, 네트워킹 관련 코드를 단순화하고 추상화하여 작성할 수 있게 도와줍니다. Moya는 우아하고 타입 안전한 API를 제공하여 네트워킹 코드 작성 시간을 단축시킬 수 있습니다.

## ObjectMapper 소개

[ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)는 Swift에서 JSON 데이터를 쉽게 매핑할 수 있는 라이브러리입니다. ObjectMapper를 사용하면 JSON 데이터와 Swift 객체 간의 매핑을 간단하고 편리하게 처리할 수 있습니다. ObjectMapper는 JSON 데이터의 키와 Swift 객체의 프로퍼티를 매핑할 수 있으며, 다양한 형식의 데이터 매핑을 지원합니다.

## Swift Moya 및 ObjectMapper 설정

먼저, Swift 프로젝트에 Moya와 ObjectMapper를 설치해야 합니다. CocoaPods를 사용하는 경우, `Podfile`에 다음과 같이 추가합니다:

```ruby
pod 'Moya'
pod 'ObjectMapper'
```

그리고 터미널에서 다음 명령어로 의존성을 설치합니다:

```bash
$ pod install
```

## REST API 통신

Moya를 사용하여 REST API 통신을 수행하는 방법은 다음과 같습니다. 먼저, Moya의 타겟(Target)을 정의해야 합니다. 타겟은 API 엔드포인트의 URL과 HTTP 메소드, 파라미터, 헤더 등의 정보를 포함합니다. 타겟을 정의하기 위해 `Moya.TargetType` 프로토콜을 채택한 클래스나 구조체를 만듭니다.

```swift
import Moya

enum ExampleAPI {
    case getUser(id: String)
    case createUser(name: String, email: String)
}

extension ExampleAPI: TargetType {
    var baseURL: URL {
        return URL(string: "https://example.com/api")!
    }
    
    var path: String {
        switch self {
        case .getUser(let id):
            return "/user/\(id)"
        case .createUser:
            return "/user"
        }
    }
    
    var method: Moya.Method {
        switch self {
        case .getUser:
            return .get
        case .createUser:
            return .post
        }
    }
    
    var task: Task {
        switch self {
        case .getUser:
            return .requestPlain
        case .createUser(let name, let email):
            return .requestParameters(parameters: ["name": name, "email": email], encoding: JSONEncoding.default)
        }
    }
    
    var headers: [String : String]? {
        return nil
    }
}
```

위 코드에서 `ExampleAPI`는 예시로 만든 API 엔드포인트의 목록입니다. `getUser`와 `createUser` 두 가지 요청을 정의하고, 각각의 URL, HTTP 메소드, 파라미터 및 헤더 정보를 설정합니다.

## 데이터 매핑

ObjectMapper를 사용하여 JSON 데이터와 Swift 객체를 매핑하는 방법은 다음과 같습니다. 먼저, Swift 객체를 만들고 `Mappable` 프로토콜을 채택합니다. 객체의 프로퍼티와 JSON 데이터의 키를 매핑하기 위해 `map` 함수를 구현합니다.

```swift
import ObjectMapper

struct User: Mappable {
    var id: String?
    var name: String?
    var email: String?
    
    init?(map: Map) {}
    
    mutating func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}
```

위 코드에서 `User`는 사용자 정보를 나타내는 Swift 구조체입니다. `Mappable`을 채택하고 `map` 함수를 구현하여 JSON 데이터의 키와 객체의 프로퍼티를 매핑합니다.

매핑된 데이터를 사용하기 위해 Moya의 `provider`를 생성하고 요청을 보냅니다. 요청 결과를 받으면 ObjectMapper를 사용하여 JSON 데이터를 Swift 객체로 변환합니다.

```swift
import Moya
import ObjectMapper

let provider = MoyaProvider<ExampleAPI>()

provider.request(.getUser(id: "123")) { result in
    switch result {
    case .success(let response):
        do {
            let user = try response.mapJSON().mapObject(User.self)
            print(user)
        } catch {
            print("Mapping error: \(error)")
        }
    case .failure(let error):
        print("Network error: \(error)")
    }
}
```

위 코드에서 `request` 함수를 사용하여 `.getUser` 요청을 보내고, 응답 결과를 받습니다. `mapJSON` 함수를 사용하여 JSON 데이터를 맵핑한 뒤, `mapObject` 함수를 사용하여 Swift 객체로 변환합니다. 변환된 객체를 출력하면 매핑이 성공적으로 수행된 결과가 출력됩니다.

## 참고 자료

- [Moya GitHub 저장소](https://github.com/Moya/Moya)
- [ObjectMapper GitHub 저장소](https://github.com/tristanhimmelman/ObjectMapper)
- [ObjectMapper 매핑 가이드](https://github.com/tristanhimmelman/ObjectMapper#mapping)