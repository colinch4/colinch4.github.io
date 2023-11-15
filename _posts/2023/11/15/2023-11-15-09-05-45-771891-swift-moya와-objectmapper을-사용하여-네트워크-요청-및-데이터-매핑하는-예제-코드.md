---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 사용하여 네트워크 요청 및 데이터 매핑하는 예제 코드"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---
import Moya
import ObjectMapper

// 모델 클래스 선언
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

// MoyaProvider 선언
let provider = MoyaProvider<MyAPI>()

// API 열거형 정의
enum MyAPI {
    case getUser(userID: Int)
}

extension MyAPI: TargetType {
    var baseURL: URL {
        return URL(string: "https://api.example.com")!
    }
    
    var path: String {
        switch self {
        case .getUser(let userID):
            return "/users/\(userID)"
        }
    }
    
    var method: Method {
        return .get
    }
    
    var headers: [String: String]? {
        return nil
    }
    
    var task: Task {
        return .requestPlain
    }
    
    var sampleData: Data {
        return Data()
    }
}

// 네트워크 요청 및 데이터 매핑
provider.request(.getUser(userID: 1)) { result in
    switch result {
    case .success(let response):
        do {
            let user = try response.mapObject(User.self)
            print(user.id)
            print(user.name)
        } catch {
            print(error)
        }
    case .failure(let error):
        print(error)
    }
}
```

위의 예제 코드는 Swift에서 Moya와 ObjectMapper 라이브러리를 사용하여 네트워크 요청을 보내고 데이터를 매핑하는 방법을 보여주고 있습니다.

먼저, User라는 모델 클래스를 선언합니다. 이 클래스는 ObjectMapper의 Mappable 프로토콜을 구현하고, 매핑을 위한 프로퍼티와 초기화 메소드를 구현합니다.

다음으로, MyAPI라는 열거형을 정의합니다. 이 열거형은 Moya의 TargetType 프로토콜을 구현하며, API의 baseURL, path, method, headers, task, sampleData 등을 정의합니다. 이 예제에서는 사용자 정보를 가져오는 API만 정의되어 있습니다.

MoyaProvider를 생성하여 API를 호출할 준비를 합니다.

마지막으로, provider.request 메소드를 사용하여 API를 호출하고, 응답 데이터를 매핑합니다. 성공적으로 매핑되면 User 객체를 얻을 수 있으며, 에러가 발생하면 해당 에러를 출력합니다.

위의 예제 코드를 참고하여 Swift에서 Moya와 ObjectMapper를 사용하여 네트워크 요청을 보내고 데이터를 매핑할 수 있습니다.