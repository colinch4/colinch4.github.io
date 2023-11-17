---
layout: post
title: "[swift] Swift에서 AlamofireObjectMapper 사용 방법"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

AlamofireObjectMapper은 Alamofire와 ObjectMapper를 결합한 라이브러리로, 서버 API로부터 받은 JSON 데이터를 쉽게 모델 객체로 매핑할 수 있게 해줍니다. 이 블로그 포스트에서는 Swift에서 AlamofireObjectMapper를 사용하는 방법에 대해 알아보겠습니다.

## 1. Alamofire와 ObjectMapper 설치하기

먼저, 프로젝트에서 Alamofire와 ObjectMapper를 설치해야 합니다. Cocoapods를 사용하는 경우, Podfile에 아래의 항목을 추가하고 `$ pod install` 명령어를 실행하세요.

```ruby
pod 'Alamofire'
pod 'ObjectMapper'
pod 'AlamofireObjectMapper'
```

## 2. 모델 객체 생성하기

다음으로, JSON 데이터를 매핑할 모델 객체를 생성해야 합니다. 예를 들어, 서버로부터 받은 유저 정보를 매핑하는 User 모델을 생성해보겠습니다.

```swift
import Foundation
import ObjectMapper

class User: Mappable {
    var id: Int?
    var name: String?
    var email: String?

    required init?(map: Map) {

    }

    func mapping(map: Map) {
        id <- map["id"]
        name <- map["name"]
        email <- map["email"]
    }
}
```

User 모델은 ObjectMapper의 `Mappable` 프로토콜을 채택하고, `mapping(map:)` 메서드를 구현해야 합니다. 이 메서드에서는 JSON 키와 모델 속성을 매핑하는 코드를 작성합니다.

## 3. Alamofire와 ObjectMapper 사용하기

이제 Alamofire와 ObjectMapper를 사용하여 서버 API로부터 받은 JSON 데이터를 User 객체로 매핑하는 방법을 알아보겠습니다.

```swift
import Alamofire
import AlamofireObjectMapper

func fetchUserInfo() {
    let url = "https://api.example.com/user"
    
    Alamofire.request(url, method: .get).responseObject { (response: DataResponse<User>) in
        switch response.result {
        case .success(let user):
            // User 객체 사용
            print(user.id)
            print(user.name)
            print(user.email)
        case .failure(let error):
            // 에러 처리
            print(error.localizedDescription)
        }
    }
}
```

위의 코드에서는 Alamofire의 `request` 메서드를 사용하여 서버로부터 유저 정보를 가져옵니다. `responseObject` 메서드를 통해 이를 User 객체로 매핑하며, 매핑 결과는 `response.result`에서 확인할 수 있습니다.

## 결론

Swift에서 Alamofire와 ObjectMapper를 함께 사용하는 방법에 대해 알아보았습니다. 이를 활용하여 서버 API로부터 받은 JSON 데이터를 쉽게 모델 객체로 매핑할 수 있습니다. 더 자세한 내용과 사용 예제는 [AlamofireObjectMapper GitHub](https://github.com/tristanhimmelman/AlamofireObjectMapper)을 참고하세요.