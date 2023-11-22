---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 채도 필터"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번에는 Swift로 간단한 이미지 뷰어를 만들어보고, 이 이미지에 채도 필터를 적용하는 방법을 알아보겠습니다. 채도 필터는 이미지의 채도 값을 조절하여 이미지의 색감을 변경하는 기능입니다.

## SimpleImageViewer 클래스 만들기

```swift
import UIKit

class SimpleImageViewer: UIImageView {
    
    // 이미지 채도 필터 메서드
    func applySaturationFilter(saturation: CGFloat) {
        // 이미지 채도 필터 적용
        let context = CIContext(options: nil)
        if let currentFilter = CIFilter(name: "CIColorControls") {
            let currentCIImage = CIImage(cgImage: self.image!.cgImage!)
            currentFilter.setValue(currentCIImage, forKey: kCIInputImageKey)
            currentFilter.setValue(saturation, forKey: kCIInputSaturationKey)
            
            if let output = currentFilter.outputImage {
                if let cgImage = context.createCGImage(output, from: output.extent) {
                    let processedImage = UIImage(cgImage: cgImage)
                    self.image = processedImage
                }
            }
        }
    }
}
```

위의 코드는 `SimpleImageViewer` 클래스를 정의한 것입니다. 이 클래스는 `UIImageView`를 상속받아 이미지를 표시하고, 채도 필터를 적용하는 기능을 제공합니다.

## 채도 필터 적용하기

```swift
let imageView = SimpleImageViewer(frame: CGRect(x: 0, y: 0, width: 300, height: 300))
imageView.image = UIImage(named: "sample_image")
imageView.applySaturationFilter(saturation: 1.5)

// 이미지 뷰를 화면에 표시
view.addSubview(imageView)
```

위의 코드는 `SimpleImageViewer`를 이용하여 이미지 뷰를 생성하고, 이미지를 로드한 후에 채도 값을 지정하여 적용하는 예시입니다. `applySaturationFilter` 메서드를 호출하여 채도 필터를 적용하면 이미지의 색감이 변경됩니다.

## 결론

이번에는 Swift로 간단한 이미지 뷰어를 만들고, 해당 뷰어에 채도 필터를 적용하는 방법을 알아보았습니다. 이미지 처리에 대한 다양한 기능을 활용하여 다양한 효과를 낼 수 있으므로, 창의적인 이미지 처리 앱을 개발할 때 유용하게 활용할 수 있습니다.

> 참고: [Apple Developer Documentation](https://developer.apple.com/documentation/coreimage)

이 글은 [Swift SimpleImageViewer 이미지 채도 필터](https://www.example.com/swift-simpleimageviewer-image-saturation-filter)에서 보여준 예시를 기반으로 작성되었습니다.