---
layout: post
title: "[swift] Swift SimpleImageViewer 이미지 배경화면 설정"
description: " "
date: 2023-11-23
tags: [swift]
comments: true
share: true
---

이번 글에서는 Swift를 사용하여 이미지를 배경화면으로 설정하는 간단한 방법을 알아보겠습니다.

```swift
import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var imageView: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        // 이미지 뷰어 만들기
        let imageViewer = UIImageView(frame: view.bounds)
        imageViewer.contentMode = .scaleAspectFill
        
        // 배경 이미지 설정
        imageViewer.image = UIImage(named: "background_image")
        
        // 이미지 뷰어를 뷰의 가장 뒤로 보내기
        view.insertSubview(imageViewer, at: 0)
        
        // 이미지 뷰어와 이미지 뷰의 관계 설정
        imageViewer.translatesAutoresizingMaskIntoConstraints = false
        imageViewer.topAnchor.constraint(equalTo: view.topAnchor).isActive = true
        imageViewer.bottomAnchor.constraint(equalTo: view.bottomAnchor).isActive = true
        imageViewer.leadingAnchor.constraint(equalTo: view.leadingAnchor).isActive = true
        imageViewer.trailingAnchor.constraint(equalTo: view.trailingAnchor).isActive = true

        // 기존의 이미지 뷰 숨기기
        imageView.isHidden = true
    }
}
```

위의 코드는 `UIIamgeView`를 사용하여 이미지를 배경으로 설정하는 방법을 보여줍니다. `viewDidLoad()` 메소드에서, view의 가장 뒤로 이미지 뷰어를 추가하고, 이미지를 설정한 후에 기존의 이미지 뷰를 숨기는 로직이 포함되어 있습니다.

배경 이미지로 사용할 이미지 파일은 프로젝트에 추가되어 있어야 합니다. `UIImage(named:)`을 사용하여 이미지를 로드하고, `imageViewer.image` 속성에 할당하여 배경 이미지로 설정합니다. 

또한 `imageViewer`와 `view`의 관계를 설정하기 위해 자동 레이아웃 제약 조건을 추가합니다. 이를 통해 이미지 뷰어가 항상 뷰와 같은 크기를 갖도록 조절됩니다. 

기존의 이미지 뷰를 숨기기 위해서는 `imageView.isHidden` 속성을 `true`로 설정하면 됩니다.

이제 위의 코드를 사용하여 앱의 배경화면으로 이미지를 설정할 수 있습니다.

## 참고 자료
- [Apple Developer Documentation - UIImageView](https://developer.apple.com/documentation/uikit/uiimageview)
- [Swift.org](https://swift.org/)