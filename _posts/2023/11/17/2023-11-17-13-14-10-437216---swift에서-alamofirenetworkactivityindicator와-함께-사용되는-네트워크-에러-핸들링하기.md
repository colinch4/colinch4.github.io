---
layout: post
title: "[swift] - Swift에서 AlamofireNetworkActivityIndicator와 함께 사용되는 네트워크 에러 핸들링하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 AlamofireNetworkActivityIndicator는 Alamofire와 함께 사용되는 유용한 라이브러리입니다. 이 라이브러리를 사용하면 네트워크 요청이 실행 중일 때 상태 표시줄에서 네트워크 활동을 감지하여 표시할 수 있습니다. 이러한 기능을 사용하는 동안 발생할 수 있는 네트워크 에러를 적절하게 처리하는 방법에 대해 알아보겠습니다.

## 1. Alamofire와 AlamofireNetworkActivityIndicator 설치하기

우선 Swift 프로젝트에 Alamofire와 AlamofireNetworkActivityIndicator를 설치해야 합니다. Cocoapods를 사용하여 간단하게 설치할 수 있습니다. Podfile에 다음 라인을 추가하세요:

```ruby
pod 'Alamofire'
pod 'AlamofireNetworkActivityIndicator'
```

그런 다음 터미널에서 `pod install`을 실행하여 라이브러리를 설치하세요.

## 2. AlamofireNetworkActivityIndicator의 기능 활성화하기

다음으로, AlamofireNetworkActivityIndicator를 활성화해야 합니다. AppDelegate.swift 파일에서 다음과 같이 코드를 추가하세요:

```swift
import AlamofireNetworkActivityIndicator

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    NetworkActivityIndicatorManager.shared.isEnabled = true
    return true
}
```

이렇게 하면 네트워크 활동이 감지되어 상태 표시줄에 표시될 것입니다.

## 3. 네트워크 에러 핸들링하기

이제 네트워크 오류를 처리하는 방법을 알아보겠습니다. Alamofire는 네트워크 요청 시 발생하는 다양한 오류를 처리하는 방법을 제공합니다. 예를 들어 404 오류(Not Found)가 발생했을 때 다음과 같은 코드를 사용할 수 있습니다:

```swift
AF.request(url).responseData { response in
    switch response.result {
    case .success(let data):
        // Handle success case
        // 성공적으로 데이터를 받아왔을 때 처리하는 로직
    case .failure(let error):
        if let statusCode = response.response?.statusCode {
            switch statusCode {
            case 404:
                // Handle 404 error
                // 404 에러에 대한 처리 로직
            default:
                // Handle other errors
                // 그 외 에러에 대한 처리 로직
            }
        } else {
            // Handle unknown errors
            // 알 수 없는 에러에 대한 처리 로직
        }
    }
}
```

위의 코드에서는 네트워크 요청의 성공 또는 실패 상태를 처리합니다. 실패한 경우, 상태 코드를 확인하여 각각의 오류에 맞는 처리를 수행합니다. 

## 4. 네트워크 에러 핸들링 시 추가적인 작업

네트워크 에러를 처리하는 동안 추가적인 작업을 수행해야 할 수도 있습니다. 예를 들어 오류 메시지를 사용자에게 알림으로 표시하는 것이 있습니다. UIAlertController를 사용하여 오류 메시지를 표시할 수 있습니다.

```swift
func showErrorAlert(message: String) {
    let alertController = UIAlertController(title: "Error", message: message, preferredStyle: .alert)
    let okAction = UIAlertAction(title: "OK", style: .default, handler: nil)
    alertController.addAction(okAction)

    self.present(alertController, animated: true, completion: nil)
}
```

위의 코드에서는 showErrorAlert 메서드를 정의하여 오류 메시지를 UIAlertController를 사용하여 표시하고 있습니다. 이를 사용하면 네트워크 에러가 발생했을 때 간단하게 사용자에게 알림을 표시할 수 있습니다.

## 마무리

Swift에서 Alamofire와 AlamofireNetworkActivityIndicator를 함께 사용하는 경우, 네트워크 에러를 적절하게 처리하여 사용자에게 알림을 표시할 수 있습니다. Alamofire의 오류 처리 기능을 활용하고 추가적인 작업을 수행하여 원활한 사용자 경험을 제공할 수 있습니다.

참고문헌:
- [Alamofire GitHub Repository](https://github.com/Alamofire/Alamofire)
- [AlamofireNetworkActivityIndicator GitHub Repository](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)