---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 썸네일 생성"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지를 효과적으로 관리하고 표시하기 위해 섬네일은 매우 유용한 도구입니다. Swift를 사용하여 이미지 썸네일을 생성하는 방법을 알아보겠습니다.

## 1. AVFoundation Framework를 import

이미지 썸네일을 생성하려면 AVFoundation 프레임워크를 사용해야 합니다. 따라서 첫 번째 단계로, 해당 프레임워크를 import 해야 합니다.

```swift
import AVFoundation
```

## 2. 이미지에서 썸네일 생성하기

다음으로, 이미지 파일로부터 썸네일을 생성하는 함수를 작성해 보겠습니다.

```swift
func generateThumbnail(from imageURL: URL, completion: @escaping (UIImage?) -> Void) {
    DispatchQueue.global(qos: .background).async {
        let asset = AVURLAsset(url: imageURL)
        let generator = AVAssetImageGenerator(asset: asset)
        
        let thumbnailTime = CMTime(seconds: 1, preferredTimescale: 60)
        
        do {
            let imageRef = try generator.copyCGImage(at: thumbnailTime, actualTime: nil)
            let thumbnail = UIImage(cgImage: imageRef)
            DispatchQueue.main.async {
                completion(thumbnail)
            }
        } catch {
            DispatchQueue.main.async {
                completion(nil)
            }
        }
    }
}
```

위의 코드에서 `generateThumbnail(from:completion:)` 함수는 `URL` 형식의 이미지 파일 경로를 인자로 받아 비동기적으로 썸네일을 생성합니다. 썸네일의 시간은 `CMTime`을 사용하여 지정할 수 있으며, 위의 예제에서는 1초를 사용하였습니다.

## 3. 썸네일 생성 후 사용하기

이제 위에서 작성한 함수를 사용하여 이미지 파일의 썸네일을 생성하고 사용하는 방법을 알아보겠습니다.

```swift
let imageURL = URL(fileURLWithPath: "image_path.png")

generateThumbnail(from: imageURL) { thumbnail in
    guard let thumbnail = thumbnail else {
        // 썸네일 생성 실패
        return
    }
    // 생성한 썸네일 이미지 사용
    // 예시: UIImageView에 이미지 설정
    imageView.image = thumbnail
}
```

위의 예제에서는 `imageURL` 변수에 이미지 파일의 경로를 지정하고, `generateThumbnail(from:completion:)` 함수를 호출하여 썸네일을 생성합니다. 생성된 썸네일은 클로저의 `thumbnail` 매개변수로 전달되며, 실패하면 `nil`이 전달됩니다.

## 결론

Swift를 사용하여 썸네일을 생성하는 방법을 알아보았습니다. AVFoundation 프레임워크를 활용하여 비동기적으로 이미지 파일의 썸네일을 생성하고 사용할 수 있습니다. 이를 활용하여 이미지를 효과적으로 관리하고 표시할 수 있습니다.

## 참고 자료

- [Apple Developer Documentation - AVFoundation](https://developer.apple.com/documentation/avfoundation)
- [Apple Developer Documentation - AVAssetImageGenerator](https://developer.apple.com/documentation/avfoundation/avassetimagegenerator)
- [CMTime - Apple Developer Documentation](https://developer.apple.com/documentation/coremedia/cmtime)