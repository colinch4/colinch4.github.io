---
layout: post
title: "[swift] Swift PKRevealController와의 서버 통신 및 API 연동"
description: " "
date: 2023-11-16
tags: [swift]
comments: true
share: true
---

## 개요
이번 포스트에서는 Swift PKRevealController와 서버 통신 및 API 연동에 대해 다루겠습니다. PKRevealController는 iOS 앱 개발에서 사이드 메뉴 기능을 제공하는 컨트롤러로, 네비게이션 컨트롤러와 함께 사용됩니다. 

우리의 목표는 PKRevealController를 사용하여 앱에서 서버와 통신하여 데이터를 가져오고 전달하는 것입니다. 이를 위해 RESTful API를 사용하여 HTTP 요청을 보내고 서버로부터 응답을 받아오는 방법을 알아보겠습니다.

## 서버 통신용 클래스 구현
먼저, 서버 통신을 위한 클래스를 구현해야 합니다. 아래는 `APIManager`라는 클래스의 예시입니다.

```swift
import Foundation

class APIManager {
    
    func requestData(completion: @escaping (Result<Data, Error>) -> Void) {
        guard let url = URL(string: "https://www.example.com/api/data") else {
            completion(.failure(NSError(domain: "Invalid URL", code: 0, userInfo: nil)))
            return
        }
        
        let task = URLSession.shared.dataTask(with: url) { (data, response, error) in
            if let error = error {
                completion(.failure(error))
                return
            }
            
            guard let httpResponse = response as? HTTPURLResponse, httpResponse.statusCode == 200 else {
                completion(.failure(NSError(domain: "Invalid response", code: 0, userInfo: nil)))
                return
            }
            
            guard let data = data else {
                completion(.failure(NSError(domain: "Invalid data", code: 0, userInfo: nil)))
                return
            }
            
            completion(.success(data))
        }
        
        task.resume()
    }
    
}
```

위의 코드는 `APIManager` 클래스를 정의하고, `requestData` 메서드를 구현하는 예시입니다. 이 메서드는 서버로부터 데이터를 요청하고, 요청 결과를 클로저를 통해 전달합니다.

## PKRevealController에 서버 통신 연동하기
이제 APIManager 클래스를 사용하여 PKRevealController에 서버 통신을 연동해보겠습니다. 

```swift
import UIKit
import PKRevealController

class MainViewController: PKRevealController {
    
    let apiManager = APIManager()
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        fetchServerData()
    }
    
    func fetchServerData() {
        apiManager.requestData { [weak self] result in
            switch result {
            case .success(let data):
                // 서버로부터 받은 데이터를 처리하는 로직 작성
                print("Received data: \(data)")
            case .failure(let error):
                // 에러 처리 로직 작성
                print("Error: \(error.localizedDescription)")
            }
        }
    }
    
}
```

위의 코드는 `MainViewController` 클래스를 정의하고, `fetchServerData` 메서드를 구현하는 예시입니다. `fetchServerData` 메서드는 `apiManager` 객체의 `requestData` 메서드를 호출하여 서버에서 데이터를 가져오는 코드입니다. 요청 결과에 따라 적절한 처리를 수행할 수 있습니다.

## 결론
이제 PKRevealController와 서버 통신 및 API 연동에 대해 알아보았습니다. PKRevealController를 사용하여 앱에 사이드 메뉴 기능을 추가하고, 서버와 통신하여 데이터를 가져오고 전달할 수 있습니다. 이를 통해 사용자에게 더욱 풍부한 경험을 제공할 수 있습니다.

더 자세한 내용은 아래 참고 자료를 참고하시기 바랍니다.

## 참고 자료
- [PKRevealController GitHub 저장소](https://github.com/pkluz/PKRevealController)
- [URLSession 공식 문서](https://developer.apple.com/documentation/foundation/urlsession)
- [Swift API 요청 및 응답 처리 방법](https://www.example.com/blog/api-request-response)
- [Swift PKRevealController 튜토리얼](https://www.example.com/blog/pkrevealcontroller-tutorial)