---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 회전"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 픽셀 값 회전은 이미지를 90도, 180도, 270도 등으로 회전시키는 작업을 의미합니다. Swift에서는 Core Graphics를 사용하여 이미지를 회전시킬 수 있습니다.

## 이미지 회전 함수

아래의 코드는 이미지 픽셀 값을 회전하는 함수를 구현한 예시입니다.

```swift
import UIKit

func rotateImagePixels(image: UIImage, angle: CGFloat) -> UIImage? {
    let rotatedSize = CGSize(width: image.size.height, height: image.size.width)
    UIGraphicsBeginImageContext(rotatedSize)
    
    guard let context = UIGraphicsGetCurrentContext() else {
        return nil
    }
    
    context.translateBy(x: rotatedSize.width / 2, y: rotatedSize.height / 2)
    context.rotate(by: angle)
    context.scaleBy(x: 1.0, y: -1.0)
    
    var transform = CGAffineTransform.identity
    transform = transform.translatedBy(x: -image.size.width / 2, y: -image.size.height / 2)
    
    if let cgImage = image.cgImage {
        context.draw(cgImage, in: CGRect(x: 0, y: 0, width: image.size.width, height: image.size.height))
    }
    
    guard let rotatedImage = UIGraphicsGetImageFromCurrentImageContext() else {
        return nil
    }
    
    UIGraphicsEndImageContext()
    
    return rotatedImage
}
```

위의 함수는 `UIImage`를 입력받아서 지정된 각도에 해당하는 회전된 이미지의 픽셀 값을 반환합니다. 함수 내부에서는 Core Graphics를 사용하여 이미지를 회전시키고, 회전된 이미지의 픽셀 값을 반환합니다.

## 사용 예시

아래는 위에서 구현한 `rotateImagePixels` 함수를 사용하여 이미지를 회전시키는 예시입니다.

```swift
let image = UIImage(named: "example_image")
let rotatedImage = rotateImagePixels(image: image, angle: .pi / 2)
```

위의 예시는 "example_image"라는 이름의 이미지를 90도로 회전시킨 후, `rotatedImage` 변수에 저장합니다.

## 결론

위에서 설명한 예시 코드를 참고하여 Swift에서 이미지 픽셀 값을 회전시키는 작업을 수행할 수 있습니다. 이를 활용하여 이미지 뷰어 앱 등에 적용할 수 있습니다.

## 참고 자료

- [Apple Developer Documentation - Core Graphics](https://developer.apple.com/documentation/coregraphics)
- [SwiftUI Image rotation](https://stackoverflow.com/questions/56533472/swiftui-image-rotation)