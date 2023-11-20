---
layout: post
title: "[swift] Alamofire를 사용하여 OCR(Optical Character Recognition) 구현하기"
description: " "
date: 2023-11-20
tags: [swift]
comments: true
share: true
---

이번 예시에서는 Swift와 Alamofire를 사용하여 OCR (Optical Character Recognition)을 구현하는 방법을 알아보겠습니다.

OCR은 이미지나 문서에서 텍스트를 인식하는 기술로, 사진이나 스캔한 문서에서 텍스트를 추출할 수 있습니다. Alamofire는 Swift에서 네트워킹을 쉽게 처리할 수 있도록 도와주는 라이브러리입니다.

## 필수 요구사항
- Xcode
- Swift 5
- Alamofire 라이브러리

## Step 1: Alamofire 설치하기
먼저, 프로젝트에 Alamofire를 설치해야 합니다. Swift Package Manager를 사용해 프로젝트를 구성하거나 CocoaPods를 사용하여 설치할 수 있습니다.

### Swift Package Manager를 사용한 설치 방법
1. Xcode를 엽니다.
2. 프로젝트를 선택하고, "File" 메뉴에서 "Swift Packages"를 선택합니다.
3. "Add Package Dependency"를 선택합니다.
4. 다음 URL을 입력하고 "Next"를 클릭합니다: `https://github.com/Alamofire/Alamofire.git`
5. "Rules" 창에서 "Branch"를 선택합니다. "master" 브랜치를 선택한 후, "Next"를 클릭합니다.
6. 사용할 타겟을 선택하고, "Finish"를 클릭합니다.

### CocoaPods를 사용한 설치 방법
1. 터미널을 열고, 프로젝트가 있는 디렉토리로 이동합니다.
2. `pod init` 명령어를 실행하여 Podfile을 생성합니다.
3. 생성된 Podfile을 열고, 아래와 같이 수정합니다:

```ruby
platform :ios, '13.0'

target 'YourApp' do
  use_frameworks!
  pod 'Alamofire', '~> 5.0'
end
```

4. 터미널에서 `pod install` 명령어를 실행하여 Alamofire를 설치합니다.

## Step 2: OCR API 사용을 위한 요청 보내기
OCR 기능을 사용하기 위해서는 OCR을 제공하는 API를 사용해야 합니다. 여러 가지 OCR API 중에서 Microsoft Azure Cognitive Services API를 사용해 볼 예정입니다.

1. Microsoft Azure Portal에 로그인하고, Cognitive Services 리소스를 만듭니다.
2. 생성한 리소스에서 "Keys and Endpoint"를 클릭하고, API Key와 Endpoint를 복사합니다.

## Step 3: Alamofire를 사용하여 OCR 요청 보내기
1. Xcode에서 Swift 프로젝트를 엽니다.
2. 필요한 import 문을 추가합니다:

```swift
import Alamofire
```

3. OCR 요청을 보내는 함수를 작성합니다:

```swift
func extractTextFromImage(image: UIImage, completion: @escaping (String?, Error?) -> Void) {
    let apiKey = "YOUR_API_KEY"
    let endpoint = "YOUR_API_ENDPOINT"

    let url = "\(endpoint)/vision/v3.0/ocr?language=ko&detectOrientation=true"
    
    // Alamofire를 사용하여 OCR 요청 보내기
    AF.upload(multipartFormData: { multipartFormData in
        // 이미지 파일로 변환
        if let imageData = image.jpegData(compressionQuality: 1.0) {
            // 이미지 파일을 multipartFormData에 추가
            multipartFormData.append(imageData, withName: "image", fileName: "image.jpg", mimeType: "image/jpeg")
        }
    }, to: url, headers: ["Content-Type": "multipart/form-data", "Ocp-Apim-Subscription-Key": apiKey])
    .responseJSON { response in
        switch response.result {
        case .success(let value):
            if let data = value as? [String: Any], let regions = data["regions"] as? [[String: Any]] {
                // 추출된 텍스트를 조합하여 반환
                let extractedText = regions.compactMap { region in
                    (region["lines"] as? [[String: Any]])?.compactMap { line in
                        (line["words"] as? [[String: Any]])?.compactMap { word in
                            (word["text"] as? String)
                        }.joined(separator: " ")
                    }.joined(separator: "\n")
                }.joined(separator: "\n\n")

                completion(extractedText, nil)
            } else {
                completion(nil, nil)
            }
        case .failure(let error):
            completion(nil, error)
        }
    }
}
```

4. 해당 함수를 호출하여 OCR 요청을 보냅니다:

```swift
let image = UIImage(named: "example.jpg")!
extractTextFromImage(image: image) { text, error in
    if let error = error {
        print("OCR 요청 실패: \(error)")
    } else {
        if let text = text {
            print("추출된 텍스트: \(text)")
        }
    }
}
```

위의 예시에서는 `extractTextFromImage` 함수를 사용하여 OCR 요청을 보내고, 응답으로 추출된 텍스트를 받아옵니다. API Key와 Endpoint는 사용자가 생성한 Microsoft Azure Cognitive Services의 정보로 대체해야 합니다.

## 결론
이번 글에서는 Swift와 Alamofire를 사용하여 OCR (Optical Character Recognition)을 구현하는 방법을 알아보았습니다. OCR은 사진이나 스캔한 문서에서 텍스트를 추출하는 데 사용되며, Alamofire는 Swift에서 네트워킹을 쉽게 처리할 수 있도록 도와줍니다. 앞서 설명한 방법을 통해 OCR 기능을 구현해 보시기 바랍니다.

## 참고 자료
- [Alamofire GitHub Repository](https://github.com/Alamofire/Alamofire)
- [Microsoft Azure Cognitive Services](https://azure.microsoft.com/services/cognitive-services/)