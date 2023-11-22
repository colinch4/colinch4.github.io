---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 밝기 조절"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지를 표시하고 조작하는 기능은 Swift 애플리케이션에서 중요한 부분입니다. 이 글에서는 Swift를 사용하여 이미지의 밝기를 조절하는 방법을 알아보겠습니다.

## 1. 이미지 로드하기

먼저, 이미지를 로드하는 방법부터 알아보겠습니다. Swift에서는 `UIImage` 클래스를 사용하여 이미지를 로드할 수 있습니다. 아래의 코드는 `UIImageView`에 이미지를 로드하는 예제입니다.

```swift
import UIKit

class ViewController: UIViewController {
    
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        if let image = UIImage(named: "example") {
            imageView.image = image
        }
    }
}
```

위의 코드에서 `example`은 앱 내에 있는 이미지 파일의 이름입니다. 해당 이미지 파일은 프로젝트의 리소스에 추가되어 있어야 합니다. `imageView.image`에 이미지를 할당하여 이미지 뷰에 이미지를 표시할 수 있습니다.

## 2. 이미지 밝기 조절하기

이제, 이미지의 밝기를 조절하는 방법을 알아보겠습니다. 이미지의 밝기를 조절하기 위해서는 이미지의 픽셀 값을 수정해야 합니다. Swift에서 `CoreImage` 프레임워크를 사용하여 이미지의 픽셀 값을 조절할 수 있습니다.

```swift
import UIKit
import CoreImage

class ImageProcessor {
    
    static func adjustBrightness(for image: UIImage, brightness: CGFloat) -> UIImage? {
        guard let ciImage = CIImage(image: image) else { return nil }
        
        let filter = CIFilter(name: "CIColorControls")
        filter?.setValue(ciImage, forKey: kCIInputImageKey)
        filter?.setValue(brightness, forKey: kCIInputBrightnessKey)
        
        if let outputImage = filter?.outputImage {
            let context = CIContext(options: nil)
            if let cgImage = context.createCGImage(outputImage, from: outputImage.extent) {
                let adjustedImage = UIImage(cgImage: cgImage)
                return adjustedImage
            }
        }
        return nil
    }
}

class ViewController: UIViewController {
    
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        if let originalImage = UIImage(named: "example") {
            let adjustedImage = ImageProcessor.adjustBrightness(for: originalImage, brightness: 0.5)
            imageView.image = adjustedImage
        }
    }
}
```

위의 코드에서 `adjustBrightness` 메서드는 입력된 이미지의 밝기를 조절하는 역할을 합니다. `CIFilter`를 사용하여 `inputBrightness` 키를 이용하여 이미지의 밝기를 수정합니다. 마지막으로 조절된 이미지를 반환합니다. `originalImage`를 `adjustBrightness` 메서드에 전달하여 밝기가 조절된 이미지를 받고, 이를 `imageView.image`에 할당하여 표시합니다.

## 결론

Swift를 사용하여 이미지의 밝기를 조절하는 방법에 대해 알아보았습니다. `CIColorControls` 필터와 `kCIInputBrightnessKey`를 활용하여 이미지의 밝기를 조절할 수 있습니다. 이를 응용하여 이미지를 다양한 방식으로 조작할 수 있습니다. 자세한 내용은 [Apple Developer Documentation](https://developer.apple.com/documentation/coreimage/cifilter)에서 확인할 수 있습니다.