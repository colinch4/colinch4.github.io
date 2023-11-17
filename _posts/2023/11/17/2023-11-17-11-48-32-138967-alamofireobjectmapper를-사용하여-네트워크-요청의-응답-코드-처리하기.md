---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 응답 코드 처리하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번 글에서는 Alamofire와 ObjectMapper를 함께 사용하여 네트워크 요청의 응답 코드 처리하는 방법에 대해 알아보겠습니다. 

## 1. AlamofireObjectMapper 라이브러리 설치하기

먼저, AlamofireObjectMapper를 사용하기 위해 라이브러리를 설치해야 합니다. CocoaPods를 사용한다면 Podfile에 다음과 같이 추가합니다.

```ruby
pod 'AlamofireObjectMapper'
```

설치를 완료한 후, `import AlamofireObjectMapper`를 통해 라이브러리를 가져옵니다.

## 2. 네트워크 요청 및 응답 코드 처리하기

AlamofireObjectMapper를 사용하면, JSON 데이터를 모델 객체로 매핑할 수 있습니다. 아래 예제는 Alamofire를 사용하여 GET 요청을 보내고, 응답 코드를 처리하는 예제입니다.

```swift
import Alamofire
import AlamofireObjectMapper

func requestAPI() {
    let url = "https://api.example.com/data"
    
    Alamofire.request(url).responseObject { (response: DataResponse<MyModel>) in
        switch response.result {
        case .success(let value):
            // 응답이 성공일 경우 처리 로직 작성
            // value에는 요청 결과를 매핑한 MyModel 객체가 들어있습니다.
            print(value)
            
        case .failure(let error):
            // 응답이 실패일 경우 처리 로직 작성
            print(error.localizedDescription)
        }
    }
}
```

위 예제에서 `MyModel`은 매핑할 데이터 모델의 타입입니다. 요청이 성공하면 `response.result`에 매핑된 객체가 반환되고, 실패하면 `response.error`에 에러 정보가 들어있습니다.

### 3. 응답 코드 처리하기

AlamofireObjectMapper를 사용하면 응답 코드를 쉽게 처리할 수 있습니다. 아래 예제는 응답 코드가 성공인지 확인하는 예제입니다.

```swift
func requestAPI() {
    // 이전 코드 생략
    Alamofire.request(url).responseJSON { response in
        switch response.response?.statusCode {
        case 200:
            // 응답 코드가 성공일 경우 처리 로직 작성
            print("Success")
            
        default:
            // 응답 코드가 실패일 경우 처리 로직 작성
            print("Failure")
        }
    }
}
```

위 예제에서는 `response.response?.statusCode`를 확인하여 응답 코드를 처리하고 있습니다. 성공적인 요청의 경우 200을 반환하므로, 해당 코드를 기준으로 성공 여부를 판단할 수 있습니다.

## 마무리

이제 Alamofire와 ObjectMapper를 사용하여 네트워크 요청의 응답 코드를 처리하는 방법에 대해 알아보았습니다. AlamofireObjectMapper를 사용하면 JSON 데이터를 손쉽게 모델 객체로 변환할 수 있습니다. 응답 코드 처리를 위해 `response.response?.statusCode`를 사용하는 것도 유용한 방법입니다. 다양한 상황에 맞게 응답 코드 처리 로직을 구현하여 안정적인 네트워크 통신을 구현해보세요.