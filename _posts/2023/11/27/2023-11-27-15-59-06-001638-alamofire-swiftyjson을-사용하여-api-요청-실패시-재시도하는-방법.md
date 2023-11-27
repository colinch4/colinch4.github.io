---
layout: post
title: "[swift] Alamofire-SwiftyJSON을 사용하여 API 요청 실패시 재시도하는 방법"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

## 서론
API 서버에서 데이터를 요청하고 응답을 받는 작업은 앱 개발에서 중요한 부분입니다. 그러나 때로는 API 요청이 실패할 수도 있습니다. 이러한 상황에서 우리는 재시도 로직을 구현하여 안정적인 앱 퍼포먼스를 유지할 수 있습니다. 이번 글에서는 Swift에서 Alamofire와 SwiftyJSON을 사용하여 API 요청이 실패할 경우에 재시도하는 방법에 대해 알아보겠습니다.

## 필요한 라이브러리 설치
먼저 해당 작업을 수행하기 위해 Alamofire와 SwiftyJSON 라이브러리를 설치해야 합니다. 이를 위해 `Podfile`에 다음과 같이 추가합니다.

```ruby
pod 'Alamofire'
pod 'SwiftyJSON'
```

그런 다음 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 설치합니다.

## Alamofire와 SwiftyJSON을 사용하여 API 요청하기
API 요청을 보내기 위해 우리는 Alamofire를 사용할 것입니다. 그리고 받아온 응답을 처리하기 위해 SwiftyJSON을 사용할 것입니다. 먼저 Alamofire와 SwiftyJSON을 import 해야합니다.

```swift
import Alamofire
import SwiftyJSON
```

다음 예시 코드에서는 `getDataFromAPI`라는 함수를 사용하여 API 요청을 보내고 응답을 처리하는 방법을 보여줍니다.

```swift
func getDataFromAPI() {
    let url = "https://api.example.com/data"
    
    Alamofire.request(url, method: .get).responseJSON { response in
        switch response.result {
        case .success(let value):
            let json = JSON(value)
            // API 응답 처리
            
        case .failure(let error):
            // API 요청 실패 처리
            print("API 요청 실패: \(error.localizedDescription)")
        }
    }
}
```

위의 코드에서는 `responseJSON` 메서드를 사용하여 API 요청을 보낸 후 응답을 처리합니다. `responseJSON`은 비동기로 작동하므로 클로저 내부에서 API 응답을 처리해야 합니다.

## API 요청 실패시 재시도
API 요청이 실패한 경우에 재시도를 구현하기 위해 우리는 `retry` 메서드를 사용할 수 있습니다. `retry` 메서드는 요청에 실패한 경우 지정된 횟수만큼 재시도합니다. 예를 들어, 요청 실패시 3회 재시도 한다면 다음과 같이 코드를 작성할 수 있습니다.

```swift
func getDataFromAPIWithRetry() {
    let url = "https://api.example.com/data"
    
    Alamofire.request(url, method: .get).responseJSON { response in
        switch response.result {
        case .success(let value):
            let json = JSON(value)
            // API 응답 처리
            
        case .failure(let error):
            print("API 요청 실패: \(error.localizedDescription)")
            
            // 재시도
            let retryCount = 3
            if response.retryCount < retryCount {
                response.request?.retry()
            } else {
                print("요청 실패 및 재시도 횟수 초과")
            }
        }
    }
}
```

위의 예시에서는 `response.retryCount`로 재시도 횟수를 체크하고, `response.request?.retry()`를 호출하여 요청을 재시도합니다. 최대 재시도 횟수가 초과된 경우에는 해당 에러를 처리할 수 있습니다.

## 결론
이렇게 Swift에서 Alamofire와 SwiftyJSON을 사용하여 API 요청이 실패한 경우에 재시도하는 방법을 알아보았습니다. 앱의 안정성과 사용자 경험 향상을 위해 API 요청 실패 시 재시도 로직을 구현하는 것은 중요한 과제 중 하나입니다. 위의 예시 코드를 참고하여 이를 구현해보세요.