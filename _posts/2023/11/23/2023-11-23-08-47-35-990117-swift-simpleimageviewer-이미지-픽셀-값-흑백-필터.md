---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 흑백 필터"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 픽셀 값을 흑백으로 변환하는 것은 이미지 처리에서 흔히 사용되는 작업입니다. Swift의 SimpleImageViewer를 사용하여 이미지를 로드하고, 픽셀 값을 읽어와서 흑백으로 변환하는 간단한 예제를 살펴보겠습니다.

## 요구 사항

이 예제를 실행하기 위해서는 다음 사항들이 필요합니다:

- Xcode 11
- Swift 5

## 프로젝트 설정

1. 새로운 Swift 프로젝트를 생성합니다.
2. Assets.xcassets 폴더에 sample.jpg라는 이름의 이미지 파일을 추가합니다. 이 파일은 테스트할 이미지로 사용됩니다.

## 이미지 불러오기

SimpleImageViewer를 사용하여 이미지를 불러오는 코드는 다음과 같습니다:

```swift
import SimpleImageViewer

let url = Bundle.main.url(forResource: "sample", withExtension: "jpg")
let image = UIImage(contentsOfFile: url?.path ?? "")

let imageView = UIImageView(image: image)
imageView.frame = CGRect(x: 0, y: 0, width: 300, height: 300)

let viewer = ImageViewer()
viewer.show(imageView)
```

이 코드는 sample.jpg 파일을 Bundle에서 로드하고, 이미지를 UIImageView에 할당한 후, ImageViewer를 사용하여 이미지를 표시합니다. 실행하면 sample.jpg 이미지가 보이는 창이 나타날 것입니다.

## 이미지 흑백 필터링

이제 이미지의 픽셀 값을 읽어와서 흑백으로 변환하는 코드를 추가해보겠습니다:

```swift
import SimpleImageViewer

let url = Bundle.main.url(forResource: "sample", withExtension: "jpg")
let image = UIImage(contentsOfFile: url?.path ?? "")

// 이미지 픽셀 데이터 가져오기
guard let imageData = image?.cgImage?.dataProvider?.data else { return }
let cfData = CFDataCreateCopy(nil, imageData)
let ptr = CFDataGetBytePtr(cfData)

// 이미지 픽셀 값을 흑백으로 변환하기
let width = image?.size.width ?? 0
let height = image?.size.height ?? 0
let bytesPerPixel = 4
let bytesPerRow = bytesPerPixel * Int(width)
let bitsPerComponent = 8
let colorSpace = CGColorSpaceCreateDeviceRGB()

let bitmapInfo = CGBitmapInfo(rawValue: CGImageAlphaInfo.premultipliedLast.rawValue)

guard let context = CGContext(data: UnsafeMutableRawPointer(mutating: ptr),
                              width: Int(width),
                              height: Int(height),
                              bitsPerComponent: bitsPerComponent,
                              bytesPerRow: bytesPerRow,
                              space: colorSpace,
                              bitmapInfo: bitmapInfo.rawValue) else { return }

guard let pixelBuffer = context.data else { return }
let pixelData = pixelBuffer.bindMemory(to: UInt32.self, capacity: Int(width) * Int(height))

for y in 0..<Int(height) {
    for x in 0..<Int(width) {
        let offset = y * Int(width) + x
        let pixel = pixelData[offset]
        
        let r = CGFloat((pixel >> 16) & 0xFF)
        let g = CGFloat((pixel >> 8) & 0xFF)
        let b = CGFloat((pixel >> 0) & 0xFF)
        
        let gray = (r + g + b) / 3
        
        let newPixel = ((UInt32(gray) << 24) | (UInt32(gray) << 16) | (UInt32(gray) << 8) | 0xFF)
        pixelData[offset] = newPixel
    }
}

// 이미지 업데이트
let newCGImage = context.makeImage()
let newImage = UIImage(cgImage: newCGImage!)

let imageView = UIImageView(image: newImage)
imageView.frame = CGRect(x: 0, y: 0, width: 300, height: 300)

let viewer = ImageViewer()
viewer.show(imageView)
```

이 코드는 이미지의 픽셀 값들을 가져와서 각 픽셀의 RGB 값을 흑백으로 변환하는 작업을 수행합니다. 변환된 픽셀 값으로 새로운 이미지를 생성하고, ImageViewer를 사용하여 흑백 이미지를 표시합니다. 실행하면 sample.jpg 이미지가 흑백으로 변환되어 보일 것입니다.

## 결론

Swift의 SimpleImageViewer를 사용하여 이미지의 픽셀 값을 읽어와서 흑백으로 변환하는 예제를 살펴보았습니다. 이미지 처리에는 다양한 작업이 가능하므로, 필요에 따라 추가적인 작업을 수행하여 이미지를 다양하게 변형할 수 있습니다.