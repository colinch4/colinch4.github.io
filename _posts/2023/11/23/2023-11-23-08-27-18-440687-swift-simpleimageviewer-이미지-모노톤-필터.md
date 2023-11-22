---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 모노톤 필터"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift에서는 UIKit을 사용하여 이미지를 모노톤 필터로 변환할 수 있습니다. 모노톤 이미지는 흑백 이미지로 변환되어 색상이 제거되고 명암만 남게 됩니다. 이번 블로그 포스트에서는 Swift를 사용하여 이미지를 모노톤으로 변환하는 간단한 ImageViewer를 만들어보겠습니다.

## Prerequisites

- Swift 프로젝트를 생성하고 개발 환경을 설정합니다.
- 이미지 파일을 준비합니다.

## 이미지 모노톤 필터 적용

1. Xcode에서 새로운 Swift 프로젝트를 생성합니다.

2. ViewController.swift 파일을 열고, `import UIKit`을 추가합니다.

3. ImageViewer 클래스를 정의합니다.

```swift
class ImageViewer: UIViewController {

    @IBOutlet weak var imageView: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 파일 이름을 입력해주세요.
        let imageName = "myImage.jpg"
        
        // 이미지 파일을 가져와서 imageView에 표시합니다.
        if let image = UIImage(named: imageName) {
            imageView.image = image
        }
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
}
```

4. Storyboard에서 View Controller의 클래스를 `ImageViewer`로 설정합니다.

5. 모노톤 필터를 적용하기 위해 `UIImageView`의 `image` 속성을 수정해야 합니다. `viewDidLoad` 메서드 내에서 모노톤 필터를 적용시켜보겠습니다.

```swift
class ImageViewer: UIViewController {

    @IBOutlet weak var imageView: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()

        // 이미지 파일 이름을 입력해주세요.
        let imageName = "myImage.jpg"

        // 이미지 파일을 가져와서 imageView에 표시합니다.
        if let image = UIImage(named: imageName) {
            let monochromeImage = convertToMonochrome(image)
            imageView.image = monochromeImage
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    
    // 이미지를 모노톤으로 변환하는 함수
    private func convertToMonochrome(_ image: UIImage) -> UIImage {
        let context = CIContext(options: nil)
        if let currentFilter = CIFilter(name: "CIPhotoEffectMono") {
            let beginImage = CIImage(image: image)
            currentFilter.setValue(beginImage, forKey: kCIInputImageKey)

            if let output = currentFilter.outputImage,
               let cgimg = context.createCGImage(output, from: output.extent) {
                return UIImage(cgImage: cgimg)
            }
        }
        return UIImage()
    }
}
```

6. 앱을 실행하고, 이미지 파일이 표시된 후 모노톤으로 변환되는지 확인합니다.

## 결론

이번에는 Swift를 사용하여 이미지를 모노톤 필터로 변환하는 간단한 ImageViewer를 만들어보았습니다. 모노톤 필터를 이용하면 이미지를 흑백으로 변환하여 독특한 시각적 효과를 낼 수 있습니다. Swift에서 이미지 필터를 적용하는 방법에 대해 알아봤으니 이를 응용하여 더 다양한 이미지 효과를 구현해보세요.

## 참고 자료

- [Apple Developer Documentation - Core Image Filters](https://developer.apple.com/documentation/coreimage/cifilter)