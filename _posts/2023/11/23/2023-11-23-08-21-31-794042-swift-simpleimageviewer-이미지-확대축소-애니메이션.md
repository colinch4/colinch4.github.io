---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 확대/축소 애니메이션"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번 포스트에서는 Swift로 간단한 이미지 뷰어를 만들고 이미지를 확대/축소할 때 애니메이션 효과를 적용하는 방법을 알아보겠습니다.

우선, 다음과 같은 코드로 이미지 뷰어를 생성합니다.

```swift
import UIKit

class SimpleImageViewerViewController: UIViewController {
    
    @IBOutlet weak var imageView: UIImageView!
    var image: UIImage?

    override func viewDidLoad() {
        super.viewDidLoad()

        imageView.image = image
        
        // 이미지 뷰어에 제스처 인식기 추가
        let pinchGesture = UIPinchGestureRecognizer(target: self, action: #selector(handlePinchGesture(_:)))
        imageView.addGestureRecognizer(pinchGesture)
        imageView.isUserInteractionEnabled = true
    }

    @objc func handlePinchGesture(_ gestureRecognizer: UIPinchGestureRecognizer) {
        imageView.transform = imageView.transform.scaledBy(x: gestureRecognizer.scale, y: gestureRecognizer.scale)
        gestureRecognizer.scale = 1
    }
}
```

위의 코드에서는 `imageView`를 화면에 표시하고, `pinchGesture`를 사용하여 이미지 확대/축소 제스처를 인식하는 기능을 추가합니다. 제스처가 감지되면 이미지 뷰의 크기를 변경하고, `scale` 속성을 원래 크기인 1로 reset합니다.

이제, SimpleImageViewerViewController를 사용하여 이미지 뷰어를 표시하는 방법을 알아보겠습니다.

```swift
let image = UIImage(named: "example_image")
let imageViewer = SimpleImageViewerViewController()
imageViewer.image = image

self.present(imageViewer, animated: true, completion: nil)
```

위의 코드에서는 `image` 변수에 표시할 이미지를 지정한 뒤, `SimpleImageViewerViewController`의 인스턴스를 생성하고 `image` 변수의 값을 전달합니다. 그리고 `present` 메소드를 사용하여 이미지 뷰어를 표시합니다.

이제, 이미지 뷰어에 애니메이션 효과를 추가해보겠습니다.

```swift
@objc func handlePinchGesture(_ gestureRecognizer: UIPinchGestureRecognizer) {
    UIView.animate(withDuration: 0.1) {
        self.imageView.transform = self.imageView.transform.scaledBy(x: gestureRecognizer.scale, y: gestureRecognizer.scale)
    }
    gestureRecognizer.scale = 1
}
```

위의 코드에서는 `UIView.animate(withDuration:)` 메소드를 사용하여 이미지 뷰의 변환(transform) 속성을 변경하는 애니메이션 효과를 적용합니다. 애니메이션의 지속 시간을 0.1로 설정하고, 이미지 뷰의 크기 변환이 애니메이션되도록 합니다.

이제 간단한 이미지 뷰어를 생성하고 이미지를 확대/축소할 때 애니메이션 효과를 적용하는 방법에 대해 알아보았습니다. 코드를 실행해보고 다양한 이미지 뷰어를 만들어보세요!