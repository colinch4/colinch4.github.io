---
layout: post
title: "[swift] - Swift에서 Alamofire 네트워크 요청에 동적인 NetworkActivityIndicator 설정하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 소개

Alamofire는 Swift에서 많이 사용되는 네트워킹 라이브러리 중 하나입니다. Alamofire를 사용하여 네트워크 요청을 보낼 때 앱의 화면 상단 상태 표시줄에 네트워크 활동 표시 기능을 추가하는 것은 사용자에게 유용합니다. 이를 통해 사용자는 앱이 네트워크 요청을 처리 중임을 쉽게 인지할 수 있습니다.

이번 포스트에서는 Swift에서 Alamofire를 사용할 때 동적으로 NetworkActivityIndicator를 설정하는 방법을 알아보겠습니다.

## 요구사항

- Swift 프로젝트
- Alamofire 라이브러리

## 구현

1. 프로젝트에 Alamofire를 설치합니다. 이를 위해 CocoaPods를 사용할 수 있습니다. 프로젝트의 Podfile에 다음을 추가합니다:

    ```ruby
    platform :ios, '10.0'
    pod 'Alamofire', '~> 5.0'
    ```

    그리고 터미널에서 다음 명령어를 실행하여 Alamofire를 설치합니다:

    ```bash
    pod install
    ```

2. 네트워크 작업을 수행할 함수 내에서 `NetworkActivityIndicatorManager`를 가져옵니다:

    ```swift
    import Alamofire
    import Network

    class NetworkManager {
    
        private let networkActivityIndicatorManager = NetworkActivityIndicatorManager.shared
        ...
    }
    ```

3. 네트워크 요청 전에 `NetworkActivityIndicatorManager`의 상태를 설정합니다. 옵셔널로 리퀘스트의 `completionHandler`를 받을 수도 있습니다:

    ```swift
    func makeNetworkRequest(url: URLConvertible, completionHandler: ((Result<Data, Error>) -> Void)? = nil) {
        networkActivityIndicatorManager.isEnabled = true
        
        AF.request(url).responseData { response in
        
            // Handle the response
            
            self.networkActivityIndicatorManager.isEnabled = false
            
            completionHandler?(response.result)
        }
    }
    ```

    위의 예제에서는 네트워크 요청 전에 `networkActivityIndicatorManager`의 `isEnabled`를 `true`로 설정하여 NetworkActivityIndicator를 활성화했습니다. 그리고 네트워크 요청 후에는 `isEnabled`를 `false`로 다시 설정하여 NetworkActivityIndicator를 비활성화했습니다.

## 결론

이제 Swift에서 Alamofire를 사용할 때 동적으로 `NetworkActivityIndicator`를 설정하는 방법을 알게 되었습니다. 이를 통해 사용자에게 앱이 네트워크 작업을 수행 중임을 시각적으로 표시할 수 있습니다. Alamofire와 `NetworkActivityIndicatorManager`를 조합하여 빠르고 안정적인 네트워킹 코드를 작성할 수 있습니다.

더 자세한 내용은 [Alamofire 문서](https://github.com/Alamofire/Alamofire)를 참조하세요.