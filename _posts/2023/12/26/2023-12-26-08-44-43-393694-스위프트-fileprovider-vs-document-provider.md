---
layout: post
title: "[swift] 스위프트 FileProvider VS Document Provider"
description: " "
date: 2023-12-26
tags: [swift]
comments: true
share: true
---

iOS 앱에서 파일 및 문서를 다루는 데 있어 FileProvider와 Document Provider는 두 가지 중요한 개념입니다. 각각의 역할과 차이점을 살펴보겠습니다.

## 1. FileProvider

FileProvider는 iOS 앱과 외부 파일 시스템 간의 상호 작용을 관리하는데 사용됩니다. 외부 저장소나 네트워크 드라이브와 같은 외부 소스에서 파일을 읽거나 쓸 수 있는 기능을 제공합니다. 이를 통해 사용자는 다른 앱이나 외부 드라이브에 있는 파일에 대한 액세스 권한을 부여할 수 있습니다.

```swift
import FileProvider

// FileProvider로 파일 읽기
let provider = NSFileProviderManager.default
provider.startProvidingItem(at: fileURL, completionHandler: { error in
    if let error = error {
        // 파일 열기 실패
    } else {
        // 파일 열기 성공
    }
})
```

## 2. Document Provider

Document Provider는 사용자가 iCloud 또는 다른 파일 공유 서비스를 통해 액세스하는 문서나 파일을 관리하는 역할을 합니다. 이를 통해 다른 서비스나 앱과의 데이터 공유 및 동기화가 가능해집니다.

```swift
// Document Provider로 파일 저장
let fileURL = // 파일의 URL
let documentPicker = UIDocumentPickerViewController(url: fileURL, in: .exportToService)
documentPicker.delegate = self
present(documentPicker, animated: true, completion: nil)
```

## 결론

FileProvider는 외부 소스에서 파일을 읽거나 쓰는 기능을 제공하고, Document Provider는 외부 파일 공유 서비스를 통해 문서나 파일을 관리하는 역할을 합니다. 앱의 파일 및 문서 관련 기능을 구현할 때, 이 두 가지 요소를 적절히 활용하여 사용자 경험을 향상시킬 수 있습니다.

참고:

Swift Documentation - [FileProvider](https://developer.apple.com/documentation/fileprovider)
Swift Documentation - [Document Provider](https://developer.apple.com/documentation/uikit/uidocumentpickerdelegate)