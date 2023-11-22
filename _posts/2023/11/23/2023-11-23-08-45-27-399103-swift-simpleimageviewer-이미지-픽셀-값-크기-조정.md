---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 크기 조정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 뷰어는 이미지를 표시하고 사용자가 해당 이미지를 확대 또는 축소하는 등의 조작을 할 수 있는 기능을 제공합니다. 이미지 뷰어를 개발하다 보면 때때로 이미지 픽셀 값의 크기를 조정해야 할 때가 있습니다.

이번 포스트에서는 Swift를 사용하여 이미지의 픽셀 값을 크기 조정하는 방법에 대해 알아보겠습니다.

## 이미지 크기 조정하기

```swift
import UIKit

func resizeImageWithPixel(image: UIImage, newSize: CGSize) -> UIImage {
    UIGraphicsBeginImageContextWithOptions(newSize, false, 0.0)
    image.draw(in: CGRect(x: 0, y: 0, width: newSize.width, height: newSize.height))
    let newImage = UIGraphicsGetImageFromCurrentImageContext()
    UIGraphicsEndImageContext()
    return newImage!
}

let originalImage = UIImage(named: "example.jpg")
let newSize = CGSize(width: 500, height: 500)
let resizedImage = resizeImageWithPixel(image: originalImage!, newSize: newSize)
```

위의 코드는 `resizeImageWithPixel` 함수를 사용하여 이미지의 픽셀 값을 크기 조정하는 예시입니다. `originalImage` 변수에 원본 이미지를 할당하고, `newSize` 변수에는 조정하고 싶은 새로운 크기를 할당합니다. `resizeImageWithPixel` 함수는 이미지를 주어진 크기로 조정한 새로운 이미지를 반환합니다.

실행 결과로 나온 `resizedImage` 변수에는 조정된 이미지가 저장됩니다.

## 참고 자료

- [UIImage - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimage)
- [UIGraphicsBeginImageContextWithOptions(_:Bool, _:CGFloat) - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uigraphicsbeginimagecontextwithoptions)