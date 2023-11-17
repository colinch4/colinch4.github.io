---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 인증 세션 처리하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift 프로그래밍 언어에서 AlamofireObjectMapper 라이브러리를 사용하여 네트워크 요청의 인증 세션을 처리하는 방법을 알아보겠습니다. 

## 필요한 라이브러리 설치하기

우선 AlamofireObjectMapper 라이브러리를 사용하기 위해 CocoaPods를 통해 설치해야 합니다. `Podfile` 파일을 열고 다음과 같이 라이브러리를 추가합니다:

```ruby
pod 'AlamofireObjectMapper'
```

그런 다음 터미널에서 아래 명령어를 실행하여 라이브러리를 설치합니다:

```
$ pod install
```

## 세션 생성과 관련된 모델 클래스 만들기

네트워크 요청의 인증 세션 처리를 위해서는 세션 생성과 관련된 정보를 담는 모델 클래스를 만들어야 합니다. 예를 들어, 다음과 같은 `Session` 모델 클래스를 만들 수 있습니다:

```swift
import Foundation

class Session: Mappable {
    var token: String?
    var expirationDate: Date?
    
    required init?(map: Map) {}
    
    func mapping(map: Map) {
        token <- map["token"]
        expirationDate <- (map["expirationDate"], ISO8601DateTransform())
    }
}
```

위의 코드는 AlamofireObjectMapper의 `Mappable` 프로토콜을 준수하는 `Session` 클래스를 정의하고 있습니다. `Session` 클래스에는 토큰과 만료 날짜를 저장하는 속성들이 있으며, `Mappable` 프로토콜의 `mapping` 메서드를 사용하여 JSON 데이터를 모델 객체로 매핑합니다.

## 세션 요청 보내기

이제 세션 생성과 관련된 모델 클래스를 만들었으니, 이를 사용하여 실제로 세션 요청을 보냅니다. 예를 들어, 다음과 같이 로그인 API를 호출하여 인증 세션을 받아올 수 있습니다:

```swift
import Alamofire
import AlamofireObjectMapper

func login(email: String, password: String, completion: @escaping (Session?, Error?) -> Void) {
    let parameters: Parameters = [
        "email": email,
        "password": password
    ]
    
    Alamofire.request("https://api.example.com/login", method: .post, parameters: parameters)
        .responseObject { (response: DataResponse<Session>) in
            switch response.result {
            case .success(let session):
                completion(session, nil)
            case .failure(let error):
                completion(nil, error)
            }
        }
}
```

위의 코드는 `login` 함수를 정의하고 있으며, `email`과 `password`를 매개변수로 받아와서 `Alamofire`를 사용하여 로그인 API를 호출합니다. 세션 요청에 대한 응답은 `DataResponse<Session>` 타입으로 받아오며, `responseObject` 메서드를 통해 JSON 응답을 `Session` 모델 객체로 매핑합니다.

## 요청 결과 처리하기

세션 요청을 보낸 뒤, 응답을 받아와서 처리해야 합니다. 예를 들어, 다음과 같이 `login` 함수를 호출하여 세션을 받아올 수 있습니다:

```swift
login(email: "test@example.com", password: "password") { (session, error) in
    if let session = session {
        // 세션 정보 사용하기
        print("토큰: \(session.token ?? "")")
        print("만료 날짜: \(session.expirationDate ?? Date())")
    } else if let error = error {
        // 에러 처리하기
        print("에러: \(error.localizedDescription)")
    }
}
```

위의 코드는 `login` 함수를 호출하여 세션을 얻은 뒤, 세션 객체의 속성들을 사용하거나, 에러를 처리합니다.

이제 AlamofireObjectMapper 라이브러리를 사용하여 네트워크 요청의 인증 세션을 처리하기 위한 기본적인 코드의 작성 방법을 배웠습니다. 이를 응용하여 실제 프로젝트에서 필요한 기능을 구현할 수 있습니다.

더 많은 정보를 알고 싶다면 다음의 참고자료를 확인하시기 바랍니다:

- AlamofireObjectMapper GitHub 페이지: [https://github.com/tristanhimmelman/AlamofireObjectMapper](https://github.com/tristanhimmelman/AlamofireObjectMapper)
- Alamofire 공식 문서: [https://github.com/Alamofire/Alamofire](https://github.com/Alamofire/Alamofire)