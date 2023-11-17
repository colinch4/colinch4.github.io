---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator를 활용하여 네트워크 에러를 사용자에게 알리는 기능 추가하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

## 개요
네트워크 요청 중 발생하는 에러를 사용자에게 알려주는 기능은 앱의 사용성을 향상시키는 중요한 부분입니다. Alamofire는 Swift에서 네트워크 요청을 간편하게 처리할 수 있는 편리한 라이브러리입니다. 이번에는 AlamofireNetworkActivityIndicator를 사용하여 네트워크 에러 시 사용자에게 알리는 기능을 추가하는 방법에 대해 알아보겠습니다.

## AlamofireNetworkActivityIndicator란?
AlamofireNetworkActivityIndicator는 Alamofire의 서브 프로젝트로, 네트워크 요청이 활성화되어 있을 때 iOS의 네트워크 활동 인디케이터를 자동으로 표시하도록 지원합니다. 이는 사용자에게 네트워크 요청이 진행 중임을 알려주는 시각적인 피드백을 제공하여 UX를 향상시킵니다.

## 구현 방법

### 1. Alamofire 및 AlamofireNetworkActivityIndicator 설치하기
먼저, Alamofire를 프로젝트에 추가해야 합니다. Podfile에 다음과 같이 Alamofire를 추가합니다.

```ruby
pod 'Alamofire'
```

Alamofire를 설치한 뒤에는 AlamofireNetworkActivityIndicator도 설치해야 합니다. Podfile에 다음과 같이 AlamofireNetworkActivityIndicator를 추가합니다.

```ruby
pod 'AlamofireNetworkActivityIndicator'
```

위의 변경사항을 Podfile에 적용한 후에 터미널에서 `pod install` 명령어를 실행합니다.

### 2. AppDelegate에 코드 추가하기
AppDelegate.swift 파일을 열고 다음 코드를 추가합니다.

```swift
import AlamofireNetworkActivityIndicator

// ...

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    NetworkActivityIndicatorManager.shared.isEnabled = true
    return true
}

```

위 코드는 앱의 네트워크 활동 인디케이터를 활성화하는 코드입니다.

### 3. 네트워크 요청 시 에러 핸들링 추가하기
네트워크 에러가 발생할 수 있는 위치에서 Alamofire의 request 호출 후에 다음과 같이 에러 핸들링을 추가합니다.

```swift
AF.request(url).responseJSON { response in
    switch response.result {
    case .success:
        // 성공적인 응답 처리
        
    case .failure(let error):
        // 네트워크 에러 처리
        // UIAlertController 등을 활용하여 사용자에게 에러 메시지 표시
    }
}
```

위 코드에서 `.failure` 케이스에 도달했을 때, 네트워크 에러가 발생한 것이므로 적절한 방법으로 사용자에게 에러 메시지를 표시할 수 있도록 합니다.

## 마무리
AlamofireNetworkActivityIndicator를 활용하여 네트워크 에러를 사용자에게 알리는 기능을 추가하는 방법에 대해 알아보았습니다. 이를 통해 사용자에게 적절한 피드백을 제공하여 앱의 사용성을 높일 수 있습니다. Alamofire를 사용하는 다른 기능과 함께 활용하여 효율적인 네트워크 요청 처리를 구현할 수 있습니다.