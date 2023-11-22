---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 회전 애니메이션"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이미지 회전 애니메이션을 구현하여 간단한 이미지 뷰어를 만들어봅시다. Swift 언어를 사용하여 작성하겠습니다.

### 1. 이미지 뷰어 구현

먼저, 이미지 뷰어를 위한 기본적인 뷰를 생성합니다. 다음과 같이 `UIImageView`와 `UIButton`을 이용하여 뷰를 구성합니다.

```swift
import UIKit

class SimpleImageViewerViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!
    @IBOutlet weak var rotateButton: UIButton!
    
    var image: UIImage?
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        imageView.image = image
    }
    
    @IBAction func rotateButtonTapped(_ sender: UIButton) {
        rotateImage()
    }
    
    func rotateImage() {
        UIView.animate(withDuration: 0.5, animations: {
            self.imageView.transform = CGAffineTransform(rotationAngle: CGFloat.pi)
        }) { (_) in
            UIView.animate(withDuration: 0.5, animations: {
                self.imageView.transform = CGAffineTransform(rotationAngle: 0)
            })
        }
    }
}
```

### 2. 이미지 뷰어 사용

위에서 구현한 `SimpleImageViewerViewController`를 사용하여 이미지 뷰어 화면을 보여줄 수 있습니다. 다음과 같이 이미지 뷰어를 띄우기 위한 코드를 작성합니다.

```swift
// 이미지 뷰어 뷰 컨트롤러 인스턴스 생성
let imageViewerVC = UIStoryboard(name: "Main", bundle: nil).instantiateViewController(withIdentifier: "SimpleImageViewerViewController") as! SimpleImageViewerViewController

// 이미지 설정
let image = UIImage(named: "exampleImage")
imageViewerVC.image = image

// 이미지 뷰어 화면 표시
self.present(imageViewerVC, animated: true, completion: nil)
```

위의 코드에서 `"exampleImage"` 대신에 실제 이미지의 이름을 사용하시면 됩니다.

### 3. 동작 확인

앱을 실행시켜 이미지 뷰어 화면으로 이동하고, 회전 버튼(`rotateButton`)을 터치하면 이미지가 180도 회전한 뒤 다시 원래대로 돌아오는 애니메이션이 동작하는지 확인해보세요.

이렇게 간단한 이미지 회전 애니메이션을 구현하여 이미지 뷰어를 만들 수 있습니다.

### 참고 자료

- [Apple Developer Documentation - CGAffineTransform](https://developer.apple.com/documentation/coregraphics/cgaffinetransform)
- [Apple Developer Documentation - UIView](https://developer.apple.com/documentation/uikit/uiview)
- [Apple Developer Documentation - UIImageView](https://developer.apple.com/documentation/uikit/uiimageview)
- [Apple Developer Documentation - UIButton](https://developer.apple.com/documentation/uikit/uibutton)