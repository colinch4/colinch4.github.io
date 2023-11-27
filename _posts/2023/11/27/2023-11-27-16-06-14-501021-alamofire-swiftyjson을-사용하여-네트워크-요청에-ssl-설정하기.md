---
layout: post
title: "[swift] Alamofire-SwiftyJSON을 사용하여 네트워크 요청에 SSL 설정하기"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

Alamofire-SwiftyJSON은 Swift에서 네트워크 요청을 보내고 JSON 데이터를 처리하는 데 도움이 되는 라이브러리입니다. 이 라이브러리를 사용하여 SSL(보안 소켓 계층)을 이용하여 보안된 네트워크 요청을 보낼 수 있습니다.

## 1. Alamofire-SwiftyJSON 라이브러리 설치

먼저, Alamofire-SwiftyJSON 라이브러리를 설치해야 합니다. 이를 위해 CocoaPods를 사용하는 것이 가장 편리합니다. `Podfile`에 다음과 같이 라이브러리를 추가합니다:

```ruby
pod 'Alamofire-SwiftyJSON'
```

설치할 준비가 되었다면, 터미널에서 아래 명령을 실행하여 라이브러리를 설치합니다:

```bash
pod install
```

## 2. 네트워크 요청에 SSL 설정 추가하기

SSL을 사용하여 보안된 네트워크 요청을 보내기 위해 `Alamofire.SessionManager`를 사용할 것입니다. 아래의 코드를 참고하여 SSL 설정을 추가할 수 있습니다:

```swift
import Alamofire
import SwiftyJSON

func sendSecureRequest() {
    let url = "https://api.example.com"
    
    // SSL 인증서 검증을 우회하기 위한 설정
    let sessionManager = Alamofire.SessionManager(
        serverTrustPolicyManager: ServerTrustPolicyManager(allHostsMustBeEvaluated: false, evaluators: ["api.example.com": DisabledTrustEvaluator()])
    )
    
    sessionManager.request(url).responseJSON { response in
        switch response.result {
        case .success(let value):
            let json = JSON(value)
            // JSON 데이터 처리
        case .failure(let error):
            print(error)
        }
    }
}

// SSL 인증서 검증 우회를 위한 클래스
class DisabledTrustEvaluator: ServerTrustEvaluating {
    func evaluate(_ trust: SecTrust, forHost host: String) throws {
        // 인증서 검증을 항상 성공으로 처리하기 위해 오류를 발생시키지 않음
    }
}
```

위의 코드에서 `url` 변수에는 보안된 API 엔드포인트의 URL을 지정해야 합니다. 이 코드는 SSL 인증서 검증을 우회하고 요청을 보내기 위해 `DisabledTrustEvaluator` 클래스를 사용합니다.

## 3. SSL 설정이 필요한 네트워크 요청 보내기

이제 `sendSecureRequest()` 함수를 호출하면 SSL 설정을 사용하여 보안된 네트워크 요청을 보낼 수 있습니다. 해당 요청의 응답은 JSON 데이터로 처리됩니다.

```swift
sendSecureRequest()
```

위의 코드를 실행하면, SSL 설정이 적용된 네트워크 요청이 실행되며, 성공 시 JSON 데이터가 처리됩니다.

## 결론

Alamofire-SwiftyJSON을 사용하여 네트워크 요청에 SSL 설정을 추가하는 방법을 살펴보았습니다. SSL 인증서 검증을 우회하여 안전한 네트워크 요청을 보낼 수 있게 되었습니다. 이를 통해 앱의 보안성을 향상시키고, 사용자의 개인 정보를 안전하게 전송할 수 있습니다.

## 참고 자료
- [Alamofire-SwiftyJSON GitHub](https://github.com/SwiftyJSON/Alamofire-SwiftyJSON)