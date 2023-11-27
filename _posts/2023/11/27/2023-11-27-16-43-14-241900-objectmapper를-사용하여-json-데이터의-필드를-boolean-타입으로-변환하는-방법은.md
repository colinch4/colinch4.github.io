---
layout: post
title: "[swift] ObjectMapper를 사용하여 JSON 데이터의 필드를 boolean 타입으로 변환하는 방법은?"
description: " "
date: 2023-11-27
tags: [swift]
comments: true
share: true
---

1. ObjectMapper 설치: ObjectMapper는 Swift JSON 매핑 라이브러리입니다. Cocoapods를 사용하여 프로젝트에 ObjectMapper를 설치합니다.

```
pod 'ObjectMapper'
```

2. 모델 클래스 생성: ObjectMapper를 사용하여 JSON 데이터를 매핑할 모델 클래스를 생성합니다. 예를 들어, 다음과 같이 User 모델 클래스를 생성합니다.

```swift
import Foundation
import ObjectMapper

class User: Mappable {
    var name: String?
    var age: Int?
    var isActive: Bool?

    required init?(map: Map) {}

    func mapping(map: Map) {
        name <- map["name"]
        age <- map["age"]
        isActive <- (map["isActive"], BooleanTransform())
    }
}
```

3. BooleanTransform 사용: ObjectMapper에서 기본적으로 boolean 타입을 지원하지 않기 때문에 BooleanTransform을 사용하여 JSON 데이터의 필드를 boolean으로 변환합니다. BooleanTransform은 ObjectMapper에서 제공하는 변환 클래스입니다.

```swift
import ObjectMapper

class BooleanTransform: TransformType {
    typealias Object = Bool
    typealias JSON = Any

    func transformFromJSON(_ value: Any?) -> Bool? {
        if let boolValue = value as? Bool {
            return boolValue
        }
        if let intValue = value as? Int {
            return intValue != 0
        }
        if let strValue = value as? String {
            return strValue.lowercased() == "true"
        }
        return nil
    }

    func transformToJSON(_ value: Bool?) -> Any? {
        return value
    }
}
```

4. JSON 데이터 매핑: Alamofire 또는 URLSession 등의 네트워크 라이브러리를 사용하여 JSON 데이터를 가져와서 ObjectMapper를 사용하여 매핑합니다.

```swift
import Alamofire
import ObjectMapper

func getUser(completion: @escaping (User?) -> Void) {
    Alamofire.request("https://api.example.com/user").responseJSON { response in
        if let json = response.result.value as? [String: Any] {
            let user = Mapper<User>().map(JSON: json)
            completion(user)
        } else {
            completion(nil)
        }
    }
}
```

위의 예제에서 `isActive` 필드는 JSON 데이터의 필드를 boolean 타입으로 변환하는 방법을 보여줍니다. `isActive` 필드는 JSON의 `isActive` 키와 매핑되며, BooleanTransform을 사용하여 boolean으로 변환됩니다.