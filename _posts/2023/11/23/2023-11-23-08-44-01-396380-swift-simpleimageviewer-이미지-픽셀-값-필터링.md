---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 필터링"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 처리는 모바일 앱 개발에서 중요한 부분입니다. 이미지를 보정하거나 특정한 효과를 적용하기 위해서는 이미지의 픽셀 값을 다루어야 합니다. Swift에서는 Core Graphics 프레임워크를 통해 이미지 처리를 간편하게 할 수 있습니다.

이번 포스트에서는 Swift를 사용하여 이미지의 픽셀 값을 필터링하는 방법을 알아보겠습니다.

## 이미지 로딩

처음으로, 이미지를 로딩해야 합니다. Swift에서는 `UIImage` 클래스를 사용하여 이미지를 로드할 수 있습니다. 다음은 이미지를 로딩하는 간단한 예제입니다.

```swift
guard let image = UIImage(named: "example.jpg") else {
    // 이미지 로딩 실패
    return
}

```

위의 예제에서 "example.jpg"는 앱 내에 있는 이미지 파일의 이름을 나타냅니다. 필요에 따라 해당 경로를 수정하여 이미지를 로드할 수 있습니다.

## 이미지 필터링

이미지를 로드한 후에는 필터링을 적용할 수 있습니다. Swift에서는 Core Graphics를 사용하여 이미지의 픽셀 값을 직접 다룰 수 있습니다. 다음은 이미지의 각 픽셀을 반전시키는 간단한 예제입니다.

```swift
guard let cgImage = image.cgImage else {
    // 이미지 변환 실패
    return
}

let width = cgImage.width
let height = cgImage.height

// 픽셀 값을 다루기 위해 픽셀 데이터에 접근합니다.
guard let data = cgImage.dataProvider?.data else {
    // 픽셀 데이터 로딩 실패
    return
}

let pointer = CFDataGetBytePtr(data)

// 픽셀 값 반전
for y in 0..<height {
    for x in 0..<width {
        let index = (y * width + x) * 4 // 각 픽셀은 RGBA 값으로 구성됩니다.
        
        let r = 255 - pointer[index]
        let g = 255 - pointer[index + 1]
        let b = 255 - pointer[index + 2]
        
        pointer[index] = r
        pointer[index + 1] = g
        pointer[index + 2] = b
    }
}

// 변경된 픽셀 값을 가지고 새로운 이미지를 생성합니다.
let context = CGContext(data: pointer, width: width, height: height, bitsPerComponent: 8, bytesPerRow: width * 4, space: CGColorSpaceCreateDeviceRGB(), bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue)

guard let newImage = context?.makeImage() else {
    // 이미지 생성 실패
    return
}

let filteredImage = UIImage(cgImage: newImage)
```

위의 예제에서는 각 픽셀의 RGBA 값을 반전시켜 이미지를 필터링합니다. 필요한 경우 다른 필터링 알고리즘을 적용하거나 원하는 효과를 구현할 수 있습니다.

## 이미지 출력

위에서 필터링한 이미지를 출력하기 위해서는 UIImageView를 사용하면 됩니다. 다음은 필터링된 이미지를 UIImageView에 출력하는 예제입니다.

```swift
let imageView = UIImageView(image: filteredImage)
imageView.frame = CGRect(x: 0, y: 0, width: 300, height: 300)
view.addSubview(imageView)
```

위의 예제에서는 필터링된 이미지를 imageView에 할당하고, 화면에 출력합니다. 필요시 imageView의 frame을 조정하여 이미지의 위치와 크기를 조절할 수 있습니다.

## 결론

이번 포스트에서는 Swift를 사용하여 이미지의 픽셀 값을 필터링하는 방법을 알아보았습니다. 이미지 처리는 모바일 앱에서 중요한 기능으로 활용되기 때문에, 필요한 경우 다양한 이미지 처리 기법을 익히는 것이 유용합니다. Core Graphics를 사용하여 이미지 처리를 할 수 있기 때문에, 다양한 필터링 알고리즘을 구현하여 원하는 효과를 적용할 수 있습니다.