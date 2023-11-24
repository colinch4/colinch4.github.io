---
layout: post
title: "[swift] SkyFloatingLabelTextField 입력한 텍스트를 다른 언어로 번역하기"
description: " "
date: 2023-11-24
tags: [swift]
comments: true
share: true
---

SkyFloatingLabelTextField는 사용자에게 입력한 텍스트를 플로팅 라벨 형식으로 표시해주는 기능을 제공하는 텍스트 필드입니다. 이번에는 사용자가 입력한 텍스트를 다른 언어로 번역하는 방법에 대해 알아보겠습니다.

## Google Translate API 사용하기

Google Translate API를 사용하면 간편하게 텍스트를 다른 언어로 번역할 수 있습니다. 먼저 Google Cloud Console에 접속하여 프로젝트를 생성하고, 번역 API를 활성화 해주세요.

다음으로, `Google Cloud Translation API`를 설치해야 합니다. 프로젝트 폴더의 `Podfile`에 다음과 같이 추가해주세요.

```swift
pod 'GoogleCloudTranslation'
```

프로젝트를 빌드하고 나면, 다음과 같은 코드를 사용하여 텍스트를 원하는 언어로 번역할 수 있습니다.

```swift
import GoogleCloudTranslation

let translation = GoogleCloudTranslation()

func translateText(text: String, targetLanguage: String, completion: @escaping (String?) -> Void) {
    translation.translateText(text, targetLanguage: targetLanguage) { result in
        switch result {
        case .success(let translation):
            completion(translation.translatedText)
        case .failure(let error):
            print("번역 실패: \(error.localizedDescription)")
            completion(nil)
        }
    }
}
```

위의 코드를 활용하여 SkyFloatingLabelTextField에 입력된 텍스트를 원하는 언어로 번역해보세요.

## 다른 번역 API 사용하기

Google Translate API 말고도 다른 번역 API도 사용할 수 있습니다. 예를 들어, `Papago Translate API`나 `IBM Watson Language Translator API` 등을 활용할 수 있습니다. 각각의 API는 해당 제공업체의 문서를 참고하여 사용법을 익히세요.

## 결론

SkyFloatingLabelTextField에 입력된 텍스트를 다른 언어로 번역하기 위해서는 번역 API를 활용하는 것이 가장 간편한 방법입니다. 여러 번역 API 중에 가장 적합한 API를 선택하여 프로젝트에 적용해보세요. 번역된 텍스트를 플로팅 라벨 형식으로 표시해주는 SkyFloatingLabelTextField와 함께 멋진 다국어 지원 앱을 개발해보세요!

---

### 참고 자료

- [Google Cloud Translation API Documentation](https://cloud.google.com/translate/docs)
- [Papago Translate API Documentation](https://developers.naver.com/docs/papago/papago-nmt-api-reference.md)
- [IBM Watson Language Translator API Documentation](https://cloud.ibm.com/apidocs/language-translator)