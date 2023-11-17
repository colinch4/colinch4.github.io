---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 인증 처리하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

AlamofireObjectMapper를 사용하면 Swift에서 네트워크 요청 및 응답을 쉽게 처리할 수 있습니다. 이 라이브러리는 Alamofire와 ObjectMapper를 결합하여 JSON 데이터를 객체로 매핑해주는 기능을 제공합니다. 이번에는 AlamofireObjectMapper를 사용하여 네트워크 요청의 인증 처리에 대해 알아보겠습니다.

## 1. AlamofireObjectMapper 설치

먼저, AlamofireObjectMapper를 사용하기 위해 프로젝트에 해당 라이브러리를 설치해야 합니다. Cocoapods를 사용하신다면 Podfile에 다음과 같이 추가합니다.

```ruby
pod 'AlamofireObjectMapper'
```

설치 후, 프로젝트를 업데이트합니다.

## 2. 네트워크 요청 구현하기

AlamofireObjectMapper를 사용하여 네트워크 요청을 구현해보겠습니다. 예를 들어, 서버로부터 JSON 형태의 사용자 정보를 가져오는 GET 요청을 보내는 코드를 작성해보겠습니다.

```swift
import Alamofire
import AlamofireObjectMapper

func fetchUserInfo(completion: @escaping (User?, Error?) -> Void) {
    let url = "https://api.example.com/user"
    
    Alamofire.request(url, method: .get).responseObject { (response: DataResponse<User>) in
        switch response.result {
        case .success(let user):
            completion(user, nil)
        case .failure(let error):
            completion(nil, error)
        }
    }
}
```

위 코드에서는 Alamofire의 `request` 메서드를 사용하여 GET 요청을 보냅니다. `responseObject` 메서드는 응답 데이터를 User 객체로 매핑해줍니다. 성공적인 응답의 경우에는 `success` 케이스에서 매핑된 User 객체를 반환하고, 실패한 경우에는 `failure` 케이스에서 에러를 반환합니다.

## 3. 인증 처리하기

네트워크 요청의 인증 처리를 위해, Alamofire의 `request` 메서드에서 `headers` 매개변수를 사용할 수 있습니다. 예를 들어, 사용자의 인증 토큰을 헤더에 추가하여 요청을 보내는 방법은 다음과 같습니다.

```swift
import Alamofire
import AlamofireObjectMapper

func fetchUserInfo(token: String, completion: @escaping (User?, Error?) -> Void) {
    let url = "https://api.example.com/user"
    let headers: HTTPHeaders = ["Authorization": "Bearer \(token)"]
    
    Alamofire.request(url, method: .get, headers: headers).responseObject { (response: DataResponse<User>) in
        switch response.result {
        case .success(let user):
            completion(user, nil)
        case .failure(let error):
            completion(nil, error)
        }
    }
}
```

위 코드에서 `headers` 변수를 생성하여 `Authorization` 키에 인증 토큰을 설정한 후, `request` 메서드에 `headers` 매개변수로 전달합니다. 이렇게 하면 헤더에 인증 토큰이 포함된 요청이 서버로 전송됩니다.

## 4. 요청 보내기

마지막으로, `fetchUserInfo` 함수를 호출하여 요청을 보내고 응답을 처리하는 코드를 작성해야 합니다. 다음은 사용자 정보를 가져와서 출력하는 예제입니다.

```swift
let token = "your_auth_token"

fetchUserInfo(token: token) { (user, error) in
    if let user = user {
        print("User ID: \(user.id)")
        print("User Name: \(user.name)")
        // 사용자 정보를 처리하는 코드 작성
    } else if let error = error {
        print("Error: \(error.localizedDescription)")
        // 에러 처리 코드 작성
    }
}
```

위 코드에서는 `fetchUserInfo` 함수를 호출하여 사용자 정보를 가져옵니다. 성공적인 응답의 경우에는 사용자 정보를 출력하고, 실패한 경우에는 에러 메시지를 출력합니다.

## 결론

이번에는 AlamofireObjectMapper를 사용하여 네트워크 요청의 인증 처리에 대해 알아보았습니다. Alamofire와 ObjectMapper의 결합으로 JSON 데이터를 쉽게 객체로 매핑할 수 있습니다. 인증 처리에 필요한 헤더 정보를 설정하여 요청을 보내고 응답을 처리하는 방법을 배웠습니다. 이를 활용하여 안전하고 신뢰할 수 있는 네트워크 요청을 구현해보세요.