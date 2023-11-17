---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 SSL 인증 처리하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 Alamofire를 사용하여 네트워크 요청을 보낼 때, 종종 SSL 인증 처리를 해주어야 합니다. AlamofireObjectMapper는 Alamofire와 ObjectMapper를 결합하여 JSON 데이터를 매핑하는 라이브러리입니다. 이번에는 AlamofireObjectMapper를 사용하여 SSL 인증 처리를 하는 방법에 대해 알아보겠습니다.

## 1. Alamofire 및 AlamofireObjectMapper 설치

먼저, 프로젝트에 Alamofire와 AlamofireObjectMapper를 설치해야 합니다. Cocoapods를 사용한다면, Podfile에 다음과 같이 추가합니다.

```
pod 'Alamofire'
pod 'AlamofireObjectMapper'
```

그리고 Terminal을 열어서 다음 명령어를 실행합니다.

```
$ pod install
```

## 2. SSL 인증 처리하기

SSL 인증 처리를 위해 `SecurityManager`라는 클래스를 생성합니다.

```swift
import Alamofire

class SecurityManager: ServerTrustManager {
    override func serverTrustEvaluator(forHost host: String) throws -> ServerTrustEvaluating? {
        // SSL 인증서 검증 로직 구현
        
        let certificates = Bundle.main.paths(forResourcesOfType: "cer", inDirectory: nil)
        let trustPolicies = certificates.reduce(into: [String: ServerTrustEvaluating]()) { acc, certificatePath in
            let serverTrustPolicy = try? ServerTrustPolicyCertificates(certificates: [.init(data: try! Data(contentsOf: URL(fileURLWithPath: certificatePath)))], validateCertificateChain: true, isRevocationEnabled: true, isRevocationCheckEnabled: true)
            acc[certificatePath] = serverTrustPolicy
        }
        
        return CompositeTrustEvaluator(evaluators: trustPolicies)
    }
}

```

위 코드에서 `serverTrustEvaluator(forHost:)` 메서드를 재정의하여 서버의 SSL 인증서를 검증하는 로직을 구현합니다. 본인의 프로젝트에서 사용하는 인증서 파일의 경로를 `certificates`에 추가해주어야 합니다.

## 3. 네트워크 요청 보내기

이제 SSL 인증 처리가 완료되었으므로, AlamofireObjectMapper를 사용하여 네트워크 요청을 보낼 수 있습니다.

```swift
import Alamofire
import AlamofireObjectMapper

func sendRequest() {
    let requestUrl = "https://example.com/api"
    
    Alamofire
        .request(requestUrl)
        .responseObject { (response: DataResponse<MyModel>) in
            // JSON 데이터를 MyModel 객체로 매핑하여 사용
            
            if let result = response.result.value {
                // 성공적으로 매핑된 데이터 사용
                print(result)
            }
        }
}
```

`responseObject` 메서드를 사용하여 요청 후에 JSON 데이터를 매핑할 객체 타입을 지정해줍니다. 이렇게 하면 네트워크 요청의 응답 데이터를 매핑한 객체로 사용할 수 있습니다.

## 결론

이제 AlamofireObjectMapper를 사용하여 SSL 인증 처리를 할 수 있게 되었습니다. 보안 상의 이슈나 서버와의 통신에 필요한 SSL 인증 처리를 간편하게 할 수 있는 이 라이브러리를 활용해보세요.