---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 그리기"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번에는 Swift로 간단한 이미지 뷰어를 만드는 방법에 대해 알아보겠습니다. 이미지 뷰어는 이미지를 로드하여 화면에 표시하는 기능을 가지고 있습니다. 그러면 시작해보겠습니다.

## 사용할 라이브러리 가져오기

이미지 뷰어를 만들기 위해 우리는 `UIKit` 라이브러리를 사용할 것입니다. 따라서 다음과 같이 `import` 문으로 `UIKit`을 가져와야 합니다.

```swift
import UIKit
```

## 이미지 뷰어 클래스 만들기

이미지 뷰어를 구현하기 위해 새로운 클래스를 만들어야 합니다. 이 클래스는 `UIViewController` 클래스를 상속받아야 하며, `UIImageView`를 사용하여 이미지를 표시할 수 있도록 설정해야 합니다.

```swift
class ImageViewerViewController: UIViewController {
    var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰 생성
        imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: view.frame.width, height: view.frame.height))
        imageView.contentMode = .scaleAspectFit
        
        // 이미지 로드
        if let image = UIImage(named: "example.jpg") {
            imageView.image = image
        }
        
        // 이미지 뷰를 뷰에 추가
        view.addSubview(imageView)
    }
}
```

## 이미지 뷰어 호출하기

이미지 뷰어를 호출하기 위해서는 다음과 같이 `ImageViewerViewController` 인스턴스를 만들고, 코드로 뷰를 표시해야 합니다.

```swift
let imageViewer = ImageViewerViewController()
self.present(imageViewer, animated: true, completion: nil)
```

위의 코드에서 `"example.jpg"`는 표시할 이미지의 파일 이름에 맞게 수정해야 합니다. 또한, 필요에 따라 이미지 뷰어를 호출하는 부분에 다른 로직을 추가할 수 있습니다.

## 결론

간단한 이미지 뷰어를 Swift로 구현하는 방법에 대해 알아보았습니다. `UIImageView`를 사용하여 이미지를 로드하고 화면에 표시하는 방법을 배웠습니다. 여러분은 이를 활용하여 사용자 지정 이미지 뷰어를 만들 수 있을 것입니다. Happy coding!