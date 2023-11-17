---
layout: post
title: "[swift] AlamofireObjectMapper를 사용하여 네트워크 요청의 업로드 진행 상황 표시하기"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

AlamofireObjectMapper는 Alamofire와 ObjectMapper를 결합한 라이브러리로, JSON 응답을 매핑하는 작업을 단순화시켜주는 편리한 도구입니다. 이것을 사용하여 네트워크 요청을 보낼 때 업로드 진행 상황을 표시하는 기능을 구현하는 방법을 알아보겠습니다.

## 프로젝트 설정

우선 Alamofire와 ObjectMapper, AlamofireObjectMapper를 프로젝트에 추가해야 합니다. CocoaPods를 사용하면 간단하게 설치할 수 있습니다. Podfile에 다음 내용을 추가하고 `pod install` 명령을 실행하세요.

```ruby
pod 'Alamofire'
pod 'ObjectMapper'
pod 'AlamofireObjectMapper'
```

## 업로드 진행 상황 표시 구현하기

다음은 Alamofire를 사용하여 이미지를 업로드하는 예제입니다. 업로드 진행 상황 표시를 위해 `Progress` 객체를 사용할 것입니다.

```swift
import Alamofire
import AlamofireObjectMapper

// 업로드할 이미지와 서버 URL
let image = UIImage(named: "sample_image")
let url = "https://example.com/upload"

// 업로드 요청 생성
let request = Alamofire.upload(
    multipartFormData: { multipartFormData in
        if let imageData = image?.pngData() {
            // 이미지 데이터를 추가합니다.
            multipartFormData.append(imageData, withName: "image", fileName: "image.png", mimeType: "image/png")
        }
    },
    to: url,
    encodingCompletion: { encodingResult in
        switch encodingResult {
        case .success(let upload, _, _):
            // 업로드 진행 상황을 표시할 옵저버 생성
            upload.uploadProgress { progress in
                // 진행 상황을 표시하는 코드 작성
                let percentComplete = progress.fractionCompleted * 100
                print("업로드 진행 상황: \(percentComplete)%")
            }
            // 응답 매핑
            upload.responseObject { (response: DataResponse<YourResponseObject>) in
                // 응답 처리 코드 작성
            }
        case .failure(let encodingError):
            // 업로드 실패 처리 코드 작성
        }
    }
)
```

위 예제에서 `upload.uploadProgress` 블록 안에서 업로드 진행 상황을 표시하는 코드를 작성하면 됩니다. 여기서는 간단하게 콘솔에 퍼센트 완료를 출력하도록 했습니다.

## 결론

이렇게 AlamofireObjectMapper를 사용하여 네트워크 요청의 업로드 진행 상황을 표시할 수 있습니다. Alamofire와 ObjectMapper의 강력한 기능을 결합하여 JSON 매핑 작업을 간편하게 수행할 수 있기 때문에, 간단하고 효율적인 네트워크 요청 구현을 위해 많이 사용되고 있습니다. 자세한 내용은 [Alamofire](https://github.com/Alamofire/Alamofire), [ObjectMapper](https://github.com/tristanhimmelman/ObjectMapper), [AlamofireObjectMapper](https://github.com/tristanhimmelman/AlamofireObjectMapper) GitHub 저장소를 참고하세요.