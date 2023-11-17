---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 리턴 타입 설정하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---
AlamofireObjectMapper는 Alamofire와 ObjectMapper을 함께 사용하여 네트워크 요청의 리턴 타입을 설정하는 데 도움을 줍니다. 이 라이브러리를 사용하면 JSON 데이터를 자동으로 모델 객체로 매핑할 수 있습니다.

## 1. AlamofireObjectMapper 설치하기
먼저 AlamofireObjectMapper을 프로젝트에 설치해야 합니다. 다음 명령어를 사용하여 CocoaPods를 통해 설치할 수 있습니다.

```shell
pod 'AlamofireObjectMapper', '~> 5.2'
```

## 2. 모델 객체 생성하기
요청의 리턴 타입으로 사용할 모델 객체를 생성해야 합니다. 예를 들어, 사용자 정보를 담기 위한 `User` 모델 객체를 만들어보겠습니다.

```swift
import Foundation
import ObjectMapper

class User: Mappable {
    var name: String?
    var email: String?

    required init?(map: Map) {}

    func mapping(map: Map) {
        name <- map["name"]
        email <- map["email"]
    }
}
```

위의 코드에서는 `Mappable` 프로토콜을 채택하여 ObjectMapper에서 사용할 수 있도록 합니다. `mapping(map:)` 메서드를 통해 JSON 데이터와 모델 객체의 프로퍼티를 매핑합니다.

## 3. Alamofire 요청 설정하기
이제 Alamofire를 사용하여 네트워크 요청을 설정해보겠습니다. `response` 메서드를 호출할 때, `responseObject` 메서드를 사용하여 리턴 타입을 설정할 수 있습니다.

```swift
import Alamofire
import AlamofireObjectMapper

func getUser(completion: @escaping (User?, Error?) -> Void) {
    Alamofire.request("https://api.example.com/users/1").responseObject { (response: DataResponse<User>) in
        switch response.result {
        case .success(let user):
            completion(user, nil)
        case .failure(let error):
            completion(nil, error)
        }
    }
}
```

위의 코드에서는 `response.result`를 통해 네트워크 요청의 성공과 실패를 처리합니다. 성공한 경우 `User` 모델 객체가 있으며, 실패한 경우에는 `Error` 객체가 반환됩니다.

## 4. 사용하기
이제 `getUser` 함수를 사용하여 사용자 정보를 가져오는 예제를 살펴보겠습니다.

```swift
getUser { user, error in
    if let user = user {
        print("Name: \(user.name)")
        print("Email: \(user.email)")
    } else if let error = error {
        print("Error: \(error.localizedDescription)")
    }
}
```

위의 코드에서는 `getUser` 함수를 호출한 후, 리턴된 `User` 객체를 사용하여 사용자의 이름과 이메일을 출력합니다. 만약 에러가 발생한 경우 에러 메시지를 출력합니다.

## 결론
AlamofireObjectMapper를 사용하여 네트워크 요청의 리턴 타입을 설정하는 방법에 대해 알아보았습니다. 이러한 방식을 사용하면 JSON 데이터를 간편하게 모델 객체로 변환할 수 있으며, 손쉽게 네트워크 요청의 결과를 다룰 수 있습니다.

---

### 참고 자료
- [AlamofireObjectMapper GitHub](https://github.com/tristanhimmelman/AlamofireObjectMapper)
- [ObjectMapper GitHub](https://github.com/tristanhimmelman/ObjectMapper)