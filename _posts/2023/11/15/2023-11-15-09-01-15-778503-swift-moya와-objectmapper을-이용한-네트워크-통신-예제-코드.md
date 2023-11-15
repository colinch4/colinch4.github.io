---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 이용한 네트워크 통신 예제 코드"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번에는 Swift에서 Moya와 ObjectMapper을 이용하여 간편하게 네트워크 통신을 하는 방법에 대해 알아보겠습니다.

## Moya란?
Moya는 Alamofire를 기반으로 한 네트워크 추상화 라이브러리로, 네트워크 호출을 보다 쉽고 간결하게 작성할 수 있도록 도와줍니다.

## ObjectMapper란?
ObjectMapper는 Swift에서 JSON 데이터를 모델 객체로 매핑하기 위한 라이브러리입니다. JSON 데이터와 Swift 객체 사이의 변환 작업을 더욱 간편하게 처리할 수 있게 도와줍니다.

## 설치하기
먼저, Moya와 ObjectMapper을 설치해야 합니다. 이를 위해서는 CocoaPods를 사용할 수 있습니다. Podfile에 다음 코드를 추가한 뒤, `pod install` 명령어를 실행합니다.

```
pod 'Moya'
pod 'ObjectMapper'
```

## 예제 코드
다음은 Moya와 ObjectMapper을 이용하여 네트워크 통신을 하는 간단한 예제 코드입니다.

```swift
import Moya
import ObjectMapper

// Moya provider 생성
let provider = MoyaProvider<API>()

// API 열거형 정의
enum API {
    case getUserInfo(id: Int)
}

extension API: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }

    var path: String {
        switch self {
        case .getUserInfo(let id):
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

    var headers: [String: String]? {
        return nil
    }
}

// 네트워크 요청
provider.request(.getUserInfo(id: 1)) { result in
    switch result {
    case let .success(response):
        do {
            let json = try response.mapJSON()
            if let user = Mapper<User>().map(JSONObject: json) {
                print("User: \(user)")
            }
        } catch {
            print("Mapping Error: \(error)")
        }
    case let .failure(error):
        print("Network Error: \(error)")
    }
}

// 모델 객체 정의
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
```

위의 코드에서는 먼저 Moya와 ObjectMapper을 import 합니다. 그 후, MoyaProvider를 생성하고 API 열거형을 정의합니다. API 열거형은 API 요청의 타깃 정보를 포함하고 있습니다.

그리고 getRequest 함수를 통해 네트워크 요청을 보냅니다. 결과는 네트워크 성공 및 실패에 따라 처리되며, 성공시 ObjectMapper를 사용하여 JSON을 모델 객체로 매핑합니다.

마지막으로 모델 객체인 User를 정의하고 ObjectMapper의 Mappable 프로토콜을 채택하여 JSON과의 매핑 작업을 수행합니다.

이렇게 간편하게 Moya와 ObjectMapper을 이용하여 네트워크 통신을 할 수 있습니다.

## 결론
Swift에서 Moya와 ObjectMapper을 함께 사용하여 네트워크 통신을 보다 쉽고 간결하게 작성할 수 있습니다. 이를 이용하여 JSON 데이터를 모델 객체로 변환하여 사용할 수 있습니다. 관련 자세한 내용은 [Moya 공식 문서](https://github.com/Moya/Moya)와 [ObjectMapper 공식 문서](https://github.com/tristanhimmelman/ObjectMapper)를 참고해주세요.