---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 파일 타입 확인"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 파일을 다루는 앱을 개발하는 경우, 때로는 이미지 파일의 타입을 확인해야 합니다. Swift 언어를 사용하여 간단한 ImageViewer를 만들 때 이미지 파일의 타입을 확인하는 방법에 대해 알아보겠습니다.

## Image 파일의 타입 확인하기

Swift에서 이미지 파일의 타입을 확인하기 위해서는 `UIImage` 클래스의 `imageOrientation` 속성을 사용합니다. 이 속성은 이미지의 속성 중 하나로, 실제 이미지 파일의 타입을 나타냅니다.

```swift
import UIKit

func getImageType(imageURL: URL) -> String? {
    if let image = UIImage(contentsOfFile: imageURL.path) {
        let imageOrientation = image.imageOrientation
        switch imageOrientation {
        case .up, .upMirrored:
            return "JPEG"
        case .down, .downMirrored:
            return "PNG"
        case .left, .leftMirrored:
            return "GIF"
        case .right, .rightMirrored:
            return "BMP"
        @unknown default:
            return nil
        }
    }
    return nil
}
```

위의 코드는 `getImageType` 함수를 정의하는 예제입니다. 함수는 이미지 파일의 URL을 입력으로 받아 해당 이미지의 타입을 반환합니다. 함수 내부에서는 `UIImage(contentsOfFile:)` 메서드를 사용하여 이미지 파일을 `UIImage` 객체로 로드하고, `imageOrientation` 속성을 사용하여 이미지 파일의 타입을 확인합니다.

위의 예제에서는 대표적인 이미지 파일 타입인 JPEG, PNG, GIF, BMP를 확인하는 예를 보여주고 있습니다. 기타 타입이나 알 수 없는 타입의 경우에는 nil을 반환하도록 처리하였습니다.

## 사용 예시

```swift
if let imageURL = Bundle.main.url(forResource: "sample", withExtension: "jpg") {
    if let imageType = getImageType(imageURL: imageURL) {
        print("Image Type: \(imageType)")
    } else {
        print("Unknown image type.")
    }
} else {
    print("Image not found.")
}
```

위의 예시는 Bundle에 포함된 "sample.jpg" 이미지 파일의 타입을 확인하는 코드입니다. `getImageType` 함수를 사용하여 이미지 타입을 얻은 후에는 해당 이미지의 타입을 출력합니다. 이미지를 찾지 못하거나 타입을 확인할 수 없는 경우에 대비하여 적절한 메시지를 출력합니다.

## 결론

이미지 파일의 타입 확인은 이미지 처리 앱 개발에 필수적인 요소입니다. Swift 언어를 사용하여 간단한 ImageViewer를 개발할 때 이미지 파일의 타입을 확인하는 방법에 대해 알아보았습니다. 이를 참고하여 Swift 앱 개발 시 이미지 파일의 타입 확인에 유용하게 활용할 수 있습니다.