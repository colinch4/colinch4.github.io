---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 요청 헤더 수정하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

AlamofireObjectMapper는 Alamofire를 기반으로하는 Swift 라이브러리입니다. 이 라이브러리를 사용하면 매우 간편하게 네트워크 요청 및 응답을 처리할 수 있습니다. 이 튜토리얼에서는 AlamofireObjectMapper를 사용하여 네트워크 요청의 요청 헤더를 수정하는 방법을 알아보겠습니다.

## Step 1: Alamofire와 AlamofireObjectMapper 설치하기

먼저 프로젝트에 Alamofire와 AlamofireObjectMapper를 설치해야 합니다. 이를 위해서는 프로젝트의 Podfile에 다음과 같이 추가해주세요.

```ruby
pod 'Alamofire'
pod 'AlamofireObjectMapper'
```

그런 다음 터미널에서 다음 명령어를 실행하여 라이브러리를 설치합니다.

```bash
$ pod install
```

## Step 2: 요청 헤더 수정하기

AlamofireObjectMapper를 사용하여 네트워크 요청의 헤더를 수정하려면 `Alamofire.RequestAdapter` 프로토콜을 구현해야 합니다. 다음과 같이 `CustomRequestAdapter` 클래스를 생성하여 이 프로토콜을 구현합니다.

```swift
import Alamofire

class CustomRequestAdapter: RequestAdapter {
    
    private let headers: [String: String]
    
    init(headers: [String: String]) {
        self.headers = headers
    }
    
    func adapt(_ urlRequest: URLRequest) throws -> URLRequest {
        var urlRequest = urlRequest
        
        for (key, value) in headers {
            urlRequest.setValue(value, forHTTPHeaderField: key)
        }
        
        return urlRequest
    }
}
```

위의 코드에서는 `CustomRequestAdapter` 클래스 내에서 `adapt` 메서드를 구현하여 헤더를 수정합니다. `adapt` 메서드는 현재의 `URLRequest`를 가져와서 `headers` 딕셔너리에 저장된 값으로 헤더를 수정한 후 반환합니다.

## Step 3: 사용자 정의 어댑터를 사용하여 요청 보내기

이제 CustomRequestAdapter를 사용하여 네트워크 요청을 보낼 수 있습니다. 다음은 사용자 정의 어댑터를 사용하여 GET 요청을 보내는 예제입니다.

```swift
import Alamofire
import AlamofireObjectMapper

let headers = [
    "Authorization": "Bearer <access_token>",
    "Content-Type": "application/json"
]

let url = "<your_api_endpoint>"

Alamofire.request(url)
    .validate()
    .adapt(using: CustomRequestAdapter(headers: headers))
    .responseObject { (response: DataResponse<YourModel>) in
        // 요청이 성공했을 때 처리할 코드 작성
    }
```

위의 코드에서 \<access_token>을 실제 액세스 토큰 값으로 대체하고 \<your_api_endpoint>를 사용할 API 엔드포인트 URL로 대체해야 합니다.

이제 `adapt(using:)` 메서드를 사용하여 `CustomRequestAdapter`를 적용하고 헤더를 요청에 적용하게 됩니다.

이렇게하면 네트워크 요청의 헤더를 수정하여 원하는 정보를 전송할 수 있게 됩니다.

## 결론

AlamofireObjectMapper를 사용하여 네트워크 요청의 헤더를 수정하는 방법을 살펴 보았습니다. 이를 통해 필요한 헤더 정보를 네트워크 요청에 쉽게 추가할 수 있습니다. 이러한 기능을 사용하여 앱의 인증 토큰과 같은 중요한 정보를 안전하게 전송할 수 있게 됩니다.