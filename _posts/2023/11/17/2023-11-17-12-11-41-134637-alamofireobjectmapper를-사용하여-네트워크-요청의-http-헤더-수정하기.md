---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 HTTP 헤더 수정하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

AlamofireObjectMapper는 Alamofire와 ObjectMapper를 통합하여 JSON 응답을 쉽게 매핑하는 라이브러리입니다. 이 라이브러리를 사용하면 네트워크 요청의 HTTP 헤더를 수정하는 것도 간단해집니다. 이번 블로그 포스트에서는 AlamofireObjectMapper를 사용하여 네트워크 요청의 HTTP 헤더를 수정하는 방법에 대해 알아보겠습니다.

## AlamofireObjectMapper 라이브러리 설치하기

먼저, `Podfile`에 Alamofire와 ObjectMapper, 그리고 AlamofireObjectMapper를 추가해주세요.

```ruby
pod 'Alamofire'
pod 'ObjectMapper'
pod 'AlamofireObjectMapper'
```

그리고 터미널을 열고 프로젝트 루트 디렉토리에서 다음 명령을 실행하여 라이브러리를 설치해주세요.

```bash
$ pod install
```

## HTTP 헤더 수정하기

HTTP 요청을 보낼 때, AlamofireObjectMapper를 사용하여 HTTP 헤더를 수정하는 방법은 간단합니다. 여기서는 예시로 토큰 기반 인증(Authentication)을 사용하여 HTTP 요청에 헤더를 추가하는 방법을 알아보겠습니다.

우선, Alamofire의 `Session` 객체를 생성하고, `Interceptor` 프로토콜을 채택한 클래스를 정의합니다. 이 클래스에서는 `adapt` 함수를 구현하고, HTTP 요청의 `URLRequest`에 헤더를 추가합니다.

```swift
import Alamofire
import AlamofireObjectMapper

class AuthInterceptor: RequestInterceptor {
    private let token: String

    init(token: String) {
        self.token = token
    }

    func adapt(_ urlRequest: URLRequest, for session: Session, completion: @escaping (Result<URLRequest, Error>) -> Void) {
        var modifiedRequest = urlRequest
        modifiedRequest.addValue(token, forHTTPHeaderField: "Authorization")
        completion(.success(modifiedRequest))
    }
}
```

이제, 네트워크 요청을 보낼 때, 해당 인터셉터를 사용하여 헤더를 수정할 수 있습니다.

```swift
let token = "your_auth_token"
let interceptor = AuthInterceptor(token: token)

AF.request("https://api.example.com/data")
    .responseObject { (response: DataResponse<DataModel, AFError>) in
        // 응답 처리
    }
    .intercept(using: interceptor) // 인터셉터 적용
```

위의 예시에서는 `AF.request`를 통해 네트워크 요청을 보내고 있습니다. `intercept(using:)` 함수를 사용하여 `AuthInterceptor`를 적용시켰습니다. 이렇게 하면 요청에 `Authorization` 헤더가 자동으로 추가됩니다.

위의 예시는 AlamofireObjectMapper를 사용하여 JSON 응답을 매핑하도록 설정해두었기 때문에, `responseObject` 함수를 사용하여 JSON 응답을 매핑할 수 있습니다. 요청에 대한 응답은 `DataResponse` 형태로 받을 수 있으며, 오류 처리 등을 추가로 구현할 수 있습니다.

이렇게 AlamofireObjectMapper를 사용하여 네트워크 요청의 HTTP 헤더를 수정할 수 있습니다.

## 마무리

이번에는 AlamofireObjectMapper를 사용하여 네트워크 요청의 HTTP 헤더를 수정하는 방법에 대해 알아보았습니다. AlamofireObjectMapper는 Alamofire와 ObjectMapper를 결합하여 JSON 응답을 쉽게 매핑할 수 있도록 도와주는 편리한 라이브러리입니다. HTTP 헤더를 수정하여 토큰 기반 인증 등의 기능을 구현할 때 유용하게 사용할 수 있습니다.