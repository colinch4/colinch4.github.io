---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 선명도 조절"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

## 개요
이번에는 Swift를 사용하여 SimpleImageViewer에 이미지의 선명도를 조절하는 방법에 대해 알아보겠습니다. 이미지 선명도 조절은 이미지의 강도나 명암을 조절하여 이미지를 더 선명하게 만들 수 있는 유용한 기능입니다.

## 필요한 라이브러리 가져오기
이미지 선명도를 조절하기 위해서는 Core Image 프레임워크의 CIFilter를 사용해야 합니다. 따라서, 프로젝트에 Core Image 프레임워크를 추가해야 합니다. 

1. 프로젝트 네비게이터에서 프로젝트 파일을 선택합니다.
2. 타겟을 선택합니다.
3. "Build Phases" 탭을 선택합니다.
4. "Link Binary With Libraries" 섹션을 찾아 더하기(+) 버튼을 클릭합니다.
5. CoreImage.framework을 선택하고 "Add" 버튼을 클릭합니다.
6. 변경 사항을 저장합니다.

## 이미지 선명도 조절하기
선명도를 조절하기 위해 CIFilter를 사용할 수 있습니다. 아래의 코드를 참고하여 이미지 선명도를 조절하는 함수를 작성해보겠습니다.

```swift
import CoreImage

func adjustSharpness(for image: UIImage, intensity: Float) -> UIImage? {
    if let ciImage = CIImage(image: image) {
        let filter = CIFilter(name: "CISharpenLuminance")
        filter?.setValue(ciImage, forKey: kCIInputImageKey)
        filter?.setValue(intensity, forKey: kCIInputSharpnessKey)
        
        if let outputImage = filter?.outputImage {
            let context = CIContext(options: nil)
            if let cgImage = context.createCGImage(outputImage, from: outputImage.extent) {
                let sharpImage = UIImage(cgImage: cgImage)
                return sharpImage
            }
        }
    }
    
    return nil
}
```

위의 함수는 입력으로 UIImage와 선명도 강도(intensity)를 받아들이고, 선명도가 적용된 UIImage를 반환합니다. 

## 함수 사용하기
위에서 작성한 함수를 실제로 사용하여 이미지의 선명도를 조절해보겠습니다.

```swift
if let originalImage = UIImage(named: "image.jpg") {
    let sharpenedImage = adjustSharpness(for: originalImage, intensity: 1.5)
    
    if let sharpenedImage = sharpenedImage {
        // 선명도가 조절된 이미지를 사용하여 뷰에 표시합니다.
        imageView.image = sharpenedImage
    }
}
```

위의 코드에서 "image.jpg" 대신 사용하고자 하는 이미지의 파일 이름으로 변경해주어야 합니다. 

## 결론
Swift에서 이미지 선명도를 조절하는 방법에 대해 알아보았습니다. Core Image 프레임워크의 CIFilter를 사용하여 선명도를 조절할 수 있으며, 이를 활용하여 더욱 선명한 이미지를 구현할 수 있습니다.