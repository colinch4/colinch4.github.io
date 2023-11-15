---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 이용한 API 클라이언트 구현하기"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번에는 Swift 프로그래밍 언어를 사용하여 Moya와 ObjectMapper을 이용하여 간단한 API 클라이언트를 구현해 보겠습니다. Moya는 Alamofire를 기반으로 한 네트워킹 라이브러리이며, ObjectMapper는 JSON 데이터를 Swift 객체로 매핑해주는 라이브러리입니다.

## 목차
- [Moya와 ObjectMapper 설치](#moya와-objectmapper-설치)
- [API 모델 정의하기](#api-모델-정의하기)
- [MoyaProvider 설정하기](#moyaprovider-설정하기)
- [API 호출하기](#api-호출하기)

## Moya와 ObjectMapper 설치

먼저, 프로젝트에 Moya와 ObjectMapper를 설치해야 합니다. 이를 위해서는 CocoaPods를 이용할 수 있습니다. 

```ruby
pod 'Moya'
pod 'ObjectMapper'
```
위와 같이 Podfile에 Moya와 ObjectMapper를 추가한 다음, 터미널을 열어 다음 명령어를 실행하세요.

```
pod install
```

## API 모델 정의하기

API를 호출하기 위해서는 먼저 API 모델을 정의해야 합니다. 예를 들어, 사용자 정보를 가져오는 API의 응답 데이터를 파싱하기 위한 모델을 정의해보도록 하겠습니다.

```swift
import Foundation
import ObjectMapper

class UserResponse: Mappable {
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

위 코드에서는 ObjectMapper의 Mappable 프로토콜을 채택한 UserResponse라는 클래스를 정의했습니다. 응답 데이터의 각 필드와 매칭되는 속성들을 선언하고, mapping 메서드를 통해 매핑 정보를 설정합니다.

## MoyaProvider 설정하기

다음으로 MoyaProvider를 설정해야 합니다. MoyaProvider는 API 호출을 담당하는 객체입니다. 

```swift
import Moya

// API Target 정의하기
enum UserAPI {
    case getUser // 사용자 정보 가져오기
}

extension UserAPI: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }

    var path: String {
        switch self {
        case .getUser:
            return "/users"
        }
    }

    var method: Moya.Method {
        switch self {
        case .getUser:
            return .get
        }
    }

    var sampleData: Data {
        return Data()
    }

    var task: Task {
        switch self {
        case .getUser:
            return .requestPlain
        }
    }

    var headers: [String: String]? {
        return nil
    }
}

// MoyaProvider 생성하기
let provider = MoyaProvider<UserAPI>()
```

위의 코드에서는 UserAPI라는 열거형을 정의하고, TargetType 프로토콜을 채택하여 API 호출에 필요한 정보를 구현했습니다. baseURL은 API의 기본 URL을 설정하고, path, method 등의 필수 속성들을 정의합니다.

그리고 마지막으로 MoyaProvider 객체를 생성하고, Generic으로 UserAPI를 전달하여 설정합니다.

## API 호출하기

이제 API를 호출해보겠습니다. getUser API를 호출하여 사용자 정보를 가져오는 예제를 살펴보도록 하겠습니다.

```swift
provider.request(.getUser) { result in
    switch result {
    case let .success(response):
        do {
            let userResponse = try response.mapObject(UserResponse.self)
            // 사용자 정보 출력
            print(userResponse)
        } catch {
            // 응답 데이터 매핑 실패
            print("Error mapping response")
        }
    case let .failure(error):
        // API 호출 실패
        print("API Request failed: \(error)")
    }
}
```

위의 코드에서는 MoyaProvider 객체의 request 메서드를 호출하여 API를 요청합니다. 이후 응답 처리는 response의 상태 코드와 응답 데이터를 확인하고, ObjectMapper를 사용하여 JSON 데이터를 UserResponse 객체로 매핑합니다.

마지막으로, 에러 처리를 위한 switch 문을 사용하여 요청이 실패한 경우와 매핑에 실패한 경우에 대한 처리를 구현합니다.

## 결론

이제 Swift Moya와 ObjectMapper을 이용하여 API 클라이언트를 구현하는 방법에 대해 알아보았습니다. 이를 통해 간단한 API 요청과 JSON 데이터 매핑을 쉽게 처리할 수 있습니다. Moya와 ObjectMapper은 각각 강력한 기능을 제공하므로, 프로젝트에 맞게 유연하게 사용할 수 있습니다.