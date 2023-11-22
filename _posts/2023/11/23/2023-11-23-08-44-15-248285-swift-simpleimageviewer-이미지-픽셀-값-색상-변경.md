---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 픽셀 값 색상 변경"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift에서는 이미지 뷰어를 만들고 이미지의 픽셀 값을 변경하여 색상을 바꿀 수 있습니다. 이를 위해 Core Graphics 프레임워크를 사용할 것입니다.

먼저, 이미지 뷰어를 만들기 위해 `UIImageView`를 사용합니다. 이미지 뷰어를 생성하고 이미지를 설정하는 코드는 다음과 같습니다.

```swift
import UIKit

class SimpleImageViewer: UIViewController {
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let image = UIImage(named: "example_image")
        imageView.image = image
    }
}
```

위 코드에서 `UIImageView`의 `image` 속성을 원하는 이미지로 설정합니다. 이미지 파일은 `Assets.xcassets`에 추가되어 있어야 합니다.

그다음, 이미지의 픽셀 값을 변경하여 색상을 바꾸는 함수를 구현해야 합니다. 이를 위해 Core Graphics의 `CGContext`를 사용할 것입니다. 아래의 코드를 `SimpleImageViewer` 클래스에 추가합니다.

```swift
func changeImageColor() {
    guard let image = imageView.image else { return }
    
    let size = image.size
    let rect = CGRect(origin: .zero, size: size)
    
    UIGraphicsBeginImageContextWithOptions(size, false, UIScreen.main.scale)
    guard let context = UIGraphicsGetCurrentContext() else { return }
    
    let cgImage = image.cgImage!
    context.draw(cgImage, in: rect)
    
    context.setBlendMode(.overlay)
    context.setFillColor(UIColor.red.cgColor)
    context.fill(rect)
    
    guard let newImage = UIGraphicsGetImageFromCurrentImageContext() else { return }
    UIGraphicsEndImageContext()
    
    imageView.image = newImage
}
```

위의 `changeImageColor` 함수는 먼저 이미지의 크기를 가져와서 `CGContext`를 생성합니다. 그런 다음, `draw` 메서드를 사용하여 이미지를 `CGContext`에 그립니다. 그리고 `setBlendMode` 메서드와 `setFillColor` 메서드를 사용하여 색상을 설정합니다. 여기에서는 빨간색으로 설정했습니다. 마지막으로 `UIGraphicsGetImageFromCurrentImageContext` 메서드를 사용하여 변경된 이미지를 가져온 다음, 이미지 뷰어의 이미지로 설정합니다.

위에서 구현한 함수를 호출하는 방법은 해당 기능을 사용하고자 하는 곳에서 `SimpleImageViewer` 클래스의 인스턴스를 생성한 다음, `changeImageColor` 메서드를 호출하면 됩니다.

이렇게 Swift에서 이미지 뷰어를 만들고 이미지의 픽셀 값을 변경하여 색상을 바꾸는 방법을 알아보았습니다. Core Graphics를 사용하면 다양한 이미지 처리 작업을 할 수 있으니 참고하시기 바랍니다.

참고 자료:
- [Apple Developer Documentation - Core Graphics](https://developer.apple.com/documentation/coregraphics)
- [Apple Developer Documentation - UIImage](https://developer.apple.com/documentation/uikit/uiimage)