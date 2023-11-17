---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 오프라인 저장소 처리하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번에는 Swift 프로젝트에서 네트워크 요청을 처리하고, 응답 데이터를 오프라인 저장소에 저장하는 방법을 알아보겠습니다. 이를 위해 [Alamofire](https://github.com/Alamofire/Alamofire)와 [ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)라는 두 가지 라이브러리를 사용할 것입니다.

## Alamofire

Alamofire는 Swift로 작성된 HTTP 네트워킹 라이브러리입니다. 이 라이브러리를 사용하면 간편하게 네트워크 요청을 만들고, 응답 데이터를 받을 수 있습니다. 프로젝트에서 Alamofire를 사용하려면 먼저 해당 라이브러리를 설치해야 합니다. 자세한 설치 방법은 [여기](https://github.com/Alamofire/Alamofire#installation)에서 확인할 수 있습니다.

## ObjectMapper

ObjectMapper는 Swift에서 JSON 데이터를 다루기 위한 라이브러리입니다. 이 라이브러리를 사용하면 간편하게 JSON 데이터를 Swift 객체로 매핑할 수 있습니다. ObjectMapper를 설치하려면 [여기](https://github.com/tristanhimmelman/ObjectMapper#getting-started)에서 자세한 설치 방법을 확인할 수 있습니다.

## 네트워크 요청 및 오프라인 저장소 처리

이제 실제로 네트워크 요청을 만들어보고, 응답 데이터를 오프라인 저장소에 저장해보겠습니다. 예를 들어, 특정 API에서 사용자 정보를 가져오는 GET 요청을 보내고, 그 응답 데이터를 오프라인 저장소에 저장하려고 합니다.

```swift
import Alamofire
import ObjectMapper

func getUserInfo(userId: Int, completion: @escaping (User?, Error?) -> Void) {
    let url = "https://api.example.com/user/\(userId)"
    
    Alamofire.request(url).responseJSON { response in
        switch response.result {
        case .success(let value):
            guard let userJSON = value as? [String: Any] else {
                completion(nil, NSError(domain: "ParsingError", code: 0, userInfo: nil))
                return
            }
            
            if let user = Mapper<User>().map(JSON: userJSON) {
                // 응답 데이터를 오프라인 저장소에 저장
                MyOfflineStorage.shared.saveUser(user)
                
                completion(user, nil)
            } else {
                completion(nil, NSError(domain: "MappingError", code: 0, userInfo: nil))
            }
            
        case .failure(let error):
            completion(nil, error)
        }
    }
}
```

위 코드에서는 `getUserInfo`라는 함수를 정의하여 네트워크 요청을 처리하고, 응답 데이터를 오프라인 저장소에 저장합니다. 네트워크 요청은 Alamofire의 `request` 메서드를 사용하여 보냅니다. 응답 데이터는 ObjectMapper를 사용하여 JSON을 User 객체로 매핑합니다. 그리고 매핑된 User 객체를 오프라인 저장소인 `MyOfflineStorage`에 저장합니다.

이제 `getUserInfo` 함수를 호출하여 사용자 정보를 가져올 수 있습니다.

```swift
getUserInfo(userId: 123) { user, error in
    if let user = user {
        // 사용자 정보 가져오기 성공
        print(user.name)
    } else if let error = error {
        // 처리 중 오류 발생
        print(error.localizedDescription)
    }
}
```

위 코드에서는 `getUserInfo` 함수를 호출하여 사용자 정보를 가져옵니다. 성공적으로 사용자 정보를 가져오면, 해당 정보를 사용하여 원하는 작업을 수행할 수 있습니다. 만약 에러가 발생하면, 해당 에러를 처리할 수 있습니다.

이처럼 Alamofire와 ObjectMapper를 사용하여 네트워크 요청의 오프라인 저장소 처리를 간단하게 구현할 수 있습니다. 이러한 방식을 사용하면 네트워크가 연결되지 않은 상황에서도 이전에 가져온 데이터를 사용할 수 있어 사용자 경험을 향상시킬 수 있습니다.

참고 자료:
- [Alamofire GitHub 페이지](https://github.com/Alamofire/Alamofire)
- [ObjectMapper GitHub 페이지](https://github.com/tristanhimmelman/ObjectMapper)