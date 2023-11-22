---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 반전"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번에는 Swift로 간단한 이미지 뷰어를 만들어보고, 이미지의 픽셀 값을 반전시켜 보겠습니다.

### 개요

이미지 뷰어는 이미지 파일을 로드하여 화면에 표시하는 기능을 가지고 있습니다. 이번 예제에서는 UIImage와 UIImageView를 사용하여 이미지를 로드하고 보여줄 것입니다. 또한, 이미지의 픽셀 값을 반전시키는 기능도 추가할 것입니다.

### 단계별 진행

1. 프로젝트 생성 및 이미지 추가

   Xcode를 열고 새로운 iOS 프로젝트를 생성합니다. 생성한 프로젝트에 이미지 파일을 추가합니다. 이미지파일은 Assets.xcassets에 추가하는 것을 권장합니다. 예를 들어, "sample_image.png"라는 이미지 파일을 추가한다고 가정하겠습니다.

2. 이미지 뷰어 화면 구성

   Storyboard에서 UIViewController를 선택하고, UIImageView를 추가합니다. 추가한 UIImageView의 크기를 조정하고, 적절한 AutoLayout 제약을 설정합니다. UIImageView에 Identifier를 부여하여 코드에서 참조할 수 있도록 합니다.

3. 이미지 로드 및 표시

   뷰컨트롤러의 viewDidLoad() 메서드에서 이미지를 로드하고 UIImageView에 표시하는 코드를 추가합니다. 예를 들어, "sample_image.png"를 로드하고 "imageView"에 표시한다고 가정하겠습니다.

   ```swift
   override func viewDidLoad() {
       super.viewDidLoad()

       if let image = UIImage(named: "sample_image.png") {
           imageView.image = image
       }
   }
   ```

4. 이미지 픽셀 반전 기능 추가

   이미지를 픽셀 값으로 반전시키는 기능을 추가할 수 있습니다. UIImage에는 grayscale 및 alpha 값을 반전시키는 메서드가 있는데, 이를 활용하여 이미지 픽셀 값을 반전시킬 수 있습니다.  반전된 이미지를 다시 UIImageView에 표시하는 코드를 추가합니다.

   ```swift
   func invertImageColors() {
       if let image = imageView.image {
           if let invertedImage = CIFilter(name: "CIColorInvert")?.outputImage {
               let context = CIContext(options: nil)
               if let cgImage = context.createCGImage(invertedImage, from: invertedImage.extent) {
                   let invertedUIImage = UIImage(cgImage: cgImage)
                   imageView.image = invertedUIImage
               }
           }
       }
   }
   ```

5. 이미지 반전 기능 호출

   이미지를 반전시키는 기능은 사용자가 특정 이벤트를 발생시킬 때 호출되도록 설정할 수 있습니다. 예를 들어, UIButton을 추가하고 버튼을 클릭하면 이미지를 반전시키는 기능을 호출하도록 설정합니다.

   ```swift
   @IBAction func invertButtonTapped(_ sender: UIButton) {
       invertImageColors()
   }
   ```

위의 단계를 따라 하면 이미지 뷰어를 만들고, 이미지의 픽셀 값을 반전시킬 수 있는 기능을 추가할 수 있습니다.

### 참고 자료

- [Apple Developer Documentation - UIImage](https://developer.apple.com/documentation/uikit/uiimage)
- [Apple Developer Documentation - UIImageView](https://developer.apple.com/documentation/uikit/uiimageview)
- [Apple Developer Documentation - Core Image](https://developer.apple.com/documentation/coreimage)
- [Stack Overflow - How to invert colors of an image in Swift?](https://stackoverflow.com/questions/30696307/how-to-invert-colors-of-an-image-in-swift)

### 결론

Swift를 사용하여 간단한 이미지 뷰어를 만들고, 이미지의 픽셀 값을 반전시켜봤습니다. 이러한 방식을 사용하여 이미지 처리 기능을 추가할 수 있으며, Core Image의 다양한 필터를 사용하여 더 다양한 이미지 처리를 할 수 있습니다.