---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 흑백 변환"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지를 흑백으로 변환하는 기능은 Swift에서 간단히 구현할 수 있습니다. 이번 포스트에서는 `UIImageView`를 사용하여 이미지를 표시하고, 해당 이미지를 흑백으로 변환하는 방법을 알아보겠습니다.

## Step 1: UIImageView 생성

먼저, 흑백으로 변환할 이미지를 표시하기 위해 `UIImageView` 객체를 생성해야 합니다. 아래는 이미지를 표시할 `UIImageView`를 생성하는 코드입니다.

```swift
let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
imageView.contentMode = .scaleAspectFit
view.addSubview(imageView)
```

위 코드에서는 `UIImageView`를 생성하고, 프레임을 설정하여 화면에 표시될 크기를 지정합니다. 또한 `contentMode`를 `.scaleAspectFit`으로 설정하여 이미지의 비율을 유지하며 이미지뷰에 표시되도록 합니다. 마지막으로 `imageView`를 뷰에 추가합니다.

## Step 2: 이미지 로드

이제 `UIImageView`에 이미지를 로드해야 합니다. 로드할 이미지는 `UIImage` 객체로 생성하고, `UIImageView`의 `image` 속성에 할당합니다. 아래는 이미지를 로드하는 코드입니다.

```swift
if let image = UIImage(named: "image.jpg") {
    imageView.image = image
}
```

위 코드에서는 `UIImage` 객체를 생성하고, `named:` 파라미터를 통해 이미지 파일의 이름을 전달합니다. 로드한 이미지를 `imageView`의 `image` 속성에 할당하여 이미지를 표시합니다.

## Step 3: 이미지 흑백 변환

이제 이미지를 흑백으로 변환하는 함수를 구현해보겠습니다. 아래는 이미지를 흑백으로 변환하는 함수의 코드입니다.

```swift
func convertToGrayScale(image: UIImage) -> UIImage? {
    let imageRect = CGRect(origin: .zero, size: image.size)
    
    let colorSpace = CGColorSpaceCreateDeviceGray()
    let context = CGContext(data: nil, width: Int(image.size.width),
                            height: Int(image.size.height),
                            bitsPerComponent: 8, bytesPerRow: 0,
                            space: colorSpace, bitmapInfo: CGImageAlphaInfo.none.rawValue)
    
    context?.draw(image.cgImage!, in: imageRect)
    
    let grayscaleImage = context?.makeImage().flatMap { UIImage(cgImage: $0) }
    
    return grayscaleImage
}
```

위 코드에서는 이미지의 사이즈를 기반으로 `CGRect`를 생성하고, `CGColorSpaceCreateDeviceGray()`를 사용하여 흑백 `CGColorSpace`를 생성합니다. 또한 `CGContext`를 생성하여 이미지를 흑백으로 변환합니다. 마지막으로 변환한 흑백 이미지를 `UIImage`로 생성하여 반환합니다.

## Step 4: 이미지 흑백 변환 적용

이제 함수를 사용하여 이미지를 흑백으로 변환해보겠습니다. 아래는 이미지를 흑백으로 변환하는 코드입니다.

```swift
if let originalImage = imageView.image,
   let grayscaleImage = convertToGrayScale(image: originalImage) {
    imageView.image = grayscaleImage
}
```

위 코드에서는 `imageView`에 표시된 이미지를 가져와 `convertToGrayScale(image:)` 함수를 사용하여 이미지를 흑백으로 변환합니다. 변환한 이미지를 다시 `imageView`의 `image` 속성에 할당하여 흑백 이미지가 표시되도록 합니다.

## 결론

Swift에서 이미지를 흑백으로 변환하는 방법을 알아보았습니다. `UIImageView`를 사용하여 이미지를 표시하고, 함수를 구현하여 이미지를 흑백으로 변환할 수 있습니다. 흑백 이미지를 사용하면 다양한 시각 효과를 적용할 수 있으며, 이미지 처리에 유용하게 사용할 수 있습니다.