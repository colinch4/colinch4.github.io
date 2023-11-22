---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 회전 제스처"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번 예시에서는 Swift로 간단한 이미지 뷰어를 만들고, 이미지를 회전시키기 위한 제스처를 구현하는 방법을 알아보겠습니다.

### 1. UIImageView 생성

먼저, 이미지 뷰를 생성하여 화면에 표시하는 코드를 작성합니다.

```swift
let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
imageView.image = UIImage(named: "exampleImage")
self.view.addSubview(imageView)
```

### 2. UITapGestureRecognizer 추가

이미지 뷰에 회전 제스처를 추가하기 위해 UITapGestureRecognizer를 생성하고 이미지 뷰에 추가합니다.

```swift
let rotateGesture = UIRotationGestureRecognizer(target: self, action: #selector(handleRotate(_:)))
imageView.isUserInteractionEnabled = true
imageView.addGestureRecognizer(rotateGesture)
```

### 3. 회전 제스처 처리

회전 제스처 처리를 위한 핸들러 함수를 작성합니다. 이 함수에서 이미지 회전을 구현할 수 있습니다.

```swift
@objc func handleRotate(_ gestureRecognizer: UIRotationGestureRecognizer) {
    if let view = gestureRecognizer.view {
        view.transform = view.transform.rotated(by: gestureRecognizer.rotation)
        gestureRecognizer.rotation = 0
    }
}
```

회전 제스처가 감지되면 이미지 뷰의 변형(transform)을 변경하여 이미지를 회전시킵니다. 회전 각도는 gestureRecognizer.rotation을 통해 가져옵니다.

### 전체 코드

```swift
import UIKit

class ViewController: UIViewController {
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        let imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 200, height: 200))
        imageView.image = UIImage(named: "exampleImage")
        self.view.addSubview(imageView)
        
        let rotateGesture = UIRotationGestureRecognizer(target: self, action: #selector(handleRotate(_:)))
        imageView.isUserInteractionEnabled = true
        imageView.addGestureRecognizer(rotateGesture)
    }
    
    @objc func handleRotate(_ gestureRecognizer: UIRotationGestureRecognizer) {
        if let view = gestureRecognizer.view {
            view.transform = view.transform.rotated(by: gestureRecognizer.rotation)
            gestureRecognizer.rotation = 0
        }
    }
}
```

위의 코드를 사용하여 간단한 이미지 뷰어를 만들고, 이미지를 회전시키는 제스처를 구현할 수 있습니다.

참고 자료:
- [Apple Developer Documentation - UIImageView](https://developer.apple.com/documentation/uikit/uiimageview)
- [Apple Developer Documentation - UITapGestureRecognizer](https://developer.apple.com/documentation/uikit/uitapgesturerecognizer)
- [Apple Developer Documentation - UIRotationGestureRecognizer](https://developer.apple.com/documentation/uikit/uirotationgesturerecognizer)