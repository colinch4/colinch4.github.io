---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 리더블 타임아웃 설정하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

AlamofireObjectMapper는 Swift에서 네트워크 요청을 보내고 응답을 매핑하는 데 도움이 되는 라이브러리입니다. 이 라이브러리를 사용하면 네트워크 요청 및 응답의 처리 과정을 간단하게 관리할 수 있습니다.

이번 글에서는 AlamofireObjectMapper를 사용하여 네트워크 요청의 리더블 타임아웃(timeout)을 설정하는 방법에 대해 알아보겠습니다.

## 1. AlamofireObjectMapper와 Alamofire 설치하기

먼저 프로젝트에 AlamofireObjectMapper와 Alamofire를 설치해야 합니다. 이를 위해서는 CocoaPods를 사용할 수 있습니다. 프로젝트 디렉토리에서 `Podfile`을 생성하고 다음과 같이 작성합니다.

```ruby
platform :ios, '9.0'
use_frameworks!

target 'YourProjectName' do
    pod 'AlamofireObjectMapper', '~> 11.0'
    pod 'Alamofire', '~> 5.4'
end
```

`Podfile`을 저장한 후 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## 2. 리더블 타임아웃 설정하기

네트워크 요청의 리더블 타임아웃은 응답이 도착하는 데 걸리는 최대 시간입니다. 이를 설정하여 네트워크 요청의 응답 속도를 제어할 수 있습니다.

```swift
import Alamofire
import AlamofireObjectMapper

let timeoutInterval: TimeInterval = 10 // 10초로 타임아웃 설정

let session = Session.default
session.sessionConfiguration.timeoutIntervalForRequest = timeoutInterval

AF.request("https://api.example.com/data")
    .responseObject { (response: AFDataResponse<Model>) in
        // 응답 처리 로직
    }
```

위의 코드에서는 Alamofire의 기본 세션을 사용하여 타임아웃을 설정합니다. `timeoutIntervalForRequest` 속성을 사용하여 타임아웃 길이를 설정한 후, `AF.request()`를 사용하여 네트워크 요청을 보냅니다. 

## 3. 요청마다 다른 타임아웃 설정하기

만약 특정 요청마다 다른 타임아웃을 설정하고 싶다면, `URLRequest` 객체를 직접 사용하여 타임아웃을 설정할 수 있습니다.

```swift
import Alamofire
import AlamofireObjectMapper

let timeoutInterval: TimeInterval = 20 // 특정 요청에 대한 타임아웃 설정

let session = Session.default

let urlRequest = try! URLRequest(url: "https://api.example.com/data", method: .get)
urlRequest.timeoutInterval = timeoutInterval

session.request(urlRequest)
    .responseObject { (response: AFDataResponse<Model>) in
        // 응답 처리 로직
    }
```

위의 코드에서는 `URLRequest` 객체를 만들고 `timeoutInterval`을 설정한 후, `session.request()`를 사용하여 네트워크 요청을 보냅니다.

## 결론

AlamofireObjectMapper와 Alamofire를 사용하여 네트워크 요청의 리더블 타임아웃을 설정하는 방법을 알아보았습니다. 이를 통해 네트워크 요청의 응답 속도를 제어하고 원하는 타임아웃을 설정할 수 있습니다. 앱의 네트워크 통신이 원활하게 이루어지도록 적절한 타임아웃 값을 설정하는 것이 중요합니다.

더 자세한 내용은 [AlamofireObjectMapper](https://github.com/tristanhimmelman/AlamofireObjectMapper)와 [Alamofire](https://github.com/Alamofire/Alamofire)의 공식 문서를 참고하시기 바랍니다.