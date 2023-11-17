---
layout: post
title: "[swift] - AlamofireNetworkActivityIndicator 오픈 소스 프레임워크 소개하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

![AlamofireNetworkActivityIndicator](https://github.com/Alamofire/AlamofireNetworkActivityIndicator/raw/master/alamofire-network-activity-indicator.gif)

AlamofireNetworkActivityIndicator는 Alamofire와 함께 사용할 수 있는 오픈 소스 프레임워크입니다. 이 프레임워크는 내 앱에서의 Alamofire 네트워크 활동을 자동으로 감지하고 네트워크 활동 표시기를 제공합니다. 

## 왜 사용해야 할까요?
일반적으로 Alamofire를 사용하여 네트워크 요청을 보낼 때는 화면의 상태를 나타내는 표시기를 직접 관리해야 합니다. 네트워크 활동이 있을 때마다 표시기를 켜고 끄는 작업은 많은 코드 작성을 필요로 하며, 코드의 가독성을 저해할 수도 있습니다.

알아서 네트워크 활동을 감지하고 표시기를 제공하는 **AlamofireNetworkActivityIndicator**는 이러한 문제를 해결해줍니다. 앱이 네트워크 활동을 수행할 때 자동으로 표시기를 활성화하고, 모든 요청이 완료되면 자동으로 표시기를 비활성화합니다. 

## 어떻게 사용하나요?

### Step 1: 프레임워크 추가
**AlamofireNetworkActivityIndicator**을 사용하려면 먼저 CocoaPods 또는 Swift Package Manager를 통해 프레임워크를 추가해야 합니다. 

CocoaPods를 사용하는 경우, `Podfile`에 다음과 같이 추가하고 `pod install` 명령을 실행합니다.

```ruby
pod 'AlamofireNetworkActivityIndicator'
```

Swift Package Manager를 사용하는 경우, Xcode의 `File` 탭에서 `Swift Packages`를 선택하고 `Add Package Dependency`를 클릭한 다음, `https://github.com/Alamofire/AlamofireNetworkActivityIndicator.git` 주소를 입력합니다.

### Step 2: 초기화
앱의 시작 지점에 아래 코드를 추가하여 **AlamofireNetworkActivityIndicator**을 초기화합니다.

```swift
import AlamofireNetworkActivityIndicator

...

NetworkActivityIndicatorManager.shared.isEnabled = true
```

### Step 3: Alamofire와 함께 사용
**AlamofireNetworkActivityIndicator**은 Alamofire와 완벽하게 통합됩니다. 더 이상 네트워크 요청을 보낼 때마다 표시기를 수동으로 관리할 필요가 없습니다. **AlamofireNetworkActivityIndicator**가 알아서 네트워크 활동을 감지하고 표시기를 제공합니다.

```swift
AF.request("https://api.example.com/users").response { response in
    debugPrint(response)
}
```

## 결론
**AlamofireNetworkActivityIndicator**은 앱의 네트워크 활동을 관리하기 위한 간단하고 효과적인 오픈 소스 프레임워크입니다. 기존의 수동 관리 방식에서 벗어나고 표시기를 자동으로 활성화하고 비활성화하는 기능을 제공하여 코드 작성의 편의성과 가독성을 향상시켜줍니다. 만약 Alamofire를 사용하는 앱을 개발 중이거나 개발할 예정이라면, **AlamofireNetworkActivityIndicator**을 고려해보세요.

---

참고: [AlamofireNetworkActivityIndicator Github](https://github.com/Alamofire/AlamofireNetworkActivityIndicator)