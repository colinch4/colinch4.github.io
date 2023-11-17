---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 진행 상황 표시하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

[Alamofire](https://github.com/Alamofire/Alamofire)는 Swift에서 네트워크 요청을 처리하기 위한 인기있는 라이브러리입니다. [ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)는 JSON 데이터를 객체로 매핑하는 데 사용되는 다른 인기있는 라이브러리입니다. 이들을 함께 사용하여 네트워크 요청의 진행 상황을 표시하는 방법을 알아보겠습니다.

## AlamofireObjectMapper 설치하기
먼저, [CocoaPods](https://cocoapods.org/)를 사용하여 AlamofireObjectMapper를 프로젝트에 추가해야 합니다. Podfile에 다음과 같이 작성합니다:

```
pod 'AlamofireObjectMapper'
```

그런 다음 터미널에서 `pod install` 명령을 실행하여 CocoaPods를 업데이트합니다.

## 네트워크 요청과 진행 상황 표시하기
AlamofireObjectMapper를 사용하여 네트워크 요청의 진행 상황을 표시하려면 `Alamofire`의 `uploadProgress` 또는 `downloadProgress` 클로저를 사용하여 프로그래스 바 또는 텍스트 레이블을 업데이트합니다.

```swift
Alamofire.request(.get, "https://api.example.com/users")
    .downloadProgress { progress in
        // 프로그래스 바 업데이트
        progressView.progress = Float(progress.fractionCompleted)
    }
    .responseArray { (response: DataResponse<[User]>) in
        if let users = response.value {
            // 요청 성공 시 사용자 목록을 처리합니다
            processUsers(users)
        } else if let error = response.error {
            // 요청 실패 시 오류를 처리합니다
            handleError(error)
        }
    }
```

위의 코드에서 `downloadProgress` 클로저를 사용하여 프로그래스 바를 업데이트하고, `responseArray` 클로저를 사용하여 요청이 성공하면 사용자 목록을 처리하고, 실패하면 오류를 처리합니다.

## 진행 상황 표시하기 위한 추가 작업
네트워크 요청의 진행 상황을 표시하려면 애플리케이션의 UI를 업데이트하기 위해 메인 큐에서 작업을 실행해야 합니다. 아래의 예시 코드를 참고하여 진행 상황을 업데이트하는 작업을 메인 큐에서 실행합니다:

```swift
Alamofire.request(.get, "https://api.example.com/users")
    .downloadProgress { progress in
        DispatchQueue.main.async {
            // 프로그래스 바 업데이트
            progressView.progress = Float(progress.fractionCompleted)
        }
    }
    .responseArray { (response: DataResponse<[User]>) in
        DispatchQueue.main.async {
            if let users = response.value {
                // 요청 성공 시 사용자 목록을 처리합니다
                processUsers(users)
            } else if let error = response.error {
                // 요청 실패 시 오류를 처리합니다
                handleError(error)
            }
        }
    }
```

위의 코드에서 `downloadProgress` 및 `responseArray` 클로저 내부의 작업을 `DispatchQueue.main.async`로 감싸서 메인 큐에서 실행하도록 했습니다.

## 결론
Alamofire와 ObjectMapper를 사용하여 네트워크 요청의 진행 상황을 표시하는 것은 간단하고 효과적인 방법입니다. 프로그래스 바, 텍스트 레이블 등을 사용하여 사용자에게 진행 상황을 시각적으로 표시하여 더 나은 사용자 경험을 제공할 수 있습니다.