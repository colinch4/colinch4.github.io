---
layout: post
title: "[swift] Swift에서 Alamofire를 사용하여 API 호출 후 Codable 모델로 데이터 변환하기"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

안녕하세요! Swift에서 API 호출 후 받은 데이터를 Codable 모델로 변환하는 방법에 대해 알아보겠습니다. 이를 위해 Alamofire 라이브러리를 사용하여 보다 간편하게 API 요청을 처리할 수 있습니다.

## 1. Alamofire 설치 및 프로젝트에 추가하기

Alamofire를 사용하기 위해서는 먼저 프로젝트에 해당 라이브러리를 추가해야 합니다. Cocoapods를 사용한다면, Podfile에 다음 줄을 추가합니다.

```ruby
pod 'Alamofire'
```

그리고 터미널에서 다음 명령어를 실행하여 Alamofire를 설치합니다.

```bash
pod install
```

Cocoapods를 사용하지 않고 수동으로 설치하고 싶다면, Alamofire Github 페이지에서 직접 소스 코드를 다운로드하여 프로젝트에 추가할 수도 있습니다.

## 2. API 호출 및 데이터 변환

이제 Alamofire를 사용하여 API를 호출하고, 받은 데이터를 Codable 모델로 변환하는 방법을 알아보겠습니다.

먼저, API 요청을 보내는 코드를 작성합니다. 아래는 GET 요청을 보내는 예시입니다.

```swift
import Alamofire

func fetchData() {
    Alamofire.request("https://api.example.com/data").responseJSON { response in
        switch response.result {
        case .success(let value):
            // 데이터 변환 코드 작성하기
        case .failure(let error):
            print("API 요청 실패: \(error)")
        }
    }
}
```

API 요청이 성공하면 `.success` case로 들어오게 되고, `value` 값에는 응답 데이터가 포함됩니다. 이때, 데이터를 Codable 모델로 변환하기 위해 다음과 같이 작성할 수 있습니다.

```swift
struct DataModel: Codable {
    let id: Int
    let name: String
    // 필요한 다른 속성들...
}

func fetchData() {
    Alamofire.request("https://api.example.com/data").responseJSON { response in
        switch response.result {
        case .success(let value):
            do {
                let jsonData = try JSONSerialization.data(withJSONObject: value)
                let decoder = JSONDecoder()
                let dataModel = try decoder.decode(DataModel.self, from: jsonData)
                // 데이터 모델 사용하기
            } catch let error {
                print("데이터 변환 실패: \(error)")
            }
        case .failure(let error):
            print("API 요청 실패: \(error)")
        }
    }
}
```

위의 코드에서 `JSONSerialization`을 사용하여 응답 데이터를 `Data`로 변환하고, 이를 `JSONDecoder`를 사용하여 `DataModel`로 디코딩합니다.

## 3. 데이터 모델 사용하기

API로부터 받아온 데이터를 Codable 모델로 변환했다면, 이제 해당 모델의 속성에 접근하여 데이터를 사용할 수 있습니다.

```swift
struct DataModel: Codable {
    let id: Int
    let name: String
    // 필요한 다른 속성들...
}

func fetchData() {
    Alamofire.request("https://api.example.com/data").responseJSON { response in
        switch response.result {
        case .success(let value):
            do {
                let jsonData = try JSONSerialization.data(withJSONObject: value)
                let decoder = JSONDecoder()
                let dataModel = try decoder.decode(DataModel.self, from: jsonData)

                // 데이터 모델 사용 예시
                print("ID: \(dataModel.id)")
                print("Name: \(dataModel.name)")
            } catch let error {
                print("데이터 변환 실패: \(error)")
            }
        case .failure(let error):
            print("API 요청 실패: \(error)")
        }
    }
}
```

위의 코드에서 `dataModel` 객체를 사용하여 데이터에 접근하고 출력합니다. 당연히 실제 개발에서는 출력 대신 데이터를 다른 용도로 활용하게 될 것입니다.

이제 Swift에서 Alamofire를 사용하여 API 호출 후 Codable 모델로 데이터를 변환하는 방법에 대해 알아보았습니다. 이를 활용하여 API 요청과 응답 데이터 처리를 보다 편리하게 해보세요!