---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 밝기 조정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지를 표시하고 조작하는 앱을 만들 때, 이미지의 밝기를 조정하는 기능은 매우 유용합니다. Swift에서 이미지의 픽셀 값을 밝기로 조정하는 방법을 알아보겠습니다.

## 이미지 픽셀 값 읽기

우선 이미지의 픽셀 값을 읽어오는 함수를 작성해야 합니다. 이 함수를 통해 이미지의 모든 픽셀 값을 가져올 수 있습니다.
```swift
import UIKit

func getPixelData(from image: UIImage) -> [UInt8]? {
    guard let cgImage = image.cgImage else {
        return nil
    }
    
    let width = cgImage.width
    let height = cgImage.height
    let bytesPerPixel = 4
    let bytesPerRow = width * bytesPerPixel
    let bitsPerComponent = 8
    let pixelData = UnsafeMutablePointer<UInt8>.allocate(capacity: width * height * bytesPerPixel)
    let colorSpace = CGColorSpaceCreateDeviceRGB()
    
    let context = CGContext(data: pixelData,
                            width: width,
                            height: height,
                            bitsPerComponent: bitsPerComponent,
                            bytesPerRow: bytesPerRow,
                            space: colorSpace,
                            bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue | CGBitmapInfo.byteOrder32Big.rawValue)
    
    context?.draw(cgImage, in: CGRect(x: 0, y: 0, width: width, height: height))
    
    var pixelArray = [UInt8]()
    for index in 0..<(width * height * bytesPerPixel) {
        pixelArray.append(pixelData[index])
    }
    
    pixelData.deallocate()
    
    return pixelArray
}
```

## 이미지 밝기 조정

이제 이미지의 픽셀 값을 가져올 수 있으므로, 이 값을 조정하여 밝기를 변경할 수 있습니다. 예를 들어, 모든 픽셀 값을 일정한 값 만큼 더하거나 뺌으로써 밝기를 조정할 수 있습니다.
```swift
func adjustBrightness(image: UIImage, adjustment: Int) -> UIImage? {
    guard let pixelData = getPixelData(from: image) else {
        return nil
    }
    
    var modifiedPixelData = pixelData
    let bytesPerPixel = 4
    
    for index in 0..<(pixelData.count / bytesPerPixel) {
        let offset = index * bytesPerPixel
        let red = modifiedPixelData[offset]
        let green = modifiedPixelData[offset + 1]
        let blue = modifiedPixelData[offset + 2]
        
        modifiedPixelData[offset] = UInt8(max(0, min(255, Int(red) + adjustment)))
        modifiedPixelData[offset + 1] = UInt8(max(0, min(255, Int(green) + adjustment)))
        modifiedPixelData[offset + 2] = UInt8(max(0, min(255, Int(blue) + adjustment)))
    }
    
    let bitsPerComponent = 8
    let width = image.cgImage!.width
    let height = image.cgImage!.height
    let bytesPerRow = width * bytesPerPixel
    let colorSpace = CGColorSpaceCreateDeviceRGB()
    
    let providerRef = CGDataProvider(data: NSData(bytes: &modifiedPixelData, length: modifiedPixelData.count * MemoryLayout<UInt8>.stride))
    
    let bitmapInfo: UInt32 = CGBitmapInfo.byteOrder32Big.rawValue | CGImageAlphaInfo.premultipliedLast.rawValue
    let renderingIntent = CGColorRenderingIntent.defaultIntent
    
    let imageRef = CGImage(width: width,
                           height: height,
                           bitsPerComponent: bitsPerComponent,
                           bitsPerPixel: bytesPerPixel * bitsPerComponent,
                           bytesPerRow: bytesPerRow,
                           space: colorSpace,
                           bitmapInfo: bitmapInfo,
                           provider: providerRef!,
                           decode: nil,
                           shouldInterpolate: true,
                           intent: renderingIntent)
    
    return UIImage(cgImage: imageRef!)
}
```

## 사용 예제

위의 함수를 사용하여 이미지 밝기를 조정하는 예제입니다.
```swift
let originalImage = UIImage(named: "image.jpg")
let adjustedImage = adjustBrightness(image: originalImage, adjustment: 50)
```

## 결론

Swift를 사용하여 이미지의 픽셀 값을 밝기로 조정하는 방법을 알아보았습니다. 이를 활용하여 이미지 처리 앱 등을 개발할 수 있습니다. 자세한 내용은 [Swift 문서](https://docs.swift.org)를 참조하십시오.