---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 이용한 REST API 통신 처리 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번 예제에서는 Swift 언어를 사용하여 Moya와 ObjectMapper을 이용하여 REST API와 통신하는 방법에 대해 알아보겠습니다. 

Moya는 Alamofire를 기반으로한 네트워킹 추상화 라이브러리이며, ObjectMapper는 JSON 데이터를 간편하게 매핑해주는 라이브러리입니다. 

## Step 1: 프로젝트 설정
1. 프로젝트에서 Moya 및 ObjectMapper 패키지를 설치하세요. 
2. 프로젝트 파일에서 `import Moya`와 `import ObjectMapper`를 추가하세요. 

## Step 2: Moya 타겟 생성
1. 타겟을 생성하고, MoyaProvider 객체를 생성하세요. 

```swift
let provider = MoyaProvider<MyAPI>()
```

2. 통신할 REST API의 endpoint와 메소드를 정의한 Enum을 생성하세요. 

```swift
enum MyAPI {
    case getUsers
}
```

3. 타겟에 필요한 프로토콜을 구현하세요.

```swift
extension MyAPI: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com/")!
    }
    
    var path: String {
        switch self {
        case .getUsers:
            return "users"
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
    
    var headers: [String: String]? {
        return ["Content-type": "application/json"]
    }
}
```

## Step 3: ObjectMapper로 데이터 매핑
1. Moya의 request를 호출하여 API와 통신하고 결과를 받아옵니다.

```swift
provider.request(.getUsers) { result in
    switch result {
    case let .success(response):
        do {
            let users = try response.mapArray(User.self)
            // 매핑된 데이터 사용
        } catch {
            // 매핑 실패 처리
        }
    case let .failure(error):
        // 에러 처리
    }
}
```

2. ObjectMapper의 `mapArray` 또는 `mapObject` 메소드를 사용하여 JSON 데이터를 매핑합니다.

```swift
struct User: Mappable {
    var name: String?

    init?(map: Map) {}

    mutating func mapping(map: Map) {
        name <- map["name"]
    }
}
```

위 예제에서는 `User`라는 모델 객체를 정의하고, `mapping` 메소드에서 JSON 데이터와 모델 객체의 속성을 매핑했습니다. 

이제, Moya와 ObjectMapper을 이용하여 REST API와 통신하고 데이터를 매핑하는 예제를 확인했습니다. 이를 기반으로 실제 프로젝트에서 활용해 보세요.


참고 자료:
- Moya GitHub 레포지토리: [https://github.com/Moya/Moya](https://github.com/Moya/Moya)
- ObjectMapper GitHub 레포지토리: [https://github.com/tristanhimmelman/ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)