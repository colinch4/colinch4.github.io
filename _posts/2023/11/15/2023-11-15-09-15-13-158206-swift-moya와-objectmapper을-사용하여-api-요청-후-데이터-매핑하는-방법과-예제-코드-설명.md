---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용하여 API 요청 후 데이터 매핑하는 방법과 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift에서 Moya와 ObjectMapper를 함께 사용하여 API 요청 후 데이터를 매핑하는 방법에 대해 알아보겠습니다. Moya는 네트워킹 라이브러리이며, ObjectMapper는 JSON 데이터를 모델 객체로 변환해주는 라이브러리입니다. 이 두 라이브러리를 함께 사용하면 간단한 스위프트 코드 몇 줄로 API 요청과 데이터 매핑을 처리할 수 있습니다.

## Moya 설치하기

먼저 Moya를 설치해야 합니다. 이를 위해 CocoaPods를 사용하겠습니다. Podfile에 다음과 같이 Moya를 추가하세요.

```ruby
pod 'Moya'
```

터미널을 열고 프로젝트 디렉토리로 이동한 뒤, 다음 명령어를 실행하여 Moya를 설치합니다.

```bash
pod install
```

## ObjectMapper 설치하기

ObjectMapper도 CocoaPods를 사용하여 설치합니다. Podfile에 다음과 같이 ObjectMapper를 추가하세요.

```ruby
pod 'ObjectMapper'
```

터미널을 열고 프로젝트 디렉토리로 이동한 후, 다음 명령어를 실행하여 ObjectMapper를 설치합니다.

```bash
pod install
```

## 예제 코드 설명

아래는 간단한 예제 코드입니다. 예제에서는 사용자 정보를 가져오는 API를 호출하고, 응답으로 받은 JSON 데이터를 User 모델 객체로 매핑합니다.

```swift
import UIKit
import Moya
import ObjectMapper

// User 모델 정의
struct User: Mappable {
    var id: Int
    var name: String
    
    init?(map: Map) {
        id = 0
        name = ""
    }
    
    mutating func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
    }
}

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // API 요청 설정
        let provider = MoyaProvider<API>()
        provider.request(.getUser(id: 1)) { (result) in
            switch result {
            case .success(let response):
                do {
                    let user = try response.mapObject(User.self)
                    print("User ID: \(user.id)")
                    print("User Name: \(user.name)")
                } catch {
                    print("JSON 매핑 실패: \(error.localizedDescription)")
                }
            case .failure(let error):
                print("API 요청 실패: \(error.localizedDescription)")
            }
        }
    }
}

// API 열거형 정의
enum API {
    case getUser(id: Int)
}

extension API: TargetType {
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
```

이 예제에서는 먼저 User 모델을 Mappable 프로토콜을 채택하여 구현합니다. id와 name 속성을 매핑하기 위해 mapping(map:) 메서드를 구현합니다.

ViewController의 viewDidLoad() 메서드에서 MoyaProvider를 사용하여 API 요청을 보냅니다. 응답으로 받은 데이터를 mapObject() 메서드를 사용하여 User 객체로 매핑합니다. 성공적으로 매핑이 되었다면, User 객체의 속성을 출력합니다. 실패한 경우에는 에러 메시지를 출력합니다.

API 열거형을 정의하고, TargetType 프로토콜을 채택하여 필요한 URL, 메서드, sample data 등의 정보를 반환합니다.

이를 통해 Moya와 ObjectMapper를 함께 사용하여 API 요청 후 데이터를 매핑하는 간단한 예제를 살펴보았습니다.

## 결론

Swift에서 Moya와 ObjectMapper를 함께 사용하여 API 요청 후 데이터를 매핑하는 방법에 대해 알아보았습니다. Moya와 ObjectMapper를 사용하면 네트워킹과 데이터 매핑에 대한 작업을 간소화할 수 있으며, 코드의 가독성과 유지보수성도 향상시킬 수 있습니다.

## 참고 자료

- [Moya GitHub 페이지](https://github.com/Moya/Moya)
- [ObjectMapper GitHub 페이지](https://github.com/tristanhimmelman/ObjectMapper)