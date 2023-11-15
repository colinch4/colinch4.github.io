---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용한 네트워크 통신 및 데이터 매핑 예제 코드"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift의 Moya와 ObjectMapper 라이브러리를 사용하여 네트워크 통신을 수행하고, 서버에서 받은 JSON 데이터를 매핑하는 방법을 알아보겠습니다.

Moya는 Alamofire를 기반으로한 네트워크 추상화 라이브러리이며, ObjectMapper는 JSON 데이터와 Swift 클래스 간의 매핑을 쉽게 해주는 라이브러리입니다.

먼저, 프로젝트에 Moya와 ObjectMapper를 설치합니다. Cocoapods를 사용한다면, Podfile에 다음과 같이 추가합니다.

```ruby
pod 'Moya'
pod 'ObjectMapper'
```

설치가 완료되었다면, 네트워크 통신을 위한 API Provider와 매핑할 모델 클래스를 선언합니다. 예제에서는 GitHub API를 사용하고 User 모델 클래스를 매핑할 것입니다.

```swift
import Foundation
import Moya
import ObjectMapper

// GitHub API Provider 정의
enum GitHubAPI {
    case getUser(username: String)
}

extension GitHubAPI: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.github.com")!
    }
    
    var path: String {
        switch self {
        case .getUser(let username):
            return "/users/\(username)"
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

// 매핑할 모델 클래스 정의
class User: Mappable {
    var login: String?
    var id: Int?
    var name: String?
    
    required init?(map: Map) {}
    
    func mapping(map: Map) {
        login <- map["login"]
        id <- map["id"]
        name <- map["name"]
    }
}
```

이제 네트워크 통신을 수행하고 데이터를 매핑하는 코드를 작성해보겠습니다.

```swift
import Moya
import ObjectMapper

// Moya Provider 생성
let provider = MoyaProvider<GitHubAPI>()

// API 호출 및 데이터 매핑
provider.request(.getUser(username: "sihyung92")) { (result) in
    switch result {
    case .success(let response):
        do {
            let user = try response.mapObject(User.self)
            print(user.name)
        } catch {
            print("Mapping Error")
        }
        
    case .failure(let error):
        print(error.localizedDescription)
    }
}
```

위의 코드에서는 Moya Provider를 생성하고, getUser API를 호출한 후 응답 데이터를 User 모델 클래스로 매핑합니다. 만약 매핑에 실패하면 "Mapping Error"를 출력하고, 성공적으로 매핑이 되었다면 User 객체의 name 속성을 출력합니다.

이렇게 Swift Moya와 ObjectMapper을 사용하여 네트워크 통신 및 데이터 매핑을 수행할 수 있습니다.

---

### 참고 자료

- [Moya GitHub Repository](https://github.com/Moya/Moya)
- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)