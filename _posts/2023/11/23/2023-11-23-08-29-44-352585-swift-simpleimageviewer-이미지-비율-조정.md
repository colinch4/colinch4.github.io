---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 비율 조정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

Swift로 개발된 iOS 앱에서 이미지를 표시하는 경우, 이미지의 비율을 적절하게 조정하는 것은 중요한 부분입니다. 사용자가 이미지를 제대로 볼 수 있도록 이미지를 화면에 맞게 조절하는 작업을 해야합니다.

이 글에서는 Swift로 간단한 이미지 뷰어를 구현하고, 이미지의 비율을 조정하는 방법에 대해 알아보겠습니다.

## 이미지 뷰어 구현하기

먼저, 이미지 뷰어를 구현하기 위해 `UIImageView`를 사용할 것입니다. 아래 코드는 이미지를 로드하고 이미지 뷰에 설정하는 기본적인 예제입니다.

```swift
import UIKit

class ImageViewController: UIViewController {
    
    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 로드
        guard let image = UIImage(named: "image_name") else {
            return
        }
        
        // 이미지 뷰에 이미지 설정
        imageView.image = image
    }
}
```

위의 코드에서 `imageView`는 `UIImageView`의 인스턴스입니다. `viewDidLoad()` 메서드에서 이미지를 로드하고, 이미지 뷰에 설정합니다. 이제 이미지의 비율을 조정하는 방법을 알아보겠습니다.

## 이미지 비율 조정하기

이미지 비율을 조정하는 방법에는 여러 가지가 있지만, 가장 간단한 방법은 `UIView.ContentMode` 속성을 사용하는 것입니다. 해당 속성을 설정하면 이미지가 뷰 내에서 어떻게 표시될지 결정할 수 있습니다.

```swift
// 이미지 뷰의 contentMode 설정
imageView.contentMode = .scaleAspectFit
```

위의 코드에서 `.scaleAspectFit`은 이미지가 뷰 내에서 비율을 유지하면서 화면에 맞게 조정됨을 의미합니다. 다른 옵션으로는 `.scaleAspectFill`, `.scaleToFill` 등이 있습니다. 각각의 옵션에 따라 이미지의 비율이 다르게 조정됩니다.

이제 이미지 뷰어에서 이미지의 비율을 조정하는 방법을 알아보았습니다. `UIImageView`의 `contentMode` 속성을 사용하여 이미지를 화면에 적절하게 표시할 수 있습니다.

이 글을 통해 Swift로 이미지 뷰어를 구현하고 이미지의 비율을 조정하는 방법에 대해 살펴보았습니다. 참고로, 더 많은 옵션과 기능을 사용하고 싶다면 Apple의 공식 문서를 참조하시기 바랍니다.

## 참고 자료

- [Apple Developer Documentation](https://developer.apple.com/documentation/uikit/uiimageview)