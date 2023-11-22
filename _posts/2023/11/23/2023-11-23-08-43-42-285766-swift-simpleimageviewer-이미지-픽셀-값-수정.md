---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 수정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift로 이미지 픽셀 값을 수정하는 방법을 알아보겠습니다. 이를 위해 SimpleImageViewer라는 간단한 이미지 뷰어 프로젝트를 사용하겠습니다.

## SimpleImageViewer 프로젝트 설정

먼저 SimpleImageViewer 프로젝트를 생성합니다. Xcode에서 "New Project"를 선택하고 "Single View App" 템플릿을 선택합니다.

![Xcode 프로젝트 생성](xcode_project.png)

## UIImageView 추가

Storyboard에서 ViewController에 UIImageView를 추가합니다. UIImageView의 IBOutlet을 ViewController와 연결합니다. IBOutlet을 사용하기 위해 ViewController 클래스에 다음 코드를 추가합니다.

```swift
@IBOutlet weak var imageView: UIImageView!
```
  
## 이미지 로드

ViewController의 viewDidLoad 함수에서 이미지를 로드하고 UIImageView에 표시합니다. 다음은 이미지를 로드하는 간단한 예입니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    if let image = UIImage(named: "image.png") {
        imageView.image = image
    }
}
```

## 이미지 픽셀 값 수정하기

이미지 픽셀을 수정하려면 Core Graphics를 사용해야 합니다. 다음은 이미지 픽셀 값을 수정하는 함수를 추가한 예입니다.

```swift
func modifyPixelValue(image: UIImage, x: Int, y: Int) -> UIImage? {
    guard let cgImage = image.cgImage else {
        return nil
    }

    let width = cgImage.width
    let height = cgImage.height

    let bytesPerPixel = 4
    let bytesPerRow = bytesPerPixel * width
    let bitsPerComponent = 8

    let imageData = UnsafeMutablePointer<UInt8>.allocate(capacity: bytesPerRow * height)

    let colorSpace = CGColorSpaceCreateDeviceRGB()

    let bitmapInfo = CGBitmapInfo(
        rawValue: CGImageAlphaInfo.premultipliedLast.rawValue
    )

    let context = CGContext(
        data: imageData,
        width: width,
        height: height,
        bitsPerComponent: bitsPerComponent,
        bytesPerRow: bytesPerRow,
        space: colorSpace,
        bitmapInfo: bitmapInfo.rawValue
    )

    context?.draw(cgImage, in: CGRect(x: 0, y: 0, width: width, height: height))

    let data = context?.data

    if let data = data {
        let pointer = data.bindMemory(
            to: UInt32.self, 
            capacity: width * height
        )

        let index = y * width + x
        pointer[index] = 0xFF0000FF
    }

    if let newCGImage = context?.makeImage() {
        let newImage = UIImage(cgImage: newCGImage)
        return newImage
    }

    return nil
}
```
위의 함수는 x, y 좌표에 해당하는 이미지 픽셀을 빨간색으로 수정하는 예입니다. x와 y 값을 원하는 좌표로 변경하여 특정 위치의 픽셀을 수정할 수 있습니다.

## 사용 예제

ViewController의 viewDidLoad 함수에서  이미지 픽셀 값을 수정한 후 변경된 이미지를 출력할 수 있습니다.

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    if let image = UIImage(named: "image.png") {
        let modifiedImage = modifyPixelValue(image: image, x: 100, y: 200)
        imageView.image = modifiedImage
    }
}
```

이제 SimpleImageViewer 프로젝트에서 이미지 픽셀 값을 수정하는 방법을 알게 되었습니다. 지정한 좌표의 픽셀을 원하는 값으로 변경하여 이미지를 수정할 수 있습니다.