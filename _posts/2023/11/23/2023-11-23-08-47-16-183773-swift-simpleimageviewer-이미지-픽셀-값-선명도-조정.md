---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 선명도 조정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지는 대부분 다양한 픽셀 값을 가지고 있으며, 주어진 이미지를 보다 선명하게 만들기 위해 픽셀 값의 조정이 필요할 수 있습니다. Swift에서는 Core Image framework를 사용하여 이미지의 픽셀 값을 수정하고 선명도를 조정할 수 있습니다. 이번 블로그 포스트에서는 Swift를 사용하여 이미지의 픽셀 값 선명도를 조정하는 방법을 알아보겠습니다.

## Core Image framework 소개

Core Image framework는 이미지 및 비디오 처리 및 분석을 위한 강력한 도구 세트를 제공합니다. 이 프레임워크를 사용하면 이미지 필터링, 픽셀 조작, 색상 조정 등 다양한 이미지 처리 작업을 수행할 수 있습니다.

## 이미지 픽셀 값 선명도 조정하기

1. **Core Image Import**: 프로젝트에서 Core Image framework를 import 해야 합니다.
```swift
import CoreImage
```

2. **이미지 로드**: 픽셀 값 선명도를 조정할 이미지를 로드해야 합니다.
```swift
guard let image = UIImage(named: "example_image.jpg") else { return }
```

3. **CIImage 생성**: Core Image framework에서 사용하는 CIImage 객체를 생성합니다.
```swift
guard let ciImage = CIImage(image: image) else { return }
```

4. **선명도 필터 생성**: 이미지의 픽셀 값을 조정하기 위해 `CIColorControls` 필터를 생성합니다.
```swift
let filter = CIFilter(name: "CIColorControls")
filter?.setValue(ciImage, forKey: kCIInputImageKey)
filter?.setValue(1.0, forKey: kCIInputSaturationKey) // 선명도 값 설정 (0.0 - 2.0)
```

5. **선명도 조정**: `CIColorControls` 필터를 적용하여 이미지의 선명도를 조정합니다.
```swift
guard let outputImage = filter?.outputImage else { return }
let context = CIContext(options: nil)
guard let cgImage = context.createCGImage(outputImage, from: outputImage.extent) else { return }
let adjustedImage = UIImage(cgImage: cgImage)
```

6. **조정된 이미지 표시**: 조정된 이미지를 화면에 표시합니다.
```swift
imageView.image = adjustedImage
```

## 전체 코드 예시

```swift
import UIKit
import CoreImage

class ViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 로드
        guard let image = UIImage(named: "example_image.jpg") else { return }
        
        // CIImage 생성
        guard let ciImage = CIImage(image: image) else { return }
        
        // 선명도 필터 생성
        let filter = CIFilter(name: "CIColorControls")
        filter?.setValue(ciImage, forKey: kCIInputImageKey)
        filter?.setValue(1.0, forKey: kCIInputSaturationKey) // 선명도 값 설정 (0.0 - 2.0)
        
        // 선명도 조정
        guard let outputImage = filter?.outputImage else { return }
        let context = CIContext(options: nil)
        guard let cgImage = context.createCGImage(outputImage, from: outputImage.extent) else { return }
        let adjustedImage = UIImage(cgImage: cgImage)
        
        // 조정된 이미지 표시
        imageView.image = adjustedImage
    }
}
```

위의 예시 코드에서 `example_image.jpg`는 선명도를 조정할 대상 이미지의 파일명으로 대체해야 합니다.

## 결론

Swift를 사용하여 이미지의 픽셀 값 선명도를 조정하는 방법에 대해 알아보았습니다. Core Image framework를 이용하면 다양한 이미지 처리 작업을 수행할 수 있으며, 이를 활용하여 이미지를 보다 선명하고 고품질로 표현할 수 있습니다.