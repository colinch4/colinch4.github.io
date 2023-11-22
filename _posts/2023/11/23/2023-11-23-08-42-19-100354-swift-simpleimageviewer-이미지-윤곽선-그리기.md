---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 윤곽선 그리기"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지를 로드하고 윤곽선을 그리는 것은 Swift에서 매우 간단합니다. 이 기능은 `UIGraphicsImageRenderer` 클래스를 사용하여 이미지에서 윤곽선을 그릴 수 있습니다.

```swift
import UIKit

func drawOutline(on image: UIImage) -> UIImage {
    let renderer = UIGraphicsImageRenderer(size: image.size)
    let outputImage = renderer.image { context in
        image.draw(at: CGPoint.zero)
        context.cgContext.setStrokeColor(UIColor.red.cgColor)
        context.cgContext.setLineWidth(2)
        context.cgContext.addRect(CGRect(x: 10, y: 10, width: image.size.width - 20, height: image.size.height - 20))
        context.cgContext.drawPath(using: .stroke)
    }
    return outputImage
}

// 사용 예시
let originalImage = UIImage(named: "example-image")
let imageWithOutline = drawOutline(on: originalImage)
```

위의 코드는 `drawOutline(on:)` 함수를 정의하여 입력 이미지 위에 빨간색 윤곽선을 그립니다. 이미지의 크기에 맞춰 `UIGraphicsImageRenderer`를 생성하고, 그리기 작업을 위한 컨텍스트에서 이미지를 그립니다. 그리기 작업에서 빨간색으로 선의 색상과 두께를 지정한 후, 원하는 영역에 사각형을 그려 윤곽선을 만듭니다.

이미지 윤곽선을 그리는 데 사용되는 좌표와 크기를 조정하여 원하는 모양과 위치로 윤곽선을 그릴 수 있습니다.

자세한 내용은 [Official Apple Documentation](https://developer.apple.com/documentation/uikit/uigraphicsimagerenderer)을 참조하세요.