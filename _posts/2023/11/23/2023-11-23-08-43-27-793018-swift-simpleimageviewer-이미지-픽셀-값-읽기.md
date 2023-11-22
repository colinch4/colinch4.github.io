---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 읽기"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 처리를 위해 이미지의 픽셀 값을 읽는 것은 중요한 작업 중 하나입니다. 이번 포스트에서는 Swift를 사용하여 이미지의 픽셀 값을 읽는 방법을 알아보겠습니다.

## ImageIO 프레임워크

이미지의 픽셀 값을 읽으려면 ImageIO 프레임워크를 사용해야 합니다. ImageIO는 이미지를 읽고 쓰는 기능을 제공하는 Cocoa Touch 프레임워크입니다.

### 이미지 로드하기

```swift
import UIKit

func loadUIImage(fromPath path: String) -> UIImage? {
    return UIImage(contentsOfFile: path)
}

func loadCGImage(fromPath path: String) -> CGImage? {
    if let image = loadUIImage(fromPath: path) {
        return image.cgImage
    }
    return nil
}
```

위의 코드는 파일 경로에서 `UIImage` 또는 `CGImage` 객체를 로드하는 두 가지 헬퍼 함수를 정의하는 것입니다. 이러한 함수들을 사용하여 이미지를 로드하고 픽셀 값을 읽을 수 있습니다.

### 픽셀 값 읽기

```swift
func getPixelColor(fromImage image: CGImage, atPoint point: CGPoint) -> UIColor? {
    let pixelData = image.dataProvider?.data
    let data = CFDataGetBytePtr(pixelData)
    
    let pixelInfo = ((image.width * Int(point.y)) + Int(point.x)) * 4
    
    let red = CGFloat(data?[pixelInfo] ?? 0) / 255.0
    let green = CGFloat(data?[pixelInfo + 1] ?? 0) / 255.0
    let blue = CGFloat(data?[pixelInfo + 2] ?? 0) / 255.0
    let alpha = CGFloat(data?[pixelInfo + 3] ?? 0) / 255.0

    return UIColor(red: red, green: green, blue: blue, alpha: alpha)
}
```

`getPixelColor` 함수는 주어진 `CGImage`에서 지정된 좌표에 해당하는 픽셀 값을 읽습니다. 함수는 이미지 데이터를 `CFData`로 가져온 다음, 해당 좌표의 픽셀의 정보를 계산합니다.

### 사용 예제

```swift
if let cgImage = loadCGImage(fromPath: "path_to_image.png") {
    let pixelColor = getPixelColor(fromImage: cgImage, atPoint: CGPoint(x: 50, y: 50))
    print(pixelColor)
}
```

위의 예제에서는 `loadCGImage` 함수를 사용하여 이미지를 로드하고, `getPixelColor` 함수를 사용하여 좌표 (50, 50)에 해당하는 픽셀 값을 가져옵니다. 가져온 픽셀 값을 출력합니다.

## 결론

Swift를 사용하여 이미지의 픽셀 값을 읽는 것은 ImageIO 프레임워크를 사용하여 간단하게 수행할 수 있습니다. 픽셀 값을 활용하여 이미지 처리 작업을 수행할 수 있습니다.

---

참고 문서:

- [Apple Developer Documentation - ImageIO Framework](https://developer.apple.com/documentation/imageio)
- [Stack Overflow - How to get pixel data from a UIImage (Cocoa Touch) or CGImage (Core Graphics)?](https://stackoverflow.com/questions/652120/how-do-i-get-the-pixel-data-of-a-uiimage-cocoa-touch-or-cgimage-core-graphics)