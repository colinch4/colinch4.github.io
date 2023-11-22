---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 특정 색상 필터링"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 프로세싱은 모바일 앱 및 웹 애플리케이션에서 매우 중요한 기능입니다. Swift에서는 UIImage 객체를 사용하여 이미지를 로드하고 처리할 수 있습니다. 이번 블로그 포스트에서는 이미지의 픽셀 값을 확인하고 특정 색상으로 필터링하는 방법을 알아보겠습니다.

## 이미지 로드하기

먼저, 이미지를 로드하기 위해 UIImage 객체를 생성해야 합니다. Swift에서는 이미지 파일 이름으로 UIImage를 생성할 수 있습니다. 예를 들어, `image.jpg`라는 이미지 파일을 로드하려면 다음과 같이 작성할 수 있습니다.

```swift
let image = UIImage(named: "image.jpg")
```

## 픽셀 값 접근하기

UIImage 객체를 통해 이미지를 로드했다면, 다음으로는 이미지의 각 픽셀 값을 액세스해야 합니다. 이를 위해서는 이미지를 CGImage로 변환해야 합니다. 다음의 코드를 사용하여 UIImage를 CGImage로 변환할 수 있습니다.

```swift
guard let cgImage = image.cgImage else { return }
```

이제 cgImage 객체를 통해 이미지의 픽셀 값을 액세스할 수 있습니다.

```swift
let width = cgImage.width
let height = cgImage.height
let bytesPerPixel = 4
let bytesPerRow = bytesPerPixel * width
let bitsPerComponent = 8

guard let pixelData = cgImage.dataProvider?.data else { return }
let data: UnsafePointer<UInt8> = CFDataGetBytePtr(pixelData)

for y in 0..<height {
    for x in 0..<width {
        let pixelOffset = (x * bytesPerPixel) + (y * bytesPerRow)
        
        let red = data[pixelOffset]
        let green = data[pixelOffset + 1]
        let blue = data[pixelOffset + 2]
        let alpha = data[pixelOffset + 3]
        
        // 픽셀 값에 대한 작업을 수행하세요.
    }
}
```

위의 코드에서는 이미지의 가로와 세로 크기를 확인하고, 각 픽셀의 RGBA 값을 가져와서 작업을 수행할 수 있습니다.

## 색상 필터링하기

이미지의 픽셀 값을 확인한 후, 특정 색상으로 필터링하는 것은 비교적 간단합니다. 예를 들어, 모든 픽셀 값을 검은색으로 설정하려면 다음과 같이 작성할 수 있습니다.

```swift
for y in 0..<height {
    for x in 0..<width {
        let pixelOffset = (x * bytesPerPixel) + (y * bytesPerRow)
        
        data[pixelOffset] = 0 // red
        data[pixelOffset + 1] = 0 // green
        data[pixelOffset + 2] = 0 // blue
        data[pixelOffset + 3] = 255 // alpha
    }
}
```

위의 코드에서는 각 픽셀의 R, G, B 값을 0으로 설정하고, 알파 값을 255로 설정하여 모든 픽셀을 검은색으로 만듭니다.

## 결론

이번 블로그 포스트에서는 Swift를 사용하여 이미지의 픽셀 값을 확인하고 특정 색상으로 필터링하는 방법에 대해 알아보았습니다. Swift의 UIImage 및 CGImage 클래스를 사용하여 이미지를 로드하고 처리할 수 있습니다. 이미지 프로세싱 기능은 다양한 앱 개발 시나리오에서 유용하게 사용될 수 있습니다.

관련 자료:
- [UIImage - Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimage)
- [CGImage - Apple Developer Documentation](https://developer.apple.com/documentation/coregraphics/cgimage)
- [Core Image - Apple Developer Documentation](https://developer.apple.com/documentation/coreimage)