---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator를 활용하여 네트워크 요청 중에만 특정 View에 Indicator 표시하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

이번에는 Alamofire 라이브러리의 `AlamofireNetworkActivityIndicator`를 사용하여 네트워크 요청 중에만 특정 View에 Indicator를 표시해보려고 합니다. 

### AlamofireNetworkActivityIndicator란?

`AlamofireNetworkActivityIndicator`는 Alamofire 라이브러리와 함께 사용되는 네트워크 활동 지시기입니다. 이를 사용하면 네트워크 요청이 진행 중일 때 앱 화면에 Indicator를 표시할 수 있습니다.

### 네트워크 요청 중에 Indicator를 표시하는 방법

1. 먼저, Alamofire와 AlamofireNetworkActivityIndicator를 프로젝트에 추가합니다. Cocoapods를 사용한다면 Podfile에 다음과 같이 추가합니다.

```ruby
pod 'Alamofire'
pod 'AlamofireNetworkActivityIndicator'
```

2. 프로젝트에서 사용할 Indicator View를 준비합니다. 예를 들어, `indicatorView`라는 이름의 UIActivityIndicatorView로 설정된 Indicator View를 사용하겠습니다.

```swift
let indicatorView = UIActivityIndicatorView(style: .gray)
```

3. `AlamofireNetworkActivityIndicator`를 사용하기 위해 AppDelegate.swift 파일에 다음 코드를 추가합니다.

```swift
import AlamofireNetworkActivityIndicator

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    NetworkActivityIndicatorManager.shared.isEnabled = true
    NetworkActivityIndicatorManager.shared.startDelay = 0.2
    NetworkActivityIndicatorManager.shared.completionDelay = 0.2
    
    return true
}
```

4. 네트워크 요청 중 Indicator를 표시할 부분에서 다음과 같이 코드를 작성합니다.

```swift
import Alamofire

func makeNetworkRequest() {
    indicatorView.startAnimating()
    
    AF.request("https://api.example.com/data").responseJSON { response in
        self.indicatorView.stopAnimating()
        
        switch response.result {
        case .success(let value):
            // 성공적으로 응답 받았을 때 처리할 작업
            print(value)
        case .failure(let error):
            // 요청 실패 시 처리할 작업
            print(error)
        }
    }
}
```

위의 코드에서 `makeNetworkRequest()` 함수가 호출되면 Indicator View가 시작되고, 네트워크 요청이 완료되면 Indicator View가 정지됩니다. 

위의 예제는 Indicator View가 단순히 시작과 정지만을 표시하고 있지만, 필요에 따라 추가적인 작업을 수행할 수도 있습니다. 

AlamofireNetworkActivityIndicator를 사용하면 네트워크 요청 중에 사용자에게 진행 상황을 시각적으로 알려주는 데 도움이 됩니다.

### 참고 자료

- Alamofire: [https://github.com/Alamofire/Alamofire](https://github.com/Alamofire/Alamofire)
- AlamofireNetworkActivityIndicator: [https://github.com/Alamofire/AlamofireNetworkActivityIndicator](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)