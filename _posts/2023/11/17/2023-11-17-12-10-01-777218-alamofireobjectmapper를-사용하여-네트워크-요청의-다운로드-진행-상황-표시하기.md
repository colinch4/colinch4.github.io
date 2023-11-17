---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 다운로드 진행 상황 표시하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

AlamofireObjectMapper는 Alamofire와 ObjectMapper와 함께 사용하는 매우 유용한 라이브러리입니다. 이 라이브러리를 사용하면 네트워크 요청의 다운로드 진행 상황을 간단하게 표시할 수 있습니다. 이번 예제에서는 Swift 언어를 사용하며, Alamofire와 AlamofireObjectMapper를 활용하여 다운로드 진행 상황을 표시하는 방법을 알아보겠습니다.

## 필수 요구사항

- Swift 5 이상
- Alamofire 라이브러리 설치
- ObjectMapper 라이브러리 설치
- iOS 10 이상

## 설치

우선, 프로젝트에 Alamofire와 ObjectMapper를 설치해야 합니다. 이를 위해서는 프로젝트의 `Podfile`에 아래와 같이 추가합니다.

```ruby
pod 'Alamofire'
pod 'ObjectMapper'
pod 'AlamofireObjectMapper'
```

설치가 완료되면 터미널에서 `pod install` 명령어를 실행하여 라이브러리를 다운로드 및 프로젝트에 적용합니다.

## 코드 예제

1. 우선, Alamofire 및 ObjectMapper와 함께 AlamofireObjectMapper 라이브러리를 import합니다.

```swift
import Alamofire
import AlamofireObjectMapper
```

2. 다운로드 진행 상황을 표시할 프로그레스바를 생성합니다.

```swift
let progressView = UIProgressView(progressViewStyle: .default)
progressView.center = view.center
progressView.setProgress(0.0, animated: false)
view.addSubview(progressView)
```

3. Alamofire와 함께 다운로드 요청을 보내고, AlamofireObjectMapper를 사용하여 응답 데이터를 매핑합니다. 이때, `Alamofire.download` 메서드를 사용하여 파일을 다운로드하고, 다운로드 진행 상황은 `downloadProgress` 클로저를 사용하여 업데이트합니다.

```swift
let fileURL = URL(string: "http://www.example.com/myfile.zip")!

Alamofire.download(fileURL, to: destination).downloadProgress { progress in
    // 다운로드 진행 상황 업데이트
    progressView.setProgress(Float(progress.fractionCompleted), animated: true)
}.response { response in
    // 다운로드 완료 후 처리
    if let destinationURL = response.destinationURL {
        // 파일 다운로드 완료 후 작업 처리
    }
}
```

위의 코드 예제에서 `fileURL`은 다운로드할 파일의 URL이며, `destination`은 파일을 저장할 로컬 디렉토리의 URL입니다.

## 참고 자료

- Alamofire: [https://github.com/Alamofire/Alamofire](https://github.com/Alamofire/Alamofire)
- ObjectMapper: [https://github.com/tristanhimmelman/ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper)
- AlamofireObjectMapper: [https://github.com/tristanhimmelman/AlamofireObjectMapper](https://github.com/tristanhimmelman/AlamofireObjectMapper)