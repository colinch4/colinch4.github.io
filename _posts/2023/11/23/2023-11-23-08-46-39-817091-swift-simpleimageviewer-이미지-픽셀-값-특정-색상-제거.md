---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 특정 색상 제거"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 처리는 앱 개발에서 중요한 부분 중 하나입니다. 때로는 원하는 색상을 이미지에서 제거하여 이미지를 개선하고 다른 작업에 활용해야 할 수도 있습니다. 이번에는 Swift를 사용하여 이미지에서 특정 색상을 제거하는 방법을 알아보겠습니다.

## 이미지 불러오기

먼저, 이미지를 불러와야 합니다. `UIImage` 클래스를 사용하여 이미지를 로드할 수 있습니다. 아래의 코드는 `example.png`라는 이미지 파일을 앱 번들에서 로드하는 예시입니다.

```swift
guard let image = UIImage(named: "example.png") else { return }
```

## 픽셀 값 접근

이미지의 픽셀 값을 접근하기 위해서는 `CGImage` 객체를 사용해야 합니다. `CGImage` 객체는 `UIImage`의 `cgImage` 속성을 통해 얻을 수 있습니다. 이제 `CGImage` 객체를 사용하여 이미지의 넓이와 높이, 각 픽셀의 색상 정보에 접근할 수 있습니다.

```swift
guard let cgImage = image.cgImage else { return }
let width = cgImage.width
let height = cgImage.height

let colorSpace = CGColorSpaceCreateDeviceRGB()
let bytesPerPixel = 4
let bytesPerRow = bytesPerPixel * width
let bitsPerComponent = 8

let imageData = UnsafeMutablePointer<UInt8>.allocate(capacity: width * height * bytesPerPixel)
let context = CGContext(data: imageData,
                        width: width,
                        height: height,
                        bitsPerComponent: bitsPerComponent,
                        bytesPerRow: bytesPerRow,
                        space: colorSpace,
                        bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue | CGBitmapInfo.byteOrder32Big.rawValue)
guard let imageContext = context else {
    imageData.deallocate()
    return
}
imageContext.draw(cgImage, in: CGRect(x: 0, y: 0, width: width, height: height))
```

## 색상 제거

이제 이미지의 픽셀 값을 변경하여 특정 색상을 제거하는 작업을 해보겠습니다. 아래의 예시 코드는 이미지에서 흰색을 제거하는 예시입니다.

```swift
for y in 0..<height {
    for x in 0..<width {
        let pixelOffset = (y * width + x) * bytesPerPixel
        let red = CGFloat(imageData[pixelOffset])
        let green = CGFloat(imageData[pixelOffset + 1])
        let blue = CGFloat(imageData[pixelOffset + 2])
        
        if red > 200 && green > 200 && blue > 200 {
            imageData[pixelOffset] = 0
            imageData[pixelOffset + 1] = 0
            imageData[pixelOffset + 2] = 0
        }
    }
}
```

위의 예시 코드는 이미지의 각 픽셀 값을 순회하며 흰색 픽셀인지 확인하고, 흰색 픽셀인 경우 각 색상 값을 0으로 변경하는 작업을 수행합니다. 원하는 색상에 대한 조건 체크와 변경할 색상 값은 필요에 따라 수정할 수 있습니다.

## 수정된 이미지 생성

마지막으로, 수정된 픽셀 값을 가지는 이미지를 생성할 차례입니다. 앞에서 작업한 `imageData`를 사용하여 수정된 이미지를 생성합니다.

```swift
let provider = CGDataProvider(data: NSData(bytesNoCopy: imageData,
                                           length: width * height * bytesPerPixel,
                                           deallocator: .free))
let modifiedImage = CGImage(width: width,
                            height: height,
                            bitsPerComponent: bitsPerComponent,
                            bitsPerPixel: bytesPerPixel * 8,
                            bytesPerRow: bytesPerRow,
                            space: colorSpace,
                            bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue | CGBitmapInfo.byteOrder32Big.rawValue,
                            provider: provider!,
                            decode: nil,
                            shouldInterpolate: false,
                            intent: .defaultIntent)

let finalImage = UIImage(cgImage: modifiedImage!)
```

위의 코드에서는 `CGDataProvider`와 `CGImage`를 사용하여 수정된 이미지를 생성합니다. `CGDataProvider`는 `imageData`로부터 데이터를 제공하고, `CGImage`는 수정된 이미지를 생성하는데 사용됩니다. 마지막으로, `UIImage`를 사용하여 `finalImage`를 생성합니다.

이제 `finalImage`는 원본 이미지에서 원하는 색상이 제거된 이미지를 가지게 됩니다.

## 결론

이번 글에서는 Swift를 사용하여 이미지에서 특정 색상을 제거하는 방법을 알아보았습니다. 이미지 처리 작업은 다양한 방식으로 활용될 수 있으며, 이러한 작업을 통해 더 나은 사용자 경험과 더 나은 이미지 품질을 달성할 수 있습니다.