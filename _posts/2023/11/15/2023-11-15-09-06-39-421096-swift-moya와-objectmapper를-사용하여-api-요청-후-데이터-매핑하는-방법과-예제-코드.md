---
layout: post
title: "[swift] Swift Moya와 ObjectMapper를 사용하여 API 요청 후 데이터 매핑하는 방법과 예제 코드"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift 언어로 API 요청을 보내고, 받은 데이터를 매핑하는 방법을 알아보겠습니다. 이를 위해 Moya와 ObjectMapper라는 유용한 라이브러리를 사용할 것입니다. Moya는 네트워크 작업을 쉽게 처리하기 위한 추상화 레이어를 제공하고, ObjectMapper는 JSON 데이터를 Swift 객체로 매핑하기 위한 라이브러리입니다.

## Moya 설치

Moya를 사용하기 위해, Cocoapods를 사용하여 프로젝트에 Moya를 설치해야 합니다. `Podfile`에 다음과 같은 내용을 추가하세요.

```ruby
pod 'Moya'
```

그리고 터미널에서 `pod install` 명령어를 실행하여 Moya를 설치하세요.

## ObjectMapper 설치

ObjectMapper도 Cocoapods를 사용하여 설치합니다. `Podfile`에 다음과 같은 내용을 추가하세요.

```ruby
pod 'ObjectMapper'
```

위와 같이 추가하고 `pod install` 명령어를 실행하여 ObjectMapper를 설치하세요.

## Moya를 통한 API 요청

먼저, Moya를 사용하여 API 요청을 보내는 방법을 알아보겠습니다. Moya는 `TargetType` 프로토콜을 사용하여 API 엔드포인트와 관련된 정보를 정의합니다. 다음은 예제 코드입니다.

```swift
import Moya

enum MyAPI {
    case getUser(id: Int)
    case updateUser(id: Int, name: String)
}

extension MyAPI: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }
    
    var path: String {
        switch self {
        case .getUser(let id):
            return "/users/\(id)"
        case .updateUser(let id, _):
            return "/users/\(id)"
        }
    }
    
    var method: Moya.Method {
        switch self {
        case .getUser:
            return .get
        case .updateUser:
            return .put
        }
    }
    
    var sampleData: Data {
        return Data()
    }
    
    var task: Task {
        switch self {
        case .updateUser(_, let name):
            return .requestParameters(parameters: ["name": name], encoding: JSONEncoding.default)
        default:
            return .requestPlain
        }
    }
    
    var headers: [String: String]? {
        return nil
    }
}
```

위의 코드에서는 `MyAPI`라는 열거형을 정의하고, `TargetType` 프로토콜을 구현해 API 엔드포인트와 관련된 정보를 제공합니다. `baseURL`, `path`, `method`, `task`, `headers` 등을 정의하여 API 요청에 필요한 정보를 설정할 수 있습니다.

## ObjectMapper를 사용하여 데이터 매핑

API 응답을 받은 후, ObjectMapper를 사용하여 JSON 데이터를 Swift 객체로 매핑합니다. 다음은 예제 코드입니다.

```swift
import ObjectMapper
import Moya

class ViewController: UIViewController {
    let provider = MoyaProvider<MyAPI>()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        provider.request(.getUser(id: 1)) { result in
            switch result {
            case let .success(response):
                do {
                    let user = try response.mapObject(User.self)
                    print(user.name)
                } catch {
                    print(error)
                }
            case let .failure(error):
                print(error)
            }
        }
    }
}

class User: Mappable {
    var id: Int?
    var name: String?
    
    required init?(map: Map) {}
    
    func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
    }
}
```

위의 코드에서는 `ViewController` 클래스 내부에서 MoyaProvider를 초기화하고, `request` 메서드를 사용하여 API 요청을 보냅니다. 응답을 받으면 `do-catch` 블록 내에서 ObjectMapper를 사용하여 JSON 데이터를 `User` 객체로 매핑합니다.

위의 예제 코드를 참고하여 Moya와 ObjectMapper를 사용하여 API 요청 후 데이터를 매핑하는 방법을 익힐 수 있습니다.

## 마무리

이번 포스트에서는 Swift 언어를 사용하여 Moya와 ObjectMapper를 활용하여 API 요청을 보내고, 받은 데이터를 매핑하는 방법을 알아보았습니다. Moya와 ObjectMapper는 네트워크 작업과 데이터 매핑을 더욱 간편하게 처리할 수 있도록 도와줍니다.

더 자세한 정보와 기능에 대해 알고 싶다면, [Moya](https://github.com/Moya/Moya)와 [ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)의 공식 문서를 참고하시기 바랍니다.