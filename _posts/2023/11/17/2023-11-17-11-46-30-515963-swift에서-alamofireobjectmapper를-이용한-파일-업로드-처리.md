---
layout: post
title: "[swift] Swift에서 AlamofireObjectMapper를 이용한 파일 업로드 처리"
description: " "
date: 2023-11-17
tags: [swift]
comments: true
share: true
---

Swift에서 AlamofireObjectMapper를 사용하면 간편하게 파일을 업로드할 수 있습니다. 이 블로그 포스트에서는 Swift에서 파일 업로드를 처리하는 과정을 알아보겠습니다.

## 1. Alamofire 및 AlamofireObjectMapper 설치

먼저 프로젝트에 Alamofire 및 AlamofireObjectMapper를 설치해야 합니다. 이를 위해 `Podfile`에 다음과 같이 라이브러리를 추가합니다.

```swift
pod 'Alamofire'
pod 'AlamofireObjectMapper'
```

그리고 터미널에서 `pod install` 명령을 실행하여 라이브러리를 설치합니다.

## 2. 파일 업로드 요청 만들기

파일 업로드 요청을 생성하기 위해 다음과 같은 코드를 작성합니다.

```swift
import Alamofire
import AlamofireObjectMapper

func uploadFile(url: String, fileURL: URL, completion: @escaping (Bool) -> Void) {
    Alamofire.upload(
        multipartFormData: { multipartFormData in
            multipartFormData.append(fileURL, withName: "file")
        },
        to: url,
        method: .post,
        headers: nil,
        encodingCompletion: { encodingResult in
            switch encodingResult {
            case .success(let upload, _, _):
                upload
                    .validate()
                    .responseObject { (response: DataResponse<UploadResponse>) in
                        switch response.result {
                        case .success(let uploadResponse):
                            completion(true)
                        case .failure(let error):
                            print(error)
                            completion(false)
                        }
                    }
            case .failure(let error):
                print(error)
                completion(false)
            }
        }
    )
}
```

위 코드에서 `uploadFile` 함수는 업로드할 파일의 URL과 업로드가 성공했는지에 대한 결과를 리턴하는 closure를 파라미터로 받습니다. 해당 closure에서 `true`라면 파일 업로드가 성공한 것을 의미하고, `false`라면 실패한 것을 의미합니다.

## 3. 파일 업로드 실행하기

실제로 파일을 업로드하는 부분은 다음과 같이 작성할 수 있습니다.

```swift
let fileURL = URL(fileURLWithPath: "path/to/file")
let uploadURL = "http://example.com/upload"

uploadFile(url: uploadURL, fileURL: fileURL) { success in
    if success {
        print("File upload successful")
    } else {
        print("File upload failed")
    }
}
```

위 코드에서 `fileURL`은 업로드할 파일의 URL을, `uploadURL`은 파일을 업로드할 서버의 URL을 나타냅니다. `uploadFile` 함수를 호출하여 파일 업로드를 실행하고, 결과에 따라 성공 혹은 실패 메시지를 출력합니다.

## 결론

위의 과정을 따라하면 Swift에서 AlamofireObjectMapper를 이용한 파일 업로드를 간편하게 처리할 수 있습니다. Alamofire와 ObjectMapper를 함께 사용하면 서버와의 통신과 JSON 매핑 작업을 손쉽게 처리할 수 있습니다. 이를 통해 개발 과정을 더욱 효율적으로 진행할 수 있습니다.

## 참고

- [Alamofire](https://github.com/Alamofire/Alamofire)
- [AlamofireObjectMapper](https://github.com/tristanhimmelman/AlamofireObjectMapper)