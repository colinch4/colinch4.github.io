---
layout: post
title: "[swift] AlamofireObjectMapper를 이용해 네트워크 요청 동기 처리하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 Alamofire와 ObjectMapper를 사용하여 네트워크 요청을 동기적으로 처리하는 방법에 대해 알아보겠습니다.

## Alamofire와 ObjectMapper 설치

먼저, Alamofire와 ObjectMapper를 프로젝트에 추가해야 합니다. 

### Cocoapods를 사용하는 경우

Podfile에 다음과 같이 작성합니다.

```ruby
pod 'Alamofire'
pod 'AlamofireObjectMapper'
pod 'ObjectMapper'
```

그리고 터미널에서 다음 명령어를 실행하여 라이브러리를 설치합니다.

```bash
pod install
```

### Swift Package Manager를 사용하는 경우

Xcode에서 `File > Swift Packages > Add Package Dependency`를 선택하고, 다음 URL을 입력합니다.

```
https://github.com/Alamofire/Alamofire.git
https://github.com/tristanhimmelman/ObjectMapper.git
https://github.com/tristanhimmelman/AlamofireObjectMapper.git
```

## 네트워크 요청 동기 처리하기

Alamofire와 ObjectMapper를 사용하여 네트워크 요청을 동기적으로 처리하는 방법은 다음과 같습니다.

```swift
import Alamofire
import AlamofireObjectMapper

func fetchDataFromAPI() {
    let url = "https://api.example.com/data"

    // Alamofire를 사용하여 GET 요청을 보냅니다.
    Alamofire.request(url, method: .get).responseJSON { response in

        if let statusCode = response.response?.statusCode {
            switch statusCode {
            case 200: // 성공
                if let result = response.result.value {
                    // ObjectMapper를 사용하여 데이터를 객체로 매핑합니다.
                    if let data = Mapper<MyData>().map(JSONObject: result) {
                        // 데이터 처리 로직을 작성합니다.
                        print(data)
                    }
                }
            default: // 실패
                print("네트워크 요청 실패")
            }
        }
    }

    // 동기적으로 요청을 처리하기 위해 대기합니다.
    RunLoop.main.run(until: Date(timeIntervalSinceNow: 2))
}

// 사용자정의 데이터 모델
class MyData: Mappable {
    var name: String?
    var age: Int?

    required init?(map: Map) { }

    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
    }
}

fetchDataFromAPI()
```

위 코드에서는 `fetchDataFromAPI` 함수를 호출하여 네트워크 요청을 보내고, 응답을 동기적으로 처리합니다. `Alamofire`를 사용하여 GET 요청을 보내고, `AlamofireObjectMapper`를 사용하여 응답된 JSON 데이터를 `MyData` 클래스로 매핑합니다. 응답이 성공적인 경우, 매핑된 데이터를 처리하는 로직을 작성할 수 있습니다.

위 코드는 동기적으로 요청을 처리하기 위해 `RunLoop.main.run(until: Date(timeIntervalSinceNow: 2))`를 사용하였습니다. 이 부분은 `RunLoop`을 통해 2초 동안 대기하고, 그 후에 프로그램이 종료됩니다.

이제 AlamofireObjectMapper를 사용하여 네트워크 요청을 동기적으로 처리하는 방법에 대해 알게 되었습니다. 이를 응용하여 데이터를 받아오고 처리하는 등의 작업을 수행할 수 있습니다.

## 참고 자료

- [Alamofire GitHub Repository](https://github.com/Alamofire/Alamofire)
- [ObjectMapper GitHub Repository](https://github.com/tristanhimmelman/ObjectMapper)
- [AlamofireObjectMapper GitHub Repository](https://github.com/tristanhimmelman/AlamofireObjectMapper)