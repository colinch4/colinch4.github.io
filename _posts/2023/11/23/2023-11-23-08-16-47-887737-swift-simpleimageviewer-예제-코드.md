---
layout: post
title: "[swift] Swift SimpleImageViewer 예제 코드"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

```swift
import UIKit

class SimpleImageViewer: UIViewController {
    // 이미지를 표시할 UIImageView
    var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰 설정
        imageView = UIImageView(frame: CGRect(x: 0, y: 0, width: 300, height: 300))
        imageView.contentMode = .scaleAspectFit
        imageView.center = view.center
        view.addSubview(imageView)
        
        // 이미지 로드
        let imageUrlString = "https://example.com/image.jpg" // 표시할 이미지의 URL
        guard let imageUrl = URL(string: imageUrlString) else { return }
        DispatchQueue.global().async {
            if let imageData = try? Data(contentsOf: imageUrl) {
                DispatchQueue.main.async {
                    self.imageView.image = UIImage(data: imageData)
                }
            }
        }
    }
}
```

이 예제 코드는 `SimpleImageViewer`라는 단순한 이미지 뷰어를 만드는 방법을 보여줍니다. `UIImageView`를 사용하여 이미지를 로드하고, `URLSession`을 사용하여 이미지를 다운로드한 후 `UIImage`로 변환하여 표시합니다. 이 코드를 사용하여 프로젝트에서 이미지를 표시하는 간단한 뷰어를 만들 수 있습니다.

이미지 URL을 변경하여 다른 이미지를 로드할 수도 있습니다.