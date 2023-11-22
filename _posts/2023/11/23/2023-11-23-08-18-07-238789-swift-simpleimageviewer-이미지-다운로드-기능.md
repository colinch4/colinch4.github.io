---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 다운로드 기능"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift로 간단한 이미지 뷰어 앱을 개발 중이신가요? 그렇다면 이미지 다운로드 기능을 추가해보는 것이 좋을 것입니다. 이 기능을 통해 사용자가 앱 내에서 이미지를 다운로드하고 저장할 수 있으므로 편리성을 높일 수 있습니다. 이번 글에서는 Swift를 사용하여 이미지 다운로드 기능을 구현하는 방법에 대해 알아보겠습니다.

### 1. 이미지 다운로드 기능 구현하기

첫 번째로, 이미지 다운로드 기능을 구현하기 위해 다음과 같은 단계를 따를 수 있습니다.

1. URL을 사용하여 원격 이미지에 접근합니다.
2. 이미지 데이터를 다운로드합니다.
3. 다운로드한 이미지 데이터를 로컬 저장소에 저장합니다.

다음은 이미지 다운로드 기능을 추가하는 예제 코드입니다.

```swift
import UIKit

func downloadImage(from url: URL, completion: @escaping (UIImage?) -> Void) {
    DispatchQueue.global(qos: .userInitiated).async {
        guard let imageData = try? Data(contentsOf: url) else {
            DispatchQueue.main.async {
                completion(nil)
            }
            return
        }
        
        let image = UIImage(data: imageData)
        
        DispatchQueue.main.async {
            completion(image)
        }
    }
}

// 사용 예시
let url = URL(string: "https://example.com/image.jpg")!
downloadImage(from: url) { image in
    if let image = image {
        // 이미지 다운로드 성공
    } else {
        // 이미지 다운로드 실패
    }
}
```

위의 코드는 비동기로 이미지를 다운로드하고, 다운로드가 완료될 때 마다 completion closure를 호출합니다. 이미지 다운로드에 성공하면 UIImage 객체를 전달하고, 실패하면 nil을 전달합니다.

### 2. 다운로드된 이미지 저장하기

이미지를 다운로드한 후에는 다운로드된 이미지를 로컬 저장소에 저장해야 합니다. UIImage 객체에서 이미지를 파일로 저장하는 방법은 다음과 같습니다.

```swift
func saveImageToFileSystem(image: UIImage, fileName: String) -> Bool {
    guard let data = image.jpegData(compressionQuality: 1.0) ?? image.pngData() else {
        return false
    }
    
    let fileURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask).first!.appendingPathComponent(fileName)
    
    do {
        try data.write(to: fileURL)
        return true
    } catch {
        return false
    }
}

// 사용 예시
if let image = image {
    let success = saveImageToFileSystem(image: image, fileName: "image.jpg")
    if success {
        // 이미지 저장 성공
    } else {
        // 이미지 저장 실패
    }
}
```

위의 코드를 이용하여 이미지를 파일로 저장할 수 있습니다. 저장에 성공하면 true를 리턴하고, 실패하면 false를 리턴합니다.

### 3. 참고 자료

- [UIImage 공식 문서](https://developer.apple.com/documentation/uikit/uiimage)
- [URLSession 공식 문서](https://developer.apple.com/documentation/foundation/urlsession)
- [FileManager 공식 문서](https://developer.apple.com/documentation/foundation/filemanager)

이제 Swift로 이미지 다운로드 기능을 구현하는 방법에 대해 알아보았습니다. 원격 서버에서 이미지를 다운로드하고, 다운로드된 이미지를 로컬에 저장하는 것은 매우 유용한 기능입니다. 이를 통해 앱의 사용자들이 편리하게 이미지를 관리할 수 있도록 제공해보세요.

### 4. 요약

- Swift로 이미지 다운로드 기능을 구현할 수 있습니다.
- URLSession과 FileManager를 사용하여 이미지 다운로드 및 저장 기능을 추가할 수 있습니다.
- 이미지를 다운로드하고 저장함으로써 사용자에게 편의성을 제공할 수 있습니다.

이제 위의 내용을 참고하여 Swift로 이미지 다운로드 기능을 구현해보세요!