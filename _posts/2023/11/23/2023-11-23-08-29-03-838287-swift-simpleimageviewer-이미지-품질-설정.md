---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 품질 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 뷰어는 iOS 앱에서 이미지를 표시하고 사용자에게 보여주는 데 사용되는 중요한 구성 요소입니다. 앱에서 이미지를 로드하고 표시할 때 이미지의 품질을 설정하는 것은 사용자 경험에 영향을 미치는 중요한 사항입니다.

이번 포스트에서는 Swift를 사용하여 이미지 뷰어에서 이미지의 품질을 설정하는 방법을 알아보겠습니다.

## 1. 이미지 품질 설정하기

Swift에서 이미지 품질을 설정하는 방법 중 가장 일반적인 방법은 이미지를 로드하고 표시할 때 사용하는 `UIImage` 객체의 `UIImage(named: String, in: Bundle?, compatibleWith: UITraitCollection?)` 메서드를 사용하는 것입니다.

```swift
// 이미지 뷰어에서 이미지 로드하기
if let image = UIImage(named: "image_name") {
    // 이미지 품질 설정하기
    let scaledImage = UIImage(data: image.jpegData(compressionQuality: 0.5)!)
    
    // 이미지 뷰에 이미지 설정하기
    imageView.image = scaledImage
} else {
    // 이미지 로드 실패 시 처리 로직
    print("이미지 로드 실패")
}
```

위의 예시 코드에서는 `UIImage(named:in:compatibleWith:)` 메서드를 사용하여 이미지를 로드하고, `jpegData(compressionQuality:)` 메서드를 사용하여 이미지의 품질을 설정합니다. `compressionQuality` 매개변수는 0에서 1 사이의 값을 가지며, 낮은 값일수록 압축률이 높아져 이미지 품질이 낮아집니다. 반대로 높은 값일수록 이미지 품질은 더욱 우수하지만 파일 크기가 커집니다.

이렇게 이미지 품질을 설정한 후, `imageView`와 같은 이미지 뷰에 설정된 이미지를 표시할 수 있습니다.

## 2. 참고 자료

- [UIImage - Apple Developers Documentation](https://developer.apple.com/documentation/uikit/uiimage)
- [Image Compression and Decompression - Apple Developers Documentation](https://developer.apple.com/documentation/coregraphics/image_compression_and_decompression)