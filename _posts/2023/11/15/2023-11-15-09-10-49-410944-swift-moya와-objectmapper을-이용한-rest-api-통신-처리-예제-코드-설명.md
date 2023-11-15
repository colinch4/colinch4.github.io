---
layout: post
title: "[swift] Swift Moya와 ObjectMapper을 이용한 REST API 통신 처리 예제 코드 설명"
description: " "
date: 2023-11-15
tags: [swift]
comments: true
share: true
---

이번에는 Swift에서 Moya와 ObjectMapper 라이브러리를 이용하여 REST API 통신을 처리하는 방법에 대해 알아보겠습니다.

## Moya란?

Moya는 Swift에서 네트워크 요청을 추상화하고 클라이언트를 만들기 위한 라이브러리입니다. Moya는 네트워크를 위한 추상화 계층을 제공하여 클라이언트와 서버 사이의 통신을 단순화합니다. Moya는 Alamofire와 함께 사용되어 네트워크 요청을 보내고 응답을 처리할 수 있습니다.

## ObjectMapper란?

ObjectMapper는 JSON 데이터를 객체로 매핑하는 라이브러리입니다. ObjectMapper를 사용하면 JSON 응답을 Swift 객체로 변환하고 Swift 객체를 JSON으로 변환할 수 있습니다. 이를 통해 네트워크에서 받아온 JSON 데이터를 쉽게 처리할 수 있습니다.

## 예제 코드 설명

먼저, 프로젝트에 Moya와 ObjectMapper를 설치해야 합니다. [CocoaPods](https://cocoapods.org)를 이용하여 다음과 같이 Podfile에 라이브러리를 추가합니다:

```
pod 'Moya'
pod 'ObjectMapper'
```
그리고 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

다음으로, Moya와 ObjectMapper를 사용하여 REST API 통신을 처리하는 코드를 작성해보겠습니다. 예제로는 [JSON Placeholder](https://jsonplaceholder.typicode.com)에서 제공하는 API를 사용하도록 하겠습니다.

```Swift
import Moya
import ObjectMapper

struct Post: Mappable {
    var id: Int?
    var title: String?
    var body: String?
    
    init?(map: Map) {}
    
    mutating func mapping(map: Map) {
        id <- map["id"]
        title <- map["title"]
        body <- map["body"]
    }
}

enum API {
    case getPosts
}

extension API: TargetType {
    var baseURL: URL {
        return URL(string: "https://jsonplaceholder.typicode.com")!
    }
    
    var path: String {
        switch self {
        case .getPosts:
            return "/posts"
        }
    }
    
    var method: Method {
        switch self {
        case .getPosts:
            return .get
        }
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

class APIManager {
    static let shared = APIManager()
    private let provider = MoyaProvider<API>()
    
    func getPosts(completion: @escaping ([Post]?) -> Void) {
        provider.request(.getPosts) { result in
            switch result {
            case let .success(response):
                do {
                    let posts = try response.mapArray(Post.self)
                    completion(posts)
                } catch {
                    print("Mapping error: \(error)")
                    completion(nil)
                }
            case let .failure(error):
                print(error)
                completion(nil)
            }
        }
    }
}

// Usage
APIManager.shared.getPosts { posts in
    if let posts = posts {
        for post in posts {
            print(post.title ?? "")
        }
    } else {
        print("Error fetching posts")
    }
}
```

이 예제에서는 `Post`라는 구조체를 생성하고, `Mappable` 프로토콜을 구현해서 ObjectMapper로 JSON 데이터를 매핑합니다. `API`라는 열거형을 만들어 API의 엔드포인트와 HTTP 요청 방식을 정의합니다. 그리고 `APIManager` 클래스를 생성하여 MoyaProvider를 이용하여 특정 API를 호출하는 `getPosts` 메서드를 구현합니다.

위의 코드를 실행하면 JSON Placeholder에서 제공하는 게시물 목록을 받아와서 출력합니다.

이 예제 코드는 Moya와 ObjectMapper를 이용하여 Swift에서 REST API 통신을 처리하는 방법을 보여주는 간단한 예제입니다. 실제 프로젝트에서는 서버와의 통신 방식에 맞게 API를 구성하고, 객체 매핑을 위한 ObjectMapper의 매핑 로직을 작성해야 합니다.

더 자세한 정보는 [Moya](https://github.com/Moya/Moya)와 [ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)의 공식 문서를 참고해주세요.