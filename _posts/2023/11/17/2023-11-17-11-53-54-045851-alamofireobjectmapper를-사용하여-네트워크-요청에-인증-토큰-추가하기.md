---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청에 인증 토큰 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift의 AlamofireObjectMapper 라이브러리를 사용하면 네트워크 요청에 간단하게 인증 토큰을 추가할 수 있습니다. 이를 통해 API 요청에 필요한 인증 과정을 간편하게 처리할 수 있습니다.

## AlamofireObjectMapper 라이브러리 추가하기

먼저, AlamofireObjectMapper 라이브러리를 프로젝트에 추가해야 합니다. Cocoapods를 사용하는 경우, Podfile에 다음과 같이 추가합니다.

```ruby
pod 'AlamofireObjectMapper'
```

이후, 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## 인증 토큰을 요청 헤더에 추가하기

인증 토큰을 요청 헤더에 추가하기 위해 다음과 같이 코드를 작성합니다.

```swift
import Alamofire
import AlamofireObjectMapper

func requestWithAuthToken() {
    // API 요청 URL
    let url = "https://api.example.com/users"
    
    // 인증 토큰 값
    let authToken = "your_auth_token"
    
    // Alamofire의 request 메서드를 사용하여 네트워크 요청 생성
    Alamofire.request(url, method: .get, headers: ["Authorization": "Bearer \(authToken)"]).responseObject { (response: DataResponse<UserResponse>) in
        switch response.result {
        case .success(let userResponse):
            // 요청 성공 시 처리할 코드
            // 받아온 데이터를 UserResponse 모델로 매핑하여 사용할 수 있습니다.
        case .failure(let error):
            // 요청 실패 시 처리할 코드
            print(error)
        }
    }
}
```

위 코드에서는 Alamofire의 `request` 메서드를 사용하여 GET 요청을 보내고, `Authorization` 헤더에 인증 토큰을 추가하고 있습니다. 응답 데이터는 `UserResponse` 모델로 매핑하여 사용할 수 있습니다.

앱에서 실제 사용하는 인증 토큰 값을 `authToken` 변수에 할당하고, 해당 코드를 호출하면 인증 토큰이 포함된 네트워크 요청이 생성됩니다.

## 결론

AlamofireObjectMapper 라이브러리를 사용하여 네트워크 요청에 인증 토큰을 간단하게 추가할 수 있습니다. 이를 통해 인증 토큰을 헤더에 포함시켜 안전하고 신뢰할 수 있는 API 요청을 보낼 수 있습니다.

---
**References**:
- [AlamofireObjectMapper GitHub repository](https://github.com/tristanhimmelman/AlamofireObjectMapper)